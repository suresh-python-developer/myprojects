from tkinter import  *

window = Tk()
window.title("km converter")
window.minsize(width=500,height=300)
window.config(padx=100,pady=100)

indication_label = Label(text="is equal to")
indication_label.grid(column=50,row=80)

miles_input = Entry()
miles_input.grid(column=70, row= 50)
miles_label = Label(text="miles")
miles_label.grid(column=100,row=50)

# input = Entry()
# input.grid(row=0,column=3)
km_label = Label(text="in km")
km_label.grid(column=100,row=80)

def calculate():
    miles = float( miles_input.get())
    km = miles*1.6
    output_label = Label(text=str(km))
    output_label.grid(column=70,row=80)
button = Button(text="calculate",command=calculate)
button.grid(column=70,row=100)


window.mainloop()