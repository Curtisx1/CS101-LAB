# Name: Curtis Lemke
# Class: CS101 LAB Section 3
# Assignment: Lab Week 15
# Date: 12/7/2022
# Created date: 12/7/2022


# Imported Libraries
import unittest
import Grades
import math

# Classes


class SimpleTest(unittest.TestCase):

    def test_average_one(self):
        values = (2, 5, 9)
        self.assertAlmostEqual(Grades.average(values), 5.33333, 5)

    def test_average_two(self):
        values = (2, 15, 22, 9)
        self.assertAlmostEqual(Grades.average(values), 12.0000, 4)

    def test_average_returns_nan(self):
        values = ()
        self.assertIs(Grades.average(values), math.nan)

# Main


if __name__ == '__main__':
    unittest.main()
