from tkinter import *

def btnclick(numbers):
    global operators
    operators=operators+str(numbers)
    text_input.set(operators)

def btnclear():
    global operators
    operators=""
    text_input.set("")

def btnequal():
    global operators
    sumup=str(eval(operators))
    text_input.set(sumup)
    operators=""


root = Tk()
root.title("Calculator")
operators = ""
text_input = StringVar()


txtDisplay = Entry(root,font=('arial',20,'bold'),textvariable = text_input,bd=30,insertwidth=4,bg="powder blue",justify="right")
txtDisplay.grid(columnspan=4)

btn7=Button(root,padx=16,bd =8,fg ="black",font=("arial",20,'bold'),text="7",bg='powder blue',command=lambda:btnclick(7))
btn7.grid(row=1,column=0)

btn8=Button(root,padx=16,bd =8,fg ="black",font=("arial",20,'bold'),text="8",bg='powder blue',command=lambda:btnclick(8))
btn8.grid(row=1,column=1)

btn9=Button(root,padx=16,bd =8,fg ="black",font=("arial",20,'bold'),text="9",bg='powder blue',command=lambda:btnclick(9))
btn9.grid(row=1,column=2)

add=Button(root,padx=16,bd =8,fg ="black",font=("arial",20,'bold'),text="+",bg='powder blue',command=lambda:btnclick("+"))
add.grid(row=1,column=3)


btn4=Button(root,padx=16,bd =8,fg ="black",font=("arial",20,'bold'),text="4",bg='powder blue',command=lambda:btnclick(4))
btn4.grid(row=2,column=0)

btn5=Button(root,padx=16,bd =8,fg ="black",font=("arial",20,'bold'),text="5",bg='powder blue',command=lambda:btnclick(5))
btn5.grid(row=2,column=1)

btn6=Button(root,padx=16,bd =8,fg ="black",font=("arial",20,'bold'),text="6",bg='powder blue',command=lambda:btnclick(6))
btn6.grid(row=2,column=2)

sub=Button(root,padx=16,bd =8,fg ="black",font=("arial",20,'bold'),text="-",bg='powder blue',command=lambda:btnclick("-"))
sub.grid(row=2,column=3)


btn1=Button(root,padx=16,bd =8,fg ="black",font=("arial",20,'bold'),text="1",bg='powder blue',command=lambda:btnclick(1))
btn1.grid(row=3,column=0)

btn2=Button(root,padx=16,bd =8,fg ="black",font=("arial",20,'bold'),text="2",bg='powder blue',command=lambda:btnclick(2))
btn2.grid(row=3,column=1)

btn3=Button(root,padx=16,bd =8,fg ="black",font=("arial",20,'bold'),text="3",bg='powder blue',command=lambda:btnclick(3))
btn3.grid(row=3,column=2)

mul=Button(root,padx=16,bd =8,fg ="black",font=("arial",20,'bold'),text="*",bg='powder blue',command=lambda:btnclick("*"))
mul.grid(row=3,column=3)


btn0=Button(root,padx=16,bd =8,fg ="black",font=("arial",20,'bold'),text="0",bg='powder blue',command=lambda:btnclick(0))
btn0.grid(row=4,column=0)

clear=Button(root,padx=16,bd =8,fg ="black",font=("arial",20,'bold'),text="Cl",bg='powder blue',command=btnclear)
clear.grid(row=4,column=1)

equal=Button(root,padx=16,bd =8,fg ="black",font=("arial",20,'bold'),text="=",bg='powder blue',command= btnequal)
equal.grid(row=4,column=2)

div=Button(root,padx=16,bd =8,fg ="black",font=("arial",20,'bold'),text="/",bg='powder blue',command=lambda:btnclick("/"))
div.grid(row=4,column=3)





root.mainloop()