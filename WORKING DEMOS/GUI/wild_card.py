########
# UNO! #
########

#create window

#import libraries
import tkinter as tk
from tkinter import *
import math

def wild():
	#temporary variables for color and number on card
	#color = input("color: ")
	#card_number = input("num: ")
	bg_color = "black"
	text_color = "white"
	colors = ["red", "blue", "green", "yellow"]
	card_number = "WILD"
	
	# constants
	h = 450 #window hieght
	w = 300 #window width
	mw = 16 #margin width
	mh = 16 #margin height
	mtb = 10 #margin text shadow
	mtw = 28 #margin text width
	mth = 6 #margin text height
	ta = 0 #text angle
	r1 = 115 #radius (y)
	r2 = 195 #radius (x)
	th = math.pi/6 #rotation angle
	num = 300 #number of verties
	border = (mw+mh)/3 #border width
	
	#initialize window (as self)
	self = tk.Tk()
	self.geometry("300x450") #define window size
	self.resizable(False, False) #make window not resizable
	
	#initialize canvas (as self.canvas)
	self.canvas = Canvas(width=w, height=h, bg=bg_color)
	
	###############################################################################
	
	
	
	#loop to draw white oval
	
	pts = []
	rx1 = r1 + border
	rx2 = r2 + border
	increment = math.pi*2/num #define delta i (angle) for each iteration of the loop
	
	i = 0 #initialize i for loop (angle)
	j = 0 #initialize j for loop (index of array)
	while j < 2*num:
		pts.append((math.cos(th))*(rx1*math.cos(i)) - (math.sin(th))*(rx2*math.sin(i)) + w/2) #x
		pts.append((math.sin(th))*(rx1*math.cos(i)) + (math.cos(th))*(rx2*math.sin(i)) + h/2) #y
		i += increment #increment i
		j += 2 #increment j
	self.canvas.create_polygon(pts, fill="white") #create polygon from pts[]
	
	######################################################################################################################
	
	
	
	#draw rainbow oval
	
	#loop to draw oval
	pts = [] #initialize array of points
	increment = math.pi*2/num #define delta i (angle) for each iteration of the loop
	i = math.pi-3*increment #initialize i for loop (angle)
	j = -6 #initialize j for loop (index of array)
	
	pts = []
	pts.append(w/2)
	pts.append(h/2)
	while j <= (num/2):
		pts.append((math.cos(th))*(r1*math.cos(i)) - (math.sin(th))*(r2*math.sin(i)) + w/2) #x
		pts.append((math.sin(th))*(r1*math.cos(i)) + (math.cos(th))*(r2*math.sin(i)) + h/2) #y
		i += increment #increment i
		j += 2 #increment j
	self.canvas.create_polygon(pts, fill=colors[0])
	j -= 2
	i -= increment
	
	pts = []
	pts.append(w/2)
	pts.append(h/2)
	while j <= (num):
		pts.append((math.cos(th))*(r1*math.cos(i)) - (math.sin(th))*(r2*math.sin(i)) + w/2) #x
		pts.append((math.sin(th))*(r1*math.cos(i)) + (math.cos(th))*(r2*math.sin(i)) + h/2) #y
		i += increment #increment i
		j += 2 #increment j
	self.canvas.create_polygon(pts, fill=colors[1])
	j -= 2
	i -= increment
	
	pts = []
	pts.append(w/2)
	pts.append(h/2)
	while j <= (3*num/2):
		pts.append((math.cos(th))*(r1*math.cos(i)) - (math.sin(th))*(r2*math.sin(i)) + w/2) #x
		pts.append((math.sin(th))*(r1*math.cos(i)) + (math.cos(th))*(r2*math.sin(i)) + h/2) #y
		i += increment #increment i
		j += 2 #increment j
	self.canvas.create_polygon(pts, fill=colors[2]) 
	j -= 2
	i -= increment
	
	pts = []
	pts.append(w/2)
	pts.append(h/2)
	while j <= (num*2):
		pts.append((math.cos(th))*(r1*math.cos(i)) - (math.sin(th))*(r2*math.sin(i)) + w/2) #x
		pts.append((math.sin(th))*(r1*math.cos(i)) + (math.cos(th))*(r2*math.sin(i)) + h/2) #y
		i += increment #increment i
		j += 2 #increment j
	self.canvas.create_polygon(pts, fill=colors[3])
	
	######################################################################################################
	
	
	
	#draw rounded corners
	
	#top left
	#constants
	pts = [] #reset pts[]
	r3 = mw+mh/2 #radius of corner
	num = 150 #number of vertices
	i = math.pi #initialize i for loop (as starting angle)
	j = 0 #initialize j for loop (index for pts[])
	increment = math.pi/num #angle increment
	increment = increment/2 
	while j < 2*num:
		pts.append(r3*math.cos(i)+mw+r3) #x
		pts.append(r3*math.sin(i)+mh+r3) #y
		i += increment
		j += 2
	pts.append(mw) #corner x
	pts.append(mh) #corner y
	self.canvas.create_polygon(pts, fill="white") #draw polygon to round corner
	
	#bottom left
	pts = []
	r3 = mw+mh/2
	num = 150
	i = math.pi/2
	j = 0
	increment = math.pi/num
	increment = increment/2
	while j < 2*num:
		pts.append(r3*math.cos(i)+mw+r3)
		pts.append(r3*math.sin(i)+h-mh-r3)
		i += increment
		j += 2
	pts.append(mw)
	pts.append(h-mh)
	self.canvas.create_polygon(pts, fill="white")
	
	#top right
	pts = []
	r3 = mw+mh/2
	num = 150
	i = 3*math.pi/2
	j = 0
	increment = math.pi/num
	increment = increment/2
	while j < 2*num:
		pts.append(r3*math.cos(i)+w-mw-r3)
		pts.append(r3*math.sin(i)+mh+r3)
		i += increment
		j += 2
	pts.append(w-mw)
	pts.append(mh)
	self.canvas.create_polygon(pts, fill="white")
	
	#bottom right
	pts = []
	r3 = mw+mh/2
	num = 150
	i = 0
	j = 0
	increment = math.pi/num
	increment = increment/2
	while j < 2*num:
		pts.append(r3*math.cos(i)+w-mw-r3)
		pts.append(r3*math.sin(i)+h-mh-r3)
		i += increment
		j += 2
	pts.append(w-mw)
	pts.append(h-mh)
	self.canvas.create_polygon(pts, fill="white")
	
	##################################################################################
	
	
	
	#borders and text
	
	#draw borders
	self.canvas.create_polygon(0,0,mw,0,mw,h,0,h, fill="white")
	self.canvas.create_polygon(0,0,w,0,w,mh,0,mh, fill="white")
	self.canvas.create_polygon(w,h,w,0,w-mw,0,w-mw,h, fill="white")
	self.canvas.create_polygon(w,h,0,h,0,h-mh,w,h-mh, fill="white")
	
	#draw text
	for b in range(mtb+1):
		self.canvas.create_text(w/2-b, h/2+b, text=card_number, fill="black", font=('Helvetica 45 bold'), angle=ta) #center shadow
	self.canvas.create_text(w/2, h/2, text=card_number, fill=text_color, font=('Helvetica 45 bold'), angle=ta) #center
	#self.canvas.create_text(mw+r3+mtw, mh+r3+mth, text=card_number, fill="white", font=('Helvetica 20 bold')) #top left
	#self.canvas.create_text(w-mw-r3-mtw, h-mh-r3-mth, text=card_number, fill="white", font=('Helvetica 20 bold')) #bottom right
	
	#pack canvas
	self.canvas.pack()
	
	#start loop
	self.mainloop()
	
	#####################################################################################
