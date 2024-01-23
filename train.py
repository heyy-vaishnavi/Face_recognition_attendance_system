from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x768+0+0")
        self.root.title("Train Data")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("Calibri", 35, "bold"), bg="blue", fg="yellow")
        title_lbl.place(x=0, y=0, width=1360, height=50)
        
        img1_top= Image.open(r"images\face-recognition-1024x630.jpg")
        img1_top= img1_top.resize((1360,630),Image.Resampling.LANCZOS)
        self.photoimg1_top = ImageTk.PhotoImage(img1_top)

        f_lbl = Label(self.root, image=self.photoimg1_top)
        f_lbl.place(x=0, y=50, width=1360, height=300)

        #button
        b1 = Button(self.root,command=self.train_classifier,text= "Train Student Data",cursor="hand2",font=("Calibri", 25, "bold"), bg="yellow", fg="black")
        b1.place(x=0, y=350, width=1360, height=40)

        img1_bottom= Image.open(r"images\download.jpeg")
        img1_bottom= img1_bottom.resize((1360,630),Image.Resampling.LANCZOS)
        self.photoimg1_bottom = ImageTk.PhotoImage(img1_bottom)

        f_lbl = Label(self.root, image=self.photoimg1_bottom)
        f_lbl.place(x=0, y=390, width=1360, height=310)

    def train_classifier(self):
        data_dir=("image_data")
        path= [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]

        for image in path:
            img= Image.open(image).convert('L') #gray scale
            imageNp= np.array(img,'uint8')
            id= int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #================================train the classifier and save================================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training data sets completed successfully!!")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()