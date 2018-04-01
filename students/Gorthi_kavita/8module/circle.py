

lst = []

class Area:


    def area(x):
         pi = 3.14
         areacircle = pi*(x*x)
         lst.append(areacircle)
         print("Area of the circle" )
         print(areacircle)
         return areacircle

    def addcircle(x,y):
        pi = 3.14
        areacircle1 = pi * (x * x)
        lst.append(areacircle1)
        print("adding two circles")
        print(areacircle1)
        areacircle2 = pi * (y * y)
        lst.append(areacircle2)
        print(areacircle2)
        addtwo = areacircle1 + areacircle2
        print("the result of  two circles is :")
        print(addtwo)
        lst.append(addtwo)
        return addtwo

    def comparecircle(x,y):
         pi = 3.14
         areacircle1 = pi*(x*x)
         a = areacircle1
         lst.append(a)
         print("Area of the circle1 " )
         print(areacircle1)
         areacircle2 = pi * (y * y)
         b = areacircle2
         lst.append(b)
         print("Area of the circle 2")
         print(areacircle2)
         if(a > b):
             print("I am bigger circle than other")
             print(a)
             return a
             print("I am smaller circle than other")
             print(b)
         elif(a < b):
             print("I am bigger circle than other")
             print(b)
             return b
             print("I am smaller circle than other")
             print(a)
         elif(a ==b):
             print("we both are same circles")
             print(a,b)
             return 1

a1 = Area
a2 = Area
a3 = Area
a4 = Area

k1 = a1.area(5)
k2 = a2.addcircle(7,5)
k3 = a3.comparecircle(9,6)
print(lst)
lst.sort()
print(lst)

import turtle
myTurtle = turtle.Turtle()
myTurtle.circle(k1)
turtle.getscreen()._root.mainloop()

import unittest
class Testmail(unittest.TestCase):

         def test_areaequal(self):
             t1 = Area
             r1 = t1.area(5)
             self.assertEqual(r1,78.5)

         def test_areanotequal(self):
             t1 = Area
             r1 = t1.area(5)
             self.assertNotEqual(r1, 78)

         def test_addequal(self):
             t2 = Area
             r2 = t2.addcircle(7,5)
             self.assertEqual(r2,232.36)

         def test_addnotequal(self):
             t2 = Area
             r2 = t2.addcircle(7,5)
             self.assertNotEqual(r2,232)

         def test_compare(self):
             t3 = Area
             r2 = t3.comparecircle(9,6)
             self.assertEqual(r2,254.34)



if __name__ == '__main__':
    unittest.main()
