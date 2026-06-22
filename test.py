import tkinter as tk
from tkinter import messagebox
import math

text = []
edited_text = "".join(map(str, text))


def add(num):
    display.insert(tk.END, num)
    text.append(str(num))


def equal():
    try:
        edited_text = "".join(map(str, text))
        evaled = eval(edited_text)
        print(text)
        print(edited_text)
        finall = f"{evaled:,}"
       
        display.delete(0, tk.END)
        display.insert(tk.END, finall)
        text.clear()
        text.append(evaled)
    except:
        pass
   


def plus():
    display.insert(tk.END, "+")
    text.append("+")


def minus():
    display.insert(tk.END, "-")
    text.append("-")


def division():
    display.insert(tk.END, "÷")
    text.append("/")


def multiplation():
    display.insert(tk.END, "×")
    text.append("*")


def dot():
    display.insert(tk.END, ".")
    text.append(".")


def clear():
    text.clear()
    display.delete(0, tk.END)


window = tk.Tk()
window.resizable(False, False)
window.config(bg="#1e1e1e")
window.geometry("175x300")
window.eval("tk::PlaceWindow . center")
display = tk.Entry(window, font=("Arial", 20, "bold"), bg="#848181", justify="right", width=10)
display.place(x=10, y=20)
tk.Button(window, text="7", font=("Arial", 20, "bold"), bg="#848181",
 command=lambda  : add(7)
 ).place(y=70, x=10)
tk.Button(window, text="8", font=("Arial", 20, "bold"), bg="#848181",
 command=lambda  : add(8)
 ).place(y=70, x=50)
tk.Button(window, text="9", font=("Arial", 20, "bold"), bg="#848181",
 command=lambda  : add(9)
 ).place(y=70, x=90)
tk.Button(window, text="4", font=("Arial", 20, "bold"), bg="#848181",
 command=lambda  : add(4)
 ).place(y=125, x=10)
tk.Button(window, text="5", font=("Arial", 20, "bold"), bg="#848181",
 command=lambda  : add(5)
 ).place(y=125, x=50)
tk.Button(window, text="6", font=("Arial", 20, "bold"), bg="#848181",
 command=lambda  : add(6)
 ).place(y=125, x=90)
tk.Button(window, text="1", font=("Arial", 20, "bold"), bg="#848181",
 command=lambda  : add(1)
 ).place(y=180, x=10)
tk.Button(window, text="2", font=("Arial", 20, "bold"), bg="#848181",
 command=lambda  : add(2)
 ).place(y=180, x=50)
tk.Button(window, text="3", font=("Arial", 20, "bold"), bg="#848181",
 command=lambda  : add(3)
 ).place(y=180, x=90)
tk.Button(window, text="0", font=("Arial", 20, "bold"), bg="#848181",
 command=lambda  : add(0)
 ).place(y=235, x=50)
tk.Button(window, text="=", font=("Arial", 20, "bold"), bg="#848181",
 command=equal).place(y=70, x=130)
tk.Button(window, text="+", font=("Arial", 20, "bold"), bg="#848181",
 command=plus).place(y=125, x=130)
tk.Button(window, text="-", font=("Arial", 20, "bold"), bg="#848181",
 command=minus, width=2).place(y=180, x=130)
tk.Button(window, text="÷", font=("Arial", 20, "bold"), bg="#848181",
 command=division, width=2).place(y=235, x=130)
tk.Button(
    window,
    text="×",
    font=("Arial", 20, "bold"),
    bg="#848181",
    command=multiplation,
).place(y=235, x=90)
tk.Button(
    window,
    text="c",
    font=("Arial", 20, "bold"),
    bg="#848181",
    command=clear,
).place(y=235, x=10)
tk.Button(window, text=".", bg="#848181", command=dot).place(y=235, x=50)
window.mainloop()
