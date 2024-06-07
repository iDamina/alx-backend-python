#!/usr/bin/env python3
"""Writing a type-annotated function make_multiplier that takes
a float multiplier as argument and returns a function that
multiplies a float by multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    def float_multiplier(val: float) -> float:
        return multiplier * val

    return float_multiplier
