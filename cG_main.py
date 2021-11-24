from tkinter import*

def vector():
    import vC

def matrix():
    import mC

def euler():
    import eM

def grsc():
    import gS

new=Tk()
new.title("Computer Graphic")

lbl=Label(new,text="Please choose one of the following : \n",font=("bold",15))
lbl.pack()

button_1=Button(new,text="vector calculator",padx=60,pady=20,command=vector,bg='aquamarine')
button_2=Button(new,text="matrix calculator",padx=60,pady=20,command=matrix,bg='VioletRed1')
button_3=Button(new,text="euler computation",padx=54,pady=20,command=euler,bg='cyan')
button_4=Button(new,text="gram schmidt orthogonalization",padx=20,pady=20,command=grsc,bg='khaki1')
button_1.pack()
button_2.pack()
button_3.pack()
button_4.pack()

spc=Label(new,text="\n")
spc.pack()

new.mainloop()