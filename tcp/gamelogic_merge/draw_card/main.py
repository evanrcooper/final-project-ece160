#!/usr/bin/python3

"""
##########################
consolidation script to manage
launching a new UNO card all
under one file

written by evan rosenfeld
special thanks:
    Prof. Robert Smyth for his
    incredible tkinter know-how.
    he truly saved us from the 
    hell that is OpenGL.
###########################
"""

"""
when running this script, make sure these py files
are present in the same pwd which this script is 
located in!
"""

from draw_card.back import *
from draw_card.card_example import *
from draw_card.plus_four import *
from draw_card.reverse import *
from draw_card.skip import *
from draw_card.wild_card import *

import tkinter as tk
from tkinter import *
import math

def draw(parent, number, color = None):
	if number in "0123456789":
		return NormalCard(parent, color, number)
	elif number == '+':
		return NormalCard(parent, color, "+2")
	elif number.upper() == 'P':
		plus4()
	elif number.upper() == 'C':
		wild()
	elif number.upper() == 'R':
		reverse(color)
	elif number.upper() == 'S':
		skip(color)
	elif number.upper() == 'B':
		back()

#draw(input("Number: "), input("Color: "))
