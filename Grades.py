# Name: Curtis Lemke
# Class: CS101 LAB Section 3
# Assignment: Lab Week 15
# Date: 12/7/2022
# Created date: 12/7/2022


# Imported Libraries
import math

# Functions


def total(value):
    total1 = 0
    for i in value:
        total1 += i
    return total1


def average(values):
    if len(values) == 0:
        return math.nan
    value = 0
    for val in values:
        value = value + val
        return value/len(values)
