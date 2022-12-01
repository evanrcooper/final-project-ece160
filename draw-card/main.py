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

draw(input("Number: "), input("Color: "))
