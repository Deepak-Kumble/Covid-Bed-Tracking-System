import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter.font as font
from tkinter import messagebox
import Nurse__menu


class PatientEnquiry:
    def __init__(self, root, hospName):
        # Initials
        self.labelFont = font.Font(family="Ubuntu", size=11, weight="bold")
        self.headerFont = font.Font(family="Ubuntu", size=15, weight="bold")

        # tkinter variables
        global regID
        regID = IntVar()

        # elements
        self.header = Label(root, text=hospName, font=self.headerFont,
                            bg="#ffdd9e", width=60, wraplength=400).place(x=70, y=50)

        self.label1 = Label(root, text='Patient Enquiry',
                            font=self.headerFont, width=20, bg="#ffdd9e").place(x=320, y=100)

        self.label2 = Label(root, text="Registered ID",
                            font=self.labelFont, width=15, bg="#ffdd9e").place(x=280, y=150)
        self.txtBox1 = Entry(root, width=20, font=self.labelFont,
                             bg="#ffdd9e", textvariable=regID).place(x=450, y=150)

        self.button0 = Button(root, text="CHECK", font=self.labelFont, bg="#ffdd9e",
                              activebackground="#ffdd9f", command=check, width=20, cursor='hand2').place(x=340, y=210)
        self.frame1 = Frame(root, bg="#ffdd9e", width=840,
                            height=230).place(x=7, y=270)

        self.frame2 = Frame(root, bg="#ffce98", width=150, height=200).place(
            x=20, y=286)

        self.frame3 = Frame(root, bg="#ffce98", width=150, height=200).place(
            x=175, y=286)

        self.frame4 = Frame(root, bg="#ffce98", width=150, height=200).place(
            x=330, y=286)

        self.frame5 = Frame(root, bg="#ffce98", width=110, height=200).place(
            x=485, y=286)

        self.frame6 = Frame(root, bg="#ffce98", width=80, height=200).place(
            x=600, y=286)

        self.frame7 = Frame(root, bg="#ffce98", width=150, height=200).place(
            x=685, y=286)

        self.sublabel1 = Label(
            root, text="Reg ID", width=15, bg="#ffc14d", font=self.labelFont).place(x=24, y=295)

        self.sublabel2 = Label(
            root, text="First Name", width=15, bg="#ffc14d", font=self.labelFont).place(x=179, y=295)

        self.sublabel3 = Label(
            root, text="Last Name", width=15, bg="#ffc14d", font=self.labelFont).place(x=334, y=295)

        self.sublabel4 = Label(
            root, text="Gender", width=10, bg="#ffc14d", font=self.labelFont).place(x=492, y=295)

        self.sublabel5 = Label(
            root, text="Age", width=7, bg="#ffc14d", font=self.labelFont).place(x=605, y=295)

        self.sublabel6 = Label(
            root, text="Assigned Doctor", width=15, bg="#ffc14d", font=self.labelFont).place(x=689, y=295)

        self.button1 = Button(root, text="BACK", font=self.labelFont, bg="#ffdd9e",
                              activebackground="#ffdd9f", command=back, width=10, cursor="hand2").place(x=750, y=520)


class StringException(Exception):
    def __init__(self, error):
        self.message = error
        super().__init__(self, error)


def check():
    labelFont = font.Font(family="Ubuntu", size=11, weight="bold")
    xc = 24

    query1 = f'select "P_ID", "P_FNAME", "P_LNAME", "P_GENDER", "P_AGE", "P_H_ID" from "PATIENT" where "P_ID" = {regID.get()}'
    query2 = f'select "D_NAME" from "DOCTOR" where "D_ID" = (select "P_D_ID" from "PATIENT" where "P_ID" = {regID.get()})'
    query3 = f'select "H_ID" from "HOSPITAL" where "H_NAME" = "{hospitalName}"'

    try:
        conn = sqlite3.connect("C:/Users/Kumble/Workspace/Projects/PROJECT (4)/Database/BTS.sqlite")
        c = conn.cursor()
        c.execute(query1)
        pdata = c.fetchone()
        if not pdata:
            raise StringException(
                f'Record with ID: {regID.get()} does not exist')
        c.execute(query3)
        hID = c.fetchone()
        if hID[0] != pdata[5]:
            raise StringException(f'Patient not in {hospitalName}')
        c.execute(query2)
        ddata = c.fetchone()
        data = []
        for i in pdata:
            data.append(i)
        data.append(ddata[0])

        label1 = Label(
            root, text=data[0], width=15, bg="#ffc14d", font=labelFont).place(x=24, y=370)
        label2 = Label(
            root, text=data[1], width=15, bg="#ffc14d", font=labelFont).place(x=179, y=370)

        label3 = Label(
            root, text=data[2], width=15, bg="#ffc14d", font=labelFont).place(x=334, y=370)

        label4 = Label(
            root, text=data[3], width=10, bg="#ffc14d", font=labelFont).place(x=492, y=370)

        label5 = Label(
            root, text=data[4], width=7, bg="#ffc14d", font=labelFont).place(x=605, y=370)

        label6 = Label(
            root, text=data[5], width=15, bg="#ffc14d", font=labelFont).place(x=689, y=370)

    except StringException as e:
        messagebox.showerror('Error', e.message)


def back():
    root.destroy()
    Nurse__menu.init(hospitalName)


def init(hospName):
    global root, hospitalName
    hospitalName = hospName
    root = Tk()
    root.geometry('870x570+200+100')
    root.title('PATIENT-DETAILS')
    #root.iconbitmap(
    #    "D:/4th sem/python/playground/project/images/GIT__LOGO.ico")
    root.config(bg='#ffce73')
    p = PatientEnquiry(root, hospName)
    root.mainloop()


if __name__ == '__main__':
    hospName = str
    init(hospName)
