from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x768+0+0")
        self.root.title("Face Recognition System")

        img = Image.open(r"images\GEHU-Dehradun-1abd6f9c.jpg")
        img = img.resize((1360,768),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1360, height=768)

        title_lbl = Label(root, text="Face Recognition Attendance Software", font=("Calibri", 38, "bold"), bg="black", fg="orange")
        title_lbl.place(x=0, y=0, width=1360, height=85)

        #student icon
        img1 = Image.open(r"images\istockphoto-1272815911-612x612.jpg")
        img1 = img1.resize((330, 280), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1_1 = Button(bg_img, image=self.photoimg1,command=self.student_details,cursor="hand2")
        b1_1.place(x=180, y=175, width=200, height=200)

        b1 = Button(bg_img,text= "Student Details",command=self.student_details,cursor="hand2",font=("Calibri", 17, "bold"), bg="black", fg="orange")
        b1.place(x=180, y=375, width=200, height=40)

        #detection icon
        img2 = Image.open(r"images\face-600x900.png")
        img2 = img2.resize((200, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1_1 = Button(bg_img, image=self.photoimg2,command=self.face_data,cursor="hand2")
        b1_1.place(x=450, y=175, width=200, height=200)

        b1 = Button(bg_img,text= "Face Detection",command=self.face_data,cursor="hand2",font=("Calibri", 17, "bold"), bg="black", fg="orange")
        b1.place(x=450, y=375, width=200, height=40)

        #attendance icon
        img3 = Image.open(r"images\istockphoto-1124965072-612x612.jpg")
        img3 = img3.resize((250, 250), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1_1 = Button(bg_img, image=self.photoimg3,command=self.attendance_data,cursor="hand2")
        b1_1.place(x=720, y=175, width=200, height=200)

        b1 = Button(bg_img,text= "Attendance",command=self.attendance_data,cursor="hand2",font=("Calibri", 17, "bold"), bg="black", fg="orange")
        b1.place(x=720, y=375, width=200, height=40)

        #help icon
        img4 = Image.open(r"images\Tier-1-vs.-Tier-2-Help-Desk-Support.jpg")
        img4 = img4.resize((240, 200), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1_1 = Button(bg_img, image=self.photoimg4,command=self.help_data,cursor="hand2")
        b1_1.place(x=990, y=175, width=200, height=200)

        b1 = Button(bg_img,text= "Help Desk",command=self.help_data,cursor="hand2",font=("Calibri", 17, "bold"), bg="black", fg="orange")
        b1.place(x=990, y=375, width=200, height=40)

        #train data icon
        img5 = Image.open(r"images\data-scientist_woman.jpg")
        img5 = img5.resize((230, 200), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1_1 = Button(bg_img, image=self.photoimg5,command=self.train_data,cursor="hand2")
        b1_1.place(x=180, y=425, width=200, height=200)

        b1 = Button(bg_img,text= "Train Data",cursor="hand2",command=self.train_data,font=("Calibri", 17, "bold"), bg="black", fg="orange")
        b1.place(x=180, y=625, width=200, height=40)

        #photos icon
        img6 = Image.open(r"images\05VXLlOuCyvq8fQnl6W3xsc-39..v1638905563.jpg")
        img6 = img6.resize((240, 200), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1_1 = Button(bg_img, image=self.photoimg6,cursor="hand2",command=self.open_img)
        b1_1.place(x=450, y=425, width=200, height=200)

        b1 = Button(bg_img,text= "Photos",cursor="hand2",command=self.open_img,font=("Calibri", 17, "bold"), bg="black", fg="orange")
        b1.place(x=450, y=625, width=200, height=40)

        #developer icon
        img7 = Image.open(r"images\software-developer-6521720_1280.jpg")
        img7 = img7.resize((230, 200), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1_1 = Button(bg_img, image=self.photoimg7,command=self.developer_data,cursor="hand2")
        b1_1.place(x=720, y=425, width=200, height=200)

        b1 = Button(bg_img,text= "Developer",cursor="hand2",command=self.developer_data,font=("Calibri", 17, "bold"), bg="black", fg="orange")
        b1.place(x=720, y=625, width=200, height=40)

        #exit icon
        img8 = Image.open(r"C:\Users\VaishnaviKainthola\Desktop\Project python\images\360_F_561961089_9wreE9D0vZYxZk5nmSDEu3iwi8TU8uIo.jpg")
        img8 = img8.resize((200, 200), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1_1 = Button(bg_img, image=self.photoimg8,command=self.iExit,cursor="hand2")
        b1_1.place(x=990, y=425, width=200, height=200)

        b1 = Button(bg_img,text= "Exit",command=self.iExit,cursor="hand2",font=("Calibri", 17, "bold"), bg="black", fg="orange")
        b1.place(x=990, y=625, width=200, height=40)

    def open_img(self):
        os.startfile("image_data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit?",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return

        #=================================Function Buttons====================================

    def student_details(self):
        self.new_window= Toplevel(self.root)
        self.app= Student(self.new_window)

    def train_data(self):
        self.new_window= Toplevel(self.root)
        self.app= Train(self.new_window)

    def face_data(self):
        self.new_window= Toplevel(self.root)
        self.app= Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window= Toplevel(self.root)
        self.app= Attendance(self.new_window)

    def developer_data(self):
        self.new_window= Toplevel(self.root)
        self.app= Developer(self.new_window)

    def help_data(self):
        self.new_window= Toplevel(self.root)
        self.app= Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition_system(root)
    root.mainloop()
