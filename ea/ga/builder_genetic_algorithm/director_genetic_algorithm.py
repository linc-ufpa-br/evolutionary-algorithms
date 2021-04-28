"""
Separate the construction of a complex object from its representation so
that the same construction process can create different representations.
"""

import abc


class DirectorAlgorithmGenetic:
    """
    Construct an object using the Builder interface.
    """

    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder._build_part_a()
        self._builder._build_part_b()
        self._builder._build_part_c()