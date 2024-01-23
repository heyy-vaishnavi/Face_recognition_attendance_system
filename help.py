from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x768+0+0")
        self.root.title("Student Details")

        #title section
        title_lb1 = Label(self.root,text="Help Desk",font=("times new roman",30,"bold"),bg="black",fg="orange")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        img=Image.open(r"images\Tier-1-vs.-Tier-2-Help-Desk-Support.jpg")
        img=img.resize((1360,750),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=45,width=1360,height=750)

        dev_label=Label(f_lb1,text="Email: vkainthola206@gmail.com",font=("times new roman",18,"bold"),fg="navyblue",bg="white")
        dev_label.place(x=200,y=250)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()