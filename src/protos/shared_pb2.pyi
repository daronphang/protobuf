from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeartBeatRequest(_message.Message):
    __slots__ = ["correlationId"]
    CORRELATIONID_FIELD_NUMBER: _ClassVar[int]
    correlationId: str
    def __init__(self, correlationId: _Optional[str] = ...) -> None: ...

class HeartBeatResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class QueryRequest(_message.Message):
    __slots__ = ["correlationId", "payload", "query", "userinfo"]
    CORRELATIONID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    USERINFO_FIELD_NUMBER: _ClassVar[int]
    correlationId: str
    payload: _any_pb2.Any
    query: str
    userinfo: UserInfo
    def __init__(self, correlationId: _Optional[str] = ..., query: _Optional[str] = ..., userinfo: _Optional[_Union[UserInfo, _Mapping]] = ..., payload: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class QueryResponse(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    def __init__(self, results: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...) -> None: ...

class TaskRequest(_message.Message):
    __slots__ = ["correlationId", "payload", "task", "userinfo"]
    CORRELATIONID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    USERINFO_FIELD_NUMBER: _ClassVar[int]
    correlationId: str
    payload: _any_pb2.Any
    task: str
    userinfo: UserInfo
    def __init__(self, correlationId: _Optional[str] = ..., task: _Optional[str] = ..., userinfo: _Optional[_Union[UserInfo, _Mapping]] = ..., payload: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class TaskResponse(_message.Message):
    __slots__ = ["taskId"]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    taskId: str
    def __init__(self, taskId: _Optional[str] = ...) -> None: ...

class TaskStatusRequest(_message.Message):
    __slots__ = ["correlationId", "task", "taskId"]
    CORRELATIONID_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    correlationId: str
    task: str
    taskId: str
    def __init__(self, correlationId: _Optional[str] = ..., taskId: _Optional[str] = ..., task: _Optional[str] = ...) -> None: ...

class TaskStatusResponse(_message.Message):
    __slots__ = ["error", "result", "state"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    error: str
    result: str
    state: str
    def __init__(self, state: _Optional[str] = ..., result: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class UserInfo(_message.Message):
    __slots__ = ["fab", "username"]
    FAB_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    fab: str
    username: str
    def __init__(self, username: _Optional[str] = ..., fab: _Optional[str] = ...) -> None: ...
