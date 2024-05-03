#!/usr/bin/env python3
"""Function that imports sequence"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """checkes length"""
    return [(i, len(i)) for i in lst]
