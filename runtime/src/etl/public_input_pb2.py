# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: public_input.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='public_input.proto',
  package='entrypoint',
  syntax='proto3',
  serialized_options=b'Z\004main',
  serialized_pb=b'\n\x12public_input.proto\x12\nentrypoint\"\xd1\x01\n\x07Request\x12\x11\n\troom_type\x18\x01 \x01(\t\x12\x10\n\x08\x62\x65\x64rooms\x18\x02 \x01(\x05\x12\x11\n\tbathrooms\x18\x03 \x01(\x02\x12\x14\n\x0c\x61\x63\x63ommodates\x18\x04 \x01(\x05\x12\x0c\n\x04\x62\x65\x64s\x18\x05 \x01(\x05\x12\x15\n\rneighbourhood\x18\x06 \x01(\t\x12\x10\n\x08latitude\x18\x07 \x01(\x02\x12\x11\n\tlongitude\x18\x08 \x01(\x02\x12\n\n\x02tv\x18\t \x01(\x05\x12\x10\n\x08\x65levator\x18\n \x01(\x05\x12\x10\n\x08internet\x18\x0b \x01(\x05\"T\n\x08Response\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x14\n\x0cmarket_price\x18\x03 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x04 \x01(\t\"T\n\x11SaveMetricRequest\x12\x1a\n\x12predicted_category\x18\x01 \x01(\t\x12\x15\n\rreal_category\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\x03\"6\n\x12SaveMetricResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xa4\x01\n\nEntrypoint\x12=\n\x0eMakePrediction\x12\x13.entrypoint.Request\x1a\x14.entrypoint.Response\"\x00\x12W\n\x14SavePredictionMetric\x12\x1d.entrypoint.SaveMetricRequest\x1a\x1e.entrypoint.SaveMetricResponse\"\x00\x42\x06Z\x04mainb\x06proto3'
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='entrypoint.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='room_type', full_name='entrypoint.Request.room_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bedrooms', full_name='entrypoint.Request.bedrooms', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bathrooms', full_name='entrypoint.Request.bathrooms', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accommodates', full_name='entrypoint.Request.accommodates', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='beds', full_name='entrypoint.Request.beds', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='neighbourhood', full_name='entrypoint.Request.neighbourhood', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='entrypoint.Request.latitude', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='entrypoint.Request.longitude', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tv', full_name='entrypoint.Request.tv', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='elevator', full_name='entrypoint.Request.elevator', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='internet', full_name='entrypoint.Request.internet', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=35,
  serialized_end=244,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='entrypoint.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='entrypoint.Response.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='entrypoint.Response.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='market_price', full_name='entrypoint.Response.market_price', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='entrypoint.Response.category', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=246,
  serialized_end=330,
)


_SAVEMETRICREQUEST = _descriptor.Descriptor(
  name='SaveMetricRequest',
  full_name='entrypoint.SaveMetricRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='predicted_category', full_name='entrypoint.SaveMetricRequest.predicted_category', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='real_category', full_name='entrypoint.SaveMetricRequest.real_category', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='entrypoint.SaveMetricRequest.date', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=332,
  serialized_end=416,
)


_SAVEMETRICRESPONSE = _descriptor.Descriptor(
  name='SaveMetricResponse',
  full_name='entrypoint.SaveMetricResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='entrypoint.SaveMetricResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='entrypoint.SaveMetricResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=418,
  serialized_end=472,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['SaveMetricRequest'] = _SAVEMETRICREQUEST
DESCRIPTOR.message_types_by_name['SaveMetricResponse'] = _SAVEMETRICRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'public_input_pb2'
  # @@protoc_insertion_point(class_scope:entrypoint.Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'public_input_pb2'
  # @@protoc_insertion_point(class_scope:entrypoint.Response)
  })
_sym_db.RegisterMessage(Response)

SaveMetricRequest = _reflection.GeneratedProtocolMessageType('SaveMetricRequest', (_message.Message,), {
  'DESCRIPTOR' : _SAVEMETRICREQUEST,
  '__module__' : 'public_input_pb2'
  # @@protoc_insertion_point(class_scope:entrypoint.SaveMetricRequest)
  })
_sym_db.RegisterMessage(SaveMetricRequest)

SaveMetricResponse = _reflection.GeneratedProtocolMessageType('SaveMetricResponse', (_message.Message,), {
  'DESCRIPTOR' : _SAVEMETRICRESPONSE,
  '__module__' : 'public_input_pb2'
  # @@protoc_insertion_point(class_scope:entrypoint.SaveMetricResponse)
  })
_sym_db.RegisterMessage(SaveMetricResponse)


DESCRIPTOR._options = None

_ENTRYPOINT = _descriptor.ServiceDescriptor(
  name='Entrypoint',
  full_name='entrypoint.Entrypoint',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=475,
  serialized_end=639,
  methods=[
  _descriptor.MethodDescriptor(
    name='MakePrediction',
    full_name='entrypoint.Entrypoint.MakePrediction',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SavePredictionMetric',
    full_name='entrypoint.Entrypoint.SavePredictionMetric',
    index=1,
    containing_service=None,
    input_type=_SAVEMETRICREQUEST,
    output_type=_SAVEMETRICRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENTRYPOINT)

DESCRIPTOR.services_by_name['Entrypoint'] = _ENTRYPOINT

# @@protoc_insertion_point(module_scope)
