from tkinter import*
import math
import numpy as np
from tkinter import messagebox
from tkinter.ttk import Combobox
from fractions import Fraction

def vector():
    top=Tk()
    top.title("VECTOR CALCULATOR")
    u=["none","none","none"]
    v=["none","none","none"]
    operation="none"

    a=Entry(top,width=90,borderwidth=5)
    a.grid(row=0,column=0,columnspan=6,padx=10,pady=10)

    def button(number):
        # get the new num enter
        current=a.get()
        # clear at the entry side
        a.delete(0,END)
        # appear a string that combine the num before and num after
        a.insert(0,str(current) + str(number))

    # define button number
    button_0=Button(top,text="0",padx=90,pady=20,command=lambda:button(0))
    # we use lambda so that we can pass a varaible through the function
    button_1=Button(top,text="1",padx=40,pady=20,command=lambda:button(1))
    button_2=Button(top,text="2",padx=40,pady=20,command=lambda:button(2))
    button_3=Button(top,text="3",padx=40,pady=20,command=lambda:button(3))
    button_4=Button(top,text="4",padx=40,pady=20,command=lambda:button(4))
    button_5=Button(top,text="5",padx=40,pady=20,command=lambda:button(5))
    button_6=Button(top,text="6",padx=40,pady=20,command=lambda:button(6))
    button_7=Button(top,text="7",padx=40,pady=20,command=lambda:button(7))
    button_8=Button(top,text="8",padx=40,pady=20,command=lambda:button(8))
    button_9=Button(top,text="9",padx=40,pady=20,command=lambda:button(9))

    def button_del():
        current=a.get().split(",")
        a.delete(0,END)
        if v[0]=="none":
            if len(current)!=3:
                if len(current)!=2:
                    u[0]="none"
                    a.delete(0,END)
                else:
                    u[0]=float(current[0])
                    a.insert(0,str(u[0])+",")
            else:
                u[0] = float(current[0])
                u[1] = float(current[1])
                a.insert(0, str(u[0]) + "," + str(u[1]) + ",")
        else:
            if len(current)!=3:
                if len(current)!=2:
                    v[0] = "none"
                    a.delete(0, END)
                else:
                    v[0] = float(current[0])
                    a.insert(0, str(v[0]) + ",")
            else:
                v[0] = float(current[0])
                v[1] = float(current[1])
                a.insert(0, str(v[0]) + "," + str(v[1]) + ",")

    def ac():
        a.delete(0,END)
        global u
        u = ["none", "none", "none"]
        global v
        v = ["none", "none", "none"]
        global operation
        operation = "none"

    def comma():
        current=a.get()
        if operation=="none":
            if u[0]=="none":
                u[0]=float(current)
                a.delete(0,END)
                a.insert(0,str(u[0])+",")
            else:
                current=current.split(",")
                u[1]=float(current[1])
                a.delete(0,END)
                a.insert(0,str(u[0])+","+str(u[1])+",")

        else:
            if v[0]=="none":
                v[0]=float(current)
                a.delete(0,END)
                a.insert(0,str(v[0])+",")
            else:
                current = current.split(",")
                v[1]=float(current[1])
                a.delete(0,END)
                a.insert(0,str(v[0])+","+str(v[1])+",")

    def add():
        first=a.get().split(",")
        if u[0]=="none":
            u[0]=float(first[0])
        elif u[1]=="none":
            u[1]=float(first[1])
        else:
            u[2]=float(first[2])
        # make a global variable named operation so that function equal can access it
        global operation
        operation="add"
        a.delete(0,END)

    def subtract():
        first = a.get().split(",")
        if u[0] == "none":
            u[0] = float(first[0])
        elif u[1] == "none":
            u[1] = float(first[1])
        else:
            u[2] = float(first[2])
        global operation
        operation = "subtract"
        a.delete(0, END)

    def dotP():
        first = a.get().split(",")
        if u[0] == "none":
            u[0] = float(first[0])
        elif u[1] == "none":
            u[1] = float(first[1])
        else:
            u[2] = float(first[2])
        global operation
        operation = "dotP"
        a.delete(0, END)

    def crossP():
        first = a.get().split(",")
        if u[0] == "none":
            u[0] = float(first[0])
        elif u[1] == "none":
            u[1] = float(first[1])
        else:
            u[2] = float(first[2])
        global operation
        operation = "crossP"
        a.delete(0, END)

    def magnitude():
        first = a.get().split(",")
        if u[0] == "none":
            u[0] = float(first[0])
        elif u[1] == "none":
            u[1] = float(first[1])
        else:
            u[2] = float(first[2])
        a.delete(0, END)
        if(u[0]=="none"):
            a.insert(0,"ERROR")
        elif(u[1]=="none"):
            # vector lies on x-axis
            a.insert(0,str(u[0]))
        elif(u[2]=="none"):
            # magnitude of 2d vector
            m = math.sqrt(float(u[0]) * float(u[0]) + float(u[1]) * float(u[1]))
            a.insert(0,m)
        else:
            # magnitude of 3d vector
            m=math.sqrt(float(u[0])*float(u[0]) + float(u[1])*float(u[1]) + float(u[2])*float(u[2]))
            a.insert(0,m)

    def scale():
        first = a.get().split(",")
        if u[0] == "none":
            u[0] = float(first[0])
        elif u[1] == "none":
            u[1] = float(first[1])
        else:
            u[2] = float(first[2])
        # global f_num
        # f_num = u
        global operation
        operation = "scale"
        a.delete(0, END)

    def equal():
        second=a.get().split(",")
        if v[0]=="none":
            v[0]=float(second[0])
        elif v[1]=="none":
            v[1]=float(second[1])
        else:
            v[2]=float(second[2])
        a.delete(0,END)

        if operation == "add":
            if (u[2] == "none" and v[2] == "none"):
                # means 2d vector
                if (u[1] == "none" and v[1] == "none"):
                    # 1d
                    if (u[0] != "none" and v[0]!="none"):
                        w = [float(u[0]) + float(v[0])]
                        a.insert(0, str(w[0]))
                    else:
                        # either u[0] or v[0] ="none"
                        a.insert(0, "ERROR")
                elif(u[1]!="none" and v[1]!="none"):
                    w = [float(u[0]) + float(v[0]),
                         float(u[1]) + float(v[1])]
                    a.insert(0, str(w[0]) + "," + str(w[1]))
                else:
                    # either u[1] or v[1] = "none", addition of vector cannot be done
                    a.insert(0, "ERROR")
            elif (u[2] != "none" and v[2] != "none"):
                # 3d vector
                w = [float(u[0]) + float(v[0]),
                     float(u[1]) + float(v[1]),
                     float(u[2]) + float(v[2])]
                a.insert(0, str(w[0]) + "," + str(w[1]) + "," + str(w[2]))
            else:
                # either u[2] or v[2]="none", addition of vector cannot be done
                a.insert(0,"ERROR")

        if operation == "subtract":
            if (u[2] == "none" and v[2] == "none"):
                if (u[1] == "none" and v[1] == "none"):
                    if (u[0] != "none" and v[0] != "none"):
                        w = [float(u[0]) - float(v[0])]
                        a.insert(0, str(w[0]))
                    else:
                        a.insert(0, "ERROR")
                elif (u[1] != "none" and v[1] != "none"):
                    w = [float(u[0]) - float(v[0]),
                         float(u[1]) - float(v[1])]
                    a.insert(0, str(w[0]) + "," + str(w[1]))
                else:
                    a.insert(0, "ERROR")
            elif (u[2] != "none" and v[2] != "none"):
                w = [float(u[0]) - float(v[0]),
                     float(u[1]) - float(v[1]),
                     float(u[2]) - float(v[2])]
                a.insert(0, str(w[0]) + "," + str(w[1]) + "," + str(w[2]))
            else:
                a.insert(0, "ERROR")

        if operation == "dotP":
            if (u[2] == "none" and v[2] == "none"):
                # means 2d vector
                if (u[1] != "none" and v[1] != "none"):
                    if(u[0]!="none" and v[0]!="none"):
                        w = float(u[0])*float(v[0]) + float(u[1])*float(v[1])
                        a.insert(0, str(w))
                    else:
                        # either u[0] or v[0] or both = "none"
                        a.insert(0,"ERROR")
                else:
                    # either u[1] or v[1] or both ="none"
                    a.insert(0,"ERROR")
            elif(u[2]=="none" or v[2]=="none"):
                # either u[2] or v[2] = "none"
                a.insert(0,"ERROR")
            else:
                w = float(u[0])*float(v[0]) + float(u[1])*float(v[1]) + float(u[2])*float(v[2])
                a.insert(0, str(w))

        if operation == "crossP":
            if (u[2] != "none" and v[2] != "none"):
                # 3d vector
                if(u[1]!="none" and v[1]!="none"):
                    if(u[0]!="none" and v[0]!="none"):
                        w = [u[1] * v[2] - u[2] * v[1],
                             u[2] * v[0] - u[0] * v[2],
                             u[0] * v[1] - u[1] * v[0]]
                        a.insert(0, str(w[0]) + "," + str(w[1]) + "," + str(w[2]))
                    else:
                        # either u[0] or v[0] or both ="none"
                        a.insert(0,"ERROR")
                else:
                    # either u[1] or v[1] or both ="none"
                    a.insert(0,"ERROR")
            else:
                # either u[2] or v[2] or both ="none"
                a.insert(0, "ERROR")

        if operation == "scale":
            if u[0]=="none":
                a.insert(0, "ERROR")
            elif u[1]=="none":
                w=[float(u[0])*float(v[0])]
                a.insert(0,str(w[0]))
            elif u[2]=="none":
                w=[float(u[0])*float(v[0]),
                   float(u[1])*float(v[0])]
                a.insert(0,str(w[0])+","+str(w[1]))
            else:
                w = [float(u[0]) *float(v[0]),
                     float(u[1]) *float(v[0]),
                     float(u[2]) *float(v[0])]
                a.insert(0, str(w[0]) + "," + str(w[1]) + "," + str(w[2]))

    # define button operation
    button_sign=Button(top,text="-",padx=40,pady=20,command=lambda:button("-"))
    button_del=Button(top,text="DEL",padx=40,pady=20,command=button_del)
    button_clear=Button(top,text="AC",padx=40,pady=20,command=ac)

    button_magnitude=Button(top,text="magnitude",padx=14,pady=20,command=magnitude)
    button_dotP=Button(top,text="dotProduct",padx=20,pady=20,command=dotP)
    button_crossP=Button(top,text="crossProduct",padx=13,pady=20,command=crossP)

    button_scale=Button(top,text="scaling",padx=25,pady=20,command=scale)
    button_add=Button(top,text="addition",padx=27,pady=20,command=add)
    button_subtract=Button(top,text="subtraction",padx=18,pady=20,command=subtract)

    button_point=Button(top,text="point(.)",padx=23,pady=20,command=lambda:button("."))
    button_comma=Button(top,text="comma(,)",padx=17,pady=20,command=comma)
    button_equal=Button(top,text="=",padx=100,pady=20,command=equal)

    # put the button on the screen
    button_7.grid(row=1,column=0)
    button_8.grid(row=1,column=1)
    button_9.grid(row=1,column=2)
    button_sign.grid(row=1,column=3)
    button_del.grid(row=1,column=4)
    button_clear.grid(row=1,column=5)

    button_4.grid(row=2,column=0)
    button_5.grid(row=2,column=1)
    button_6.grid(row=2,column=2)
    button_magnitude.grid(row=2,column=3)
    button_dotP.grid(row=2,column=4)
    button_crossP.grid(row=2,column=5)

    button_1.grid(row=3,column=0)
    button_2.grid(row=3,column=1)
    button_3.grid(row=3,column=2)
    button_scale.grid(row=3,column=3)
    button_add.grid(row=3,column=4)
    button_subtract.grid(row=3,column=5)

    button_0.grid(row=4,column=0,columnspan=2)
    button_point.grid(row=4,column=2)
    button_comma.grid(row=4,column=3)
    button_equal.grid(row=4,column=4,columnspan=2)

    top.mainloop()

def matrix():
    root = Tk()
    root.title("Matrix Calculator")

    line_A = Label(root, text="Dimension of Matrix A =")
    line_A.grid(row=1, column=0)
    var_m = StringVar()
    var_m.set(1)
    spin_mA = Spinbox(root, from_=0, to=4, textvariable=var_m, width=3)
    spin_mA.grid(row=1, column=1)
    line_A_con = Label(root, text="by")
    line_A_con.grid(row=1, column=2)
    var_n = StringVar()
    var_n.set(1)
    spin_nA = Spinbox(root, from_=0, to=4, textvariable=var_n, width=3)
    spin_nA.grid(row=1, column=3)

    line_B = Label(root, text="Dimension of Matrix B =")
    line_B.grid(row=1, column=8, columnspan=3)
    spin_mB = Spinbox(root, from_=0, to=4, width=3)
    spin_mB.grid(row=1, column=11)
    line_B_con = Label(root, text="by")
    line_B_con.grid(row=1, column=12)
    spin_nB = Spinbox(root, from_=0, to=4, width=3)
    spin_nB.grid(row=1, column=13)

    mA = 0
    nA = 0
    mB = 0
    nB = 0
    a = {}
    b = {}
    A = []
    B = []
    ans = []
    num = 0
    matrix_want = []

    def matrix():
        global A, B
        A = []
        B = []
        for i in range(mA):
            row = []
            for j in range(nA):
                index = (i, j)
                current = a[index].get().split("/")
                try:
                    if (len(current) == 2):
                        up = float(current[0])
                        down = float(current[1])
                        final = up / down
                        row.append(final)
                    elif (len(current) == 1):
                        row.append(float(current[0]))
                    else:
                        statement = "INVALID INPUT FOR VALUE a" + str(i + 1) + str(j + 1) + "\nPLEASE TRY AGAIN"
                        msg = messagebox.showerror("INVALID INPUT", statement)
                        box_a.delete(0, END)
                except ValueError:
                    statement = "INVALID INPUT FOR VALUE a" + str(i + 1) + str(j + 1) + "\nPLEASE TRY AGAIN"
                    msg = messagebox.showerror("INVALID INPUT", statement)
                    box_a.delete(0, END)
            A.append(row)

        for i in range(mB):
            row = []
            for j in range(nB):
                index = (i, j)
                current = b[index].get().split("/")
                try:
                    if (len(current) == 2):
                        up = float(current[0])
                        down = float(current[1])
                        final = up / down
                        row.append(final)
                    elif (len(current) == 1):
                        row.append(float(current[0]))
                    else:
                        statement = "INVALID INPUT FOR VALUE b" + str(i + 1) + str(j + 1) + "\nPLEASE TRY AGAIN"
                        msg = messagebox.showerror("INVALID INPUT", statement)
                        box_b.delete(0, END)
                except ValueError:
                    statement = "INVALID INPUT FOR VALUE b" + str(i + 1) + str(j + 1) + "\nPLEASE TRY AGAIN"
                    msg = messagebox.showerror("INVALID INPUT", statement)
                    box_b.delete(0, END)
            B.append(row)
        A = np.array(A)
        B = np.array(B)
        button_submit.configure(text="edit entries")
        global num
        if (num == 1):
            choice_A.deselect()
        elif (num == 2):
            choice_B.deselect()
        num = 0

    def resize():
        spin_mA.configure(state='normal')
        spin_nA.configure(state='normal')
        spin_mB.configure(state='normal')
        spin_nB.configure(state='normal')
        for i in range(4):
            for j in range(4):
                box_a = Entry(root, width=5, state='disable')
                box_a.grid(row=3 + i, column=1 + j)
        for i in range(4):
            for j in range(4):
                box_b = Entry(root, width=5, state='disable')
                box_b.grid(row=3 + i, column=11 + j)
        button_ok.configure(state='active')
        button_edit.configure(state='disable')
        button_submit.configure(text="submit", state='disable')

    def displayBox():
        global mA, nA, mB, nB
        mA = int(spin_mA.get())
        nA = int(spin_nA.get())
        mB = int(spin_mB.get())
        nB = int(spin_nB.get())
        spin_mA.configure(state='disable')
        spin_nA.configure(state='disable')
        spin_mB.configure(state='disable')
        spin_nB.configure(state='disable')

        for i in range(mA):
            for j in range(nA):
                index = (i, j)
                box_a = Entry(root, width=5)
                box_a.grid(row=3 + i, column=1 + j)
                a[index] = box_a

        for i in range(mB):
            for j in range(nB):
                index = (i, j)
                box_b = Entry(root, width=5)
                box_b.grid(row=3 + i, column=11 + j)
                b[index] = box_b
        button_edit.configure(state='active')
        button_ok.configure(state='disable')
        button_submit.configure(state='active')

    button_ok = Button(root, text="OK", padx=5, pady=5, command=displayBox)
    button_ok.configure(bg='royalblue1', font=("Bold"))
    button_edit = Button(root, text="edit", command=resize, padx=5, pady=5)
    button_edit.configure(bg='pink', state='disable')
    button_ok.grid(row=1, column=16)
    button_edit.grid(row=1, column=17)

    for i in range(4):
        for j in range(4):
            box_a = Entry(root, width=5, state='disable')
            box_a.grid(row=3 + i, column=1 + j)
            box_b = Entry(root, width=5, state='disable')
            box_b.grid(row=3 + i, column=11 + j)

    button_submit = Button(root, text="Submit", padx=20, pady=5, command=matrix)
    button_submit.configure(bg='VioletRed1', state='disable')
    button_submit.grid(row=7, column=6, columnspan=3)
    lbl_space_1 = Label(root, text=" \n ")
    lbl_space_1.grid(row=8, column=0, rowspan=2)
    operation = Label(root, text="Operation", font=(10))
    operation.grid(row=13, column=0)
    transformation = Label(root, text="Transformation (only for 2d matrix)", font=(10))
    transformation.grid(row=11, column=9, columnspan=10)

    lbl_space_2 = Label(root, text=" \n ")
    lbl_space_2.grid(row=17, column=0, rowspan=2)
    lbl_ans = Label(root, text="Result", font=(15))
    lbl_ans.grid(row=19, column=0)
    box_result = Label(root, text="[]", font=("bold", 15), fg='green')
    box_result.grid(row=20, column=1, rowspan=5, columnspan=14)

    def trace(x):
        global ans
        if (num != 0):
            e = testEmpty(num)
            if (e is True):
                y = np.size(x, 0)
                z = np.size(x, 1)
                q = min(y, z)
                ans = 0
                for i in range(q):
                    ans += x[i][i]
                box_result.configure(text=ans)
                button_chg.configure(state="active")
        else:
            warning(0)

    def orthogonal(x):
        if (num != 0):
            e = testEmpty(num)
            if (e is True):
                y = np.size(x, 0)
                z = np.size(x, 1)
                if (y == z):
                    T = x.transpose()
                    det = calDet(x)
                    if (det != 0):
                        adj = calAdj(x)
                        I = (1 / det) * adj
                        bool = np.any(T - I)
                        if bool == True:
                            ans = "IS NOT AN ORTHOGONAL MATRIX"
                        else:
                            ans = "IS ORTHOGONAL MATRIX"
                    else:
                        ans = "IS NOT AN ORTHOGONAL MATRIX"
                    box_result.configure(text=ans)
                    button_chg.configure(state="disable")
                else:
                    errorSquare(0)
        else:
            warning(0)

    def symmetric(x):
        if (num != 0):
            e = testEmpty(num)
            if (e is True):
                y = np.size(x, 0)
                z = np.size(x, 1)
                if (y == z):
                    T = x.transpose()
                    temp = np.zeros((y, y))
                    for i in range(y):
                        for j in range(y):
                            temp[i][j] = x[i][j] / T[i][j]
                    one = np.ones((y, y))
                    bool = np.any(temp - one)
                    # check non-zero element
                    if bool is True:
                        for i in range(y):
                            temp[i][i] = -1
                        bool = np.any(temp + one)
                        if bool is True:
                            ans = "IS NOT SYMMETRIC MATRIX"
                        else:
                            ans = "IS SKEW-SYMMETRIC MATRIX"
                    else:
                        ans = "IS SYMMETRIC MATRIX"
                    box_result.configure(text=ans)
                    button_chg.configure(state="disable")
                else:
                    errorSquare(0)
        else:
            warning(0)

    def rank(x):
        if (num != 0):
            e = testEmpty(num)
            if (e is True):
                y = np.size(x, 0)
                z = np.size(x, 0)
                q = min(y, z)
                z = np.zeros((q, q))
                z = np.array(x[:q][:q])
                det = calDet(z)
                if (det != 0):
                    ans = q
                else:
                    minor = np.delete(z, 0, 0)
                    minor = np.delete(minor, 0, 1)
                    det = calDet(minor)
                    if (det != 0):
                        ans = q - 1
                    else:
                        minor = np.delete(minor, 0, 0)
                        minor = np.delete(minor, 0, 1)
                        det = calDet(minor)
                        if (det != 0):
                            ans = q - 2
                        else:
                            minor = np.delete(minor, 0, 0)
                            minor = np.delete(minor, 0, 1)
                            det = calDet(minor)
                            if (det != 0):
                                ans = q - 3
                            else:
                                ans = 0
                box_result.configure(text=ans)
                button_chg.configure(state="disable")
        else:
            warning(0)

    def adj(x):
        global ans
        if (num != 0):
            e = testEmpty(num)
            if (e is True):
                y = np.size(x, 0)
                z = np.size(x, 1)
                if (y == z):
                    ans = calAdj(x)
                    box_result.configure(text=ans)
                    button_chg.configure(state="active")
                    if (num == 3):
                        global matrix_want
                        matrix_want = ans
                else:
                    errorSquare(0)
        else:
            warning(0)

    def cofactor(x):
        global ans
        if (num != 0):
            e = testEmpty(num)
            if (e is True):
                y = np.size(x, 0)
                z = np.size(x, 1)
                if (y == z):
                    ans = calCofactor(x)
                    box_result.configure(text=ans)
                    button_chg.configure(state="active")
                    if (num == 3):
                        global matrix_want
                        matrix_want = ans
                else:
                    errorSquare(0)
        else:
            warning(0)

    def minor(x):
        global ans
        if (num != 0):
            e = testEmpty(num)
            if (e is True):
                y = np.size(x, 0)
                z = np.size(x, 1)
                if (y == z):
                    ans = calMinor(x)
                    box_result.configure(text=ans)
                    button_chg.configure(state="active")
                    if (num == 3):
                        global matrix_want
                        matrix_want = ans
                else:
                    errorSquare(0)
        else:
            warning(0)

    def det(x):
        global ans
        if (num != 0):
            e = testEmpty(num)
            if (e is True):
                # determine no. of row
                y = np.size(x, 0)
                # determine no. of column
                z = np.size(x, 1)
                if (y == z):
                    ans = calDet(x)
                    box_result.configure(text=ans)
                    button_chg.configure(state="active")
                else:
                    errorSquare(0)
        else:
            warning(0)

    def errorSquare(x):
        statement = "MATRIX IS NOT SQUARE MATRIX.\nPLEASE EDIT MATRIX"
        msg = messagebox.showerror("ERROR", statement)

    def calMinor(x):
        y = np.size(x, 0)
        if (y == 1):
            z = np.array([1])
        else:
            z = np.zeros((y, y))
            for i in range(y):
                for j in range(y):
                    minor = np.delete(x, i, 0)
                    minor = np.delete(minor, j, 1)
                    z[i][j] = calDet(minor)
        return z

    def calCofactor(x):
        y = np.size(x, 0)
        z = np.zeros((y, y))
        z = calMinor(x)
        for i in range(y):
            for j in range(y):
                z[i][j] = math.pow(-1, i + j) * z[i][j]
        return z

    def calAdj(x):
        y = np.size(x, 0)
        if (y == 1):
            z = np.array([1])
        else:
            z = np.zeros((y, y))
            z = calCofactor(x)
            z = z.transpose()
        return z

    def calDet(x):
        y = np.size(x, 0)
        if (y == 1):
            return x[0][0]
        elif (y == 2):
            return x[0][0] * x[1][1] - x[0][1] * x[1][0]
        elif (y == 3):
            d = x[1][1] * x[2][2] - x[1][2] * x[2][1]
            e = x[1][0] * x[2][2] - x[1][2] * x[2][0]
            f = x[1][0] * x[2][1] - x[1][1] * x[2][0]
            return x[0][0] * d - x[0][1] * e + x[0][2] * f
        else:
            d_1 = x[2][2] * x[3][3] - x[2][3] * x[3][2]
            d_2 = x[2][1] * x[3][3] - x[2][3] * x[3][1]
            d_3 = x[2][1] * x[3][2] - x[2][2] * x[3][1]
            d = x[1][1] * d_1 - x[1][2] * d_2 + x[1][3] * d_3
            e_1 = x[2][2] * x[3][3] - x[2][3] * x[3][2]
            e_2 = x[2][0] * x[3][3] - x[2][3] * x[3][0]
            e_3 = x[2][0] * x[3][2] - x[2][2] * x[3][0]
            e = x[1][0] * e_1 - x[1][2] * e_2 + x[1][3] * e_3
            f_1 = x[2][1] * x[3][3] - x[2][3] * x[3][1]
            f_2 = x[2][0] * x[3][3] - x[2][3] * x[3][0]
            f_3 = x[2][0] * x[3][1] - x[2][1] * x[3][0]
            f = x[1][0] * f_1 - x[1][1] * f_2 + x[1][3] * f_3
            g_1 = x[2][1] * x[3][2] - x[2][2] * x[3][1]
            g_2 = x[2][0] * x[3][2] - x[2][2] * x[3][0]
            g_3 = x[2][0] * x[3][1] - x[2][1] * x[3][0]
            g = x[1][0] * g_1 - x[1][1] * g_2 + x[1][2] * g_3
            return (x[0][0] * d - x[0][1] * e + x[0][2] * f - x[0][3] * g)

    def inverse(x):
        global ans
        if (num != 0):
            e = testEmpty(num)
            if (e is True):
                y = np.size(x, 0)
                z = np.size(x, 1)
                if (y == z):
                    det = calDet(x)
                    if (det != 0):
                        adj = calAdj(x)
                        ans = (1 / det) * adj
                    else:
                        ans = "DETERMINANT OF MATRIX IS 0.\nMATRIX IS NOT INVERTIBLE"
                    box_result.configure(text=ans)
                    button_chg.configure(state="active")
                    if (num == 3):
                        global matrix_want
                        matrix_want = ans
                else:
                    errorSquare(0)
        else:
            warning(0)

    def transpose(x):
        global ans
        if (num != 0):
            e = testEmpty(num)
            if (e is True):
                ans = x.transpose()
                box_result.configure(text=ans)
                button_chg.configure(state="active")
                if (num == 3):
                    global matrix_want
                    matrix_want = ans
        else:
            warning(0)

    def invalidInputScalar(x):
        statement = "INVALID INPUT FOR SCALAR.\nPLEASE TRY AGAIN"
        msg = messagebox.showerror("ERROR", statement)
        scalar_apply.delete(0, END)

    def scalar(x):
        global ans
        if (num != 0):
            e = testEmpty(num)
            if (e is True):
                temp = scalar_apply.get().split("/")
                if (len(temp) == 1):
                    try:
                        c = float(temp[0])
                    except ValueError:
                        invalidInput(0)
                elif (len(temp) == 2):
                    try:
                        c_1 = float(temp[0])
                        c_2 = float(temp[1])
                        c = c_1 / c_2
                    except ValueError:
                        invalidInputScalar(0)
                else:
                    invalidInputScalar(0)
                ans = np.multiply(x, c)
                box_result.configure(text=ans)
                button_chg.configure(state="active")
                if (num == 3):
                    global matrix_want
                    matrix_want = ans
        else:
            warning(0)

    def errorMxN(x):
        if (num == 1):
            y = "A"
        elif (num == 2):
            y = "B"
        else:
            y = "C"
        if (x == 1):
            statement = "MULTIPLICATION NOT ALLOWED DUE TO DIFFERENT ROW OF MATRIX " + y
            statement += " WITH COLUMN OF MATRIX A.\nPLEASE EDIT MATRIX"
        elif (x == 2):
            statement = "MULTIPLICATION NOT ALLOWED DUE TO DIFFERENT ROW OF MATRIX " + y
            statement += " WITH COLUMN OF MATRIX B.\nPLEASE EDIT MATRIX"
        else:
            statement = "MULTIPLICATION NOT ALLOWED DUE TO DIFFERENT ROW OF MATRIX " + y
            statement += " WITH COLUMN OF MATRIX C.\nPLEASE EDIT MATRIX"
        msg = messagebox.showerror("ERROR", statement)

    def multiply(x):
        global ans
        if (num != 0):
            e_1 = testEmpty(num)
            if (e_1 is True):
                y = np.size(x, 1)
                choose = multiply_matrix.get()
                if (choose == "A"):
                    e_2 = testEmpty(1)
                    if (e_2 is True):
                        if (y == mA):
                            ans = np.dot(x, A)
                        else:
                            errorMxN(1)
                elif (choose == "B"):
                    e_2 = testEmpty(2)
                    if (e_2 is True):
                        if (y == mB):
                            ans = np.dot(x, B)
                        else:
                            errorMxN(2)
                else:
                    e_2 = testEmpty(3)
                    if (e_2 is True):
                        row_ans = np.size(ans, 0)
                        if (y == row_ans):
                            ans = np.dot(x, ans)
                        else:
                            errorMxN(3)
                box_result.configure(text=ans)
                button_chg.configure(state="active")
                if (num == 3):
                    global matrix_want
                    matrix_want = ans
        else:
            warning(0)

    def warning(x):
        if (x == 0):
            statement = "YOU HAVEN'T CHOOSE WHICH MATRIX TO UNDERGO THIS OPERATION"
            msg = messagebox.showwarning("WARNING", statement)
        else:
            statement = "TRANSFORMATION ONLY VALID FOR MATRIX WITH ROW=2"
            msg = messagebox.showwarning("WARNING", statement)

    def minus(x):
        global ans
        if (num != 0):
            e_1 = testEmpty(num)
            if (e_1 is True):
                y = np.size(x, 0)
                z = np.size(x, 1)
                choose = minus_matrix.get()
                if (choose == "A"):
                    e_2 = testEmpty(1)
                    if (e_2 is True):
                        if (mA == y and nA == z):
                            ans = x - A
                        else:
                            differentDimension(1)
                elif (choose == "B"):
                    e_2 = testEmpty(2)
                    if (e_2 is True):
                        if (mB == y and nB == z):
                            ans = x - B
                        else:
                            differentDimension(2)
                else:
                    e_2 = testEmpty(3)
                    if (e_2 is True):
                        row_ans = np.size(ans, 0)
                        column_ans = np.size(ans, 1)
                        if (row_ans == y and column_ans == z):
                            ans = x - ans
                        else:
                            differentDimension(3)
                box_result.configure(text=ans)
                button_chg.configure(state="active")
                if (num == 3):
                    global matrix_want
                    matrix_want = ans
        else:
            warning(0)

    def differentDimension(x):
        if (num == 1):
            y = "A"
        elif (num == 2):
            y = "B"
        else:
            y = "C"
        if (x == 1):
            statement = "DIMENSION DIFFERENT BETWEEN MATRIX " + y
            statement += " AND A.\nPLEASE EDIT MATRIX"
        elif (x == 2):
            statement = "DIMENSION DIFFERENT BETWEEN MATRIX " + y
            statement += " AND B.\nPLEASE EDIT MATRIX"
        else:
            statement = "DIMENSION DIFFERENT BETWEEN MATRIX " + y
            statement += " AND C.\nPLEASE EDIT MATRIX"
        msg = messagebox.showerror("ERROR", statement)

    def testEmpty(x):
        if (x == 1):
            if (mA == 0 or nA == 0):
                statement = "MATRIX A IS EMPTY"
                msg = messagebox.showwarning("WARNING", statement)
                return False
            else:
                return True
        elif (x == 2):
            if (mB == 0 or nB == 0):
                statement = "MATRIX B IS EMPTY"
                msg = messagebox.showwarning("WARNING", statement)
                return False
            else:
                return True
        else:
            try:
                y = np.size(ans, 0)
                return True
            except IndexError:
                statement = "RESULT IS NOT A MATRIX"
                msg = messagebox.showwarning("WARNING", statement)
                return False

    def add(x):
        global ans
        if (num != 0):
            e_1 = testEmpty(num)
            if (e_1 is True):
                y = np.size(x, 0)
                z = np.size(x, 1)
                choose = add_matrix.get()
                if (choose == "A"):
                    e_2 = testEmpty(1)
                    if (e_2 is True):
                        if (mA == y and nA == z):
                            ans = x + A
                        else:
                            differentDimension(1)
                elif (choose == "B"):
                    e_2 = testEmpty(2)
                    if (e_2 is True):
                        if (mB == y and nB == z):
                            ans = x + B
                        else:
                            differentDimension(2)
                else:
                    e_2 = testEmpty(3)
                    if (e_2 is True):
                        row_ans = np.size(ans, 0)
                        column_ans = np.size(ans, 1)
                        if (row_ans == y and column_ans == z):
                            ans = x + ans
                        else:
                            differentDimension(3)
                box_result.configure(text=ans)
                button_chg.configure(state="active")
                if (num == 3):
                    global matrix_want
                    matrix_want = ans
        else:
            warning(0)

    def update():
        global num, matrix_want
        num = v.get()
        if (num == 1):
            matrix_want = A
        elif (num == 2):
            matrix_want = B
        else:
            matrix_want = ans

    v = IntVar()
    choice_A = Radiobutton(root, text="Matrix A", variable=v, value=1, command=update)
    choice_A.configure(font=("bold", 15))
    choice_B = Radiobutton(root, text="Matrix B", variable=v, value=2, command=update)
    choice_B.configure(font=("bold", 15))
    choice_R = Radiobutton(root, text="Matrix C (Result)", variable=v, value=3)
    choice_R.configure(command=update, font=("bold", 15))
    choice_A.grid(row=10, column=1, columnspan=3)
    choice_B.grid(row=10, column=4, columnspan=3)
    choice_R.grid(row=10, column=7, columnspan=4)

    button_add = Button(root, text="add matrix \t ", padx=18, pady=5, bg='pink')
    button_add.configure(command=lambda: add(matrix_want))
    button_add.grid(row=12, column=1, columnspan=3)
    add_matrix = Combobox(root, values=["A", "B", "C"], width=3)
    add_matrix.grid(row=12, column=3)
    button_minus = Button(root, text="minus matrix \t ", padx=18, pady=5, bg='pink')
    button_minus.configure(command=lambda: minus(matrix_want))
    button_minus.grid(row=12, column=4, columnspan=3)
    minus_matrix = Combobox(root, values=["A", "B", "C"], width=3)
    minus_matrix.grid(row=12, column=6)

    button_multiply = Button(root, text="multiply matrix   \t          ", padx=5, pady=5)
    button_multiply.configure(bg='pink', command=lambda: multiply(matrix_want))
    button_multiply.grid(row=13, column=1, columnspan=3)
    multiply_matrix = Combobox(root, values=["A", "B", "C"], width=3)
    multiply_matrix.grid(row=13, column=3)
    button_scalar = Button(root, text="multiply by \t      ", padx=10, pady=5)
    button_scalar.configure(bg='pink', command=lambda: scalar(matrix_want))
    button_scalar.grid(row=13, column=4, columnspan=3)
    scalar_apply = Entry(root, width=5, borderwidth=3)
    scalar_apply.grid(row=13, column=6)

    button_transpose = Button(root, text="transpose", padx=17, pady=5, bg='pink')
    button_transpose.configure(command=lambda: transpose(matrix_want))
    button_transpose.grid(row=14, column=1, columnspan=2)
    button_inverse = Button(root, text="inverse", padx=25, pady=5, bg='pink')
    button_inverse.configure(command=lambda: inverse(matrix_want))
    button_inverse.grid(row=14, column=3, columnspan=2)
    button_det = Button(root, text="determinant", padx=10, pady=5, bg='pink')
    button_det.configure(command=lambda: det(matrix_want))
    button_det.grid(row=14, column=5, columnspan=2)

    button_minor = Button(root, text="minor", padx=7, pady=5, bg='pink')
    button_minor.configure(command=lambda: minor(matrix_want))
    button_minor.grid(row=15, column=1)
    button_cofactor = Button(root, text="cofactor", padx=18, pady=5, bg='pink')
    button_cofactor.configure(command=lambda: cofactor(matrix_want))
    button_cofactor.grid(row=15, column=2, columnspan=2)
    button_adj = Button(root, text="adjugate", padx=17, pady=5, bg='pink')
    button_adj.configure(command=lambda: adj(matrix_want))
    button_adj.grid(row=15, column=4, columnspan=2)
    button_rank = Button(root, text="rank", padx=9, pady=5, bg='pink')
    button_rank.configure(command=lambda: rank(matrix_want))
    button_rank.grid(row=15, column=6)

    button_symmetric = Button(root, text="symmetric", padx=12, pady=5, bg='pink')
    button_symmetric.configure(command=lambda: symmetric(matrix_want))
    button_symmetric.grid(row=16, column=1, columnspan=2)
    button_orthogonal = Button(root, text="orthogonal", padx=15, pady=5, bg='pink')
    button_orthogonal.configure(command=lambda: orthogonal(matrix_want))
    button_orthogonal.grid(row=16, column=3, columnspan=2)
    button_trace = Button(root, text="trace", padx=8, pady=5, bg='pink')
    button_trace.configure(command=lambda: trace(matrix_want))
    button_trace.grid(row=16, column=5)

    def invalidInputAngel(x):
        statement = "INVALID INPUT FOR ANGLE.\nPLEASE TRY AGAIN"
        msg = messagebox.showerror("ERROR", statement)
        rad.delete(0, END)

    def rotate(x):
        global ans
        if (num != 0):
            if (num == 1):
                e = testEmpty(1)
            elif (num == 2):
                e = testEmpty(2)
            else:
                e = testEmpty(3)
            if (e is True):
                y = np.size(x, 0)
                if (y == 2):
                    direction = clock.get()
                    z = np.zeros((2, 2))
                    temp = rad.get().split("/")
                    if (len(temp) == 1):
                        try:
                            angle = float(temp[0])
                        except ValueError:
                            invalidInputAngel(0)
                    elif (len(temp) == 2):
                        try:
                            angle_1 = float(temp[0])
                            angle_2 = float(temp[1])
                            angle = angle_1 / angle_2
                        except ValueError:
                            invalidInputAngel(0)
                    else:
                        invalidInputAngel(0)
                    if (direction == "clockwise"):
                        z = np.array([[math.cos(angle), math.sin(angle)],
                                      [-math.sin(angle), math.cos(angle)]])
                    else:
                        z = np.array([[math.cos(angle), -math.sin(angle)],
                                      [math.sin(angle), math.cos(angle)]])
                    ans = np.dot(z, x)
                    box_result.configure(text=ans)
                    button_chg.configure(state="active")
                    if (num == 3):
                        global matrix_want
                        matrix_want = ans
                else:
                    warning(1)
        else:
            warning(0)

    def invlidInputTranslate(x):
        statement = "INVALID INPUT FOR d" + x + "\nPLEASE TRY AGAIN"
        msg = messagebox.showerror("ERROR", statement)
        translate.delete(0, END)

    def translation(x):
        global ans
        if (num != 0):
            if (num == 1):
                e = testEmpty(1)
            elif (num == 2):
                e = testEmpty(2)
            else:
                e = testEmpty(3)
            if (e is True):
                y = np.size(x, 0)
                z = np.size(x, 1)
                if (y == 2):
                    direction = translate_direction.get()
                    result = np.zeros((y, z))
                    if (direction != "x and y"):
                        temp = translate.get().split("/")
                        if (len(temp) == 1):
                            try:
                                d = float(temp[0])
                            except ValueError:
                                invlidInputTranslate(direction)
                        elif (len(temp) == 2):
                            try:
                                d_up = float(temp[0])
                                d_down = float(temp[1])
                                d = d_up / d_down
                            except ValueError:
                                invlidInputTranslate(direction)
                        else:
                            invlidInputTranslate(direction)
                        if (direction == "x"):
                            for i in range(z):
                                result[0][i] = d + x[0][i]
                                result[1][i] = x[1][i]
                        elif (direction == "y"):
                            for i in range(z):
                                result[0][i] = x[0][i]
                                result[1][i] = d + x[0][i]
                    else:
                        d = translate.get().split(",")
                        if (len(d) == 2):
                            dx_val = d[0]
                            dy_val = d[1]
                            # check dx is fraction
                            temp = dx_val.split("/")
                            if (len(temp) == 1):
                                try:
                                    dx = float(temp[0])
                                except ValueError:
                                    invlidInputTranslate("x")
                            elif (len(temp) == 2):
                                try:
                                    dx_up = float(temp[0])
                                    dx_down = float(temp[1])
                                    dx = dx_up / dx_down
                                except ValueError:
                                    invlidInputTranslate("x")
                            else:
                                invlidInputTranslate("x")
                            # check dy is fraction
                            temp = dy_val.split("/")
                            if (len(temp) == 1):
                                try:
                                    dy = float(temp[0])
                                except ValueError:
                                    invlidInputTranslate("y")
                            elif (len(temp) == 2):
                                try:
                                    dy_up = float(temp[0])
                                    dy_down = float(temp[1])
                                    dy = dy_up / dy_down
                                except ValueError:
                                    invlidInputTranslate("y")
                            else:
                                invlidInputTranslate("y")
                        else:
                            statement = "INVALID INPUT FOR dx AND dy\nPLEASE TRY "
                            statement += "AGAIN BY USING COMMA(,) TO SPLIT dx AND dy"
                            msg = messagebox.showwarning("ERROR", statement)
                            translate.delete(0, END)
                        for i in range(z):
                            result[0][i] = dx + x[0][i]
                            result[1][i] = dy + x[1][i]
                    ans = result
                    box_result.configure(text=ans)
                    button_chg.configure(state="active")
                    if (num == 3):
                        global matrix_want
                        matrix_want = ans
                else:
                    warning(1)
        else:
            warning(0)

    def invalidInputScale(x):
        statement = "INVALID INPUT OF" + x + "\nPLEASE TRY AGAIN"
        msg = messagebox.showerror("ERROR", statement)
        scale.delete(0, END)

    def scaling(x):
        global ans
        if (num != 0):
            if (num == 1):
                e = testEmpty(1)
            elif (num == 2):
                e = testEmpty(2)
            else:
                e = testEmpty(3)
            if (e is True):
                y = np.size(x, 0)
                if (y == 2):
                    s = scale.get().split(",")
                    z = np.zeros((2, 2))
                    if (len(s) == 2):
                        s_x_val = s[0]
                        s_y_val = s[1]
                        temp = s_x_val.split("/")
                        if (len(temp) == 1):
                            try:
                                s_x = float(temp[0])
                            except ValueError:
                                invalidInputScalar("Sx")
                        elif (len(temp) == 2):
                            try:
                                s_x_up = float(temp[0])
                                s_x_down = float(temp[1])
                                s_x = s_x_up / s_x_down
                            except ValueError:
                                invalidInputScalar("Sx")
                        else:
                            invalidInputScalar("Sx")
                        temp = s_y_val.split("/")
                        if (len(temp) == 1):
                            try:
                                s_y = float(temp[0])
                            except ValueError:
                                invalidInputScalar("Sy")
                        elif (len(temp) == 2):
                            try:
                                s_y_up = float(temp[0])
                                s_y_down = float(temp[1])
                                s_y = s_y_up / s_y_down
                            except ValueError:
                                invalidInputScalar("Sy")
                        else:
                            invalidInputScalar("Sy")
                    else:
                        statement = "INVALID INPUT \nPLEASE TRY AGAIN BY "
                        statement += "USING COMMA(,) TO SPLIT Sx AND Sy"
                        statement += "\nIF Sx=Sy , USING 'multiply by' BUTTON"
                        msg = messagebox.showwarning("ERROR", statement)
                        scale.delete(0, END)
                    z = np.array([[s_x, 0], [0, s_y]])
                    ans = np.dot(z, x)
                    box_result.configure(text=ans)
                    button_chg.configure(state="active")
                    if (num == 3):
                        global matrix_want
                        matrix_want = ans
                else:
                    warning(1)
        else:
            warning(0)

    def reflect(x):
        global ans
        if (num != 0):
            if (num == 1):
                e = testEmpty(1)
            elif (num == 2):
                e = testEmpty(2)
            else:
                e = testEmpty(3)
            if (e is True):
                y = np.size(x, 0)
                if (y == 2):
                    axis = axis_reflect.get()
                    z = np.zeros((2, 2))
                    if (axis == "x-axis"):
                        z = np.array([[1, 0], [0, -1]])
                    elif (axis == "y-axis"):
                        z = np.array([[-1, 0], [0, 1]])
                    elif (axis == "y=x"):
                        z = np.array([[0, 1], [1, 0]])
                    elif (axis == "y=-x"):
                        z = np.array([[0, -1], [-1, 0]])
                    else:
                        z = np.array([[-1, 0], [0, -1]])
                    ans = np.dot(z, x)
                    box_result.configure(text=ans)
                    button_chg.configure(state="active")
                    if (num == 3):
                        global matrix_want
                        matrix_want = ans
                else:
                    warning(1)
        else:
            warning(0)

    def invalidInputShear(x):
        statement = "INVALID INPUT FOR sh_" + x + "\nPLEASE TRY AGAIN"
        msg = messagebox.showerror("ERROR", statement)
        shear.delete(0, END)

    def shearing(x):
        global ans
        if (num != 0):
            if (num == 1):
                e = testEmpty(1)
            elif (num == 2):
                e = testEmpty(2)
            else:
                e = testEmpty(3)
            if (e is True):
                y = np.size(x, 0)
                if (y == 2):
                    direction = shear_direction.get()
                    z = np.zeros((2, 2))
                    if (direction != "x and y"):
                        temp = shear.get().split("/")
                        if (len(temp) == 1):
                            try:
                                h = float(temp[0])
                            except ValueError:
                                invalidInputShear(direction)
                        elif (len(temp) == 2):
                            try:
                                h_up = float(temp[0])
                                h_down = float(temp[1])
                                h = h_up / h_down
                            except ValueError:
                                invalidInputShear(direction)
                        else:
                            invalidInputShear(direction)
                        if (direction == "x"):
                            z = np.array([[1, h], [0, 1]])
                        elif (direction == "y"):
                            z = np.array([[1, 0], [h, 1]])
                    else:
                        h = shear.get().split(",")
                        if (len(h) == 2):
                            hx_val = h[0]
                            hy_val = h[1]
                            temp = hx_val.split("/")
                            if (len(temp) == 1):
                                try:
                                    h_x = float(temp[0])
                                except ValueError:
                                    invalidInputShear("x")
                            elif (len(temp) == 2):
                                try:
                                    hx_up = float(temp[0])
                                    hx_down = float(temp[1])
                                    h_x = hx_up / hx_down
                                except ValueError:
                                    invalidInputShear("x")
                            else:
                                invalidInputShear("x")
                            temp = hy_val.split("/")
                            if (len(temp) == 1):
                                try:
                                    h_y = float(temp[0])
                                except ValueError:
                                    invalidInputShear("y")
                            elif (len(temp) == 2):
                                try:
                                    hy_up = float(temp[0])
                                    hy_down = float(temp[1])
                                    h_y = hy_up / hy_down
                                except ValueError:
                                    invalidInputShear("y")
                            else:
                                invalidInputShear("y")
                            z = np.array([[1, h_x], [h_y, 1]])
                        else:
                            statement = "INVALID INPUT \nPLEASE TRY AGAIN BY "
                            statement += "USING COMMA(,) TO SPLIT sh_x AND sh_y"
                            msg = messagebox.showwarning("ERROR", statement)
                            shear.delete(0, END)
                    ans = np.dot(z, x)
                    box_result.configure(text=ans)
                    button_chg.configure(state="active")
                    if (num == 3):
                        global matrix_want
                        matrix_want = ans
                else:
                    warning(1)
        else:
            warning(0)

    button_shear = Button(root, text="Shear  \t\t        by\t\t", padx=25, pady=5)
    button_shear.configure(bg='pink', command=lambda: shearing(matrix_want))
    button_shear.grid(row=12, column=11, columnspan=5)
    shear_direction = Combobox(root, values=["x", "y", "x and y"], width=7)
    shear_direction.grid(row=12, column=12, columnspan=2)
    shear = Entry(root, width=10, borderwidth=3)
    shear.grid(row=12, column=14, columnspan=2)

    button_reflect = Button(root, text="\treflect through\t\t\t", pady=5, bg='pink')
    button_reflect.configure(command=lambda: reflect(matrix_want))
    button_reflect.grid(row=13, column=11, columnspan=5)
    axis_reflect = Combobox(root, values=["x-axis", "y-axis", "y=x", "y=-x", "origin"], width=5)
    axis_reflect.grid(row=13, column=14, columnspan=2)

    button_scale = Button(root, text="scale by factor (Sx,Sy)\t\t", padx=25, pady=5)
    button_scale.configure(bg='pink', command=lambda: scaling(matrix_want))
    button_scale.grid(row=14, column=11, columnspan=5)
    scale = Entry(root, width=10, borderwidth=3)
    scale.grid(row=14, column=14, columnspan=2)

    button_translate = Button(root, text="  translate\t\tby\t\t", pady=5, bg='pink')
    button_translate.configure(command=lambda: translation(matrix_want))
    button_translate.grid(row=15, column=11, columnspan=5)
    translate_direction = Combobox(root, values=["x", "y", "x and y"], width=7)
    translate_direction.grid(row=15, column=12, columnspan=2)
    translate = Entry(root, width=10, borderwidth=3)
    translate.grid(row=15, column=14, columnspan=2)

    button_rotate = Button(root, text="   rotate\t\t\t\t(in rad)\t  ", padx=30, pady=5)
    button_rotate.configure(bg='pink', command=lambda: rotate(matrix_want))
    button_rotate.grid(row=16, column=11, columnspan=6)
    clock = Combobox(root, values=["counter-colckwise", "clockwise"], width=18)
    clock.grid(row=16, column=12, columnspan=3)
    rad = Entry(root, width=5, borderwidth=3)
    rad.grid(row=16, column=16)

    def ori(ans):
        box_result.configure(text=ans)
        button_chg.configure(state="active")
        button_ori.configure(state="disable")

    def chg(ans):
        y = np.size(ans, 0)
        z = np.size(ans, 1)
        ans = ans.astype('object')
        for i in range(y):
            for j in range(z):
                temp = Fraction(ans[i][j]).limit_denominator()
                ans[i][j] = str(temp.numerator) + "/" + str(temp.denominator)
        box_result.configure(text=ans)
        button_chg.configure(state="disable")
        button_ori.configure(state="active")

    button_chg = Button(root, text="change to\n fraction", padx=5, pady=5, bg='VioletRed1')
    button_chg.configure(command=lambda: chg(ans), state='disable')
    button_chg.grid(row=20, column=0, rowspan=2)
    button_ori = Button(root, text="change to\n float", padx=5, pady=5, bg='VioletRed1')
    button_ori.configure(command=lambda: ori(ans), state='disable')
    button_ori.grid(row=22, column=0, rowspan=2)

    def exit():
        msg = messagebox.askyesno("EXIT", "Are you sure want to exit?")
        if (msg):
            root.destroy()

    button_exit = Button(root, text="EXIT", padx=20, pady=20, command=exit, bg='red')
    button_exit.grid(row=23, column=17)

    root.mainloop()

new=Tk()
new.title("Computer Graphic")

button_1=Button(new,text="vector",padx=40,pady=20,command=vector)
button_2=Button(new,text="matrix",padx=40,pady=20,command=matrix)
button_1.pack()
button_2.pack()

new.mainloop()
