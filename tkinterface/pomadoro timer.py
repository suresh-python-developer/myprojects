from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps=0
timer_runner =None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer_runner)
    timer_label.config(text="TIMER")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_start():
    global reps
    reps = reps+1
    work_min_sec = WORK_MIN*60
    short_break_sec= SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60
    if reps%2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="BREAK",fg=PINK)
    elif reps%8 ==0:
        count_down(long_break)
        timer_label.config(text="LONG BREAK", fg=RED)
    else:
        count_down(work_min_sec)
        timer_label.config(text="WORK", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    timer=math.floor(count/60)
    timer_sec = count%60
    if timer_sec==0:
        timer_sec="00"
    if int(timer_sec)<10 and int(timer_sec)!=00:
        timer_sec=str(timer_sec)
        timer_sec="0"+timer_sec
    canvas.itemconfig(timer_text,text=f"{timer}:{timer_sec}")
    if count>0:
      global  timer_runner
      timer_runner = window.after(1000,count_down,count-1)
    else:
        timer_start()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.config(padx=100,pady=150,bg=YELLOW)

canvas = Canvas(width= 250,height=224,bg=YELLOW,highlightthickness=0 )
photo = PhotoImage(file="tomato.png")
canvas.create_image(125,112,image=photo)
timer_text = canvas.create_text(125,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


timer_label = Label(text="TIMER",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
timer_label.grid(column=1,row=0)

start_button = Button(text="START",command=timer_start,font=(FONT_NAME,20))
start_button.grid(column=0,row=2)

reset_button = Button(text="RESET",font=(FONT_NAME,20),command=reset)
reset_button.grid(column=3,row=2)

chek_mark = Label(font=(FONT_NAME,10))
chek_mark.grid(column=1,row=3)
window.mainloop()