import turtle

turtle.getscreen()
turtle.pensize(5)
turtle.color('blue')

p = [
    (-200, -100),
    (-150, 100),
    (150, 100),
    (200, -100),
]

turtle.hideturtle()
turtle.penup()
turtle.goto(p[0])
turtle.pendown()

lines_t = turtle.Turtle()
lines_t.pensize(3)
lines_t.hideturtle()
lines_t.penup()
lines_t.goto(p[0])
lines_t.pendown()
for coords in p:
    lines_t.goto(coords)

for coords in p:
    t = turtle.Turtle()
    t.color('red')
    t.hideturtle()
    t.penup()
    t.setposition(coords)
    t.dot(10)

for t in range(100):
    t /= 100
    x = (1 - t)**3 * p[0][0] + 3 * t * (1 - t)**2 * p[1][0] + 3 * t**2 * (1 - t) * p[2][0] + t**3 * p[3][0]
    y = (1 - t)**3 * p[0][1] + 3 * t * (1 - t)**2 * p[1][1] + 3 * t**2 * (1 - t) * p[2][1] + t**3 * p[3][1]
    turtle.goto(x, y)

turtle.mainloop()