# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class CosignEd25519(p.MessageType):
    MESSAGE_WIRE_TYPE = 1009

    def __init__(
        self,
        *,
        digest: bytes,
        ctr: int,
        global_pubkey: bytes,
        global_commit: bytes,
        address_n: List[int] = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.digest = digest
        self.ctr = ctr
        self.global_pubkey = global_pubkey
        self.global_commit = global_commit

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('digest', p.BytesType, p.FLAG_REQUIRED),
            3: ('ctr', p.UVarintType, p.FLAG_REQUIRED),
            4: ('global_pubkey', p.BytesType, p.FLAG_REQUIRED),
            5: ('global_commit', p.BytesType, p.FLAG_REQUIRED),
        }
