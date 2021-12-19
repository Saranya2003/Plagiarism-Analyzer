import os
from pyswip import Prolog
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from difflib import SequenceMatcher




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
    doc1=txtarea1.get("1.0",END)
    doc2=txtarea2.get("1.0",END)
    print(list(prolog.query('plagiarismCheck("'+doc1+'"="'+doc2+'", Res).')))
    #result = SequenceMatcher(None,doc1,doc2).ratio()
    #result = "%.2f"%(result)
    #plag_result = "Plagiarism Score : "+str(result)
    #showresult.config(text=plag_result)
    #print(list(prolog.query('("'+doc1+'" = "'+doc2+'", X=1); ("'+doc1+'" \= "'+doc2+'", X=2).')))
    result = list(prolog.query('plagiarismCheck("'+doc1+'","'+doc2+'",Res).'))
    result = result[0]
    finalres = result['Res']
    
    if finalres == 2:
        showresult.config(text="Not plagiarism")
    else:
        showresult.config(text="plagiarism")




    ####
    #result = list(prolog.query("isub('"+doc1+"', '"+doc2+"', D, [normalize(true),zero_to_one(true)])."))
    #print(result[0]["D"]) #Use internal Prolog function
    #showresult.config(text=result)
    ####

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

