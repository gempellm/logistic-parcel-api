# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gempellm/logistic_parcel_api/v1/logistic_parcel_api.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gempellm/logistic_parcel_api/v1/logistic_parcel_api.proto',
  package='gempellm.logistic_parcel_api.v1',
  syntax='proto3',
  serialized_options=b'ZSgithub.com/gempellm/logistic-parcel-api/pkg/logistic-parcel-api;logistic_parcel_api',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n9gempellm/logistic_parcel_api/v1/logistic_parcel_api.proto\x12\x1fgempellm.logistic_parcel_api.v1\x1a\x17validate/validate.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"`\n\x06Parcel\x12\x0e\n\x02id\x18\x01 \x01(\x04R\x02id\x12\x10\n\x03\x66oo\x18\x02 \x01(\x04R\x03\x66oo\x12\x34\n\x07\x63reated\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x63reated\"?\n\x17\x44\x65scribeParcelV1Request\x12$\n\tparcel_id\x18\x01 \x01(\x04\x42\x07\xfa\x42\x04\x32\x02 \x00R\x08parcelId\"Y\n\x18\x44\x65scribeParcelV1Response\x12=\n\x05value\x18\x01 \x01(\x0b\x32\'.gempellm.logistic_parcel_api.v1.ParcelR\x05value2\xc5\x01\n\x18LogisticParcelApiService\x12\xa8\x01\n\x10\x44\x65scribeParcelV1\x12\x38.gempellm.logistic_parcel_api.v1.DescribeParcelV1Request\x1a\x39.gempellm.logistic_parcel_api.v1.DescribeParcelV1Response\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/v1/parcels/{parcel_id}BUZSgithub.com/gempellm/logistic-parcel-api/pkg/logistic-parcel-api;logistic_parcel_apib\x06proto3'
  ,
  dependencies=[validate_dot_validate__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_PARCEL = _descriptor.Descriptor(
  name='Parcel',
  full_name='gempellm.logistic_parcel_api.v1.Parcel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gempellm.logistic_parcel_api.v1.Parcel.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='foo', full_name='gempellm.logistic_parcel_api.v1.Parcel.foo', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='foo', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created', full_name='gempellm.logistic_parcel_api.v1.Parcel.created', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='created', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=278,
)


_DESCRIBEPARCELV1REQUEST = _descriptor.Descriptor(
  name='DescribeParcelV1Request',
  full_name='gempellm.logistic_parcel_api.v1.DescribeParcelV1Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parcel_id', full_name='gempellm.logistic_parcel_api.v1.DescribeParcelV1Request.parcel_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\0042\002 \000', json_name='parcelId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=280,
  serialized_end=343,
)


_DESCRIBEPARCELV1RESPONSE = _descriptor.Descriptor(
  name='DescribeParcelV1Response',
  full_name='gempellm.logistic_parcel_api.v1.DescribeParcelV1Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='gempellm.logistic_parcel_api.v1.DescribeParcelV1Response.value', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=345,
  serialized_end=434,
)

_PARCEL.fields_by_name['created'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DESCRIBEPARCELV1RESPONSE.fields_by_name['value'].message_type = _PARCEL
DESCRIPTOR.message_types_by_name['Parcel'] = _PARCEL
DESCRIPTOR.message_types_by_name['DescribeParcelV1Request'] = _DESCRIBEPARCELV1REQUEST
DESCRIPTOR.message_types_by_name['DescribeParcelV1Response'] = _DESCRIBEPARCELV1RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Parcel = _reflection.GeneratedProtocolMessageType('Parcel', (_message.Message,), {
  'DESCRIPTOR' : _PARCEL,
  '__module__' : 'gempellm.logistic_parcel_api.v1.logistic_parcel_api_pb2'
  # @@protoc_insertion_point(class_scope:gempellm.logistic_parcel_api.v1.Parcel)
  })
_sym_db.RegisterMessage(Parcel)

DescribeParcelV1Request = _reflection.GeneratedProtocolMessageType('DescribeParcelV1Request', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEPARCELV1REQUEST,
  '__module__' : 'gempellm.logistic_parcel_api.v1.logistic_parcel_api_pb2'
  # @@protoc_insertion_point(class_scope:gempellm.logistic_parcel_api.v1.DescribeParcelV1Request)
  })
_sym_db.RegisterMessage(DescribeParcelV1Request)

DescribeParcelV1Response = _reflection.GeneratedProtocolMessageType('DescribeParcelV1Response', (_message.Message,), {
  'DESCRIPTOR' : _DESCRIBEPARCELV1RESPONSE,
  '__module__' : 'gempellm.logistic_parcel_api.v1.logistic_parcel_api_pb2'
  # @@protoc_insertion_point(class_scope:gempellm.logistic_parcel_api.v1.DescribeParcelV1Response)
  })
_sym_db.RegisterMessage(DescribeParcelV1Response)


DESCRIPTOR._options = None
_DESCRIBEPARCELV1REQUEST.fields_by_name['parcel_id']._options = None

_LOGISTICPARCELAPISERVICE = _descriptor.ServiceDescriptor(
  name='LogisticParcelApiService',
  full_name='gempellm.logistic_parcel_api.v1.LogisticParcelApiService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=437,
  serialized_end=634,
  methods=[
  _descriptor.MethodDescriptor(
    name='DescribeParcelV1',
    full_name='gempellm.logistic_parcel_api.v1.LogisticParcelApiService.DescribeParcelV1',
    index=0,
    containing_service=None,
    input_type=_DESCRIBEPARCELV1REQUEST,
    output_type=_DESCRIBEPARCELV1RESPONSE,
    serialized_options=b'\202\323\344\223\002\031\022\027/v1/parcels/{parcel_id}',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOGISTICPARCELAPISERVICE)

DESCRIPTOR.services_by_name['LogisticParcelApiService'] = _LOGISTICPARCELAPISERVICE

# @@protoc_insertion_point(module_scope)