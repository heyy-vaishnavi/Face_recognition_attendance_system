from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import csv
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x768+0+0")
        self.root.title("Face Detection")

        title_lbl = Label(self.root, text="FACE DETECTION", font=("Calibri", 35, "bold"), bg="black", fg="yellow")
        title_lbl.place(x=0, y=0, width=1360, height=50)
        
        img1_left= Image.open(r"images\Thumbnail_facial-recognition@2x.png")
        img1_left= img1_left.resize((700,700),Image.Resampling.LANCZOS)
        self.photoimg1_left = ImageTk.PhotoImage(img1_left)

        f_lbl = Label(self.root, image=self.photoimg1_left)
        f_lbl.place(x=0, y=50, width=680, height=700)

        img1_right= Image.open(r"images\abshfkjedsshkfjd.jpg")
        img1_right= img1_right.resize((700,700),Image.Resampling.LANCZOS)
        self.photoimg1_right = ImageTk.PhotoImage(img1_right)

        f_lbl = Label(self.root, image=self.photoimg1_right)
        f_lbl.place(x=680, y=50, width=700, height=700)

        b1 = Button(f_lbl,text= "FACE RECOGNITION",command=self.face_recog,cursor="hand2",font=("Calibri", 15, "bold"), bg="red", fg="white")
        b1.place(x=260, y=590, width=180, height=35)

    #===============================Attendance===============================================
    def mark_attendance(self,n):
        already_in_file = set()
        with open("vaishnavi.csv","r+",newline="\n") as f:
            for line in f:
                already_in_file.add(line.split(",")[0])
            
            if((n not in already_in_file)):
                with open("vaishnavi.csv","r+",newline="\n") as f:
                    now=datetime.now()
                    d1=now.strftime("%d/%m/%Y")
                    dtString=now.strftime("%H:%M:%S")
                    f.writelines(f"\n{n},{dtString},{d1},Present")

    #=================================face recognition========================================

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features= classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence= int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Faridabad8320", database="face_recognition",port=3306)
                my_cursor=conn.cursor()
                 
        
                known_id = 1
                my_cursor.execute("select Name from student where studentID=" + str(known_id))
                n= my_cursor.fetchone()

                if confidence>77:
                    cv2.putText(img, f"{n}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                    self.mark_attendance(n)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Detection",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)

                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade): 
            coord= draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap= cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img= recognize(img,clf,faceCascade)
            cv2.imshow("Face Recognition",img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()