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
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")



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
		

		
	def ueberClicked(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
                tx1, ty1, tx2, ty2 = drawpad.coords(target)
		# Ensure that we are doing our collision detection
		if y1 >= 0:
		    drawpad.move(player, 0, -6.9)
		    
		# After we move our object!
                didWeHit = collisionDetect()
                if(didWeHit == True):
                    # We made contact! Stop our animation!
                    print "Do something"
	# Use a function to do our collision detection
	# This way we only have to write it once, and call it from
	# every button click function.
	def collisionDetect(self):
                global oval
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)

                # Do your if statement - remember to return True if successful!
                
	    
		
myapp = MyApp(root)

root.mainloop()