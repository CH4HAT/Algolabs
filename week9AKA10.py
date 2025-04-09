import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_snowflake(t, order - 1, size)
        t.left(60)
        koch_snowflake(t, order - 1, size)
        t.right(120)
        koch_snowflake(t, order - 1, size)
        t.left(60)
        koch_snowflake(t, order - 1, size)

def draw_snowflake(order, size):
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    
    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)
    
    screen.mainloop()

draw_snowflake(order=4, size=300)
