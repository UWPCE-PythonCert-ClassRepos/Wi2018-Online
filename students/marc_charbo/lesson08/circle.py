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
        self._radius = radius

    def __str__(self):
        return "Circle with radius: {:8.6f}".format(self.radius)

    def __repr__(self):
        return "Circle ({})".format(self.radius)

    def __add__(self, other_circle):
        return Circle(self.radius + other_circle.radius) # question should this be radius or _radius?

    def __mul__(self, other_variable):
        return Circle(self.radius * 2)

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
    cr1 = Circle(4)
    print (cr1.radius)


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