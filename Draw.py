from graphics import *
import random

class BallDraw(object):
        
    def getColor(self):
        color = random.randint(0, 4)
        self.color = color
        return color
    
    def Ball(self, x, y, color, win):
        self.x = 25 + 50 * (x + 1)
        self.y = 25 + 50 * (y + 1)
        circle = Circle(Point(self.x, self.y), 19)
        circle.setOutline("black")
        circle.setWidth(1)
        circle.setFill(color)
        circle.draw(win)

    def HighlightedBall(self, x, y, color, win):
        self.x = 25 + 50 * (x + 1)
        self.y = 25 + 50 * (y + 1)
        circle = Circle(Point(self.x, self.y), 16)
        circle.setOutline("black")
        circle.setWidth(4)
        circle.setFill(color)
        circle.draw(win)

    def delete(self, x, y, win):
        self.x = 50 * (x + 1)
        self.y = 50 * (y + 1)
        Rec = Rectangle(Point(self.x, self.y), Point(self.x + 50, self.y + 50))
        Rec.setOutline("grey")
        Rec.setFill("white")
        Rec.draw(win)
        
        
