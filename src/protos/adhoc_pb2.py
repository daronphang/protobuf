# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: adhoc.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from . import shared_pb2 as shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x61\x64hoc.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x0cshared.proto\"\x15\n\x13QueryDiffusionTools\"F\n\x12QueryFDCViolations\x12\r\n\x05tools\x18\x01 \x03(\t\x12\x14\n\x0clookbackDays\x18\x02 \x01(\x05\x12\x0b\n\x03\x66\x61\x62\x18\x03 \x01(\t\"y\n\x11QueryDPNLoadLocks\x12\x10\n\x08\x65quipIds\x18\x01 \x03(\t\x12\x11\n\tstartDate\x18\x02 \x01(\t\x12\x0f\n\x07\x65ndDate\x18\x03 \x01(\t\x12\x18\n\x10loadlockEntrance\x18\x04 \x03(\t\x12\x14\n\x0cloadlockExit\x18\x05 \x03(\t\"7\n\x12QuerySPCViolations\x12\x0e\n\x06lotIds\x18\x01 \x03(\t\x12\x11\n\tmeasSteps\x18\x02 \x03(\t\")\n\x11\x46\x44\x43ViolationsTask\x12\x14\n\x0clookbackDays\x18\x01 \x01(\x05\"x\n\x10\x44PNLoadLocksTask\x12\x10\n\x08\x65quipIds\x18\x01 \x03(\t\x12\x11\n\tstartDate\x18\x02 \x01(\t\x12\x0f\n\x07\x65ndDate\x18\x03 \x01(\t\x12\x18\n\x10loadlockEntrance\x18\x04 \x03(\t\x12\x14\n\x0cloadlockExit\x18\x05 \x03(\t\"\x0c\n\nSPCOOCTask\"\x13\n\x11\x44PNMonitoringTask\"\x1b\n\x19\x42lockedEtchMonitoringTask2\xc7\x01\n\x05\x41\x64hoc\x12\x34\n\theartbeat\x12\x11.HeartBeatRequest\x1a\x12.HeartBeatResponse\"\x00\x12(\n\x05query\x12\r.QueryRequest\x1a\x0e.QueryResponse\"\x00\x12%\n\x04task\x12\x0c.TaskRequest\x1a\r.TaskResponse\"\x00\x12\x37\n\ntaskStatus\x12\x12.TaskStatusRequest\x1a\x13.TaskStatusResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'adhoc_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _QUERYDIFFUSIONTOOLS._serialized_start=86
  _QUERYDIFFUSIONTOOLS._serialized_end=107
  _QUERYFDCVIOLATIONS._serialized_start=109
  _QUERYFDCVIOLATIONS._serialized_end=179
  _QUERYDPNLOADLOCKS._serialized_start=181
  _QUERYDPNLOADLOCKS._serialized_end=302
  _QUERYSPCVIOLATIONS._serialized_start=304
  _QUERYSPCVIOLATIONS._serialized_end=359
  _FDCVIOLATIONSTASK._serialized_start=361
  _FDCVIOLATIONSTASK._serialized_end=402
  _DPNLOADLOCKSTASK._serialized_start=404
  _DPNLOADLOCKSTASK._serialized_end=524
  _SPCOOCTASK._serialized_start=526
  _SPCOOCTASK._serialized_end=538
  _DPNMONITORINGTASK._serialized_start=540
  _DPNMONITORINGTASK._serialized_end=559
  _BLOCKEDETCHMONITORINGTASK._serialized_start=561
  _BLOCKEDETCHMONITORINGTASK._serialized_end=588
  _ADHOC._serialized_start=591
  _ADHOC._serialized_end=790
# @@protoc_insertion_point(module_scope)
