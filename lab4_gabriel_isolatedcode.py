import turtle
def draw_circles(bob, size, decrease_amount):
    for _ in range(4):
        bob.circle(size)
        size -= decrease_amount
def draw_special(bob, size, repeat, decrease_amount):
    for x in range(repeat):
        draw_circles(bob, size, decrease_amount)
        bob.right(360 / repeat)
def draw_picture_nice():
    bob = turtle.Turtle()
    bob.speed(0)
    colours = ["white", "yellow", "blue", "orange", "red"]
    decrease_amount = [4, 5, 10, 19, 20]
    for x in range(len(colours)):
        bob.color(colours[x])
        draw_special(bob, 100, 10, decrease_amount[x])
if __name__ == "__main__":
    drawing_screen = turtle.Screen()
    drawing_screen.bgcolor('black')
    draw_picture_nice()
    #draw_picture()
    drawing_screen.mainloop() # Wait for the user to close the drawing screen
