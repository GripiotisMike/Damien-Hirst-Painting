import turtle as t
import random
import colorgram

colors = colorgram.extract('dot painting.jpg', 10)
t.colormode(255)
color_list = []
for i in range(len(colors)):
    rgb = colors[i].rgb
    red = rgb.r
    green = rgb.g
    blue = rgb.b
    color_list.append((red, green, blue))


color_list = [(224, 162, 69), (228, 240, 235), (19, 44, 82), (133, 62, 85), (171, 65, 45), (125, 39, 60), (23, 85, 61)]


def dot_paint(distance, canvas):
    tim.pensize(12)
    for i in range(0, canvas, distance):
        tim.color(random.choice(color_list))
        tim.pendown()
        tim.circle(6)
        tim.penup()
        tim.forward(dist)


tim = t.Turtle()
tim.penup()
tim.speed("fastest")
start_pos = [-500, -350]
dist = 50
tim.setpos(start_pos[0], start_pos[1])
for i in range(0, 700, dist):
    dot_paint(15, 300)
    tim.penup()
    start_pos[1] += dist
    tim.setpos(start_pos[0],start_pos[1])
    tim.pendown()


screen = t.Screen()
screen.exitonclick()
