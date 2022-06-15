import string
import tkinter
import tkinter as tkcık
from collections import Counter
from tkinter import END

myTk = tkcık.Tk()

# textcik=myFile.read()
title = myTk.title("My qute gui")
myTk.geometry("500x500")


def readFile():
    myFile = open('C:\\Users\\ibrahim\\Desktop\\Marvel.txt', 'r')
    content = myFile.readlines()
    for i in content:
        text.insert('1.0', i)
    text.pack()
    myFile.close()


def calculateAndRead():
    myFile = open('C:\\Users\\ibrahim\\Desktop\\Marvel.txt', 'r')
    t2 = myFile.readlines()
    freq = {}
    words = []
    for line in t2:
        words.append(line.split())

    for item in words:
        for i in item:
            if (i in freq):
                freq[i] += 1
            else:
                freq[i] = 1
    for allKeys in freq:
        print("\"", allKeys, "\"", end=" ")
        print(freq[allKeys], end=" ")
        print()
        str_ = (allKeys, "=", (freq[allKeys]))
        text.insert(END, str_)
        text.insert(END, "\n")

    myFile.close()


def clearToTextInput():
    text.delete("1.0", "end")


# Text adding
text = tkinter.Text(myTk, height=50, width=200, padx=5, pady=5)
text.pack()
buttonRead = tkcık.Button(master=myTk, text='Read', compound=tkcık.LEFT, width=15, command=readFile,
                          font=('Times New Roman', 20))
buttonRead.pack()
buttonCalculate = tkcık.Button(master=myTk, text='Calculate and Show', command=calculateAndRead)
buttonCalculate.pack()
btn = tkcık.Button(myTk, height=1, width=10, text="Clear", command=clearToTextInput)
btn.pack()

myTk.mainloop()