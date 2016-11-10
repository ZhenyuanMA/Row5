from graphics import *
import random
from Draw import *

def easy():
    win = GraphWin("Row 5",750,600)
    win.setCoords(0.0,0.0,750.0,600.0)
    win.setBackground('grey')
    theWhole = Rectangle(Point(50,550),Point(550,50))
    theWhole.setFill('white')
    theWhole.setOutline('grey')
    theWhole.draw(win)
    for i in range(1,10):
        line = Line(Point(50*(i+1),50),Point(50*(i+1),550))
        line.setFill('grey')
        line.draw(win)
    for i in range(1,10):
        line = Line(Point(50,50*(i+1)),Point(550,50*(i+1)))
        line.setFill('grey')
        line.draw(win)
    number = 0
    theGrades = Rectangle(Point(580,265),Point(720,225))
    theGrades.setFill('black')
    theGrades.setOutline('grey')
    theGrades.draw(win)
    Grades = Text(Point(650,245),"Grades")
    Grades.setFill('white')
    Grades.draw(win)
    theNumber = Rectangle(Point(580,165),Point(720,125))
    theNumber.setFill('black')
    theNumber.setOutline('grey')
    theNumber.draw(win)
    Number = Text(Point(650,145),number)
    Number.setFill('white')
    Number.draw(win)
    List = [['0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0']]
    Color = ["red","blue","yellow","green","orange"]
    ball = BallDraw()
    ball1 = BallDraw()
    def addBalls():
        x = 3
        while x > 0:
            i = random.randint(0, 9)
            j = random.randint(0, 9)
            if List[i][j] == '0':
                List[i][j] = Color[ball.getColor()]
                ball.Ball(i, j, List[i][j], win)
                x = x - 1
    first = True
    second = True
    add = True
    while first == True:
        while add == True:
            addBalls()
            add = False
        p = win.getMouse()
        if p.getX() > 50 and p.getX() < 550 and p.getY() > 50 and p.getY() <550:
            a = int(p.getX()/50) - 1
            b = int(p.getY()/50) - 1
            if List[a][b] != '0':
                color = Color.index(List[a][b])
                ball.HighlightedBall(a, b, Color[color], win)
                List[a][b] = color + 1
                first = False
                second = True
            else:
                first = True
                second = False
                add = False
            while second == True:
                p = win.getMouse()
                c = int(p.getX()/50) - 1
                d = int(p.getY()/50) - 1
                if List[c][d] == color + 1 :
                    ball.Ball(c, d, Color[color], win)
                    List[c][d] = Color[color]
                    first = True
                    second = False
                    add = False
                elif List[c][d] != '0':
                    ball.Ball(a, b, Color[color], win)
                    List[a][b] = Color[color]
                    color = Color.index(List[c][d])
                    ball.HighlightedBall(c, d, Color[color], win)
                    List[c][d] = color + 1
                    a = c
                    b = d
                    first = False
                    second = True
                    add = False
                elif List[c][d] == '0':
                    ball.delete(a, b, win)
                    ball.Ball(c, d, Color[color], win)
                    List[c][d] = Color[color]
                    List[a][b] = '0'
                    first = True
                    second = False
                    add = True            
        else:
            win.close()
            finish()
           
def start():
    print("Welcome to the game \"Row 5\" !")
    enter = input("\nPlease press <Enter> to start the game: ")
    easy()

def finish():
    print("="*40)
    print("Thanks for your playing!")
    input("Press <Enter> to close.")

start()
