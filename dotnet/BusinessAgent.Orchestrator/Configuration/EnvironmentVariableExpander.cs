using System.Text.RegularExpressions;

namespace BusinessAgent.Orchestrator.Configuration;

internal static partial class EnvironmentVariableExpander
{
    private static readonly Regex s_malformedFullPattern = MalformedFullPattern();
    private static readonly Regex s_pattern = Pattern();

    public static string Expand(string input)
    {
        if (string.IsNullOrEmpty(input))
        {
            return input;
        }

        var malformedMatch = s_malformedFullPattern.Match(input);
        if (malformedMatch.Success)
        {
            var variableName = malformedMatch.Groups["braced"].Value;
            var defaultValue = malformedMatch.Groups["default"].Success
                ? malformedMatch.Groups["default"].Value
                : string.Empty;
            var resolved = Environment.GetEnvironmentVariable(variableName);
            return string.IsNullOrWhiteSpace(resolved)
                ? defaultValue
                : resolved;
        }

        return s_pattern.Replace(input, match =>
        {
            var variableName = match.Groups["braced"].Success
                ? match.Groups["braced"].Value
                : match.Groups["plain"].Value;
            var defaultValue = match.Groups["default"].Success
                ? match.Groups["default"].Value
                : string.Empty;
            var resolved = Environment.GetEnvironmentVariable(variableName);
            return string.IsNullOrWhiteSpace(resolved)
                ? defaultValue
                : resolved;
        });
    }

    [GeneratedRegex(
        @"\$\{(?<braced>[A-Za-z_][A-Za-z0-9_]*)(:-(?<default>[^}]*))?\}|\$(?<plain>[A-Za-z_][A-Za-z0-9_]*)",
        RegexOptions.Compiled)]
    private static partial Regex Pattern();

    [GeneratedRegex(
        @"^\$\{(?<braced>[A-Za-z_][A-Za-z0-9_]*)(:-(?<default>.*))?$",
        RegexOptions.Compiled)]
    private static partial Regex MalformedFullPattern();
}
