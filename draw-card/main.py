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
from back import *
from card_example import *
from plus_four import *
from reverse import *
from skip import *
from wild_card import *

import tkinter as tk
from tkinter import *
import math

def draw(number, color = None):
	if number in "0123456789":
		drawCard(color, number)
	elif number == '+':
		drawCard(color, "+2")
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

<<<<<<< HEAD
draw(input("Number: "), input("Color: "))
=======


number = None
while not number in valid_cards:
	number = input("number: ").upper()

if number in str({*range(10)}) or number == '+':
	color = input("color: ")
	drawCard(color, number)
#color isnt important for some cards!
elif number == 'P':
	plus4()
elif number == 'C':
	wild()
elif number == 'R':
	color = input("color: ")
	reverse(color)
elif number == 'S':
	color = input("color: ")
	skip(color)
elif number == 'B':
	back()
>>>>>>> d540d72 (added comments and attributions)
