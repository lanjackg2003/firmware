# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class Ed25519Signature(p.MessageType):
    MESSAGE_WIRE_TYPE = 1010

    def __init__(
        self,
        *,
        sig: bytes,
        r: bytes,
        s1: bytes,
    ) -> None:
        self.sig = sig
        self.r = r
        self.s1 = s1

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('sig', p.BytesType, p.FLAG_REQUIRED),
            2: ('r', p.BytesType, p.FLAG_REQUIRED),
            3: ('s1', p.BytesType, p.FLAG_REQUIRED),
        }
