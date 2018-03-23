#!/usr/bin/env python3

import logging
import logging.config
import math

#logging.cong file
logging.config.fileConfig('logging.conf')
# create logger
logger = logging.getLogger('circle_log')

class Circle(object):
    """ create circles and computes various metrics """
    def __init__(self,radius):
        """initialize with radius"""
        self._radius = radius

    def __str__(self):
        """overload str to return circle radius"""
        return "Circle with radius: {:8.6f}".format(self.radius)

    def __repr__(self):
        return "Circle ({})".format(self.radius)

    def __add__(self, other):
        """overload add operator to sum circle radius"""
        return Circle(self.radius + other.radius) # question should this be radius or _radius?

    def __mul__(self, other):
        """overload add operator to multiply circle radius by a number"""
        return Circle(self.radius * other)

    def __lt__(self, other):
        """overload less than operator which compares two circle"""
        return self.radius < other.radius

    def __gt__(self, other):
        """overload greater than operator which compares two circle"""
        return self.radius > other.radius

    def __eq__(self, other):
        """overload equal operator which compares two circle"""
        return self.radius == other.radius

    def __ne__(self, other):
        """overload not equal operator which compares two circle"""
        return self.radius != other.radius

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self,diameter):
        self._radius = diameter / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2.0

def run():
    """ function which runs program """
    print ("Started Circle Programm")
    circles = []
    cr1 = Circle(1)
    circles.append(cr1)
    cr2 = Circle(2)
    circles.append(cr2)
    cr3 = Circle(3)
    circles.append(cr3)
    cr4 = Circle(4)
    circles.append(cr4)
    cr5 = Circle(5)
    circles.append(cr5)
    circles.sort()
    print("Sorted Circle List")
    print (circles)


def main():
    try:
        logging.info('Started Circle Program')
        run()
    except Exception as e:
        print ('error with task running program\n {}'.format(e))
        logging.debug('error with running program\n %s' % e)
    finally:
        logging.info('Finished Circle Program')

if __name__ == "__main__":
    main()