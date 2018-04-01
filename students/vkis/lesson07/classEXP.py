"""
Learning Classes 101
    Step1: Look through the code, read the comments to get a grasp of naming convention
    (class attribute vs instance attribute)
    Step2: Define a c1 = Circle(5) and a c2 = Circle(10) and notice the difference between
        class attribute == same values from both c1 and c2
        instance attribute == different between c1 and c2
    Step3: Walk through each of the mutate examples one by one, and id() everything to see the changes
"""

class Circle():
    # CLASS ATTRIBUTE: local definition specifically used within the class. (PEP8: constants should be all capital)
    PI = 3.14
    ClassList = ["this was defined as a Class Attribute"]

    # INSTANCE ATTRIBUTE: takes in data directly fed to Circle() <-- inside the parentesese
    # NOTE ALSO: __new__ gets called in the background to initialize the class to a variable (see def from_dia method)
    # NOTE: an attribute uses the convention self.SomeAttribute as syntax. ALWAYS use "self" for proper practice,
    # and same with variable -- attribute name, however you dont have to; consider the following to see what goes where
    def __init__(FirstPosArg, RadiusIN = 0):
        FirstPosArg.radius = RadiusIN
        FirstPosArg.InstanceList = ["this was defined as a Instance Attribute"]

    # METHOD: takes existing data and works on it to return a value
    # called by Circle.area() as opposed to a instance like circle.PI
    def area(self):
        return self.PI * self.radius ** 2
    
    # STATIC METHOD: stand alone - no "self", so it does not manipulate the class data
    @staticmethod
    def color(color = 'black'):
        return 'the color of the circle is: ' + color

    # CLASS METHOD: used to alternatively initialize and define a class.
    # Ex: Circle(RadiusIN = 5) versus Circle.from_dia(Diameter = 10)
    @classmethod
    def from_dia(cls, Diameter):
        # METHOD 1 ---------------
        # cls() calls __new__ to initilize the class (forces a __new__)
        # self = cls()
        # self.radius = val / 2
        # return self

        # METHOD 2 ---------------
        # by calling Circle directly (instead of self) we define that the output is be to created from the class Circle
        return Circle(Diameter / 2)
    
    # mutation
    def mutate(self, val):
        # CAUTION: self.pi is NOT redefining the class attribute "pi", it is overwriting the attribute to be a
        # instance attribute instead (this is bad practice; class attributes are meant to be changed everywhere.
        # Convince yourself by calling id(c1.pi) before and after mutate
        self.PI = val

        # CAUTION: pi = val, pi in this case is NOT a attribute of the class Circle.
        # It is a local variable to the function
        PI = val

        # Note: similar to how self.pi overwrite the class attribute to become a instance attribute
        # in this case, self.radius is already a instance attribute therefore, this is a proper redefinition
        # of self.radius (instance attribute: a local redefinition of radius)
        self.radius = val

        # ATTENTION: you would think that a class attribute "ClassList" expression here would act the same as
        # the example above about self.pi = val, however this is a special case where we do in fact redefine
        # the class attribute "ClassList" instead of overwriting it with a local instance attribute because
        # in this case ClassList does not get a new ID, instead we just extend ClassList to contain more data
        # Convince yourself by calling id(c1.ClassList) before and after mutate
        self.ClassList.append(val)

        # This is similar to self.radius example above. It's just to again highlight the difference between
        # class and instance attributes with the .append(val) example.
        self.InstanceList.append(val)


# SUBCLASSING: Cricle's attributes into CircleV2 (ie: CircleV2 has all the capability of Circle and more)
class CircleV2(Circle):

    def halfarea(self):
        return self.area() / 2
