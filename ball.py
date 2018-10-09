from graphics import Circle
from time import sleep
import random

class Ball(Circle):
    def __init__(self, center, size, win):
        self.center = center
        self.size = size
        self.win = win
        Circle.__init__(self, (self.center), self.size)
        self.draw(win)

    def color_ball(self):
        self.setFill('blue')



            

            
