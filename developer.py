from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x768+0+0")
        self.root.title("Developer")

        # first header image  
        img=Image.open(r"images\tes_gen_blog_post_071921_1233182206-1-800x412.jpg")
        img=img.resize((1360,450),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1360,height=150)

        # backgorund image 
        bg1=Image.open(r"images\software-developer-6521720_1280.jpg")
        bg1=bg1.resize((1360,768),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=150,width=1360,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Developer Pannel",font=("times new roman",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        #main frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=850,y=50,width=500,height=450)

        img_top=Image.open(r"images\IMG_20240118_202924new.jpg")
        img_top=img_top.resize((240,230),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        # set image as lable
        f_lb1 = Label(main_frame,image=self.photoimg_top)
        f_lb1.place(x=300,y=0,width=200,height=200)

        dev_label=Label(main_frame,text="Hii, My name is Vaishnavi Kainthola.",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=6)

        dev_label=Label(main_frame,text="I am a student of Graphic Era Hill",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=30)

        dev_label=Label(main_frame,text="University , Dehradun.",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=54)

        dev_label=Label(main_frame,text="This mini project is developed in order",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=78)

        dev_label=Label(main_frame,text="to streamline and enhance the efficiency",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=102)

        dev_label=Label(main_frame,text="of attendance management processes,",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=126)

        dev_label=Label(main_frame,text="by eliminating the need for traditional",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=150)

        dev_label=Label(main_frame,text="methods.",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=0,y=174)

        img_down=Image.open(r"images\GEHu-1abd6f9c.jpg")
        img_down=img_down.resize((500,230),Image.Resampling.LANCZOS)
        self.photoimg_down=ImageTk.PhotoImage(img_down)

        # set image as lable
        f_lb1 = Label(main_frame,image=self.photoimg_down)
        f_lb1.place(x=2,y=210,width=493,height=230)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop() 