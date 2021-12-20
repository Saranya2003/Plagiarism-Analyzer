from pyswip import Prolog
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import re



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
    i = 0
    j = 0
    arr1_slp = []
    arr2_slp = []
    doc1=txtarea1.get("1.0",END)
    doc2=txtarea2.get("1.0",END)
    #read text and cutout \n . and ,
    delimiters = "\n",".\s",".",".\n",",\s",","
    regexPattern = '|'.join(map(re.escape, delimiters))
    arr1 = re.split(regexPattern,doc1)
    arr2 = re.split(regexPattern,doc2)
    arr1_l = len(arr1)
    arr2_l = len(arr2)
    for i in range(arr1_l):
        xa = arr1[i]
        if xa != '':
            arr1_slp.append(arr1[i])
    print(arr1_slp)
    for i in range(arr2_l):
        xa = arr2[i]
        if xa != '':
            arr2_slp.append(arr2[i])
    print(arr2_slp)
    #check and calculate % of plagiarism

    #Use isub to check similarity
    result = list(prolog.query("isub('"+doc1+"', '"+doc2+"', D, [normalize(true),zero_to_one(true)]).")) #Use internal Prolog function
    print(result[0]["D"])
    res = result[0]["D"]
    res = res*100
    showresult.config(text="{:.2f}".format(res) + " % plagiarism")

#GUI for the program
ws = Tk()
ws.title("Plagiarism Analyzer")
ws.geometry("400x600")

ws['bg']='#C63785'

title=Label(text="Please open a file to check plagiarism.",font=('Arial', 16))
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