#Danielle Tuck
#section 2

import turtle
import random

#function that draws a tree with variation in branch length and angle
#as well as a slight lean to the right
def tree(branchLen,t):
    angle = random.randint(-10, 10)
    leng = random.randint(-10, 10)
    lean = 10
    branchLen += leng
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20+lean)
        tree(branchLen-15,t)
        t.left(40+angle+lean)
        tree(branchLen-15,t)
        t.right(20+angle)
        t.backward(branchLen)


#main fucntion that picks the starting position and calls the tree function
def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(120,t)
    myWin.exitonclick()

main()
