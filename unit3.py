#By: Magnus Crooke, File name: unit3.py, Last modified 9-21-2017, this program draws a flower with clors of your choice
import turtle


def move_turtle(x, y):
    """
    this function moves turtle without drawing a line
    :param x: the "x" coordinate
    :param y: the "y" coordinate
    :return: nothing
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_hexagon(size, color):
    """

    :param size: the length of one side on the hexagon
    :param color: the fill color
    :return: draws a hexagon
    """
    turtle.color(color)
    turtle.begin_fill()

    for x in range(6):
        turtle.forward(size)
        turtle.left(60)
    turtle.end_fill()
    turtle.forward(size)
    turtle.right(60)


def main():
   
    size = getsidelenth()
    center = getCenterColor()
    pedals = getpedalColors()

    move_turtle(0, 0)
    draw_hexagon(size, center)
    turtle.right(120)
    for x in range(6):
        draw_hexagon(size, pedals)


def getsidelenth():
    """
    :return: gets the side length of one side of a hexagon
    """
    sidelenth = input("How long do you want your pedals?")
    return int(sidelenth)


def getCenterColor():
    """
    :return: gets the center pedal color
    """
    centerColor = input("What color do u want the center pedal to be?")
    return centerColor


def getpedalColors():
    """

    :return: gets the pedal color
    """
    pedalcolors = input("What color do you want the pedals to be?")
    return pedalcolors

if __name__ == '__main__':
    main()

turtle.exitonclick()
