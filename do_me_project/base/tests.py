from django.test import TestCase
from collections.abc import Mapping
import unittest
from base.models import Rectangle

# Create your tests here.


class TestGetAreaRectangle(unittest.TestCase):
    def testArea(self):
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.get_area(), 6, "incorrect area")
    
    def testNegativeArea(self):
        #Excluding negative areas"
        rectangle = Rectangle(-1, 2)
        self.assertEqual(rectangle.get_area(), -1, "Negative area")

if __name__ == '__main__':
    unittest.main()




