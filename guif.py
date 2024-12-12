from tkinter import *
import subprocess
import webbrowser
import os

r = Tk()
r.title("Creativity")
r.geometry("400x500")

def runCPP():
    subprocess.run(["g++", "f.cpp", "-o", "f.out"])
    subprocess.run(["./f.out"])

def runCPP0():
    subprocess.run(["g++", "f0.cpp", "-o", "f.out0"])
    subprocess.run(["./f.out0"])

def runHTML():
    file_path = os.path.abspath('bw.html') 
    webbrowser.open(f'file://{file_path}')

btn1 = Button(r, text="Number Counter (Terminal Program).", command=runCPP).pack()
btn2 = Button(r, text="About (Terminal).", command=runCPP0).pack()
btn3 = Button(r, text="Exit", command=r.quit).pack()
btn4 = Button(r, text="Blank Website (Website)", command=runHTML).pack()

r.mainloop()
