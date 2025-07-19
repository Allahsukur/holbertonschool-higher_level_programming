#!/usr/bin/python3
'''
Module to test max_integer() function
'''

max_integer = __import__('6-max_integer').max_integer
import unittest


class TestMaxInteger(unittest.TestCase):
    '''
    Class for testing max_integer() function with two methods
    '''
    def test_max(self):
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([1,2,3,4,5]), 5)
        self.assertAlmostEqual(max_integer([10,2,24,52,1]), 52)
        self.assertAlmostEqual(max_integer([-1,-2,-3,-4,-5]), -1)
        self.assertAlmostEqual(max_integer([-1,-2,-3,-4, 0]), 0)
        self.assertAlmostEqual(max_integer([1,2,3,-4,-5]), 3)

    # def test_values(self):
    #     self.assertRaises(TypeError, max_integer('a'), 'argument must be a list')
    #     self.assertRaises(TypeError, max_integer(['a', 1, 2, 3]), '\'>\' not supported between instances of \'int\' and \'str\'')
    