import calendar
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *

def showCal():
    fetch_year = int(year_field.get()) 
    cal_content = calendar.calendar(fetch_year) 
    root2 = tk.Tk()
    cal_year = Label(root2, text = cal_content, font = "Consolas 10 bold") 
    cal_year.grid(row = 5, column = 1, padx = 20) 

root = tk.Tk()


root.title("CALENDAR")
root.geometry('287x219')
root.resizable(width=False, height=False)

GLabel_558 = tk.Label(root)
GLabel_558["bg"] = "#d0cece"
ft = tkFont.Font(family='Times',size=28)
GLabel_558["font"] = ft
GLabel_558["fg"] = "#333333"
GLabel_558["justify"] = "center"
GLabel_558["text"] = "CALENDAR"
GLabel_558.place(x=0,y=0,width=287,height=78)

GLabel_877 = tk.Label(root)
ft = tkFont.Font(family='Times',size=15)
GLabel_877["font"] = ft
GLabel_877["fg"] = "#333333"
GLabel_877["justify"] = "center"
GLabel_877["text"] = "ENTER YEAR"
GLabel_877.place(x=0,y=90,width=124,height=39)

GButton_325 = tk.Button(root)
GButton_325["bg"] = "#80e70f"
ft = tkFont.Font(family='Times',size=17)
GButton_325["font"] = ft
GButton_325["fg"] = "#000000"
GButton_325["justify"] = "center"
GButton_325["text"] = "SHOW CALENDAR"
GButton_325.place(x=40,y=150,width=209,height=47)
GButton_325["command"] = showCal

year_field = tk.Entry(root)
year_field["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
year_field["font"] = ft
year_field["fg"] = "#333333"
year_field["justify"] = "center"
year_field.place(x=130,y=90,width=152,height=41)

root.mainloop()