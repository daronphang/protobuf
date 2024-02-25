from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import struct_pb2 as _struct_pb2
import shared_pb2 as _shared_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChronicChartsMonitoringTask(_message.Message):
    __slots__ = ["module"]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    module: str
    def __init__(self, module: _Optional[str] = ...) -> None: ...

class Common(_message.Message):
    __slots__ = ["module"]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    module: str
    def __init__(self, module: _Optional[str] = ...) -> None: ...

class CriticalChartsMonitoringTask(_message.Message):
    __slots__ = ["designIds", "module"]
    DESIGNIDS_FIELD_NUMBER: _ClassVar[int]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    designIds: _containers.RepeatedScalarFieldContainer[str]
    module: str
    def __init__(self, module: _Optional[str] = ..., designIds: _Optional[_Iterable[str]] = ...) -> None: ...

class FixedChartsMonitoringTask(_message.Message):
    __slots__ = ["module"]
    MODULE_FIELD_NUMBER: _ClassVar[int]
    module: str
    def __init__(self, module: _Optional[str] = ...) -> None: ...

class QuerySpaceChartMetadata(_message.Message):
    __slots__ = ["chId", "ckcId"]
    CHID_FIELD_NUMBER: _ClassVar[int]
    CKCID_FIELD_NUMBER: _ClassVar[int]
    chId: int
    ckcId: int
    def __init__(self, chId: _Optional[int] = ..., ckcId: _Optional[int] = ...) -> None: ...

class QuerySpaceSamples(_message.Message):
    __slots__ = ["chId", "ckcId", "endDate", "lookbackDays", "samples", "startDate"]
    CHID_FIELD_NUMBER: _ClassVar[int]
    CKCID_FIELD_NUMBER: _ClassVar[int]
    ENDDATE_FIELD_NUMBER: _ClassVar[int]
    LOOKBACKDAYS_FIELD_NUMBER: _ClassVar[int]
    SAMPLES_FIELD_NUMBER: _ClassVar[int]
    STARTDATE_FIELD_NUMBER: _ClassVar[int]
    chId: int
    ckcId: int
    endDate: str
    lookbackDays: int
    samples: int
    startDate: str
    def __init__(self, chId: _Optional[int] = ..., ckcId: _Optional[int] = ..., samples: _Optional[int] = ..., lookbackDays: _Optional[int] = ..., startDate: _Optional[str] = ..., endDate: _Optional[str] = ...) -> None: ...
