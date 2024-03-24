import tkinter
from tkinter import *


root = Tk()
root.title("Neha's Grade Calculator")
root.geometry("500x400")
def Calculation():
    iot = int(iotentry.get())
    c = int(centry.get())
    java = int(javaentry.get())
    total = (iot+c+java)
    Label(text=f"{total}",font="arial 15 bold").place(x=250,y=170)

    average = int(total/3)
    Label(text=f"{average}",font="arial 15 bold").place(x=250,y=211)

    if( average>50):
        grade="Pass"
    else:
        grade="Fail"
    Label(text=f"{grade}",font="arial 15 bold",fg="green").place(x=250,y=250)
sub1 = Label(root,text="IoT", font="arial 10")
sub2 = Label(root,text="C", font="arial 10")
sub3 = Label(root,text="Java", font="arial 10")

total = Label(root,text="Total",font="arial 10")
avg = Label(root,text="Average", font="arial 10")
grade = Label(root,text="Grade", font="arial 10")

sub1.place(x=50, y=20)
sub2.place(x=50, y=70)
sub3.place(x=50, y=120)
total.place(x=50, y=174)
avg.place(x=52, y=211)
grade.place(x=51, y=252)

iotvalue = StringVar()
cValue = StringVar()
javavalue = StringVar()

iotentry = Entry(root,textvariable=iotvalue,font="arial 15",width=16)
centry = Entry(root,textvariable=cValue,font="arial 15",width=16)
javaentry = Entry(root,textvariable=javavalue,font="arial 15",width=16)

iotentry.place(x=250,y=20)
centry.place(x=250,y=70)
javaentry.place(x=250,y=120)
Button(text="Calculate", font="arial 15", bg="grey",bd=10,command=Calculation).place(x=50,y=300)
Button(text="Exit", font="arial 15", bg="red",bd=10,width=8,command=lambda:exit()).place(x=350,y=220)
root.mainloop()