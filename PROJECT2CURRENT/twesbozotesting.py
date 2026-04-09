from logging import root
from PIL import Image
import os
file_directory = (os.getcwd())
import turtle
import p2constants
import PIL.ImageGrab
import tkinter as tk
screen = turtle.Screen()
root = screen.getcanvas().winfo_toplevel()
root.attributes('-fullscreen', True)
screen.setup(width=1000, height=700)
screen.title("project 2")
screen.bgcolor("black")
screen.listen()
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.pencolor("yellow")
player.speed(p2constants.player_speed)
psize = 1
psize == p2constants.pen_size
def move_forward():
    player.forward(p2constants.movement_distance)
def move_backward():
    player.backward(p2constants.movement_distance)
def turn_left():
    player.speed(0)
    player.left(90)
    player.speed(p2constants.player_speed)
def slow_turn_left():
    player.speed(0)
    player.left(p2constants.slow_turn_angle)
    player.speed(p2constants.player_speed)
def turn_right():
    player.speed(0)
    player.right(90)
    player.speed(p2constants.player_speed)
def slow_turn_right():
    player.speed(0)
    player.right(p2constants.slow_turn_angle)
    player.speed(p2constants.player_speed)
def trail_on():
    player.fillcolor(player.pencolor())
    player.begin_fill()
    player.pendown()
def trail_off():
    player.penup()
    player.end_fill()
def open_colour_picker():
    import tkinter as tk
    from tkinter import colorchooser
    root = tk.Tk()
    root.withdraw()
    color_code = colorchooser.askcolor(title="pick trail/fill colour")
    if color_code[1] is not None:
        player.pencolor(color_code[1])
        player.fillcolor(color_code[1])
    root.destroy()
def take_screenshot():
    player.hideturtle()
    root.config(cursor="none")
    save_directory = r"screenshots"
    PIL.ImageGrab.grab().save(os.path.join(save_directory, "screenshot.png"))
    root.config(cursor="arrow")
    player.showturtle()
def clear_screen():
    player.clear()
def undo():
    player.undo()
def leave_program():
    screen.bye()
def size_up():
    psize += 1
    player.pensize(psize)
def size_down():
    psize -= 1
    if psize < 1:
        psize = 1
    player.pensize(psize)
def print_pen_size():
    print(player.pensize())
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.onkeypress(slow_turn_left, "q")
screen.onkeypress(slow_turn_right, "e")
screen.onkey(trail_on, "r")
screen.onkey(trail_off, "t")
screen.onkey(open_colour_picker, "c")
screen.onkey(clear_screen, "v")
screen.onkeypress(undo, "z")
screen.onkeypress(leave_program, "x")
screen.onkey(take_screenshot, "p")
screen.onkeypress(size_up, "1")
screen.onkeypress(size_down, "2")
screen.onkey(print_pen_size, "3")
root.mainloop()
screen.mainloop()