from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import struct_pb2 as _struct_pb2
import shared_pb2 as _shared_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ESPECMonitoringTask(_message.Message):
    __slots__ = ["designIds", "lookbackWeeks"]
    DESIGNIDS_FIELD_NUMBER: _ClassVar[int]
    LOOKBACKWEEKS_FIELD_NUMBER: _ClassVar[int]
    designIds: _containers.RepeatedScalarFieldContainer[str]
    lookbackWeeks: int
    def __init__(self, lookbackWeeks: _Optional[int] = ..., designIds: _Optional[_Iterable[str]] = ...) -> None: ...
