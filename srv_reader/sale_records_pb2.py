# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sale_records.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12sale_records.proto\"\x0e\n\x0c\x45mptyMessage\"\'\n\x18PingSalesRecordsResponse\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\t\"#\n\x13SalesRecordResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"\x82\x01\n\x12SalesRecordRequest\x12\x0e\n\x06region\x18\x01 \x01(\t\x12\x11\n\titem_type\x18\x02 \x01(\t\x12\x12\n\nunits_sold\x18\x03 \x01(\t\x12\x12\n\nunit_price\x18\x04 \x01(\t\x12\x11\n\tunit_cost\x18\x05 \x01(\t\x12\x0e\n\x06source\x18\x06 \x01(\t2\x89\x01\n\x0bSalesRecord\x12<\n\x10PingSalesRecords\x12\r.EmptyMessage\x1a\x19.PingSalesRecordsResponse\x12<\n\x0fSendSalesRecord\x12\x13.SalesRecordRequest\x1a\x14.SalesRecordResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sale_records_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTYMESSAGE._serialized_start=22
  _EMPTYMESSAGE._serialized_end=36
  _PINGSALESRECORDSRESPONSE._serialized_start=38
  _PINGSALESRECORDSRESPONSE._serialized_end=77
  _SALESRECORDRESPONSE._serialized_start=79
  _SALESRECORDRESPONSE._serialized_end=114
  _SALESRECORDREQUEST._serialized_start=117
  _SALESRECORDREQUEST._serialized_end=247
  _SALESRECORD._serialized_start=250
  _SALESRECORD._serialized_end=387
# @@protoc_insertion_point(module_scope)
