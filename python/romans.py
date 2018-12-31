#!/usr/bin/env python3

""" An attempt to solve Roaming Romans on Kattis """

MODERN_MILE_FEET = 5280.0
ROMAN_MILE_IN_FEET = 4854.0

miles = float(input().rstrip())

roman_paces = (1000 * (MODERN_MILE_FEET/ROMAN_MILE_IN_FEET)) * miles
print(round(roman_paces))
