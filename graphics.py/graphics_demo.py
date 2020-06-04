from graphics import *
'''This is a sample client script of the graphics library from https://mcsp.wartburg.edu/zelle/python/graphics.py

Note the anchor point for most of these objects is centered.

'''

win = GraphWin("1st Windows", 800, 500)

win.setBackground(color_rgb(100, 74, 52))

point1 = Point(0,250)
point2 = Point(400,400)

line1 = Line(point1, point2)
line1.setOutline(color_rgb(254,254, 254))
line1.setWidth(4)
line1.draw(win)

rect = Rectangle(Point(10, 100),Point(200,250))
rect.setOutline('blue')
rect.setFill('red')
rect.setWidth(7)
rect.draw(win)



circle = Circle(Point(87,87), 50)
circle.setFill(color_rgb(30, 30, 30))
circle.setOutline('white')
circle.setWidth(3)
circle.draw(win)

txt = Text(Point(300,30),"some text")
txt.setTextColor('purple')
txt.setSize(30)
txt.setFace('arial')
txt.draw(win)

img = Image(Point(500, 200), 'pork.gif')
img.draw(win)

win.getMouse()
win.close()

