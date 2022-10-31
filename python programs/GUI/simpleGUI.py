from tkinter import  *

window = Tk()  #create a window

label = Label(window, text="Welcome to Python")
button = Button(window, text="Click Me")

label.pack()  #place the label in the window
button.pack() #place the button in the window

window.mainloop()  #create an event