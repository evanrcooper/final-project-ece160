import tkinter as tk
from tkinter import *
import math

color = input("color: ")
card_number = input("num: ")

h = 450
w = 300
mw = 16
mh = 16
mt = 4

self = tk.Tk()
self.geometry("300x450")
self.resizable(False, False)

self.canvas = Canvas(width=w, height=h, bg=color)

pts = []
r1 = 115
r2 = 195
th = math.pi/6
num = 300

i = 0
j = 0
increment = math.pi*2/num
while j < 2*num:
	pts.append((math.cos(th))*(r1*math.cos(i)) - (math.sin(th))*(r2*math.sin(i)) + w/2)
	pts.append((math.sin(th))*(r1*math.cos(i)) + (math.cos(th))*(r2*math.sin(i)) + h/2)
	i += increment
	j += 2
self.canvas.create_polygon(pts, fill="white")

pts = []
r3 = mw+mh/2
num = 150
i = math.pi
j = 0
increment = math.pi/num
increment = increment/2
while j < 2*num:
	pts.append(r3*math.cos(i)+mw+r3)
	pts.append(r3*math.sin(i)+mh+r3)
	i += increment
	j += 2
pts.append(mw)
pts.append(mh)
self.canvas.create_polygon(pts, fill="white")

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

pts = []
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

self.canvas.create_polygon(0,0,mw,0,mw,h,0,h, fill="white")
self.canvas.create_polygon(0,0,w,0,w,mh,0,mh, fill="white")
self.canvas.create_polygon(w,h,w,0,w-mw,0,w-mw,h, fill="white")
self.canvas.create_polygon(w,h,0,h,0,h-mh,w,h-mh, fill="white")

self.canvas.create_text(w/2+mt, h/2+mt, text=card_number, fill="black", font=('Helvetica 55 bold'))
self.canvas.create_text(w/2, h/2, text=card_number, fill=color, font=('Helvetica 55 bold'))
self.canvas.create_text(mw+r3, mh+r3+mt, text=card_number, fill="white", font=('Helvetica 20 bold'))
self.canvas.create_text(w-mw-r3, h-mh-r3, text=card_number, fill="white", font=('Helvetica 20 bold'))

self.canvas.pack()

self.mainloop()
