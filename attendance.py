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
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x768+0+0")
        self.root.title("Attendance Details")

        #========================variables====================
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()

        img = Image.open(r"images\GEHu-1abd6f9c.jpg")
        img = img.resize((1360,650),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1360, height=768)

        title_lbl = Label(self.root, text="ATTENDANCE DETAILS", font=("Calibri", 25, "bold"), bg="black", fg="orange")
        title_lbl.place(x=0, y=0, width=1360, height=40)

        img1_left= Image.open(r"images\GettyImages-1093523312.jpg")
        img1_left= img1_left.resize((700,700),Image.Resampling.LANCZOS)
        self.photoimg1_left = ImageTk.PhotoImage(img1_left)

        f_lbl = Label(self.root, image=self.photoimg1_left)
        f_lbl.place(x=0, y=40, width=680, height=150)

        img1_right= Image.open(r"images\shegstory_0.jpg")
        img1_right= img1_right.resize((700,600),Image.Resampling.LANCZOS)
        self.photoimg1_right = ImageTk.PhotoImage(img1_right)

        f_lbl = Label(self.root, image=self.photoimg1_right)
        f_lbl.place(x=680, y=40, width=700, height=150)

        #main frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=195,width=1345,height=492)

        #Left label frame
        Left_frame= LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=3,y=1,width=664,height=485)

        img_left = Image.open(r"images\uc-san-diego-washington-monthly.jpg")
        img_left = img_left.resize((650,280),Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=3, y=0, width=655, height=145)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=2,y=150,width=655,height=310)

        attendanceid_label= Label(left_inside_frame,text="Attendance ID:",font=("times new roman",12,"bold"),bg="white")
        attendanceid_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        attendanceid_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_id,font=("times new roman",12,"bold"))
        attendanceid_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        student_roll_label = Label(left_inside_frame,text="Roll.No:",font=("times new roman",12,"bold"),bg="white")
        student_roll_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_roll,font=("times new roman",12,"bold"))
        student_roll_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        student_name_label = Label(left_inside_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_name,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        dep_label = Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        dep_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_dep,font=("times new roman",12,"bold"))
        dep_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        date_label = Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(left_inside_frame,width=20,textvariable=self.var_date,font=("times new roman",12,"bold"))
        date_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        time_label = Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        time_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_time,font=("verdana",12,"bold"))
        time_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

        attendance_status= Label(left_inside_frame,text="Attendance Status:",font=("times new roman",12,"bold"),bg="white")
        attendance_status.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        attendance_status_combo= ttk.Combobox(left_inside_frame,font=("times new roman",12,"bold"),width=18,textvariable=self.var_attend,state="readonly")
        attendance_status_combo["values"]=("Select Status","Present","Absent","No Status")
        attendance_status_combo.current(0)
        attendance_status_combo.grid(row=4,column=1,padx=3,pady=8,sticky=W) 

        button_frame= Frame(Left_frame,bd=2,bg="white",relief=RIDGE)
        button_frame.place(x=4,y=370,width=651,height=36)

        #save
        icsv_btn= Button(button_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        icsv_btn.grid(row=0,column=0)
        
        #update
        ecsv_btn= Button(button_frame,text="Export csv", command=self.exportCsv,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        ecsv_btn.grid(row=0,column=1)

        #reset
        Reset_btn= Button(button_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=2)

        #delete
        Delete_btn= Button(button_frame,text="Delete",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Delete_btn.grid(row=0,column=3)

        #Right label frame
        Right_frame= LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=670,y=1,width=668,height=485)

        table_frame= Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=3,y=1,width=657,height=458)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL) 
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendanceReport = ttk.Treeview(table_frame,column=("ID","RollNo.","Name","Department","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("ID",text="Student ID")
        self.attendanceReport.heading("RollNo.",text="RollNo.")
        self.attendanceReport.heading("Name",text="Std-Name")
        self.attendanceReport.heading("Department",text="Department")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Attend",text="Attend-status")
        self.attendanceReport["show"]="headings"

        self.attendanceReport.column("ID",width=30)
        self.attendanceReport.column("RollNo.",width=30)
        self.attendanceReport.column("Name",width=30)
        self.attendanceReport.column("Department",width=30)
        self.attendanceReport.column("Time",width=30)
        self.attendanceReport.column("Date",width=30)
        self.attendanceReport.column("Attend",width=30)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor)

#+++++++++++++++++fetch data++++++++++++++++++++++++++++++
        
    def fetchData(self,rows):
        self.attendanceReport.delete(*self.attendanceReport.get_children())
        for i in rows:
            self.attendanceReport.insert("",END,values=i)
        
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"), ("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfull","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 

    def get_cursor(self,event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        rows = content["values"]

        self.var_id.set(rows[0]),
        self.var_roll.set(rows[1]),
        self.var_name.set(rows[2]),
        self.var_time.set(rows[3]),
        self.var_date.set(rows[4]),
        self.var_attend.set(rows[5])   

    def reset_data(self):
        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("Status")

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()