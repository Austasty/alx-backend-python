#!/usr/bin/env python3
"""function that imports list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """initialization of the float"""
    acc: float = 0
    for i in range(len(mxd_lst)):
        acc = acc + mxd_lst[i]
    return acc
