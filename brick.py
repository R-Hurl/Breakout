from graphics import Rectangle

class Brick(Rectangle):
    def __init__(self, point1, point2, win):
        self.point1 = point1
        self.point2 = point2
        self.win = win
        Rectangle.__init__(self, (self.point1), (self.point2))
        self.draw(win)

    def color_brick(self):
        self.setFill('brown')
        self.setOutline('gray')
