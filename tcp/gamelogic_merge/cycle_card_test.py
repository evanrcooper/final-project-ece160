# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
import math
# creates a Tk() object
master = Tk()
# list = [*range(1,11)]
# sets the geometry of main
# root window
master.geometry("500x500")
num = -1
arr = ["+1","+2","+3","+4","JPT3"]
master.canvas = Canvas(width=300, height=450, bg="black")

def getNum():
	global num
	num += 1
	return num % len(arr)

# function to open a new window
# on a button click
#nextCard(xxx)
def nextCard():
	master.canvas.delete('all')
	#temporary variables for color and number on card
	color = "white"
	colors = ["red", "blue", "yellow", "green"]
	card_number_center = "\u25AE"
	#card_number_corner = xxx
	card_number_corner = arr[getNum()]
	
	# constants
	h = 450 #window hieght
	w = 300 #window width
	mw = 16 #margin (width)
	mh = 16 #margin (height)
	mt = 4 #margin (text, width)
	mtb = 10
	offsetw0 = 10
	offseth0 = 20
	offsetw1 = -10
	offseth1 = -20
	offsetw2 = 35
	offseth2 = -40
	offsetw3 = -35
	offseth3 = 40
	offsetw = 5
	
	###############################################################################
	
	#draw oval
	
	#initialize canvas (as master.canvas)
	#global master.canvas
	
	#constants
	pts = [] #initialize array of points
	r1 = 115 #radius (y)
	r2 = 195 #radius (x)
	th = math.pi/6 #rotation angle
	num = 300 #number of verties
	
	#loop to draw oval
	i = 0 #initialize i for loop (angle)
	j = 0 #initialize j for loop (index of array)
	increment = math.pi*2/num #define delta i (angle) for each iteration of the loop
	while j < 2*num:
		pts.append((math.cos(th))*(r1*math.cos(i)) - (math.sin(th))*(r2*math.sin(i)) + w/2) #x
		pts.append((math.sin(th))*(r1*math.cos(i)) + (math.cos(th))*(r2*math.sin(i)) + h/2) #y
		i += increment #increment i
		j += 2 #increment j
	master.canvas.create_polygon(pts, fill="white") #create polygon from pts[]
	
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
	master.canvas.create_polygon(pts, fill="white") #draw polygon to round corner
	
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
	master.canvas.create_polygon(pts, fill="white")
	
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
	master.canvas.create_polygon(pts, fill="white")
	
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
	master.canvas.create_polygon(pts, fill="white")
	
	##################################################################################
	
	
	
	#borders and text
	
	#draw borders
	master.canvas.create_polygon(0,0,mw,0,mw,h,0,h, fill="white")
	master.canvas.create_polygon(0,0,w,0,w,mh,0,mh, fill="white")
	master.canvas.create_polygon(w,h,w,0,w-mw,0,w-mw,h, fill="white")
	master.canvas.create_polygon(w,h,0,h,0,h-mh,w,h-mh, fill="white")
	
	#draw text
	for b in range(mtb+1):
		master.canvas.create_text(w/2+offsetw3-b, h/2+offseth3+b, text=card_number_center, fill="black", font=('Helvetica 55 bold'))
		master.canvas.create_text(w/2+offsetw3+offsetw-b, h/2+offseth3+b, text=card_number_center, fill="black", font=('Helvetica 55 bold')) 
	for b in range(mtb+1):
		master.canvas.create_text(w/2+offsetw2-b, h/2+offseth2+b, text=card_number_center, fill="black", font=('Helvetica 55 bold'))
		master.canvas.create_text(w/2+offsetw2+offsetw-b, h/2+offseth2+b, text=card_number_center, fill="black", font=('Helvetica 55 bold'))
	for b in range(mtb+1):
		master.canvas.create_text(w/2+offsetw1-b, h/2+offseth1+b, text=card_number_center, fill="black", font=('Helvetica 55 bold')) 
		master.canvas.create_text(w/2+offsetw1+offsetw-b, h/2+offseth1+b, text=card_number_center, fill="black", font=('Helvetica 55 bold'))
	for b in range(mtb+1):
		master.canvas.create_text(w/2+offsetw0-b, h/2+offseth0+b, text=card_number_center, fill="black", font=('Helvetica 55 bold')) 
		master.canvas.create_text(w/2+offsetw0+offsetw-b, h/2+offseth0+b, text=card_number_center, fill="black", font=('Helvetica 55 bold')) 
	master.canvas.create_text(w/2+offsetw3, h/2+offseth3, text=card_number_center, fill=colors[3], font=('Helvetica 55 bold'))
	master.canvas.create_text(w/2+offsetw3+offsetw, h/2+offseth3, text=card_number_center, fill=colors[3], font=('Helvetica 55 bold'))
	master.canvas.create_text(w/2+offsetw2, h/2+offseth2, text=card_number_center, fill=colors[2], font=('Helvetica 55 bold'))
	master.canvas.create_text(w/2+offsetw2+offsetw, h/2+offseth2, text=card_number_center, fill=colors[2], font=('Helvetica 55 bold'))
	master.canvas.create_text(w/2+offsetw1, h/2+offseth1, text=card_number_center, fill=colors[1], font=('Helvetica 55 bold')) 
	master.canvas.create_text(w/2+offsetw1+offsetw, h/2+offseth1, text=card_number_center, fill=colors[1], font=('Helvetica 55 bold'))
	master.canvas.create_text(w/2+offsetw0, h/2+offseth0, text=card_number_center, fill=colors[0], font=('Helvetica 55 bold')) 
	master.canvas.create_text(w/2+offsetw0+offsetw, h/2+offseth0, text=card_number_center, fill=colors[0], font=('Helvetica 55 bold')) 
	master.canvas.create_text(mw+r3, mh+r3+mt, text=card_number_corner, fill="white", font=('Helvetica 20 bold')) #top left
	master.canvas.create_text(w-mw-r3, h-mh-r3, text=card_number_corner, fill="white", font=('Helvetica 20 bold')) #bottom right
	
	#pack canvas
	master.canvas.pack()
	
	#####################################################################################
	


label = Label(master,
			text ="This is the main window")

label.pack(pady = 10)

# a button widget which will open a
# new window on button click
#xxx = "LOL"
btn = Button(master,
			text ="Click To Cycle Next Card",
			command = nextCard)
btn.pack(pady = 10)

# mainloop, runs infinitely
master.mainloop()
