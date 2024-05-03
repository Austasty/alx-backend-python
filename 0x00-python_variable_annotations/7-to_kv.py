#!/usr/bin/env python3
"""function that imports tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Union[Tuple[str, float]]:
    """using the sytring and union"""
    data = (k, v)

    return data
