#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in colision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="orange")
player = drawpad.create_rectangle(240,240,260,260, fill="#6f00ff")



class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
       	        self.ueber = Button(self.myContainer1)
       	        self.ueber.configure(text="ueber", background= "red")
       	        self.ueber.grid(row=0,column=1)
       	        self.ueber.bind("<Button-1>", self.ueberClicked)
       	    
       	        self.unter = Button(self.myContainer1)
       	        self.unter.configure(text="unter", background= "red")
       	        self.unter.grid(row=2,column=1)
       	        self.unter.bind("<Button-1>", self.unterClicked)
       	    
       	        self.linke = Button(self.myContainer1)
       	        self.linke.configure(text="linke", background= "red")
       	        self.linke.grid(row=1,column=0)
       	        self.linke.bind("<Button-1>", self.linkeClicked)
       	    
       	        self.recht = Button(self.myContainer1)
       	        self.recht.configure(text="recht", background= "red")
       	        self.recht.grid(row=1,column=2)
       	        self.recht.bind("<Button-1>", self.rechtClicked)
	  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		self.animate()
		

		
	def ueberClicked(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
		global target
		global player
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
                tx1, ty1, tx2, ty2 = drawpad.coords(target)
		# Ensure that we are doing our collision detection
		if y1 >= 0:
		    drawpad.move(player, 0, -6.9)
		    
		    
	def linkeClicked(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
		global target
		global player
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
                tx1, ty1, tx2, ty2 = drawpad.coords(target)
		# Ensure that we are doing our collision detection
		if x1 >= 0:
		    drawpad.move(player, -6.9, 0)
		    
	def unterClicked(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
		global target
		global player
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
                tx1, ty1, tx2, ty2 = drawpad.coords(target)
		# Ensure that we are doing our collision detection
		if y2 <= 320:
		    drawpad.move(player, 0, 6.9)
		    
	def rechtClicked(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
		global target
		global player
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
                tx1, ty1, tx2, ty2 = drawpad.coords(target)
		# Ensure that we are doing our collision detection
		if x2 <= 480:
		    drawpad.move(player, 6.9, 0)
		    
	def animate(self):
            global direction
            global target
            x1, y1, x2, y2 = drawpad.coords(target)
            if x2 > int(drawpad.winfo_width())+40: 
                direction = - 840
            elif x1 < 0:
                direction = 6.9
            drawpad.move(target,direction,0)
            didWeHit = self.collisionDetect()
            if(didWeHit == False):
                # We made contact! Stop our animation!
                drawpad.after(1, self.animate)
            else:
                drawpad.itemconfig(target, fill="red")
    
        # After we move our object!
                
	# Use a function to do our collision detection
	# This way we only have to write it once, and call it from
	# every button click function.
	def collisionDetect(self):
            global oval
	    global drawpad
            x1,y1,x2,y2 = drawpad.coords(player)
            global target
            tx1,ty1,tx2,ty2 = drawpad.coords(target)
            if (x1 >= tx1 and y1 >= ty1) and (x2 <= tx2 and y2 <= ty2):
                return True
            else:
                return False

                # Do your if statement - remember to return True if successful!
                
	    
		
myapp = MyApp(root)

root.mainloop()