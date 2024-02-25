from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import struct_pb2 as _struct_pb2
import shared_pb2 as _shared_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BlockedEtchMonitoringTask(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DPNLoadLocksTask(_message.Message):
    __slots__ = ["endDate", "equipIds", "loadlockEntrance", "loadlockExit", "startDate"]
    ENDDATE_FIELD_NUMBER: _ClassVar[int]
    EQUIPIDS_FIELD_NUMBER: _ClassVar[int]
    LOADLOCKENTRANCE_FIELD_NUMBER: _ClassVar[int]
    LOADLOCKEXIT_FIELD_NUMBER: _ClassVar[int]
    STARTDATE_FIELD_NUMBER: _ClassVar[int]
    endDate: str
    equipIds: _containers.RepeatedScalarFieldContainer[str]
    loadlockEntrance: _containers.RepeatedScalarFieldContainer[str]
    loadlockExit: _containers.RepeatedScalarFieldContainer[str]
    startDate: str
    def __init__(self, equipIds: _Optional[_Iterable[str]] = ..., startDate: _Optional[str] = ..., endDate: _Optional[str] = ..., loadlockEntrance: _Optional[_Iterable[str]] = ..., loadlockExit: _Optional[_Iterable[str]] = ...) -> None: ...

class DPNMonitoringTask(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FDCViolationsTask(_message.Message):
    __slots__ = ["lookbackDays"]
    LOOKBACKDAYS_FIELD_NUMBER: _ClassVar[int]
    lookbackDays: int
    def __init__(self, lookbackDays: _Optional[int] = ...) -> None: ...

class QueryDPNLoadLocks(_message.Message):
    __slots__ = ["endDate", "equipIds", "loadlockEntrance", "loadlockExit", "startDate"]
    ENDDATE_FIELD_NUMBER: _ClassVar[int]
    EQUIPIDS_FIELD_NUMBER: _ClassVar[int]
    LOADLOCKENTRANCE_FIELD_NUMBER: _ClassVar[int]
    LOADLOCKEXIT_FIELD_NUMBER: _ClassVar[int]
    STARTDATE_FIELD_NUMBER: _ClassVar[int]
    endDate: str
    equipIds: _containers.RepeatedScalarFieldContainer[str]
    loadlockEntrance: _containers.RepeatedScalarFieldContainer[str]
    loadlockExit: _containers.RepeatedScalarFieldContainer[str]
    startDate: str
    def __init__(self, equipIds: _Optional[_Iterable[str]] = ..., startDate: _Optional[str] = ..., endDate: _Optional[str] = ..., loadlockEntrance: _Optional[_Iterable[str]] = ..., loadlockExit: _Optional[_Iterable[str]] = ...) -> None: ...

class QueryDiffusionTools(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class QueryFDCViolations(_message.Message):
    __slots__ = ["fab", "lookbackDays", "tools"]
    FAB_FIELD_NUMBER: _ClassVar[int]
    LOOKBACKDAYS_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    fab: str
    lookbackDays: int
    tools: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tools: _Optional[_Iterable[str]] = ..., lookbackDays: _Optional[int] = ..., fab: _Optional[str] = ...) -> None: ...

class QuerySPCViolations(_message.Message):
    __slots__ = ["lotIds", "measSteps"]
    LOTIDS_FIELD_NUMBER: _ClassVar[int]
    MEASSTEPS_FIELD_NUMBER: _ClassVar[int]
    lotIds: _containers.RepeatedScalarFieldContainer[str]
    measSteps: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, lotIds: _Optional[_Iterable[str]] = ..., measSteps: _Optional[_Iterable[str]] = ...) -> None: ...

class SPCOOCTask(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
