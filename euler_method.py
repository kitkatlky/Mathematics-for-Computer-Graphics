from tkinter import *
from math import*
import numpy as np

root=Tk()
root.title("Euler method")

lbl=Label(root,text="PLEASE ENTER THOSE INFORMATION:",font=("bold",15))
lbl.grid(row=0,column=0,columnspan=4)
lbl_eq=Label(root,text="dy/dx = ")
lbl_eq.grid(row=1,column=0)
ent_eq=Entry(root,width=40,borderwidth=3)
ent_eq.grid(row=1,column=1,columnspan=4)

lbl_x_ori=Label(root,text="func(")
lbl_x_ori.grid(row=2,column=0)
ent_x_ori=Entry(root,width=10,borderwidth=3)
ent_x_ori.grid(row=2,column=1)
lbl_y_ori=Label(root,text=") = ")
lbl_y_ori.grid(row=2,column=2)
ent_y_ori=Entry(root,width=10,borderwidth=3)
ent_y_ori.grid(row=2,column=3)

lbl_h=Label(root,text="step size = ")
lbl_h.grid(row=3,column=0)
ent_h=Entry(root,width=10,borderwidth=3)
ent_h.grid(row=3,column=1)

lbl_find=Label(root,text="approximation of func(")
lbl_find.grid(row=4,column=0,columnspan=2)
ent_x_f=Entry(root,width=10,borderwidth=3)
ent_x_f.grid(row=4,column=2)
lbl_x_f=Label(root,text=")")
lbl_x_f.grid(row=4,column=3)

def button(x):
    name=root.focus_get()
    if name is ent_eq:
        current=ent_eq.get()
        ent_eq.delete(0,END)
        ent_eq.insert(0,current+" "+x+" ")

    elif name is ent_y_ori:
        current = ent_y_ori.get()
        ent_y_ori.delete(0, END)
        ent_y_ori.insert(0, current + " " + x + " ")

button_x = Button(root, text="x", padx=10, pady=5, command=lambda :button("x"))
button_y = Button(root, text="y", padx=10, pady=5, command=lambda :button("y"))
button_add = Button(root, text="+", padx=10, pady=5, command=lambda :button("+"))
button_subtract = Button(root, text="-", padx=10, pady=5, command=lambda :button("-"))
button_multiply = Button(root, text="*", padx=10, pady=5, command=lambda :button("*"))
button_divide = Button(root, text="÷", padx=10, pady=5, command=lambda :button("÷"))
button_factorial = Button(root, text="x!", padx=10, pady=5, command=lambda :button("!"))
button_faction = Button(root, text="b/c", padx=10, pady=5, command=lambda :button("/"))
button_pow = Button(root, text="^", padx=10, pady=5, command=lambda :button("^"))
button_log = Button(root, text="log(base 10)", pady=5, command=lambda :button("log"))
button_ln = Button(root, text="ln", padx=10, pady=5, command=lambda :button("ln"))
button_exp = Button(root, text="e^x", padx=10, pady=5, command=lambda :button("e"))
button_sin = Button(root, text="sin(in rad)", padx=5, pady=5, command=lambda :button("sin"))
button_cos= Button(root, text="cos(in rad)", padx=5, pady=5, command=lambda :button("cos"))
button_tan = Button(root, text="tan(in rad)", padx=5, pady=5, command=lambda :button("tan"))
button_open_bracket = Button(root, text="(", padx=10, pady=5, command=lambda :button("("))
button_close_bracket= Button(root, text=")", padx=10, pady=5, command=lambda :button(")"))

button_x.grid(row=6,column=0,columnspan=2)
button_y.grid(row=6,column=2,columnspan=2)

button_add.grid(row=7,column=0)
button_subtract.grid(row=7,column=1)
button_multiply.grid(row=7,column=2)
button_divide.grid(row=7,column=3)

button_factorial.grid(row=8,column=0)
button_faction.grid(row=8,column=1)
button_open_bracket.grid(row=8,column=2)
button_close_bracket.grid(row=8,column=3)

button_pow.grid(row=9,column=0)
button_log.grid(row=9,column=1)
button_ln.grid(row=9,column=2)
button_exp.grid(row=9,column=3)

button_sin.grid(row=10,column=0)
button_cos.grid(row=10,column=1)
button_tan.grid(row=10,column=2)

def removeSpace(x):
    while True:
        try:
            x.remove('')
            print("after",x)
        except ValueError:
            return x

def doFractorial(x):
    while True:
        try:
            q=x.index("!")
            num=float(x[q-1])
            x[q-1]=factorial(int(num))
            x.remove("!")
            print("after fac",x)
        except ValueError:
            return x

def doFraction(x):
    while True:
        try:
            q=x.index("/")
            num=float(x[q-1])/float(x[q+1])
            x[q-1]=num
            x.remove("/")
            x.pop(q)
            print("after fraction",x)
        except ValueError:
            return x

def doPow(x):
    while True:
        try:
            q=x.index("^")
            num=pow(float(x[q-1]),float(x[q+1]))
            x[q-1]=num
            x.remove("^")
            x.pop(q)
            print("after pow",x)
        except ValueError:
            return x

def doLog(x):
    while True:
        try:
            q=x.index("log")
            num=log10(float(x[q+1]))
            x[q]=num
            x.pop(q+1)
            print("after log",x)
        except ValueError:
            return x

def doLn(x):
    while True:
        try:
            q = x.index("ln")
            num = log(float(x[q + 1]))
            x[q] = num
            x.pop(q + 1)
            print("after ln", x)
        except ValueError:
            return x

def doExp(x):
    while True:
        try:
            q = x.index("e")
            num = exp(float(x[q + 1]))
            x[q] = num
            x.pop(q + 1)
            print("after exp", x)
        except ValueError:
            return x

def doSin(x):
    while True:
        try:
            q = x.index("sin")
            num = sin(float(x[q + 1]))
            x[q] = num
            x.pop(q + 1)
            print("after sin", x)
        except ValueError:
            return x

def doCos(x):
    while True:
        try:
            q = x.index("cos")
            num = cos(float(x[q + 1]))
            x[q] = num
            x.pop(q + 1)
            print("after cos", x)
        except ValueError:
            return x

def doTan(x):
    while True:
        try:
            q = x.index("tan")
            num = tan(float(x[q + 1]))
            x[q] = num
            x.pop(q + 1)
            print("after tan", x)
        except ValueError:
            return x

def multiply(x):
    while True:
        try:
            q=x.index("*")
            num=float(x[q-1])*float(x[q+1])
            x[q-1]=num
            x.remove("X")
            x.pop(q)
            print("after multiply",x)
        except ValueError:
            return x

def divide(x):
    while True:
        try:
            q=x.index("÷")
            num=float(x[q-1])/float(x[q+1])
            x[q-1]=num
            x.remove("÷")
            x.pop(q)
            print("after divide",x)
        except ValueError:
            return x

def add(x):
    while True:
        try:
            q=x.index("+")
            num=float(x[q-1])+float(x[q+1])
            x[q-1]=num
            x.remove("+")
            x.pop(q)
            print("after add",x)
        except ValueError:
            return x

def minus(x):
    while True:
        try:
            q=x.index("-")
            num=float(x[q-1])-float(x[q+1])
            x[q-1]=num
            x.remove("-")
            x.pop(q)
            print("after minus",x)
        except ValueError:
            return x

def rest(x):
    x=multiply(x)
    x=divide(x)
    x=add(x)
    x=minus(x)
    return x

def doBracket(x):
    while True:
        try:
            start=x.index("(")
            end=x.index(")")
            q=[]
            for i in range(start+1,end):
                q.append(x[i])
            value=rest(q)
            for i in range(len(value)):
                x[start+i]=value[i]
            print("after insert",x)
            if end>(len(value)+start):
                for i in range(end-start-len(value)+1):
                    x.pop(start+len(value))
                    i+=1
            print("after bracket",x)
        except ValueError:
            return x

def step(x):
    x = removeSpace(x)
    x = doFractorial(x)
    x = doFraction(x)
    x = doPow(x)
    x = doLog(x)
    x = doLn(x)
    x = doExp(x)
    x = doSin(x)
    x = doCos(x)
    x = doTan(x)
    x = doBracket(x)
    x = rest(x)
    return x

def f(xVal,yVal):
    func=eq.copy()
    print("im here",func)
    bol=True
    while bol:
        try:
            place_x=func.index("x")
            place_y=func.index("y")
            func[place_x]=xVal
            func[place_y]=yVal
        except ValueError:
            bol=False
    func_with_value=step(func)
    return func_with_value[0]

def do():
    equation=ent_eq.get().split(" ")
    print("ori",equation)
    global eq
    eq=step(equation)
    print("here",eq)

    x_0=float(ent_x_ori.get())
    ori=ent_y_ori.get().split(" ")
    y_0=step(ori)[0]

    x_f=float(ent_x_f.get())
    h=float(ent_h.get())

    n=int((x_f-x_0)/h +1)
    x=np.linspace(x_0,x_f,n)
    y=np.zeros([n])
    y[0]=y_0
    for i in range(1, n):
        y[i]=y[i-1]+h*f(x[i-1],y[i-1])
        print("y",i,"is"+str(y[i]))

    for i in range (1,n):
        ans.insert(END,'%.1f        %f'%(x[i],y[i]))

button_submit=Button(root,text="submit",padx=10,pady=5,command=do,bg='blue')
button_submit.grid(row=5,column=5)

lbl_space=Label(root,text=" \n ")
lbl_space.grid(row=11,column=0)

lbl_result=Label(root,text="TABLE RESULT : ")
lbl_result.grid(row=1,column=6)
sb=Scrollbar(root)
sb.grid(row=1,column=9,rowspan=200,sticky=N+S)
ans=Listbox(root,yscrollcommand=sb.set,height=19,font=(10))
ans.insert(END,'x               y')
ans.grid(row=1,column=7,columnspan=2,rowspan=200)

root.mainloop()