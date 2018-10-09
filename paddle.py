
from graphics import *
from inputlistener import InputListener
from ball import Ball


class Paddle(Rectangle):
    def __init__(self, point1, point2, win, border, r_barrier):
      self.point1 = point1
      self.point2 = point2
      self.win = win
      self.border = border
      self.r_barrier = r_barrier
      Rectangle.__init__(self,(self.point1),(self.point2))
      self.draw(win)
        
    def color_paddle(self):
        self.setFill('purple')

    def move_paddle(self, key):
        if key == "Right" and self.getP2().getX() <= self.r_barrier.getP2().getX():
            self.move(15, 0)

        if key == "Left" and self.getP1().getX() >= self.border.getP1().getX():
            self.move(-15, 0)

        
            

    

        


        
        
  
