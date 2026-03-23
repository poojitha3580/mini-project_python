import tkinter as tk
import random

# window
root = tk.Tk()
root.title("Car Racing Game")

WIDTH = 400
HEIGHT = 600

canvas = tk.Canvas(root,width=WIDTH,height=HEIGHT,bg="gray")
canvas.pack()

# player car
car = canvas.create_rectangle(180,500,220,550,fill="blue")

# obstacle
obstacle = canvas.create_rectangle(190,0,210,40,fill="red")

score = 0

def move_car(event):

    x = canvas.coords(car)[0]

    if event.keysym == "Left" and x > 0:
        canvas.move(car,-20,0)

    if event.keysym == "Right" and x < WIDTH-40:
        canvas.move(car,20,0)

root.bind("<Left>",move_car)
root.bind("<Right>",move_car)

def move_obstacle():

    global score

    canvas.move(obstacle,0,10)

    ox,oy,ox2,oy2 = canvas.coords(obstacle)
    cx,cy,cx2,cy2 = canvas.coords(car)

    # collision
    if ox < cx2 and ox2 > cx and oy2 > cy:
        canvas.create_text(200,300,text="GAME OVER",font=("Arial",30),fill="white")
        return

    # reset obstacle
    if oy > HEIGHT:
        canvas.coords(obstacle,random.randint(50,350),0,random.randint(80,380),40)
        score += 1
        score_label.config(text="Score: "+str(score))

    root.after(50,move_obstacle)

score_label = tk.Label(root,text="Score: 0",font=("Arial",14))
score_label.pack()

move_obstacle()

root.mainloop()