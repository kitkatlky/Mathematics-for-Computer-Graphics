import numpy as np
from tkinter import *
from tkinter.ttk import Combobox

top=Tk()
top.title("Gram Schmidt")

a={}

lbl_size=Label(top,text="Choose size of matrix : ",font=(10))
lbl_size.grid(row=0,column=0,columnspan=4)
size=Combobox(top,values=["1x1","2x2","3x3","4x4"],width=5)
size.grid(row=0,column=4)
lbl=Label(top,text="Enter your matrix here : ",font=(10))
lbl.grid(row=1,column=0,columnspan=4)

for i in range(4):
    for j in range(4):
        index = (i, j)
        box_a = Entry(top, width=5,borderwidth=3)
        box_a.grid(row=2 + i, column=0 + j)
        a[index] = box_a

def get():
    x=size.get()
    if (x=="1x1"):
        x=1
    elif(x=="2x2"):
        x=2
    elif(x=="3x3"):
        x=3
    else:
        x=4
    return x

def gs():
    num=get()
    A=[]
    for i in range (num):
        row=[]
        for j in range(num):
            index=(i,j)
            try:
                row.append(float(a[index].get()))
            except ValueError:
                return
        A.append(row)
    A=np.array(A)

    n = A.shape[1]
    for j in range(n):
        for k in range(j):
            A[:,j]-=np.dot(A[:,k],A[:,j])*A[:,k]
        A[:,j]=A[:,j]/np.linalg.norm(A[:,j])
    result.configure(text=A)


button_submit=Button(top,text="submit",padx=20,pady=20,command=gs,bg='orange')
button_submit.grid(row=6,column=0,columnspan=2)
lbl_result=Label(top,text="RESULT : ")
lbl_result.grid(row=7,column=0)
result = Label(top, text="[]", font=("bold", 15))
result.grid(row=8, column=0, rowspan=5, columnspan=12)

# def gram_schmidt(A):
#     """Orthogonal a set of vectors stored as the columns of matrix A"""
# #     Get the number of vectors
#     n=A.shape[1]
#     for j in range(n):
#         # To orthogonalize the vector in column j with respect to the
#         # previous vectors, subtract from it its projection onto
#         # each of the previous vectors.
#         for k in range(j):
#             A[:,j]-=np.dot(A[:,k],A[:,j])*A[:,k]
#         A[:,j]=A[:,j]/np.linalg.norma(A[:,j])
#     return A
top.mainloop()