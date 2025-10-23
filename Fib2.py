#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 10:21:35 2022

@author: gourangsingh
"""

from tkinter import *
root = Tk()


root.title("Fibonacci")
root.geometry("600x400")


label_series = Label(root, text="Fibonacci Series : ")
label_flower = Label(root)
label_spiral = Label(root)

def Fibonacci():
    
    num = 10
    first_no=0
    second_no = 1
    sum = 0
    counter = 1
    
    while(counter <= num):
        
        label_series["text"] += str(sum) + " "
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        
        label_flower["text"] = "The flower has fully bloomed"
        label_spiral["text"] = "The spirals in the right direction are " + str(first_no) + " and the spirals in the left direction are " + str(second_no) + "\n. The total number of spirals are " + str(sum)
        
button = Button(root, text="Fibonacci Series", command = Fibonacci)
button.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()
        
        

root.mainloop()