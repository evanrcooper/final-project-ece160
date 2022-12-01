from back import *
from card_example import *
from plus_four import *
from reverse import *
from skip import *
from wild_card import *

import tkinter as tk
from tkinter import *
import math

valid_cards = ('0','1','2','3','4','5','6','7','8','9','+','P','C','R','S','B')



number = None
while not number in valid_cards:
	number = input("number: ").upper()

if number in str({*range(10)}) or number == '+':
	color = input("color: ")
	drawCard(color, number)
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
