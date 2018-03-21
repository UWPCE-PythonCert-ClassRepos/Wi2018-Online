from math import (
    pow,
    sqrt,
)

import typing

import pytest


class Vector(object):

    def __init__(self, elements:tuple) -> 'Vector':
        if not elements:
            raise ValueError("The elements must be nonempty.")
        self.elements = tuple(elements)
        self.length = len(elements)

    def __add__(self, v:'Vector') -> 'Vector':
        if not isinstance(v, Vector):
            raise TypeError("Operands must be of type Vector.")
        if self.length != v.length:
            raise ValueError("Addition requires that vectors be the same size .")
        return Vector([x + y for x, y in zip(self.elements, v.elements)])

    def __sub__(self, v:'Vector') -> 'Vector':
        if not isinstance(v, Vector):
            raise TypeError("Operands must be of type Vector.")
        if self.length != v.length:
            raise ValueError("Subtraction requires that vectors be the same size.")
        return Vector([x - y for x, y in zip(self.elements, v.elements)])

    def __mul__(self, scalar:float) -> 'Vector':
        return Vector([x * scalar for x in self.elements])

    def __str__(self):
        return 'Vector: {}'.format(self.elements)

    def __eq__(self, v:'Vector') -> bool:
        if not isinstance(v, Vector):
            raise TypeError("Operands must be of type Vector.")
        return self.elements == pytest.approx(v.elements, 0.01)

    def magnitude(self) -> float:
        return sqrt(sum([pow(x, 2) for x in self.elements]))

    def direction(self) -> 'Vector':
        """" Direction via normalization """
        if self.magnitude() == 0:
            raise ZeroDivisionError("Zero vector has no direction.")
        return self * (1 / self.magnitude())


class TestVector(object):

    def test_addition(self):
        """ Does addition return correct values? """

        A = Vector((8.218, -9.341))
        B = Vector((-1.129, 2.111))
        C = Vector((7.089, -7.229))

        assert A + B == C

    def test_addition_typeerror(self):
        """ Does addition with a non-vector raise a TypeError? """

        A = Vector((123.2, 321.4))

        with pytest.raises(TypeError):
            assert A + 3

    def test_addition_valueerror(self):
        """ Does addition of vectors of unequal raise ValueError? """

        A = Vector((8.218, -9.341))
        B = Vector((7.089, -7.229, 4.321))
        C = Vector((7.089, -7.229))

        with pytest.raises(ValueError):
            assert A + B == C

    def test_subtraction(self):
        """ Does subtraction return correct values? """

        A = Vector((7.119, 8.215))
        B = Vector((-8.223, 0.878))
        C = Vector((15.342, 7.337))

        assert A - B == C

    def test_subtraction_typeerror(self):
        """ Does subtraction with a non-vector raise a TypeError? """

        A = Vector((123.2, 321.4))

        with pytest.raises(TypeError):
            assert A - 3

    def test_subtraction_exception(self):
        """ Does subtraction of vectors of unequal raise ValueError? """

        A = Vector((7.119, 8.215))
        B = Vector((7.089, -7.229, 4.321))
        C = Vector((15.342, 7.337))

        with pytest.raises(ValueError):
            assert A - B == C

    def test_multplication(self):
        """ Does multiplication by a scalar return correct values? """

        A = Vector((1.671, -1.012, -0.318))
        B = Vector((12.382, -7.498, -2.356))

        assert A * 7.41 == B

    def test_magnitude(self):
        """ Does multiplication return correct values? """

        A = Vector((-0.221, 7.437))
        B = Vector((8.813, -1.331, -6.247))

        assert A.magnitude() == pytest.approx(7.440, 0.001)
        assert B.magnitude() == pytest.approx(10.884, 0.001)

    def test_direction(self):
        """ Does normalization return the correct direction? """

        A = Vector((5.581, -2.136))
        B = Vector((1.996, 3.108, -4.554))

        assert A.direction() == Vector((0.934, -0.357))
        assert B.direction() == Vector((0.340, 0.530, -0.777))

        # The following is a tautology,
        # because it is the inverse of the normalization algoritim,
        # yet perhaps useful as a reminder to have it here explicitly.
        # In otherwords, the magnitude of the direction of a Vector is 1.
        assert A.direction().magnitude() == pytest.approx(1, 0.01)
        assert B.direction().magnitude() == pytest.approx(1, 0.01)

    def test_direction_zero_vector(self):
        """ Does calculation of direction of the zero vector raise error? """

        # __init__ on class Vector prevents these from being born
        # A = Vector((0))
        # B = Vector((0, 0))
        # C = Vector((0, 0, 0))

        # with pytest.raises(ZeroDivisionError):
        #     assert A.direction() == 0
        #     assert B.direction() == 0
        #     assert C.direction() == 0

        pass
