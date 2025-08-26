import json
import base64

class FunctionDBValue:
    """Represents the value structure for the function database."""
    def __init__(
        self,
        lowered_name: bytes,
        cubin_data: bytes
    ):
        self.lowered_name = lowered_name
        self.cubin_data = cubin_data

    def to_bytes(self) -> bytes:
        """Serialize the value to a bytes object for LMDB storage."""
        value_dict = {
            'lowered_name': base64.b64encode(self.lowered_name).decode('utf-8'),
            'cubin_data': base64.b64encode(self.cubin_data).decode('utf-8')
        }
        return json.dumps(value_dict, sort_keys=True).encode('utf-8')

    @classmethod
    def from_bytes(cls, data: bytes) -> 'FunctionDBValue':
        """Deserialize bytes to a FunctionDBValue object."""
        value_dict = json.loads(data.decode('utf-8'))
        return cls(
            lowered_name=base64.b64decode(value_dict['lowered_name']),
            cubin_data=base64.b64decode(value_dict['cubin_data'])
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, FunctionDBValue):
            return False
        return (
            self.lowered_name == other.lowered_name and
            self.cubin_data == other.cubin_data
        )

    def __repr__(self) -> str:
        return (f"FunctionDBValue(lowered_name={self.lowered_name!r}, "
                f"cubin_data={self.cubin_data!r})")