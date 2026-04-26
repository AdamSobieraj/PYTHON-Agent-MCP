import unittest

from pydantic import ValidationError

from buissnes_agent.a2a_agent.ag_ui import (
    AG_UI_MEDIA_TYPE,
    ActivitySnapshotEvent,
    EventEncoder,
    RunAgentInput,
    TextMessageContentEvent,
    flatten_text_content,
    parse_tool_call_arguments,
)


class AgUiProtocolTests(unittest.TestCase):
    def test_run_agent_input_accepts_camel_case_payload_and_defaults(self) -> None:
        payload = RunAgentInput.model_validate(
            {
                'threadId': 'thread-1',
                'runId': 'run-1',
                'messages': [
                    {
                        'id': 'user-1',
                        'role': 'user',
                        'content': 'hello',
                    }
                ],
            }
        )

        self.assertEqual(payload.thread_id, 'thread-1')
        self.assertEqual(payload.run_id, 'run-1')
        self.assertEqual(payload.state, {})
        self.assertEqual(payload.tools, [])
        self.assertEqual(payload.context, [])
        self.assertEqual(payload.forwarded_props, {})

    def test_event_encoder_negotiates_sse_and_ndjson(self) -> None:
        event = ActivitySnapshotEvent(
            message_id='activity-1',
            activity_type='PLAN',
            content={'message': 'Planning the next action.'},
        )

        sse_encoder = EventEncoder(accept='text/event-stream')
        ndjson_encoder = EventEncoder(accept='application/json')

        self.assertEqual(sse_encoder.get_content_type(), AG_UI_MEDIA_TYPE)
        self.assertTrue(sse_encoder.encode(event).startswith('data: '))
        self.assertEqual(
            ndjson_encoder.get_content_type(),
            'application/x-ndjson',
        )
        self.assertFalse(ndjson_encoder.encode(event).startswith('data: '))

    def test_flatten_text_content_handles_multimodal_content(self) -> None:
        content = [
            {'type': 'text', 'text': 'Find the page'},
            {
                'type': 'image',
                'source': {
                    'type': 'url',
                    'value': 'https://example.com/image.png',
                },
            },
            {
                'type': 'document',
                'source': {
                    'type': 'data',
                    'value': 'JVBERi0xLjQK...',
                },
            },
        ]

        self.assertEqual(
            flatten_text_content(content),
            'Find the page\n[image: https://example.com/image.png]\n[document: inline content]',
        )

    def test_parse_tool_call_arguments_supports_json_and_raw_text(self) -> None:
        self.assertEqual(
            parse_tool_call_arguments('{"query":"architecture"}'),
            {'query': 'architecture'},
        )
        self.assertEqual(
            parse_tool_call_arguments({'query': 'architecture'}),
            {'query': 'architecture'},
        )
        self.assertEqual(
            parse_tool_call_arguments('not-json'),
            {'raw': 'not-json'},
        )

    def test_text_message_delta_must_be_non_empty(self) -> None:
        with self.assertRaises(ValidationError):
            TextMessageContentEvent(message_id='msg-1', delta='')

    def test_activity_snapshot_defaults_to_replace_true(self) -> None:
        event = ActivitySnapshotEvent(
            message_id='activity-1',
            activity_type='TOOL',
            content={'message': 'Running tool search_docs.'},
        )

        self.assertTrue(event.replace)


if __name__ == '__main__':
    unittest.main(verbosity=2)
