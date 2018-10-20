#-------------------------------------------------------------------------------
# Name:        GCSE Revision Quiz
# Purpose:     To be a revision source for all GCSE subjects
#
# Author:      Sprouse; Joel Sprouse
#
# Created:     04/06/2018
# Modified:    04/06/2018
# Copyright:   (c) Sprouse 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
##Imports##
import random
from tkinter import *

##Subject Commands##
def EngLang():
    subjectsList.append("Eng Lang")
def EngLit():
    subjectsList.append("Eng Lit")
def Maths():
    subjectsList.append("Maths")
def Biology():
    subjectsList.append("Biology")
def Chemistry():
    subjectsList.append("Chemistry")
def Physics():
    subjectsList.append("Physics")
def IT():
    subjectsList.append("ICT")
def BS():
    subjectsList.append("Business")
def MS():
    subjectsList.append("Media")
def RE():
    subjectsList.append("Religious Education")

##Subject Questions Lists##
EngLangQs = [""]
EngLitQs = [""]
MathsQs = [""]
BiologyQs = ["What is the role of the nucleus?"]

##Program##
root = Tk()
hi = Label(root, text="""Welcome to GCSE Revision Quiz
""")
hi.pack()

#root.mainloop()

v=IntVar()
subjectsList =['']
EngLangQuery = Checkbutton(root, text="English Language", command=EngLang) 
EngLangQuery.pack()
EngLitQuery = Checkbutton(root, text="English Literature", command=EngLit)
EngLitQuery.pack()
MathsQuery = Checkbutton(root, text="Maths", command=Maths)
MathsQuery.pack()
BiologyQuery = Checkbutton(root, text="Biology", command=Biology)
BiologyQuery.pack()
ChemistryQuery = Checkbutton(root, text="Chemistry", command=Chemistry)
ChemistryQuery.pack()
PhysicsQuery = Checkbutton(root, text="Physics", command=Physics)
PhysicsQuery.pack()
ITQuery = Checkbutton(root, text="ICT/Computer Science", command=IT)
ITQuery.pack()
MSQuery = Checkbutton(root, text="Media Studies", command=MS)
MSQuery.pack()
BSQuery = Checkbutton(root, text="Business Studies", command=BS)
BSQuery.pack()
REQuery = Checkbutton(root, text="Religious Education", command=RE)
REQuery.pack()
button=Button(root, text="Done", command=root.destroy)
button.pack()
root.mainloop()

subjectsList = str(subjectsList)
print(subjectsList + " have been selected")


# For testing purposes
if "Biology" in subjectsList:
   BioQ1 = label(text=random.choice(BiologyQs))
   BioQ1.pack()
   root.mainloop()
