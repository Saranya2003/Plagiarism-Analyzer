#from pyswip import Prolog
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 

def openFile():
    tf = askopenfile(
        initialdir="C:/Users/Saranya Prasertsang/Desktop/Saranya/SE/AI/Project AI/Plagiarism-Analyzer", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()
def checkPlagiarism():
    pass

ws = Tk()
ws.title("Plagiarism Analyzer")

ws['bg']='#C63785'

txtarea = Text(ws, width=40, height=20)
txtarea.pack(pady=20)

pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)


Button(
    ws, 
    text="Open File 1", 
    command=openFile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)

txtarea2 = Text(ws, width=40, height=20)
txtarea2.pack(pady=20)

pathh2 = Entry(ws)
pathh2.pack(side=LEFT, expand=True, fill=X, padx=20)

Button(
    ws, 
    text="Open File 2", 
    command=openFile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)

Button(
    ws, 
    text="Compare", 
    command=checkPlagiarism
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)
ws.mainloop()