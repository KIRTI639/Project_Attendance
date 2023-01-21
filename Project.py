from datetime import date
from datetime import datetime
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter.ttk import Combobox
import sqlite3

win = Tk()
win.title("Daily Attendance - FWL")
win.geometry("1000x710")
win.resizable(0,0)

#Define Images...
bg = PhotoImage(file="Img_Updated.png")
morning = PhotoImage(file="Morning.png")
noon = PhotoImage(file="Noon.png")
evening = PhotoImage(file="Evening.png")


#Define Functions/Methods here...
class UIDesign:
    college_code = StringVar()
    college_name = StringVar()
    state = StringVar()
    city = StringVar()
    pincode = StringVar()
    password1 = StringVar()
    password2 = StringVar()
    collegeId = StringVar()

    id = StringVar()
    faculty_name = StringVar()
    branch = StringVar()
    sem = StringVar()
    l_no = StringVar()
    total = StringVar()
    subject = StringVar()
    date1 = StringVar()
    date2 = StringVar()
    month = StringVar()

    #Task Finished...
    def add_college_records(self):
        collegeID = self.college_id()
        db = sqlite3.connect("MyDatabase.db")
        cr = db.cursor()
        cr.execute("INSERT INTO College_Records(College_ID, Password, College_Code, College_Name, State, City, Pincode) VALUES('" + collegeID + "', '" + self.password1.get() + "', '" + self.college_code.get() + "', "
                            "'" + self.college_name.get().title() + "', '" + self.state.get().title() + "', "
                            "'" + self.city.get().title() +"', '" + self.pincode.get() + "')")
        db.commit()
        db.close()

    #Task Finished...
    def add_entry_data(self):
        collegeID = self.college_id()
        self.current_date = date.today()

        db = sqlite3.connect("MyDatabase.db")
        cr = db.cursor()
        cr.execute("INSERT INTO Attendance_Table(College_ID, Faculty_Name, Subject, Branch, Semester, Lecture, "
                   "Total_Students, Date)"
                   " VALUES('" + collegeID + "', '" + self.faculty_name.get() + "', '" + self.subject.get() + "', "
                            "'" + self.branch.get().title() + "', '" + self.sem.get().title() + "', '" + self.l_no.get().title() + "', "
                            "'" + self.total.get() + "', '"+str(self.current_date)+"')")
        db.commit()
        db.close()

    #Task Finished...
    def add_lab_data(self):
        collegeID = self.college_id()
        self.current_date = date.today()

        db = sqlite3.connect("MyDatabase.db")
        cr = db.cursor()
        cr.execute("INSERT INTO Lab_Table(College_ID, Faculty_Name, Lab_Name, Branch, Semester, "
                   "Total_Students, Date)"
                   " VALUES('" + collegeID + "', '" + self.faculty_name.get() + "', '" + self.subject.get() + "', "
                            "'" + self.branch.get().title() + "', '" + self.sem.get().title() + "',"
                            " '" + self.total.get() + "', '" + str(self.current_date) + "')")
        db.commit()
        db.close()

    # Task Finished...
    def reset(self):
        self.id.set('')
        self.faculty_name.set('')
        self.branch.set('')
        self.sem.set('')
        self.l_no.set('')
        self.total.set('')
        self.subject.set('')

    #Work is in progress...
    def get_attendance_data(self):
        f = Frame()
        f.place(x=0, y=0, width=1000, height=710)

        code = self.college_code
        name = self.college_name
        col_name = str(code) + ' - ' + str(name)
        label1 = Label(f, text="\n" + col_name + "\n", font=("Arial", 18, "bold"), fg="white", bg='darkred')
        label1.pack(fill=X)

        btn1 = Button(f, text="Back", font=('Helvetica', 12), width=7, bg='#cf2d30', fg='White',
                      command=self.view_attendance_page)
        btn1.place(x=30, y=100)
        btn2 = Button(f, text="Home", font=('Helvetica', 12), width=7, bg='#cf2d30', fg='White', command=self.home)
        btn2.place(x=150, y=100)
        btn3 = Button(f, text="Exit", font=('Helvetica', 12), width=7, bg='#cf2d30', fg='White',
                      command=self.custom_quit)
        btn3.place(x=270, y=100)

        Label(f, text='Faculty_Name', font=("Arial", 12, "bold"), fg="#cf2d30").place(x=50, y=140)
        Label(f, text='Subject', font=("Arial", 12, "bold"), fg="#cf2d30").place(x=230, y=140)
        Label(f, text='Branch', font=("Arial", 12, "bold"), fg="#cf2d30").place(x=410, y=140)
        Label(f, text='Semester', font=("Arial", 12, "bold"), fg="#cf2d30").place(x=590, y=140)
        Label(f, text='Total_Students', font=("Arial", 12, "bold"), fg="#cf2d30").place(x=770, y=140)

        count = 0
        db = sqlite3.connect("MyDatabase.db")
        cr = db.cursor()
        if self.month.get()!='' and self.faculty_name.get()!='' and self.date1.get()!=0:
            count += 1
            self.result = cr.execute("SELECT Faculty_Name, Subject, Branch, Semester, Total_Students FROM "
                                  "Attendance_Table "
                                "WHERE College_ID = '" + self.collegeId + "' AND Month = '"+self.month.get()+"' AND "
                                "Faculty_Name = '" +self.faculty_name.get()+ "' AND Date = '"+self.date1.get()+"'")
        elif self.month.get()!='' and self.faculty_name.get()!='':
            count += 1
            self.result = cr.execute("SELECT Faculty_Name, Subject, Branch, Semester, Total_Students FROM "
                                  "Attendance_Table "
                                "WHERE College_ID = '" + self.collegeId + "' AND Month = '"+self.month.get()+"' AND "
                                "Faculty_Name = '" +self.faculty_name.get()+ "' ")
        elif self.month.get()!='' and self.date1.get()!=0:
            count += 1
            self.result = cr.execute("SELECT Faculty_Name, Subject, Branch, Semester, Total_Students FROM "
                                  "Attendance_Table "
                                "WHERE College_ID = '" + self.collegeId + "' AND Month = '" + self.month.get() + "' AND "
                                "Date = '" + self.date1.get() + "' ")
        elif self.faculty_name.get()!=0 and self.date1.get()!=0:
            count += 1
            self.result = cr.execute("SELECT Faculty_Name, Subject, Branch, Semester, Total_Students FROM "
                                  "Attendance_Table "
                                "WHERE College_ID = '"+self.collegeId+ "' AND Faculty_Name = '"
                                +self.faculty_name.get()+"' AND Date = '"+self.date1.get()+"'")
        else:
            tkinter.messagebox.askokcancel("Warning", "Atleast two fields are required. Please enter valid input.")

        if count==1:
            #x, y = 300, 300
            for r in self.result:
                print(r[0])
                print(r[1])
                #Label(f, text=r[0]).place(x=x, y=y)
            print('Hello Peter...')
        db.commit()
        db.close()

    # Work is in progress...
    def get_lab_data(self):
        db = sqlite3.connect("MyDatabase.db")
        cr = db.cursor()
        if self.month.get() != '' and self.faculty_name.get() != '' and self.branch.get() != 0:
            result = cr.execute("SELECT Faculty_Name, Lab_Name, Branch, Semester, Total_Students FROM Lab_Table "
                                "WHERE College_ID = '" + self.collegeId.get() + "' AND Month = '" + self.month.get() + "' AND "
                                "Faculty_Name = '" + self.faculty_name.get() + "' AND Branch = '" + self.branch.get() + "'")
        elif self.month.get() != '' and self.faculty_name.get() != '':
            result = cr.execute("SELECT Faculty_Name, Lab_Name, Branch, Semester, Total_Students FROM Lab_Table "
                                "WHERE College_ID = '" + self.collegeId.get() + "' AND Month = '" + self.month.get() + "' AND "
                                "Faculty_Name = '" + self.faculty_name.get() + "' ")
        elif self.month.get() != '' and self.branch.get() != 0:
            result = cr.execute("SELECT Faculty_Name, Lab_Name, Branch, Semester, Total_Students FROM Lab_Table "
                                "WHERE College_ID = '" + self.collegeId.get() + "' AND Month = '" + self.month.get() + "' AND "
                                "Branch = '" + self.branch.get() + "' ")
        elif self.faculty_name.get() != 0 and self.branch.get()!=0:
            result = cr.execute("SELECT Faculty_Name, Lab_Name, Branch, Semester, Total_Students FROM Lab_Table "
                                "WHERE College_ID = '" + self.collegeId.get() + "' AND Faculty_Name = '"
                                + self.faculty_name.get() + "' AND Branch = '"+self.branch.get()+"'")
        else:
            tkinter.messagebox.askokcancel("Warning", "Atleast two fields are required. Please enter valid input.")

    #Task Finished...
    def view_lab_page(self):
        f1 = Frame()
        f1.place(x=0, y=0, width=1000, height=710)
        bg_label = Label(f1, image=bg)
        bg_label.place(x=0, y=0)

        code = self.college_code
        name = self.college_name
        col_name = code + ' - ' + name
        label1 = Label(f1, text="\n" + col_name + "\n", font=("Arial", 18, "bold"), fg="white", bg='darkred')
        label1.pack(fill=X)

        nav = Label(f1, text="View > Lab Records", font=("Arial", 14, "underline"), fg='darkred')
        nav.place(x=20, y=110)

        # LabelFrames...
        frame1 = LabelFrame(f1, font=('Helvetica', 12))
        frame1.pack(pady=100)
        my_message = Message(frame1, text="Select Month", font=('Helvetica', 14), aspect=600)
        my_message.pack(pady=10)
        e2 = Combobox(frame1, font=("Arial", 14), values=['January', 'February', 'March', 'April', 'May', 'June',
                                                          'July', 'August', 'September', 'October', 'November',
                                                          'December'], justify="left", textvariable=self.month)
        #e2.place(x=300, y=270, width=280, height=30)
        e2.pack(pady=0)
        # btn2 = Button(frame1, text="Get Data", font=('Helvetica', 12), width=10, bg='#cf2d30', fg='White',
        #               command=self.get_data_by_month)
        # btn2.pack(padx=10, pady=10)

        my_message = Message(frame1, text="Enter Faculty Name", font=('Helvetica', 14), aspect=600,
                             justify=CENTER)
        my_message.pack(pady=10)
        e1 = Combobox(frame1, font=("Arial", 14), values=['Ankit Sir', 'Vivek Sir', 'Neha Mam', 'Nidhi Bisnoi', 'Ila Mam'
            , 'Shubham Sir', 'Lalit Rathi', 'Mohit Sir', 'Shueb Sir'], textvariable=self.faculty_name, justify="left")
        #e1.place(x=300, y=170, width=280, height=30)
        e1.pack(pady=0)
        my_message = Message(frame1, text="Enter Date(YYYY-MM-DD)", font=('Helvetica', 14), aspect=600,
                             justify=LEFT)
        my_message.pack(pady=10, padx=100)
        e5 = Entry(frame1, font=("Arial", 14), width=22, textvariable=self.date1)
        #e5.place(x=300, y=370)
        e5.pack(pady=0)

        btn2 = Button(frame1, text="Get Data", font=('Helvetica', 12), width=10, bg='#cf2d30', fg='White', command=self.get_lab_data)
        btn2.pack(padx=10, pady=20)

        exit = Button(win, text="Back", font=("Arial", 15, 'bold'), fg="white", bg="blue", command=self.view)
        exit.place(x=280, y=570)
        label1 = Label(f1, text="POWERED By ~ FunWithLearning.", font=("Arial", 10, "bold"), fg="white", bg="darkred")
        label1.pack(side=BOTTOM, fill=X)

    #Done...
    def view_attendance_page(self):
        f1 = Frame()
        f1.place(x=0, y=0, width=1000, height=710)
        bg_label = Label(f1, image=bg)
        bg_label.place(x=0, y=0)

        code = self.college_code
        name = self.college_name
        col_name = code + ' - ' + name
        label1 = Label(f1, text="\n" + col_name + "\n", font=("Arial", 18, "bold"), fg="white", bg='darkred')
        label1.pack(fill=X)

        nav = Label(f1, text="View > Attendance Record", font=("Arial", 14, "underline"), fg='darkred')
        nav.place(x=20, y=110)

        # LabelFrames...
        frame1 = LabelFrame(f1, font=('Helvetica', 12))
        frame1.pack(pady=100)
        my_message = Message(frame1, text="Select Month", font=('Helvetica', 14), aspect=600)
        my_message.pack(pady=10)
        e2 = Combobox(frame1, font=("Arial", 14), values=['January', 'February', 'March', 'April', 'May', 'June',
                                                          'July', 'August', 'September', 'October', 'November',
                                                          'December'], justify="left", textvariable=self.month)
        #e2.place(x=300, y=270, width=280, height=30)
        e2.pack(pady=0)
        # btn2 = Button(frame1, text="Get Data", font=('Helvetica', 12), width=10, bg='#cf2d30', fg='White',
        #               command=self.get_data_by_month)
        # btn2.pack(padx=10, pady=10)

        my_message = Message(frame1, text="Enter Faculty Name", font=('Helvetica', 14), aspect=600,
                             justify=CENTER)
        my_message.pack(pady=10)
        e1 = Combobox(frame1, font=("Arial", 14), values=['Mr. Ankit Rajan', 'Mr. Vivek Kumar', 'Ms. Neha',
                                                       'Ms. Nidhi Bisnoi','Ms. Ila', 'Mr. Shubham', 'Mr. Lalit Rathi',
                                                       'Mr. Mohit Kumar', 'Mr. Shueb Ali'], textvariable=self.faculty_name, justify="left")
        #e1.place(x=300, y=170, width=280, height=30)
        e1.pack(pady=0)
        my_message = Message(frame1, text="Enter Date(YYYY-MM-DD)", font=('Helvetica', 14), aspect=600,
                             justify=LEFT)
        my_message.pack(pady=10, padx=100)
        e5 = Entry(frame1, font=("Arial", 14), width=22, textvariable=self.date1)
        #e5.place(x=300, y=370)
        e5.pack(pady=0)

        btn2 = Button(frame1, text="Get Data", font=('Helvetica', 12), width=10, bg='#cf2d30', fg='White',
                      command=self.get_attendance_data)
        btn2.pack(padx=10, pady=20)

        exit = Button(win, text="Back", font=("Arial", 15, 'bold'), fg="white", bg="blue", command=self.view)
        exit.place(x=280, y=570)
        label1 = Label(f1, text="POWERED By ~ FunWithLearning.", font=("Arial", 10, "bold"), fg="white",
                       bg="darkred")
        label1.pack(side=BOTTOM, fill=X)

    # Almost Done...
    def view(self):
        f1 = Frame()
        f1.place(x=0, y=0, width=1000, height=710)
        bg_label = Label(f1, image=bg)
        bg_label.place(x=0, y=0)

        code = self.college_code
        name = self.college_name
        col_name = code + ' - ' + name
        label1 = Label(f1, text="\n" + col_name + "\n", font=("Arial", 18, "bold"), fg="white", bg='darkred')
        label1.pack(fill=X)
        # LabelFrames...
        frame1 = LabelFrame(f1, font=('Helvetica', 12))
        frame1.pack(pady=100)
        my_message = Message(frame1, text="View Attendance Records", font=('Helvetica', 14), aspect=600, justify=CENTER)
        my_message.pack(pady=10, padx=100)

        btn2 = Button(frame1, text="Next", font=('Helvetica', 15), width=10, bg='#cf2d30', fg='White',
                      command=self.view_attendance_page)
        btn2.pack(padx=10, pady=0)

        my_message = Message(frame1, text="OR\nView Lab Records", font=('Helvetica', 14), aspect=600, justify=CENTER)
        my_message.pack(pady=10, padx=100)

        btn2 = Button(frame1, text="Next", font=('Helvetica', 15), width=10, bg='#cf2d30', fg='White', command=self.view_lab_page)
        btn2.pack(padx=10, pady=15)

        exit = Button(win, text="Back", font=("Arial", 15, 'bold'), fg="white", bg="blue", command=self.home)
        exit.place(x=280, y=510)
        label1 = Label(f1, text="POWERED By ~ FunWithLearning.", font=("Arial", 10, "bold"), fg="white", bg="darkred")
        label1.pack(side=BOTTOM, fill=X)

    # Task Finished...
    def submit(self):
        #self.add_entry_data()
        self.reset()
        code = self.college_code
        name = self.college_name
        col_name = code + ' - ' + name

        f9 = Frame()
        f9.place(x=0, y=0, width=1000, height=710)
        label1 = Label(f9, text="\n" + col_name + "\n", font=("Arial", 18, "bold"), fg="white", bg='darkred')
        label1.pack(fill=X)

        thank = Label(f9, text="Thank You!", fg="green", font=("Arial 18 bold"))
        thank.place(x=100, y=200)
        responce = "Your responce has been stored successfully."
        res = Label(f9, text=responce, fg="green", font=("Arial 12 bold"))
        res.place(x=100, y=240)

        b0 = Button(f9, text="Re-Entry", font=("Arial", 15, 'bold'), borderwidth=0, fg="white", bg="darkred", command=self.entry_page)
        b0.place(x=100, y=500, width=120, height=40)
        b1 = Button(f9, text="Home", font=("Arial", 15, 'bold'), fg="white", bg="darkred", command=self.home)
        b1.place(x=300, y=500, width=100, height=40)
        b2 = Button(f9, text="View Data", font=("Arial", 15, 'bold'), bg="darkred", fg='white', command=self.view)
        b2.place(x=450, y=500, width=120, height=40)
        label1 = Label(f9, text="POWERED By ~ FunWithLearning.", font=("Arial", 10, "bold"), fg="white", bg="darkred")
        label1.pack(side=BOTTOM, fill=X)

    # Task Finished...
    def sorry(self):
        code = self.college_code
        name = self.college_name
        col_name = code + ' - ' + name

        f8 = Frame()
        f8.place(x=0, y=0, width=1000, height=710)
        label1 = Label(f8, text="\n" + col_name + "\n", font=("Arial", 18, "bold"), fg="white", bg='darkred')
        label1.pack(fill=X)

        thank = Label(f8, text="We're Sorry!", fg="#99991f", font=("Arial 18 bold"))
        thank.place(x=100, y=200)
        responce = "Your data is not valid for the database."
        res = Label(f8, text=responce, fg="#99991f", font=("Arial 12 bold"))
        res.place(x=100, y=240)

        b0 = Button(f8, text="Re-Entry", font=("Arial", 15, 'bold'), fg="white", bg="darkred", command=self.entry_page)
        b0.place(x=100, y=500, width=120, height=40)
        b1 = Button(f8, text="Home", font=("Arial", 15, 'bold'), fg="white", bg="darkred", command=self.home)
        b1.place(x=300, y=500, width=100, height=40)
        b2 = Button(f8, text="View Data", font=("Arial", 15, 'bold'), bg="darkred", fg='white', command=self.view)
        b2.place(x=450, y=500, width=120, height=40)
        label1 = Label(f8, text="Copyrights - 1999-2021\nAll Rights Reserved.", font=("Arial", 10, "bold"), fg="white", bg="darkred")
        label1.pack(side=BOTTOM, fill=X)

    #Task Finished...
    def check_valid(self):
        if self.faculty_name.get() != '' and self.subject.get()!='' and self.branch.get() != '' and self.sem.get() !=''\
                and self.l_no.get() != '' and self.total.get() != '':
            #self.submit()
            if not(self.l_no.get().isdigit()) or int(self.l_no.get()) > 8:
                tkinter.messagebox.askokcancel("Warning", "This field requires digits only and must be less than or "
                                                          "equal to 8.")
            if not(self.total.get().isdigit()):
                tkinter.messagebox.askokcancel("Warning", "This field requires digits only.")
            if self.data_is_attend:
                self.add_entry_data()
                self.submit()
            if self.data_is_lab:
                self.add_lab_data()
                self.submit()
        else:
            self.sorry()

    # Task Finished...
    def lab_record(self):
        #self.reset()
        self.data_is_attend = False
        self.data_is_lab = True

        code = self.college_code
        name = self.college_name
        col_name = code + ' - ' + name

        f7 = Frame()
        f7.place(x=0, y=0, width=1000, height=710)
        label1 = Label(f7, text="\n" + col_name.title() + "\n", font=("Arial", 18, "bold"), fg="white", bg='darkred')
        label1.pack(fill=X)
        #
        # l0 = Label(f7, text="Faculty ID : ", font=("Arial", 14))
        # l0.place(x=100, y=120)
        # e0 = Entry(f7, font=("Arial", 14), width=25, textvariable=self.id)
        # e0.place(x=300, y=120)

        l1 = Label(f7, text="Faculty Name : ", font=("Arial", 14))
        l1.place(x=100, y=170)
        e1 = Combobox(win, font=("Arial", 14), values=['Ankit Sir', 'Vivek Sir', 'Neha Mam', 'Nidhi Bisnoi', 'Ila Mam'
                          , 'Shubham Sir', 'Lalit Rathi', 'Mohit Sir', 'Shueb Sir'], textvariable=self.faculty_name)
        e1.place(x=300, y=170, width=280, height=30)
        l = Label(f7, text="Lab Name : ", font=("Arial", 14))
        l.place(x=100, y=220)
        e = Combobox(win, font=("Arial", 14), values=['DBMS Lab', 'DAA Lab', 'CD Lab', 'HCI Lab', 'Web Designing Lab',
                                                      'Operating System Lab', 'DSTL Lab'], textvariable=self.subject)
        e.place(x=300, y=220, width=280, height=30)

        l2 = Label(f7, text="Branch : ", font=("Arial", 14))
        l2.place(x=100, y=270)
        e2 = Combobox(win, font=("Arial", 14), values=['CSE', 'CE', 'ME', 'ECE',], textvariable=self.branch)
        e2.place(x=300, y=270, width=280, height=30)

        l3 = Label(f7, text="Semester : ", font=("Arial", 14))
        l3.place(x=100, y=320)
        e3 = Combobox(win, font=("Arial", 14), values=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th'], textvariable=self.sem)
        e3.place(x=300, y=320, width=280, height=30)

        l5 = Label(f7, text="Lecture No. : ", font=("Arial", 14))
        l5.place(x=100, y=370)
        e5 = Entry(f7, font=("Arial", 14), width=25, textvariable=self.l_no)
        e5.place(x=300, y=370)

        l6 = Label(f7, text="Total Students : ", font=("Arial", 14))
        l6.place(x=100, y=420)
        e6 = Entry(f7, font=("Arial", 14), width=25, textvariable=self.total)
        e6.place(x=300, y=420)

        b0 = Button(f7, text="Go Back", font=("Arial", 15, 'bold'), borderwidth=1, command=self.home, fg="white", bg="darkred")
        b0.place(x=100, y=550, width=120, height=40)
        b1 = Button(f7, text="Submit", font=("Arial", 15, 'bold'), fg="white", bg="darkred", command=self.check_valid)
        b1.place(x=300, y=550, width=100, height=40)
        b2 = Button(f7, text="Reset", font=("Arial", 15, 'bold'), bg="darkred", fg='white', command=self.reset)
        b2.place(x=450, y=550, width=120, height=40)
        label1 = Label(f7, text="POWERED By ~ FunWithLearning", font=("Arial", 10, "bold"), fg="white", bg="darkred")
        label1.pack(side=BOTTOM, fill=X)

    # Task Finished...
    def entry_page(self):
        #self.reset()
        self.data_is_attend = True
        self.data_is_lab = False

        code = self.college_code
        name = self.college_name
        col_name = code + ' - ' + name

        f7 = Frame()
        f7.place(x=0, y=0, width=1000, height=710)
        label1 = Label(f7, text="\n" + col_name.title() + "\n", font=("Arial", 18, "bold"), fg="white", bg='darkred')
        label1.pack(fill=X)

        # l0 = Label(f7, text="Faculty ID : ", font=("Arial", 14))
        # l0.place(x=100, y=120)
        # e0 = Entry(f7, font=("Arial", 14), width=25, textvariable=self.id)
        # e0.place(x=300, y=120)

        l1 = Label(f7, text="Faculty Name : ", font=("Arial", 14))
        l1.place(x=100, y=170)
        e1 = Combobox(win, font=("Arial", 14), values=['Mr. Ankit Rajan', 'Mr. Vivek Kumar', 'Ms. Neha',
                                                       'Ms. Nidhi Bisnoi','Ms. Ila', 'Mr. Shubham', 'Mr. Lalit Rathi',
                                                       'Mr. Mohit Kumar', 'Mr. Shueb Ali'],
                      textvariable=self.faculty_name)
        e1.place(x=300, y=170, width=280, height=30)
        l = Label(f7, text="Subject : ", font=("Arial", 14))
        l.place(x=100, y=220)
        e = Combobox(win, font=("Arial", 14), values=['DBMS', 'DAA', 'CD', 'HCI', 'WD', 'OS','Math I', 'Math II',
                                                      'Math IV', 'DSTL', 'PPS', 'Chemistry', 'Physics',
                                                      'Electronics', 'DS', 'Java', 'Python', 'WT', 'UHBNEC', 'ITCS'],
                     textvariable=self.subject)
        e.place(x=300, y=220, width=280, height=30)

        l2 = Label(f7, text="Branch : ", font=("Arial", 14))
        l2.place(x=100, y=270)
        e2 = Combobox(win, font=("Arial", 14), values=['CSE', 'ME', 'CE', 'EE', 'Bio-Tech'], textvariable=self.branch)
        e2.place(x=300, y=270, width=280, height=30)

        l3 = Label(f7, text="Semester : ", font=("Arial", 14))
        l3.place(x=100, y=320)
        e3 = Combobox(win, font=("Arial", 14), values=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th'],
                      textvariable=self.sem)
        e3.place(x=300, y=320, width=280, height=30)

        l5 = Label(f7, text="Lecture No. : ", font=("Arial", 14))
        l5.place(x=100, y=370)
        e5 = Entry(f7, font=("Arial", 14), width=25, textvariable=self.l_no)
        e5.place(x=300, y=370)

        l6 = Label(f7, text="Total Students : ", font=("Arial", 14))
        l6.place(x=100, y=420)
        e6 = Entry(f7, font=("Arial", 14), width=25, textvariable=self.total)
        e6.place(x=300, y=420)

        b0 = Button(f7, text="Go Back", font=("Arial", 15, 'bold'), borderwidth=1, command=self.home, fg="white", bg="darkred")
        b0.place(x=100, y=550, width=120, height=40)
        b1 = Button(f7, text="Submit", font=("Arial", 15, 'bold'), fg="white", bg="darkred", command=self.check_valid)
        b1.place(x=300, y=550, width=100, height=40)
        b2 = Button(f7, text="Reset", font=("Arial", 15, 'bold'), bg="darkred", fg='white', command=self.reset)
        b2.place(x=450, y=550, width=120, height=40)
        label1 = Label(f7, text="POWERED By ~ FunWithLearning", font=("Arial", 10, "bold"), fg="white", bg="darkred")
        label1.pack(side=BOTTOM, fill=X)

    def custom_logout(self):
        answer = tkinter.messagebox.askokcancel("Fun_With_Learning", "Are you sure you want to Log-Out ?")
        if answer:
            self.sign_in()

    # Task Finished...
    def home(self):
        code = self.college_code
        name = self.college_name
        col_name = code + ' - ' + name

        f6 = Frame()
        f6.place(x=0, y=0, width=1000, height=710)
        label1 = Label(f6, text="\n" + col_name.title() + "\n", font=("Arial", 18, "bold"), fg="white", bg='darkred')
        label1.pack(fill=X)
        enter_button = Button(f6, text="Attendance", font=("Arial", 15, 'bold'), fg="white", bg='darkred',
                              command=self.entry_page)
        enter_button.place(x=250, y=200, width=140, height=40)
        view_button = Button(f6, text="View Data", font=("Arial", 15, 'bold'), fg="white", bg='darkred', command=self.view)
        view_button.place(x=250, y=300, width=140, height=40)
        exit_button = Button(f6, text="Exit", font=("Arial", 15, 'bold'), command=self.custom_quit, bg='darkred', fg="white")
        exit_button.place(x=250, y=400, width=140, height=40)
        privacy_button = Button(f6, text="Lab Records", font=("Arial", 15, 'bold'), fg="white", bg='darkred', command=self.lab_record)
        privacy_button.place(x=550, y=200, width=140, height=40)
        contact_button = Button(f6, text="Themes", font=("Arial", 15, 'bold'), fg="white", bg='darkred')
        contact_button.place(x=550, y=300, width=140, height=40)
        links_button = Button(f6, text="Sign Out", font=("Arial", 15, 'bold'), fg="white", bg='darkred', command=self.custom_logout)
        links_button.place(x=550, y=400, width=140, height=40)
        label1 = Label(f6, text="POWERED By ~ FunWithLearning", font=("Arial", 10, "bold"), fg="white", bg='darkred')
        label1.pack(side=BOTTOM, fill=X)

    def dashboard(self):
        code = self.college_code
        name = self.college_name
        col_name = code+' - '+name

        f5 = Frame()
        f5.place(x=0, y=0, width=1000, height=710)
        label1 = Label(f5, text="\n" + col_name.title() + "\n", font=("Arial", 18, "bold"), fg="white", bg='darkred')
        label1.pack(fill=X)
        # Get System's Date and Time...
        now = datetime.now()
        hours = now.strftime("%H")
        if int(hours) < 12:
            greet = "Good Morning \n😊😊😊"
            label2 = Label(f5, text=greet, font=("Arial", 20, "bold"), fg="green")
            label2.place(x=380, y=120)
            bg_label = Label(f5, image=morning, width=500, height=400, justify="center")
            bg_label.place(x=250, y=190)
        elif int(hours) >= 12 and int(hours) < 16:
            greet = "Good Afternoon \n😊😊😊"
            label2 = Label(f5, text=greet, font=("Arial", 20, "bold"), fg="green")
            label2.place(x=380, y=120)
            bg_label = Label(f5, image=noon, width=500, height=400, justify="center")
            bg_label.place(x=250, y=190)
        elif int(hours) >= 16:
            greet = "Good Evening \n😊😊😊"
            label2 = Label(f5, text=greet, font=("Arial", 20, "bold"), fg="green")
            label2.place(x=380, y=120)
            bg_label = Label(f5, image=evening, width=500, height=400, justify="center", border=10)
            bg_label.place(x=250, y=190)

        btn1 = Button(f5, text='Sign-Out', font=('Helvetica', 14), bg='darkred', fg='White', width=8, command=self.custom_logout)
        btn1.place(x=380, y=560)
        btn2 = Button(f5, text='Next -->', font=('Helvetica', 14), bg='darkred', fg='White', width=8, command=self.home)
        btn2.place(x=520, y=560)
        label = Label(f5, text="POWERED By ~ FunWithLearning", font=("Arial", 10, "bold"), fg="white", bg='darkred')
        label.pack(side=BOTTOM, fill=X)

    # Task Finished...
    def reset_all(self):
        self.college_code.set('')
        self.college_name.set('')
        self.state.set('')
        self.city.set('')
        self.pincode.set('')
        self.password1.set('')
        self.password2.set('')

    # Task Finished...
    def reset_col_ID(self):
        self.collegeId.set('')
        self.password1.set('')

    # Task Finished...
    def check_signin_validity(self):
        if self.collegeId.get()!='' and self.password1.get()!='':
            db = sqlite3.connect("MyDatabase.db")
            cr = db.cursor()
            result = cr.execute("SELECT * FROM College_Records WHERE College_ID = "
                                "'" + self.collegeId.get() + "' AND Password = '" + self.password1.get() + "'")
            count = 0
            for r in result:
                count += 1
                self.collegeId = r[0]
                self.college_code = r[2]
                self.college_name = r[3]
            if count != 0:
                self.dashboard()
            else:
                tkinter.messagebox.askokcancel("Warning", "The information, you have filled, not found in Database.")
            db.commit()
            db.close()
        else:
            tkinter.messagebox.askokcancel("Warning", "All fields are required. Please fill all the fields")

    # Task Finished...
    def sign_in(self):
        self.reset_col_ID()
        f4 = Frame()
        f4.place(x=0, y=0, width=1000, height=710)
        bg_label = Label(f4, image=bg)
        bg_label.place(x=0, y=0)
        # LabelFrames...
        frame4 = LabelFrame(f4, text="Sign-In", font=('Helvetica', 12), width=600, height=350)
        frame4.place(x=185, y=170)
        # Labels
        label1 = Label(frame4, text='Enter College ID :', font=('Helvetica', 14))
        label1.place(x=50, y=80)
        label2 = Label(frame4, text='Enter Password :', font=('Helvetica', 14))
        label2.place(x=50, y=120)
        #Entry Boxes...
        entry1 = Entry(frame4, font=("Arial", 15), width=25, textvariable=self.collegeId)
        entry1.place(x=270, y=80)
        entry2 = Entry(frame4, font=("Arial", 15), width=25, textvariable=self.password1, show="*")
        entry2.place(x=270, y=120)
        #Buttons...
        btn1 = Button(frame4, text='Sign-in', font=('Helvetica', 14), bg='#cf2d30', fg='White', width=8,
                      command=self.check_signin_validity)
        btn1.place(x=150, y=220)
        btn2 = Button(frame4, text='Clear', font=('Helvetica', 14), bg='#cf2d30', fg='White', width=8, command=self.reset_col_ID)
        btn2.place(x=260, y=220)
        btn3 = Button(frame4, text='Go Back', font=('Helvetica', 14), bg='#cf2d30', fg='White', width=8, command=self.first_page)
        btn3.place(x=370, y=220)

    # Task Finished...
    def custom_quit(self):
        answer = tkinter.messagebox.askokcancel("Fun_With_Learning", "Are you sure you want to exit this window ?")
        if answer:
            quit()

    def college_id(self):
        code = self.college_code
        name = self.college_name.title()
        count = 0
        str1 = ""
        for i in name.split():
            if count > 2:
                break
            str1 = str1 + i[0].upper()
            count += 1
        result = "ID" + code + str1
        return result

    # Task Finished...
    def save(self):
        # Store Data in Database...
        self.add_college_records()

        result = self.college_id()
        # Create Frame...
        f3 = Frame()
        f3.place(x=0, y=0, width=1000, height=710)
        bg_label = Label(f3, image=bg)
        bg_label.place(x=0, y=0)
        # LabelFrames...
        frame3 = LabelFrame(f3, text="Added Successfully...", font=('Helvetica', 12), width=700, height=450)
        frame3.place(x=160, y=170)
        my_message = Message(frame3, text="Your college has been added successfully.\nPlease note down your College "
                            "ID i.e. "+result, font=('Helvetica', 14, 'bold'), aspect=550, justify=CENTER, fg="Green")
        my_message.place(x=140, y=40)
        btn1 = Button(frame3, text='Exit', font=('Helvetica', 14), bg='#cf2d30', fg='White', width=8, command=self.custom_quit)
        btn1.place(x=200, y=220)
        btn2 = Button(frame3, text='Sign-In', font=('Helvetica', 14), bg='#cf2d30', fg='White', width=8, command=self.sign_in)
        btn2.place(x=360, y=220)

    # Task Finished...
    def valid_college_data(self):
        if (len(self.college_code.get())!=0 and self.college_name.get()!=0 and self.state.get()!=0 and\
                self.city.get()!=0 and len(self.pincode.get())==6 and self.password1.get()!=0 and self.password2.get()!=0):
            #self.save()
            if not(self.college_code.get().isdigit()):
                tkinter.messagebox.askokcancel("Warning", "Only Digits should be entered in College_Code (length of 3)")
            if not(self.pincode.get().isdigit()):
                tkinter.messagebox.askokcancel("Warning", "Only Digits should be entered in Pincode (length of 6)")
            if self.password1.get()!=self.password2.get() or not(self.password1.get().isalnum()) or \
                    len(self.password1.get()) < 6:
                tkinter.messagebox.askokcancel("Warning", "Alphanumeric Value should be entered in Password (Minimum Length of 6)")
            self.save()
        else:
            tkinter.messagebox.askokcancel("Warning", "All fields are required. Please fill all the fields")

    # Task Finished...
    def add_college(self):
        self.reset_all()
        f2 = Frame()
        f2.place(x=0, y=0, width=1000, height=710)
        bg_label = Label(f2, image=bg)
        bg_label.place(x=0, y=0)
        # LabelFrames...
        frame2 = LabelFrame(f2, text="Add College", font=('Helvetica, 12'), width=700, height=450)
        frame2.place(x=160, y=170)
        #Labels
        label1 = Label(frame2, text='Enter College Code :', font=('Helvetica', 14))
        label1.place(x=50, y=20)
        label2 = Label(frame2, text='Enter College Name :', font=('Helvetica', 14))
        label2.place(x=50, y=60)
        label3 = Label(frame2, text='College State :', font=('Helvetica', 14))
        label3.place(x=50, y=100)
        label4 = Label(frame2, text='College City :', font=('Helvetica', 14))
        label4.place(x=50, y=140)
        label5 = Label(frame2, text='Pincode :', font=('Helvetica', 14))
        label5.place(x=50, y=180)
        label6 = Label(frame2, text='Create Password :', font=('Helvetica', 14))
        label6.place(x=50, y=220)
        label7 = Label(frame2, text='Confirm Password :', font=('Helvetica', 14))
        label7.place(x=50, y=260)
        #Entry Boxes...
        entry1 = Entry(frame2, font=("Arial", 15), width=25, textvariable=self.college_code)
        entry1.place(x=280, y=20)
        entry2 = Entry(frame2, font=("Arial", 15), width=25, textvariable=self.college_name)
        entry2.place(x=280, y=60)
        entry3 = Entry(frame2, font=("Arial", 15), width=25, textvariable=self.state)
        entry3.place(x=280, y=100)
        entry4 = Entry(frame2, font=("Arial", 15), width=25, textvariable=self.city)
        entry4.place(x=280, y=140)
        entry5 = Entry(frame2, font=("Arial", 15), width=25, textvariable=self.pincode)
        entry5.place(x=280, y=180)
        entry6 = Entry(frame2, font=("Arial", 15), width=25, textvariable=self.password1, show="*")
        entry6.place(x=280, y=220)
        entry7 = Entry(frame2, font=("Arial", 15), width=25, textvariable=self.password2, show="*")
        entry7.place(x=280, y=260)
        #Buttons
        btn1 = Button(frame2, text='Save', font=('Helvetica', 14), bg='#cf2d30', fg='White', width=8, command=self.valid_college_data)
        btn1.place(x=50, y=320)
        btn2 = Button(frame2, text='Reset', font=('Helvetica', 14), bg='#cf2d30', fg='White', width=8, command=self.reset_all)
        btn2.place(x=180, y=320)
        btn3 = Button(frame2, text='Go Back', font=('Helvetica', 14), bg='#cf2d30', fg='White', width=8, command=self.first_page)
        btn3.place(x=310, y=320)

    # Task Finished...
    def first_page(self):
        f1 = Frame()
        f1.place(x=0, y=0, width=1000, height=710)
        bg_label = Label(f1, image=bg)
        bg_label.place(x=0, y=0)
        # LabelFrames...
        frame1 = LabelFrame(f1, text="Register Here", font=('Helvetica', 12))
        frame1.pack(pady=150)
        my_message = Message(frame1, text="Don't have any account?\nAdd New College", font=('Helvetica', 14), aspect=650, justify=CENTER)
        my_message.pack(pady=10, padx=100)
        # Add New Button
        btn1 = Button(frame1, text="+Add", font=('Helvetica', 15), width=10, bg='#cf2d30', fg='White', command=self.add_college)
        btn1.pack(padx=10, pady=10)
        my_message = Message(frame1, text="OR\nHave Already Account ?,sign-in", font=('Helvetica', 14), aspect=550, justify=CENTER)
        my_message.pack(pady=0, padx=100)
        btn2 = Button(frame1, text="Sign In", font=('Helvetica', 15), width=10, bg='#cf2d30', fg='White', command=self.sign_in)
        btn2.pack(padx=10, pady=30)


obj = UIDesign()
obj.first_page()  #Function Calling...
if __name__ == '__main__':
    win.mainloop()
