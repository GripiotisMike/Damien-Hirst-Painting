import turtle as t
import random
import colorgram

# Extract 10 most prominent colors from the image using colorgram
colors = colorgram.extract('dot painting.jpg', 10)

# Convert colorgram colors to RGB tuples and store them in color_list
color_list = []
for color in colors:
    rgb = color.rgb
    color_list.append((rgb.r, rgb.g, rgb.b))

# Predefined color palette
color_list = [(224, 162, 69), (228, 240, 235), (19, 44, 82), (133, 62, 85), 
              (171, 65, 45), (125, 39, 60), (23, 85, 61)]

# Function to draw a series of dots spaced by 'distance' on the canvas
def dot_paint(distance, canvas):
    tim.pensize(12)  # Set the pen size for the dots
    for _ in range(int(canvas / distance)):  # Loop to draw multiple dots
        tim.color(random.choice(color_list))  # Pick a random color from the color list
        tim.pendown()
        tim.circle(6)  # Draw a small circle (dot)
        tim.penup()
        tim.forward(distance)  # Move forward by the specified distance between dots

# Set up the turtle screen and turtle object
tim = t.Turtle()
tim.penup()  # Don't draw lines as the turtle moves to the start position
tim.speed("fastest")  # Set speed to fastest for drawing efficiency

# Starting position for the turtle
start_pos = [-500, -350]
dist = 50  # Distance between dots
tim.setpos(start_pos[0], start_pos[1])  # Set the turtle's starting position

# Create a dot painting by moving the turtle and calling dot_paint
for row in range(10):  # Number of rows of dots
    dot_paint(dist, 300)  # Draw a row of dots
    tim.penup()
    start_pos[1] += dist  # Move the turtle down for the next row
    tim.setpos(start_pos[0], start_pos[1])  # Reset the turtle position for the next row
    tim.pendown()

# Set up the screen to wait for a click to exit
screen = t.Screen()
screen.exitonclick()  # Wait until the user clicks to close the window
