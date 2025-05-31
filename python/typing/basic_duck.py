from collections.abc import Iterable, Mapping, MutableMapping, Sequence

"In typical Python code, many functions that can take a list or a dict as an argument only need their argument"

" to be somehow “list-like” or “dict-like”. A specific meaning of “list-like” or “dict-like” "
"(or something-else-like) is called a “duck type”, and several duck types that are common in idiomatic Python are standardized."
# or 'from typing import ...' (required in Python 3.8)


# Use Iterable for generic iterables (anything usable in "for"),
# and Sequence where a sequence (supporting "len" and "__getitem__") is
# required
def f(ints: Iterable[int]) -> list[str]:
    return [str(x) for x in ints]


f(range(1, 3))


# Mapping describes a dict-like object (with "__getitem__") that we won't
# mutate, and MutableMapping one (with "__setitem__") that we might
def f(my_mapping: Mapping[int, str]) -> list[int]:
    my_mapping[5] = "maybe"  # mypy will complain about this line...
    return list(my_mapping.keys())


f({3: "yes", 4: "no"})


def f(my_mapping: MutableMapping[int, str]) -> set[str]:
    my_mapping[5] = "maybe"  # ...but mypy is OK with this.
    return set(my_mapping.values())


f({3: "yes", 4: "no"})

import sys
from typing import IO


# Use IO[str] or IO[bytes] for functions that should accept or return
# objects that come from an open() call (note that IO does not
# distinguish between reading, writing or other modes)
def get_sys_IO(mode: str = "w") -> IO[str]:
    if mode == "w":
        return sys.stdout
    elif mode == "r":
        return sys.stdin
    else:
        return sys.stdout
