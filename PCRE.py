import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog
import tkinter
import re
import Needleman
from Needleman import needle

main = tkinter.Tk()
main.title("Machine Learning Techniques Applied To Detect Cyber Attacks On Web Applications")
main.geometry("1200x600")

train = []
test = []
global train_file
global test_file
global true_positive
global true_negative

def readTrain():
   text.delete('1.0', END)
   strs = ""
   global train_file
   train_file = askopenfilename(initialdir = "train")
   with open(train_file, "r") as file:
    for line in file:
       line = line.strip('\n')
       x = re.findall("[a-z]+[:.].*?(?=\s)", line)
       strs = strs.join(x)
       if strs.startswith("http"):
          train.append(strs)
          text.insert(END,strs+"\n");
   print("Train loaded");

def readTest():
   text.delete('1.0', END)
   strs = ""
   test.clear()
   global test_file
   test_file = askopenfilename(initialdir = "test")
   with open(test_file, "r") as file:
    for line in file:
       line = line.strip('\n')
       x = re.findall("[a-z]+[:.].*?(?=\s)", line)
       strs = strs.join(x)
       if strs.startswith("http"):
          test.append(strs)
          text.insert(END,strs+"\n");
   print("Test loaded");

def Needleman():
  global true_positive
  global true_negative
  true_positive = 0
  true_negative = 0
  text.delete('1.0', END)
  for t in test: 
    sim = 0
    for r in train:
      value  = needle(r,t)
      if value > sim:
         sim = value
    if sim < 70:
      text.insert(END,str(sim)+" "+t+" contains attack signatures\n\n");
      true_negative = true_negative + 1
    if sim >= 70:
      text.insert(END,str(sim)+" "+t+" does not contains attack signatures\n\n");
      true_positive = true_positive + 1

def graph():
  global true_positive
  true_pos = (true_positive/len(test)) * 100;
  true_neg = (true_negative/len(test)) * 100;
  height = [true_pos,true_neg]
  bars = ('True Positive','True Negative')
  y_pos = np.arange(len(bars))
  plt.bar(y_pos, height)
  plt.xticks(y_pos, bars)
  plt.show()

trainbutton = Button(main, text="Upload Train Dataset", command=readTrain)
trainbutton.grid(row=0)

testbutton = Button(main, text="Upload Test Dataset", command=readTest)
testbutton.grid(row=1)

datasetbutton = Button(main, text="Run Needleman-Wunsch Dissimilarites", command=Needleman)
datasetbutton.grid(row=2)

graphbutton = Button(main, text="Training Samples Vs TP Rate", command=graph)
graphbutton.grid(row=3)

text=Text(main,height=30,width=150)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.grid(row=8)

main.mainloop()