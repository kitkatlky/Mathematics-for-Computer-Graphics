from tkinter import *
import numpy as np

top = Tk()
top.title("Gram Schmidt Orthogonalization")

a = {}

dimension = Label(top, text="dimension of vector (row) = ")
dimension.grid(row=0, column=0, columnspan=3)
var_m = StringVar()
spin_m = Spinbox(top, from_=1, to=4, textvariable=var_m, width=3)
spin_m.grid(row=0, column=3)

num = Label(top, text="number of vector (column) = ")
num.grid(row=1, column=0, columnspan=3)
var_n = StringVar()
spin_n = Spinbox(top, from_=1, to=4, textvariable=var_n, width=3)
spin_n.grid(row=1, column=3)

for i in range(4):
    for j in range(4):
        box_a = Entry(top, width=5, borderwidth=3, state='disable')
        box_a.grid(row=3 + i, column=0 + j)

def display():
    global m, n
    m = int(spin_m.get())
    n = int(spin_n.get())
    spin_m.configure(state='disable')
    spin_n.configure(state='disable')
    for i in range(m):
        for j in range(n):
            index = (i, j)
            box_a = Entry(top, width=5, borderwidth=3)
            box_a.grid(row=3 + i, column=0 + j)
            a[index] = box_a
    button_edit.configure(state='active')
    button_ok.configure(state='disable')

def resize():
    spin_m.configure(state='normal')
    spin_n.configure(state='normal')
    for i in range(4):
        for j in range(4):
            box_a = Entry(top, width=5, borderwidth=3, state='disable')
            box_a.grid(row=3 + i, column=0 + j)
    button_ok.configure(state='active')
    button_edit.configure(state='disable')

button_ok = Button(top, text="OK", padx=5, pady=5, command=display, bg='peach puff')
button_edit = Button(top, text="edit", command=resize, padx=5, pady=5)
button_edit.configure(bg='peach puff', state='disable')
button_ok.grid(row=2, column=5)
button_edit.grid(row=2, column=6)

def gs():
    A = []
    for i in range(m):
        row = []
        for j in range(n):
            index = (i, j)
            try:
                row.append(float(a[index].get()))
            except ValueError:
                return
        A.append(row)
    A = np.array(A)
    for j in range(n):
        for k in range(j):
            A[:, j] -= np.dot(A[:, k], A[:, j]) * A[:, k]
        A[:, j] = A[:, j] / np.linalg.norm(A[:, j])
    result.configure(text=A)

lbl_space=Label(top,text=" \n ")
lbl_space.grid(row=8,column=0,rowspan=2)
button_submit = Button(top, text="submit", padx=20, pady=10, command=gs, bg='khaki1')
button_submit.grid(row=9, column=3, columnspan=2)
lbl_result = Label(top, text="RESULT : ")
lbl_result.grid(row=10, column=0)
result = Label(top, text="[]", font=("bold", 15))
result.grid(row=11, column=0, rowspan=5, columnspan=12)

top.mainloop()