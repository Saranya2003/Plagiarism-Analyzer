import os
from pyswip import Prolog
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import math
 
#Load prolog file
prolog = Prolog()
prolog.consult("Plagiarism Analyzer")
 
#open file 1
def openFile1():
    txtarea1.delete("1.0",END)
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh1.insert(END, tf)
    data=""
    with open(tf) as f:
        for line in f:
            data+=line
        txtarea1.insert(END,data)
    return data
 
#open file 2  
def openFile2():
    txtarea2.delete("1.0",END)
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh2.insert(END, tf)
    data=""
    with open(tf) as f:
        for line in f:
            data+=line
        txtarea2.insert(END,data)
    return data
 
#Check plagiarism function
def checkPlagiarism():
    cout = 0.0
    val = 0.0
    doc1=txtarea1.get("1.0",END)
    doc2=txtarea2.get("1.0",END)
    arr1 = doc1.strip().split("\n")
    arr2 = doc2.strip().split("\n")
    print(len(arr1))
    print(arr1)
    print(len(arr2))
    print(arr2)
    result = list(prolog.query('plagiarismCheck("'+doc1+'","'+doc2+'",Res).'))
    #print(result)
    result = result[0]
    finalres = result['Res']
    if finalres == 2:
        for x in range((len(arr1))):
            for y in range(len(arr2)):
                cout += 1.0
                result = list(prolog.query('plagiarismCheck("'+arr1[x]+'","'+arr2[y]+'",Res).'))
                result = result[0]
                finalres = result['Res']
                if finalres == 0:
                    print("0")
                    finalres = 0.0
                    val += finalres
                else:
                    print("1")
                    finalres = 1.0
                    val += finalres
        res = (val * 100)/ math.sqrt(cout)
        showresult.config(text="{:.2f}".format(res) + " % plagiarism")
    else:
        showresult.config(text="100% plagiarism")
   
    print(val)
    print(cout)
 
#GUI for the program
ws = Tk()
ws.title("Plagiarism Analyzer")
ws.geometry("400x600")
 
ws['bg']='#C63785'
 
title=Label(text="Please open a file to check plagiarism.")
title.pack()
 
#text display 1
txtarea1 = Text(ws,height=10)
txtarea1.pack()
 
#file dirctory 1
pathh1 = Entry(ws)
pathh1.pack()
 
loadfilebtn1 = Button(ws, text="Open File 1", command=openFile1).pack()
 
#text display 2
txtarea2 = Text(ws,height=10)
txtarea2.pack()
 
#file dirctory 2
pathh2 = Entry(ws)
pathh2.pack()
 
loadfilebtn2 = Button(ws, text="Open File 2", command=openFile2).pack()
 
 
showresult = Label(ws, text = "                                   ")
showresult.pack()
plagiarismCheckbtn = Button(ws, text="Check", command=checkPlagiarism).pack()
 
 
 
ws.mainloop()
