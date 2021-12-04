import os
from pyswip import Prolog
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from numpy import vectorize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Define file directory and attribute in plagiarism checking function
files = [doc for doc in os.listdir() if doc.endswith('.txt')]
contents = [open(File).read() for File in files]
vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()

similarity = lambda doc1, doc2: cosine_similarity([doc1,doc2])

vectors = vectorize(contents)
s_vectors = list(zip(files,vectors))
#Load prolog file
prolog = Prolog()
prolog.consult("Plagiarism Analyzer")

#open file 1
def openFile1():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh1.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    txtarea1.insert(END, data)
    tf.close()
#open file 2   
def openFile2():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh2.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    txtarea2.insert(END, data)
    tf.close()
#Check plagiarism
def checkPlagiarism():
    global s_vectors
    for file_a, text_a in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((file_a,text_a))
        del new_vectors[current_index]
        for file_b, text_b in new_vectors:
            sim_score = similarity(text_a,text_b)[0][1]
            sim_score = "%.2f" %sim_score
            score = "Plagiarize result: "+str(sim_score)
    showresult.config(text=score)

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

