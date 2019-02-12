#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#


def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE

    if(a <= 0) | (b <= 0) | (c <= 0):
        raise TriangleError("Triangle Sides length should be greater than Zero")

    if(a + b <= c) | (b + c <= a) | (c + a <= b):
        raise TriangleError("The sum of any two sides should be greater than the third one")

    if a == b == c:
        return 'equilateral'
    elif a != b != c != a:
        return 'scalene'
    elif (a == b) | (b == c) | (c == a):
        return 'isosceles'


# Error class used in part 2.  No need to change this code.


class TriangleError(Exception):
    pass



