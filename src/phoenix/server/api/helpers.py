from typing import Iterable, List, Optional, TypeVar

T = TypeVar("T")


def ensure_list(obj: Optional[Iterable[T]]) -> List[T]:
    if isinstance(obj, List):
        return obj
    return list(obj) if isinstance(obj, Iterable) else []
