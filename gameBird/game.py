from PIL import Image, ImageTk
import tkinter as tk
import random
import sys


window = tk.Tk()
window.geometry('1000x600')
window.title("Flappy Bird")
x = 150
y = 300
score = 0
speed = 10
game_over = False

canvas = tk.Canvas(window, highlightthickness = 0, bg = "#00bfff")
canvas.place(relheight=1, relwidth=1)
text_score = canvas.create_text(50,50, text="0", fill="white", font=("D2 Arial outline", 22))

img_bird = Image.open("bird.png")
img_bird = ImageTk.PhotoImage(img_bird)

img_pipe_down = Image.open('pipe.png')
img_pipe_top = img_pipe_down.rotate(180)
img_pipe_down = ImageTk.PhotoImage(img_pipe_down)
img_pipe_top = ImageTk.PhotoImage(img_pipe_top)

img_reset = Image.open("rebord.png")
img_reset = ImageTk.PhotoImage(img_reset)

bird = canvas.create_image(x, y, anchor="nw", image=img_bird)
pipe_down = canvas.create_image(1200, 550, anchor="nw", image = img_pipe_down)
pipe_top = canvas.create_image(1200, 550, anchor="nw", image = img_pipe_down)

