from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x768+0+0")
        self.root.title("Student Details")

        #========================================variables==============================================

        self.var_ID=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_sem=StringVar()
        self.var_sec=StringVar()
        self.var_roll=StringVar()
        self.var_year=StringVar()
        self.var_DOB=StringVar()
        self.var_gender=StringVar()
        self.var_father=StringVar()
        self.var_mother=StringVar()
        self.var_contact=StringVar()
        self.var_CC=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_photo=StringVar()

        img = Image.open(r"C:\Users\VaishnaviKainthola\Desktop\Project python\images\college-building-academic-building-university-in-traditional-english-style-with-trees-and-a-green-lawn-and-playground-illustration-on-white-background-free-vector.jpg")
        img = img.resize((1360,768),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1360, height=768)

        title_lbl = Label(root, text="Student Management System", font=("Comic Sans MS", 20, "bold"), bg="lightblue", fg="black")
        title_lbl.place(x=0, y=120, width=1360, height=40)

        #first image
        img1 = Image.open(r"C:\Users\VaishnaviKainthola\Desktop\Project python\images\la-persona-obtiene-conocimiento-de-ilustración-vectorial-del-libro-educación-estudio-carácter-grupo-mujeres-hombres-leídos-194374358.jpg")
        img1 = img1.resize((455,120),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=455, height=120)

        #second image
        img2 = Image.open(r"C:\Users\VaishnaviKainthola\Desktop\Project python\images\attend.jpg")
        img2 = img2.resize((455,120),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=450, y=0, width=455, height=120)

        #third image
        img3 = Image.open(r"C:\Users\VaishnaviKainthola\Desktop\Project python\images\123180494-young-people-learn-and-gain-knowledge-flat-cartoon-design-of-students-learn-on-books-for-posters.jpg")
        img3 = img3.resize((457,120),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=900, y=0, width=457, height=120)

        #main frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=160,width=1345,height=530)

        #Left label frame
        Left_frame= LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=3,y=1,width=660,height=525)

        img_left = Image.open(r"C:\Users\VaishnaviKainthola\Desktop\Project python\images\stock-vector-stationery-for-school-and-office-vector-cartoon-icons-of-education-supplies-notebooks-pen-2104758662.jpg")
        img_left = img_left.resize((650,180),Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=3, y=0, width=650, height=67)

        #current course
        current_course= LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course.place(x=3,y=65,width=650,height=100)

        #Department
        dep_label= Label(current_course,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=2,sticky=W)

        dep_combo= ttk.Combobox(current_course,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=19,state="readonly")
        dep_combo["values"]=("Select Department","Bachelor of Technology","Information Technology","Agriculture","MBA","BBA","BCA","Design","Law","Management")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        #Course
        course_label= Label(current_course,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=2,sticky=W)

        course_combo= ttk.Combobox(current_course,textvariable=self.var_course,font=("times new roman",12,"bold"),width=19,state="readonly")
        course_combo["values"]=("Select Course","Computer Science","Electrical","Electronics","Mechanical","Civil","Chemical","Aerospace","Biotechnology")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=5,sticky=W)        

        #Year
        Year_label= Label(current_course,text="Year",font=("times new roman",12,"bold"),bg="white")
        Year_label.grid(row=1,column=0,padx=2,sticky=W)

        Year_combo= ttk.Combobox(current_course,textvariable=self.var_year,font=("times new roman",12,"bold"),width=19,state="readonly")
        Year_combo["values"]=("Select Year","2024","2023","2022","2021","2020","2019","2018","2017","2016","2015","2014","2013")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)        

        #Semester
        Sem_label= Label(current_course,text="Semester",font=("times new roman",12,"bold"),bg="white")
        Sem_label.grid(row=1,column=2,padx=2,sticky=W)

        Sem_combo= ttk.Combobox(current_course,textvariable=self.var_sem,font=("times new roman",12,"bold"),width=19,state="readonly")
        Sem_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        Sem_combo.current(0)
        Sem_combo.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        #Class Student information
        student_info= LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        student_info.place(x=3,y=164,width=650,height=336)

        #student id
        Studentid_label= Label(student_info,text="Student ID",font=("times new roman",12,"bold"),bg="white")
        Studentid_label.grid(row=0,column=0,padx=2,pady=5,sticky=W)

        Studentid_entry=ttk.Entry(student_info,textvariable=self.var_ID,width=20,font=("times new roman",12,"bold"))
        Studentid_entry.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        #student name
        Studentname_label= Label(student_info,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        Studentname_label.grid(row=0,column=2,padx=2,pady=5,sticky=W)

        Studentname_entry=ttk.Entry(student_info,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        Studentname_entry.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        #DOB
        dateofbirth_label= Label(student_info,text="Date of Birth",font=("times new roman",12,"bold"),bg="white")
        dateofbirth_label.grid(row=1,column=0,padx=2,pady=5,sticky=W)

        dateofbirth_entry=ttk.Entry(student_info,textvariable=self.var_DOB,width=20,font=("times new roman",12,"bold"))
        dateofbirth_entry.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        #gender
        gender_label= Label(student_info,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=1,column=2,padx=2,pady=5,sticky=W)

        gender_combo= ttk.Combobox(student_info,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=3,pady=8,sticky=W) 

        #Father's name
        Fathername_label= Label(student_info,text="Father's name",font=("times new roman",12,"bold"),bg="white")
        Fathername_label.grid(row=2,column=0,padx=2,pady=5,sticky=W)

        Fathername_entry=ttk.Entry(student_info,textvariable=self.var_father,width=20,font=("times new roman",12,"bold"))
        Fathername_entry.grid(row=2,column=1,padx=2,pady=5,sticky=W)

        #Mother's name
        Mothername_label= Label(student_info,text="Mother's name",font=("times new roman",12,"bold"),bg="white")
        Mothername_label.grid(row=2,column=2,padx=2,pady=5,sticky=W)

        Mothername_entry=ttk.Entry(student_info,textvariable=self.var_mother,width=20,font=("times new roman",12,"bold"))
        Mothername_entry.grid(row=2,column=3,padx=2,pady=5,sticky=W)

        #Section
        Section_label= Label(student_info,text="Section",font=("times new roman",12,"bold"),bg="white")
        Section_label.grid(row=3,column=0,padx=2,pady=5,sticky=W)

        sec_combo= ttk.Combobox(student_info,textvariable=self.var_sec,font=("times new roman",12,"bold"),width=18,state="readonly")
        sec_combo["values"]=("Select Section","A","B","C","D","E","F","G")
        sec_combo.current(0)
        sec_combo.grid(row=3,column=1,padx=3,pady=8,sticky=W)

        #RollNo
        RollNo_label= Label(student_info,text="RollNo.",font=("times new roman",12,"bold"),bg="white")
        RollNo_label.grid(row=3,column=2,padx=2,pady=5,sticky=W)

        RollNo_entry=ttk.Entry(student_info,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        RollNo_entry.grid(row=3,column=3,padx=2,pady=5,sticky=W)

        #ContactNo
        ContactNo_label= Label(student_info,text="ContactNo.",font=("times new roman",12,"bold"),bg="white")
        ContactNo_label.grid(row=4,column=0,padx=2,pady=5,sticky=W)

        ContactNo_entry=ttk.Entry(student_info,textvariable=self.var_contact,width=20,font=("times new roman",12,"bold"))
        ContactNo_entry.grid(row=4,column=1,padx=2,pady=5,sticky=W)

        #ClassCordinator
        ClassCordinator_label= Label(student_info,text="Class Cordinator",font=("times new roman",12,"bold"),bg="white")
        ClassCordinator_label.grid(row=4,column=2,padx=2,pady=5,sticky=W)

        ClassCordinator_entry=ttk.Entry(student_info,textvariable=self.var_CC,width=20,font=("times new roman",12,"bold"))
        ClassCordinator_entry.grid(row=4,column=3,padx=2,pady=5,sticky=W)

        #Email
        Email_label= Label(student_info,text="Email ID",font=("times new roman",12,"bold"),bg="white")
        Email_label.grid(row=5,column=0,padx=2,pady=5,sticky=W)

        Email_entry=ttk.Entry(student_info,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        Email_entry.grid(row=5,column=1,padx=2,pady=5,sticky=W)

        #Address
        Address_label= Label(student_info,text="Address",font=("times new roman",12,"bold"),bg="white")
        Address_label.grid(row=5,column=2,padx=2,pady=5,sticky=W)

        Address_entry=ttk.Entry(student_info,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        Address_entry.grid(row=5,column=3,padx=2,pady=5,sticky=W)

        #radiobutton
        self.var_photo = StringVar()
        radiobutton1 = ttk.Radiobutton(student_info, variable=self.var_photo, text="Take Photo Sample", value="Yes")
        radiobutton1.grid(row=6, column=0)

        radiobutton2 = ttk.Radiobutton(student_info, variable=self.var_photo, text="No Photo Sample", value="No")
        radiobutton2.grid(row=6, column=1)

        #Buttons Frame
        button_frame= Frame(student_info,bd=2,bg="white",relief=RIDGE)
        button_frame.place(x=0,y=244,width=644,height=48)

        #save
        save_btn= Button(button_frame,command=self.add_data,text="Save",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        #update
        Update_btn= Button(button_frame,command=self.update_data,text="Update",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Update_btn.grid(row=0,column=1)

        #reset
        Reset_btn= Button(button_frame,command=self.reset_data,text="Reset",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=2)

        #delete
        Delete_btn= Button(button_frame,command=self.delete_data,text="Delete",width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Delete_btn.grid(row=0,column=3)

        #sample frame
        photo_frame= Frame(student_info,bd=2,bg="white",relief=RIDGE)
        photo_frame.place(x=0,y=277,width=644,height=35)

        photosample_btn= Button(photo_frame,command=self.generate_data,text="Take photo Sample",width=35,font=("times new roman",12,"bold"),bg="green",fg="white")
        photosample_btn.grid(row=1,column=0)

        Updatesample_btn= Button(photo_frame,text="Update photo Sample",width=35,font=("times new roman",12,"bold"),bg="green",fg="white")
        Updatesample_btn.grid(row=1,column=1)


        #Right label frame
        Right_frame= LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=665,y=1,width=672,height=525)

        img_right = Image.open(r"C:\Users\VaishnaviKainthola\Desktop\Project python\images\Productive-ways-of-using-a-WordPress-table-plugin.jpg")
        img_right = img_right.resize((670,160),Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=3, y=0, width=664, height=100)

        #+++++++++==================SEARCHING SYSTEM=========================+++++++++
        #+++++++++==================SEARCHING SYSTEM=========================+++++++++
        #+++++++++==================SEARCHING SYSTEM=========================+++++++++

        search_info= LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_info.place(x=3,y=100,width=664,height=60)        

        Search_label= Label(search_info,text="Search by",font=("times new roman",15,"bold"),bg="pink")
        Search_label.grid(row=0,column=0,sticky=W)

        search_combo= ttk.Combobox(search_info,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select","Student ID","Name","Roll No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        search_entry=ttk.Entry(search_info,width=19,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=2,pady=5,sticky=W)

        #search
        Search_btn= Button(search_info,text="Search",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=2)

        #showall
        Show_btn= Button(search_info,text="Show All",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Show_btn.grid(row=0,column=4,padx=2)

        table_info= Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_info.place(x=3,y=162,width=664,height=345)

        scroll_x= ttk.Scrollbar(table_info,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_info,orient=VERTICAL)

        self.student_table= ttk.Treeview(table_info,column=("ID","name","dep","course","sem","sec","roll","year","DOB","gender","father","mother","contact","CC","email","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID",text="Student Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("sec",text="Section")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("DOB",text="Date of Birth")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("father",text="Father's Name")
        self.student_table.heading("mother",text="Mother's Name")
        self.student_table.heading("contact",text="Contact No.")
        self.student_table.heading("CC",text="Class Cordinator")
        self.student_table.heading("email",text="Email Id")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="PhotoSample")

        self.student_table["show"]="headings"

        self.student_table.column("ID",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("sec",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("father",width=100)
        self.student_table.column("mother",width=100)
        self.student_table.column("contact",width=100)
        self.student_table.column("CC",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #================================function declaration===================================

    def add_data(self): 
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_ID=="":
            messagebox.showerror("Error!","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Faridabad8320",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                        self.var_ID.get(),
                                                                                                                        self.var_name.get(),
                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_sem.get(),
                                                                                                                        self.var_sec.get(),
                                                                                                                        self.var_roll.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_DOB.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_father.get(),
                                                                                                                        self.var_mother.get(),
                                                                                                                        self.var_contact.get(),
                                                                                                                        self.var_CC.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_photo.get()

                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details have been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #==============================fetching data from the database======================================

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Faridabad8320",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #==============================get cursor================================================

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_ID.set(data[0])
        self.var_name.set(data[1])
        self.var_dep.set(data[2])
        self.var_course.set(data[3])
        self.var_sem.set(data[4])
        self.var_sec.set(data[5])
        self.var_roll.set(data[6])
        self.var_year.set(data[7])
        self.var_DOB.set(data[8])
        self.var_gender.set(data[9])
        self.var_father.set(data[10])
        self.var_mother.set(data[11])
        self.var_contact.set(data[12])
        self.var_CC.set(data[13])
        self.var_email.set(data[14])
        self.var_address.set(data[15])
        self.var_photo.set(data[16])

#======================================update function============================================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_ID.get()=="":
            messagebox.showerror("Error!","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update the student details?",parent=self.root)
                if Update==1:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Faridabad8320",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set `Name`=%s,`Department`=%s,`Course`=%s,`Sem`=%s,`Sec`=%s,`Rollno.`=%s,`Year`=%s,`DOB`=%s,`Gender`=%s,`Father`=%s,`Mother`=%s,`Contact`=%s,`ClassCordinator`=%s,`Email`=%s,`Address`=%s,`PhotoSample`=%s where `studentID`=%s",(
                                                                                                                       self.var_name.get(),
                                                                                                                       self.var_dep.get(),
                                                                                                                       self.var_course.get(),
                                                                                                                       self.var_sem.get(),
                                                                                                                       self.var_sec.get(),
                                                                                                                       self.var_roll.get(),
                                                                                                                       self.var_year.get(),
                                                                                                                       self.var_DOB.get(),
                                                                                                                       self.var_gender.get(),
                                                                                                                       self.var_father.get(),
                                                                                                                       self.var_mother.get(),
                                                                                                                       self.var_contact.get(),
                                                                                                                       self.var_CC.get(),
                                                                                                                       self.var_email.get(),
                                                                                                                       self.var_address.get(),
                                                                                                                       self.var_photo.get(),

           self.var_ID.get()
                                                                            ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)  

#delete button operation==============================================================
    def delete_data(self):
        if self.var_ID.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete= messagebox.askyesno("Confirm Delete","Do you want to delete the Student Details record?",parent=self.root)
                if delete:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Faridabad8320",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where `studentID`=%s"
                    val=(self.var_ID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details deleted successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

#reset data function=========================================================================
    def reset_data(self):
        self.var_ID.set("")
        self.var_name.set("")
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_sem.set("Select Semester")
        self.var_sec.set("Select Section")
        self.var_roll.set("")
        self.var_year.set("Select Year")
        self.var_DOB.set("")
        self.var_gender.set("Select Gender")
        self.var_father.set("")
        self.var_mother.set("")
        self.var_contact.set("")
        self.var_CC.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_photo.set("")

#===========================generate data set and take photo samples==============================
#    ========================================================================================

    def generate_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_ID.get()=="":
            messagebox.showerror("Error!","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Faridabad8320", database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set `Name`=%s,`Department`=%s,`Course`=%s,`Sem`=%s,`Sec`=%s,  `Rollno.`=%s,`Year`=%s,`DOB`=%s,`Gender`=%s,`Father`=%s,`Mother`=%s,`Contact`=%s, `ClassCordinator`=%s,`Email`=%s,`Address`=%s,`PhotoSample`=%s where `studentID`=%s",(
                                                                                                                                self.var_name.get(),
                                                                                                                                self.var_dep.get(),
                                                                                                                                self.var_course.get(),
                                                                                                                                self.var_sem.get(),
                                                                                                                                self.var_sec.get(),
                                                                                                                                self.var_roll.get(),
                                                                                                                                self.var_year.get(),
                                                                                                                                self.var_DOB.get(),
                                                                                                                                self.var_gender.get(),
                                                                                                                                self.var_father.get(),
                                                                                                                                self.var_mother.get(),
                                                                                                                                self.var_contact.get(),
                                                                                                                                self.var_CC.get(),
                                                                                                                                self.var_email.get(),
                                                                                                                                self.var_address.get(),
                                                                                                                                self.var_photo.get(),

                           self.var_ID.get()==id+1
                                                                            ))   
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

        #=====================load predefined data on face frontals from opencv======================
                face_classifier= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                ##scaling factor,minimum neighbour##

                    for (x,y,w,h) in faces:
                        face_cropped= img[y:y+h,x:x+w]
                        return face_cropped
                
                cap= cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY) 
                        file_name_path="image_data/user."+str(id+1)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Data set generation completed successfully!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()