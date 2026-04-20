"""
Patch a2a-sdk proto validation for protobuf runtimes without FieldDescriptor.is_repeated.

This affects Python 3.14 environments using the upb-backed protobuf descriptors.
"""

from google.protobuf.descriptor import FieldDescriptor

from a2a.utils import proto_utils


def _is_repeated(field: FieldDescriptor) -> bool:
    return getattr(field, 'is_repeated', None) or (
        field.label == FieldDescriptor.LABEL_REPEATED
    )


def _check_required_field_violation(msg, field):
    val = getattr(msg, field.name)
    if _is_repeated(field):
        if not val:
            return proto_utils.ValidationDetail(
                field=field.name,
                message='Field must contain at least one element.',
            )
    elif field.has_presence:
        if not msg.HasField(field.name):
            return proto_utils.ValidationDetail(
                field=field.name,
                message='Field is required.',
            )
    elif val == field.default_value:
        return proto_utils.ValidationDetail(
            field=field.name,
            message='Field is required.',
        )
    return None


def _recurse_validation(msg, field):
    errors = []
    if field.type != FieldDescriptor.TYPE_MESSAGE:
        return errors

    val = getattr(msg, field.name)
    if not _is_repeated(field):
        if msg.HasField(field.name):
            sub_errs = proto_utils._validate_proto_required_fields_internal(val)
            proto_utils._append_nested_errors(errors, field.name, sub_errs)
    elif field.message_type.GetOptions().map_entry:
        for key, value in val.items():
            if hasattr(value, 'DESCRIPTOR'):
                sub_errs = proto_utils._validate_proto_required_fields_internal(
                    value
                )
                proto_utils._append_nested_errors(
                    errors,
                    f'{field.name}[{key}]',
                    sub_errs,
                )
    else:
        for index, item in enumerate(val):
            sub_errs = proto_utils._validate_proto_required_fields_internal(item)
            proto_utils._append_nested_errors(
                errors,
                f'{field.name}[{index}]',
                sub_errs,
            )
    return errors


if not getattr(proto_utils, '_PY314_FIELD_DESCRIPTOR_PATCHED', False):
    proto_utils._check_required_field_violation = _check_required_field_violation
    proto_utils._recurse_validation = _recurse_validation
    proto_utils._PY314_FIELD_DESCRIPTOR_PATCHED = True
