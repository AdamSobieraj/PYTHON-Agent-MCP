using System.Collections;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Text.Json;

using BusinessAgent.Orchestrator.Configuration;

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using Microsoft.SemanticKernel.Services;

namespace BusinessAgent.Orchestrator.Services;

internal sealed class TracedChatCompletionService(
    IChatCompletionService inner,
    OrchestratorConfig runtimeConfig,
    string fallbackModelId) : IChatCompletionService
{
    public IReadOnlyDictionary<string, object?> Attributes => inner.Attributes;

    public async Task<IReadOnlyList<ChatMessageContent>> GetChatMessageContentsAsync(
        ChatHistory chatHistory,
        PromptExecutionSettings? executionSettings = null,
        Kernel? kernel = null,
        CancellationToken cancellationToken = default)
    {
        var generationActivity = LangfuseTracing.StartGenerationActivity(
            "orchestrator.llm.chat_completion",
            input: SerializeChatHistory(chatHistory),
            model: ResolveModelId(executionSettings),
            runtimeConfig: runtimeConfig,
            observationMetadata: BuildObservationMetadata(
                executionSettings,
                callMode: "non_streaming"));
        LangfuseTracing.SetModelParameters(
            generationActivity,
            ExtractModelParameters(executionSettings));

        try
        {
            var results = await inner.GetChatMessageContentsAsync(
                chatHistory,
                executionSettings,
                kernel,
                cancellationToken);

            LangfuseTracing.SetOutput(
                generationActivity,
                SerializeChatOutputs(results));
            LangfuseTracing.SetUsage(
                generationActivity,
                ExtractUsageDetails(results.Cast<object>()));

            return results;
        }
        catch (Exception ex)
        {
            LangfuseTracing.MarkError(generationActivity, ex);
            throw;
        }
        finally
        {
            generationActivity?.Dispose();
        }
    }

    public IAsyncEnumerable<StreamingChatMessageContent> GetStreamingChatMessageContentsAsync(
        ChatHistory chatHistory,
        PromptExecutionSettings? executionSettings = null,
        Kernel? kernel = null,
        CancellationToken cancellationToken = default)
    {
        return TraceStreamingChatCompletionAsync(
            chatHistory,
            executionSettings,
            kernel,
            cancellationToken);
    }

    private async IAsyncEnumerable<StreamingChatMessageContent> TraceStreamingChatCompletionAsync(
        ChatHistory chatHistory,
        PromptExecutionSettings? executionSettings,
        Kernel? kernel,
        [EnumeratorCancellation] CancellationToken cancellationToken)
    {
        var generationActivity = LangfuseTracing.StartGenerationActivity(
            "orchestrator.llm.chat_completion_stream",
            input: SerializeChatHistory(chatHistory),
            model: ResolveModelId(executionSettings),
            runtimeConfig: runtimeConfig,
            observationMetadata: BuildObservationMetadata(
                executionSettings,
                callMode: "streaming"));
        LangfuseTracing.SetModelParameters(
            generationActivity,
            ExtractModelParameters(executionSettings));

        Exception? failure = null;
        var outputBuilder = new System.Text.StringBuilder();
        IReadOnlyDictionary<string, object?>? usage = null;

        try
        {
            await using var enumerator = inner.GetStreamingChatMessageContentsAsync(
                chatHistory,
                executionSettings,
                kernel,
                cancellationToken).GetAsyncEnumerator(cancellationToken);

            while (true)
            {
                StreamingChatMessageContent chunk;
                try
                {
                    if (!await enumerator.MoveNextAsync())
                    {
                        break;
                    }

                    chunk = enumerator.Current;
                }
                catch (Exception ex)
                {
                    failure = ex;
                    throw;
                }

                if (!string.IsNullOrWhiteSpace(chunk.Content))
                {
                    outputBuilder.Append(chunk.Content);
                }

                usage = ExtractUsageDetails(new object[] { chunk }) ?? usage;
                yield return chunk;
            }
        }
        finally
        {
            if (failure is not null)
            {
                LangfuseTracing.MarkError(generationActivity, failure);
            }
            else
            {
                LangfuseTracing.SetOutput(
                    generationActivity,
                    outputBuilder.ToString().Trim());
                LangfuseTracing.SetUsage(generationActivity, usage);
            }

            generationActivity?.Dispose();
        }
    }

    private string ResolveModelId(PromptExecutionSettings? executionSettings)
    {
        if (!string.IsNullOrWhiteSpace(executionSettings?.ModelId))
        {
            return executionSettings.ModelId!;
        }

        if (inner.Attributes.TryGetValue("ModelId", out var modelIdValue)
            && modelIdValue is not null
            && !string.IsNullOrWhiteSpace(modelIdValue.ToString()))
        {
            return modelIdValue.ToString()!;
        }

        return fallbackModelId;
    }

    private static IReadOnlyDictionary<string, object?> BuildObservationMetadata(
        PromptExecutionSettings? executionSettings,
        string callMode) =>
        new Dictionary<string, object?>
        {
            ["call_mode"] = callMode,
            ["service_id"] = executionSettings?.ServiceId ?? PromptExecutionSettings.DefaultServiceId,
        };

    private static object? ExtractModelParameters(PromptExecutionSettings? executionSettings)
    {
        if (executionSettings is null)
        {
            return null;
        }

        var parameters = new Dictionary<string, object?>(StringComparer.Ordinal);
        foreach (var property in executionSettings.GetType().GetProperties(BindingFlags.Instance | BindingFlags.Public))
        {
            if (!property.CanRead || property.GetIndexParameters().Length > 0)
            {
                continue;
            }

            var name = property.Name;
            if (name is "ServiceId" or "ModelId")
            {
                continue;
            }

            object? value;
            try
            {
                value = property.GetValue(executionSettings);
            }
            catch
            {
                continue;
            }

            if (value is null || IsDefaultLikeValue(value))
            {
                continue;
            }

            parameters[name] = NormalizeParameterValue(value);
        }

        return parameters.Count == 0 ? null : parameters;
    }

    private static bool IsDefaultLikeValue(object value) =>
        value switch
        {
            false => true,
            0 or 0L or 0U or 0UL or 0f or 0d or 0m => true,
            string text when string.IsNullOrWhiteSpace(text) => true,
            _ => false,
        };

    private static object NormalizeParameterValue(object value) =>
        value switch
        {
            string or bool or byte or sbyte or short or ushort or int or uint or long or ulong
                or float or double or decimal => value,
            Enum => value.ToString() ?? string.Empty,
            _ => JsonSerializer.Serialize(value),
        };

    private static string SerializeChatHistory(ChatHistory chatHistory)
    {
        var messages = chatHistory.Select(message => new
        {
            role = message.Role.ToString(),
            author = message.AuthorName,
            content = message.Content,
        });

        return JsonSerializer.Serialize(messages);
    }

    private static string SerializeChatOutputs(IEnumerable<ChatMessageContent> results)
    {
        var outputs = results
            .Select(result => string.IsNullOrWhiteSpace(result.Content)
                ? result.ToString()
                : result.Content)
            .Where(static text => !string.IsNullOrWhiteSpace(text))
            .ToList();

        return outputs.Count switch
        {
            0 => string.Empty,
            1 => outputs[0]!,
            _ => JsonSerializer.Serialize(outputs),
        };
    }

    private static IReadOnlyDictionary<string, object?>? ExtractUsageDetails(
        IEnumerable<object> contents)
    {
        var usage = new Dictionary<string, object?>(StringComparer.OrdinalIgnoreCase);
        foreach (var content in contents)
        {
            var metadata = ExtractMetadata(content);
            if (metadata is null)
            {
                continue;
            }

            foreach (var (key, value) in metadata)
            {
                TryCollectUsage(usage, key, value, depth: 0);
            }
        }

        return usage.Count == 0 ? null : usage;
    }

    private static void TryCollectUsage(
        IDictionary<string, object?> usage,
        string? key,
        object? value,
        int depth)
    {
        if (value is null || depth > 3)
        {
            return;
        }

        if (!string.IsNullOrWhiteSpace(key) && TryMapUsageKey(key, value, out var normalizedKey, out var normalizedValue))
        {
            usage[normalizedKey] = normalizedValue;
        }

        switch (value)
        {
            case JsonElement json:
                TraverseJsonElement(usage, json, depth + 1);
                break;
            case IReadOnlyDictionary<string, object?> dictionary:
                foreach (var (nestedKey, nestedValue) in dictionary)
                {
                    TryCollectUsage(usage, nestedKey, nestedValue, depth + 1);
                }

                break;
            case IDictionary dictionary:
                foreach (DictionaryEntry entry in dictionary)
                {
                    TryCollectUsage(
                        usage,
                        entry.Key?.ToString(),
                        entry.Value,
                        depth + 1);
                }

                break;
            default:
                TraverseObjectProperties(usage, value, depth + 1);
                break;
        }
    }

    private static void TraverseJsonElement(
        IDictionary<string, object?> usage,
        JsonElement element,
        int depth)
    {
        switch (element.ValueKind)
        {
            case JsonValueKind.Object:
                foreach (var property in element.EnumerateObject())
                {
                    TryCollectUsage(usage, property.Name, property.Value, depth);
                }

                break;
            case JsonValueKind.Array:
                foreach (var item in element.EnumerateArray())
                {
                    TryCollectUsage(usage, null, item, depth);
                }

                break;
        }
    }

    private static void TraverseObjectProperties(
        IDictionary<string, object?> usage,
        object value,
        int depth)
    {
        var type = value.GetType();
        if (type == typeof(string) || type.IsPrimitive || type.IsEnum)
        {
            return;
        }

        foreach (var property in type.GetProperties(BindingFlags.Instance | BindingFlags.Public))
        {
            if (!property.CanRead || property.GetIndexParameters().Length > 0)
            {
                continue;
            }

            object? propertyValue;
            try
            {
                propertyValue = property.GetValue(value);
            }
            catch
            {
                continue;
            }

            TryCollectUsage(usage, property.Name, propertyValue, depth);
        }
    }

    private static IReadOnlyDictionary<string, object?>? ExtractMetadata(object content)
    {
        if (content is KernelContent kernelContent)
        {
            return kernelContent.Metadata;
        }

        var metadataProperty = content.GetType().GetProperty("Metadata", BindingFlags.Instance | BindingFlags.Public);
        if (metadataProperty?.CanRead != true)
        {
            return null;
        }

        return metadataProperty.GetValue(content) as IReadOnlyDictionary<string, object?>;
    }

    private static bool TryMapUsageKey(
        string key,
        object value,
        out string normalizedKey,
        out object? normalizedValue)
    {
        normalizedKey = string.Empty;
        normalizedValue = null;

        var normalizedSourceKey = NormalizeUsageKey(key);
        if (!TryNormalizeScalar(value, out var scalarValue))
        {
            return false;
        }

        normalizedKey = normalizedSourceKey switch
        {
            "prompttokens" or "inputtokens" or "inputtokencount" => "input",
            "completiontokens" or "outputtokens" or "outputtokencount" => "output",
            "totaltokens" or "totaltokencount" => "total",
            "reasoningtokens" or "reasoningtokencount" => "reasoning",
            _ => string.Empty,
        };

        if (string.IsNullOrWhiteSpace(normalizedKey))
        {
            return false;
        }

        normalizedValue = scalarValue;
        return true;
    }

    private static string NormalizeUsageKey(string key) =>
        key.Trim().Replace("_", string.Empty).Replace("-", string.Empty).Replace(" ", string.Empty)
            .ToLowerInvariant();

    private static bool TryNormalizeScalar(object value, out object normalizedValue)
    {
        switch (value)
        {
            case byte or sbyte or short or ushort or int or uint or long or ulong
                or float or double or decimal:
                normalizedValue = value;
                return true;
            case JsonElement json when json.ValueKind == JsonValueKind.Number:
                if (json.TryGetInt64(out var longValue))
                {
                    normalizedValue = longValue;
                    return true;
                }

                if (json.TryGetDouble(out var doubleValue))
                {
                    normalizedValue = doubleValue;
                    return true;
                }

                break;
            case string text when long.TryParse(text, out var parsedLong):
                normalizedValue = parsedLong;
                return true;
            case string text when double.TryParse(text, out var parsedDouble):
                normalizedValue = parsedDouble;
                return true;
        }

        normalizedValue = 0;
        return false;
    }
}
