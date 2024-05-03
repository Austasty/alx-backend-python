#!/usr/bin/env python3
"""function that is callable"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """the first multipleir"""
    def myfunc(multiplier: float) -> float:
        """second multiplier """
        return multiplier * multiplier
    
    return myfunc
        