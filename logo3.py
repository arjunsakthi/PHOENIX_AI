import turtle
import time
# Set up the screen and turtle
screen = turtle.Screen()    
#screen.screensize()
turtle.setup(width=1200, height=640)
screen.bgcolor("#2c2c2c")
screen.title("PHEONIX Logo")
turtle = turtle.Turtle()
turtle.speed(0)
turtle.hideturtle()

# Define a function to draw a rounded rectangle with a given color, dimensions, and corner radius
def draw_rounded_rect(color, width, height, radius):
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius, 90)
    turtle.forward(width - 2 * radius)
    turtle.circle(radius, 90)
    turtle.forward(height - 2 * radius)
    turtle.circle(radius, 90)
    turtle.forward(width - 2 * radius)
    turtle.circle(radius, 90)
    turtle.end_fill()

# Draw the outer rectangle
draw_rounded_rect("#ff8800", 300, 200, 30)

# Draw the inner rectangle
draw_rounded_rect("black", 280, 180, 25)

# Draw the JARVIS letters
turtle.color("white")
turtle.penup()
turtle.goto(-70, 40)
turtle.pendown()
turtle.write("P", align="center", font=("Arial", 80, "bold"))
turtle.penup()
turtle.goto(0, 40)
turtle.pendown()
turtle.write("H", align="center", font=("Arial", 80, "bold"))
turtle.penup()
turtle.goto(70, 40)
turtle.pendown()
turtle.write("E", align="center", font=("Arial", 80, "bold"))
turtle.penup()
turtle.goto(140, 40)
turtle.pendown()
turtle.write("O", align="center", font=("Arial", 80, "bold"))
turtle.penup()
turtle.goto(210, 40)
turtle.pendown()
turtle.write("N", align="center", font=("Arial", 80, "bold"))
turtle.penup()
turtle.goto(280, 40)
turtle.pendown()
turtle.write("I", align="center", font=("Arial", 80, "bold"))
turtle.penup()
turtle.goto(350, 40)
turtle.pendown()
turtle.write("X", align="center", font=("Arial", 80, "bold"))

# Draw the circles
turtle.penup()
turtle.goto(-100, -60)
turtle.pendown()
turtle.color("#ff8800")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()
turtle.penup()
turtle.goto(100, -60)
turtle.pendown()
turtle.color("#ff8800")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

# Draw the lines
turtle.penup()
turtle.goto(-90, -60)
turtle.pendown()
turtle.color("white")
turtle.setheading(45)
turtle.forward(60)
turtle.backward(30)
turtle.setheading(135)
turtle.forward(30)
turtle.backward(60)
turtle.penup()
turtle.goto(90, -60)
turtle.pendown()
turtle.color("white")
turtle.setheading(135)
turtle.forward(60)
turtle.backward(30)
turtle.setheading(45)
turtle.forward(30)
turtle.backward(60)

# Write the "AI Voice Assistant" text
turtle.penup()
turtle.goto(0, -120)
turtle.color("white")
turtle.write("AI Voice Assistant", align="center", font=("Arial", 20, "bold"))

time.sleep(2)
screen.bye()
# Keep the screen open until it is clicked
#screen.mainloop()
