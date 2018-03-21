#!/usr/local/bin/python3

class C:
    _x = None
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value


class CircleWithReadOnyDiameter():
    """
    circle class with the following attributes / properites
    ARGS:
        radius : set on initialization, can be overwritten.
        diameter : not set on initializtion, calulated, read only.
        (No setter for diameter)
    """

    def __init__(self, initial_radius_parameter):
        """ self.radius is an instance vairable"""
        self.radius = initial_radius_parameter

    @property
    def diameter(self):
        return 2 * self.radius


class CircleWithSettableDiameter():
    """
    circle class with the following attributes / properites
    ARGS:
        radius : set on initialization, can be overwritten.
        diameter : not set on initializtion, calulated, SETTABLE.
    """

    def __init__(self, initial_radius_parameter):
        self.radius = initial_radius_parameter

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2


class CircleWithRadiusValidation():
    """
    circle class with the following attributes / properites
    ARGS:
        radius : set on initialization, can be overwritten using setter.
        diameter : not set on initializtion, calulated, SETTABLE.
    """

    def __init__(self, initial_radius_parameter):
        self._radius_variable = initial_radius_parameter

    @property
    def radius(self):
        return self._radius_variable

    @radius.setter
    def radius(self, value):
        if value < 0 or value > 100:
            raise ValueError("radius is not in the range 0 - 100")
        self._radius_variable = value

    @property
    def diameter(self):
        """
        this is calling the radius function which returns the radius
        variable value.  It is not referencing the variable directly
        unlike previous examples.
        """
        return 2 * self.radius

    @diameter.setter
    def diameter(self, value):
        """
        this sets the _radius_vairable via the radius function.
        """
        self.radius = value / 2
