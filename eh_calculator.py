from tkinter import *
import numpy as npy

root=Tk()
root.title("Not a basic calculator")

#Creating a small width, text box.
text_box=Entry(root, width=35)
text_box.grid(row=0,columnspan=3)
#text_box.insert(0, 0) LOOK INTO THIS LATER ON.







#########################################################ALL FUNCTIONS FOR BUTTONS START FROM HERE#########################################################


#Entering a Number
def num_enter(number):
    data=text_box.get()
    text_box.delete(0,END)
    text_box.insert(0,data+str(number))

#Misc functions
def clear():
    text_box.delete(0,END)

def equal_to():
    global num2
    if op == "+":
    
        num2=int(text_box.get())
        text_box.delete(0,END)
        text_box.insert(0,num1+num2)
    elif op == "-":
        
        num2=int(text_box.get())
        text_box.delete(0,END)
        text_box.insert(0,num1-num2)
    elif op == "*":
        
        num2=int(text_box.get())
        text_box.delete(0,END)
        text_box.insert(0,num1*num2)
    elif op == "/":
        
        num2=int(text_box.get())
        text_box.delete(0,END)
        text_box.insert(0,num1/num2)
    elif op == "sqroot":
        ans = npy.sqrt(int(numb))
        text_box.insert(0,int(ans))




#Operation functions
def addition():
    global op
    global num1
    op='+'
    num1 = int(text_box.get())
    text_box.delete(0,END)
def subtraction():
    global op
    global num1
    op='-'
    num1 = int(text_box.get())
    text_box.delete(0,END)
def multiplication():
    global op
    global num1
    op='*'
    num1 = int(text_box.get())
    text_box.delete(0,END)
def division():
    global op
    global num1
    op='/'
    num1 = int(text_box.get())
    text_box.delete(0,END)

def sqroot():
    global op
    global numb
    op = "sqroot"
    numb = int(text_box.get())
    text_box.delete(0,END)




############################################################ALL FUNCTIONS FOR BUTTONS END HERE############################################################





#Creating Number Buttons 
button_1=Button(root,text="1",padx=40,pady=20, command= lambda: num_enter(1))
button_2=Button(root,text="2",padx=40,pady=20, command= lambda: num_enter(2))
button_3=Button(root,text="3",padx=40,pady=20, command= lambda: num_enter(3))
button_4=Button(root,text="4",padx=40,pady=20, command= lambda: num_enter(4))
button_5=Button(root,text="5",padx=40,pady=20, command= lambda: num_enter(5))
button_6=Button(root,text="6",padx=40,pady=20, command= lambda: num_enter(6))
button_7=Button(root,text="7",padx=40,pady=20, command= lambda: num_enter(7))
button_8=Button(root,text="8",padx=40,pady=20, command= lambda: num_enter(8))
button_9=Button(root,text="9",padx=40,pady=20, command= lambda: num_enter(9))
button_0=Button(root,text="0",padx=40,pady=20, command= lambda: num_enter(0))
#Placing Number Buttons
button_0.grid(row=4,column=0)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

#Creating Operation Buttons
button_plus=Button(root,text="+",padx=40,pady=20,command=addition)
button_minus=Button(root,text="-",padx=43,pady=20,command=subtraction)
button_multiply=Button(root,text="*",padx=40,pady=20,command=multiplication)
button_divide=Button(root,text="/",padx=41,pady=20,command=division)
button_root=Button(root,text="√",padx=40,pady=20,command=sqroot)


#Miscellaneous Buttons
button_clear=Button(root,text='CLR',padx=81,pady=20,command=clear)
button_eq=Button(root,text='=',padx=40,pady=20,command=equal_to)

#Placing Miscellaneous and Operation Buttons
button_clear.grid(row=4,column=1,columnspan=2)
button_eq.grid(row=6,column=2)

button_plus.grid(row=5,column=0)
button_minus.grid(row=5,column=1)
button_multiply.grid(row=5,column=2)
button_divide.grid(row=6,column=0)
button_root.grid(row=6,column=1)





root.mainloop()