#from pyswip import Prolog
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 

def openFile1():
    tf = askopenfile(
        initialdir="C:/Users/Saranya Prasertsang/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh1.insert(END, tf)
    tf = open(tf,'r')
    data = tf.read()
    txtarea1.insert(END, data)
    tf.close()
def openFile2():
    tf = askopenfile(
        initialdir="C:/Users/Saranya Prasertsang/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh2.insert(END, tf)
    tf = open(tf,'r')
    data = tf.read()
    txtarea2.insert(END, data)
    tf.close()
def checkPlagiarism():
    pass

ws = Tk()
ws.title("Plagiarism Analyzer")
ws.resizable(False,False)

ws['bg']='#C63785'

txtarea1 = Text(ws, width=20, height=20)
txtarea1.pack()

pathh1 = Entry(ws)
pathh1.pack()

loadfilebtn1 = Button(ws, text="Open File 1", command=openFile1).pack()

txtarea2 = Text(ws, width=20, height=20)
txtarea2.pack()

pathh2 = Entry(ws)
pathh2.pack()

loadfilebtn2 = Button(ws, text="Open File 2", command=openFile2).pack()

plagiarismCheckbtn = Button(ws, text="Check", command=checkPlagiarism).pack()
showresult = Text(ws, width=20, height=20)
showresult.pack()
ws.mainloop()

