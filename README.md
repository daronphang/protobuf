## Deployment

1. Run protobuf compiler

```
src/shared.proto
src/espec.proto
src/adhoc.proto
```

```console
$ cd path/to/directory
$ py -m grpc_tools.protoc -I src --python_out=src/protos --pyi_out=src/protos --grpc_python_out=src/protos src/<proto file>
```

2. Change all imports to relative imports (python3).

```py
import shared_pb2 as shared__pb2    # old
from . import shared_pb2 as shared__pb2 # new
```

3. Copy protobufs to respective directories.
