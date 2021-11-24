from tkinter import*
import math

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
button_0=Button(top,text="0",padx=90,pady=20,command=lambda:button(0),bg='aquamarine')
# we use lambda so that we can pass a varaible through the function
button_1=Button(top,text="1",padx=40,pady=20,command=lambda:button(1),bg='aquamarine')
button_2=Button(top,text="2",padx=40,pady=20,command=lambda:button(2),bg='aquamarine')
button_3=Button(top,text="3",padx=40,pady=20,command=lambda:button(3),bg='aquamarine')
button_4=Button(top,text="4",padx=40,pady=20,command=lambda:button(4),bg='aquamarine')
button_5=Button(top,text="5",padx=40,pady=20,command=lambda:button(5),bg='aquamarine')
button_6=Button(top,text="6",padx=40,pady=20,command=lambda:button(6),bg='aquamarine')
button_7=Button(top,text="7",padx=40,pady=20,command=lambda:button(7),bg='aquamarine')
button_8=Button(top,text="8",padx=40,pady=20,command=lambda:button(8),bg='aquamarine')
button_9=Button(top,text="9",padx=40,pady=20,command=lambda:button(9),bg='aquamarine')

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
button_sign=Button(top,text="-",padx=40,pady=20,command=lambda:button("-"),bg='aquamarine')
button_del=Button(top,text="DEL",padx=40,pady=20,command=button_del,bg='salmon')
button_clear=Button(top,text="AC",padx=40,pady=20,command=ac,bg='salmon')

button_magnitude=Button(top,text="magnitude",padx=14,pady=20,command=magnitude,bg='aquamarine')
button_dotP=Button(top,text="dotProduct",padx=20,pady=20,command=dotP,bg='aquamarine')
button_crossP=Button(top,text="crossProduct",padx=13,pady=20,command=crossP,bg='aquamarine')

button_scale=Button(top,text="scaling",padx=25,pady=20,command=scale,bg='aquamarine')
button_add=Button(top,text="addition",padx=27,pady=20,command=add,bg='aquamarine')
button_subtract=Button(top,text="subtraction",padx=18,pady=20,command=subtract,bg='aquamarine')

button_point=Button(top,text="point(.)",padx=23,pady=20,command=lambda:button("."),bg='aquamarine')
button_comma=Button(top,text="comma(,)",padx=17,pady=20,command=comma,bg='aquamarine')
button_equal=Button(top,text="=",padx=100,pady=20,command=equal,bg='aquamarine')

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