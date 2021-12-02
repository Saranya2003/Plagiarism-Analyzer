import os
#from pyswip import Prolog
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from numpy import vectorize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

files = [doc for doc in os.listdir() if doc.endswith('.txt')]
contents = [open(File).read() for File in files]
vectorize = lambda Text: TfidfVectorizer().fit_transform(Text).toarray()

similarity = lambda doc1, doc2: cosine_similarity([doc1,doc2])

vectors = vectorize(contents)
s_vectors = list(zip(files,vectors))

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

def checkPlagiarism():
    results = set()
    global s_vectors
    for file_a, text_a in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((file_a,text_a))
        del new_vectors[current_index]
        for file_b, text_b in new_vectors:
            sim_score = similarity(text_a,text_b)[0][1]
            score = file_a[0], file_b[1], sim_score
            results.add(score)
        return results

ws = Tk()
ws.title("Plagiarism Analyzer")
ws.geometry("400x600")

ws['bg']='#C63785'

title=Label(text="Please open a file to check plagiarism.")
title.pack()

txtarea1 = Text(ws,height=10)
txtarea1.pack()

pathh1 = Entry(ws)
pathh1.pack()

loadfilebtn1 = Button(ws, text="Open File 1", command=openFile1).pack()

txtarea2 = Text(ws,height=10)
txtarea2.pack()

pathh2 = Entry(ws)
pathh2.pack()

loadfilebtn2 = Button(ws, text="Open File 2", command=openFile2).pack()

plagiarismCheckbtn = Button(ws, text="Check", command=checkPlagiarism).pack()
showresult = Text(ws,width=10, height=5)
showresult.pack()
ws.mainloop()

