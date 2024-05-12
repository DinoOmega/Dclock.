# -*- coding: utf-8 -*-
"""
Created on Sun May 12 01:55:26 2024

@author: Mwila
"""

#A simple digital watch using tkinter 
import sys
from tkinter import *
import time
def tick():
    time_string = time.strftime("%I:%M:%S")
    clock.config(text=time_string)
    clock.after(200,tick)
    
root = Tk()
clock = Label(root, font = ("times", 100, "bold"), bg = "yellow")
clock.grid(row=1, column=1)
tick()
root.mainloop()