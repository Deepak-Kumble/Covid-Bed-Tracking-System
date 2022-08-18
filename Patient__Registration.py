import sqlite3
from sqlite3.dbapi2 import OperationalError
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font
import Nurse__menu
import Doctor__assign


class PatientDetails:
    def __init__(self):

        # Initials
        self.labelFont = font.Font(family="Ubuntu", size=11, weight="bold")
        self.headerFont = font.Font(family="Ubuntu", size=15, weight="bold")
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", selectBackground="#ffdd9e",
                        background="#ffdd9e")
        global UID, fname, mname, lname, age, phno, address, gender, dname, drelation, dphno, combo_box1, combo_box2, combo_box3, com_box1, com_box2, com_box3, Button5

        # tkinter variables
        UID = IntVar()
        fname = StringVar()
        mname = StringVar()
        lname = StringVar()
        age = IntVar()
        phno = IntVar()
        address = StringVar()
        gender = StringVar()
        dname = StringVar()
        drelation = StringVar()
        dphno = IntVar()
        combo_box1 = StringVar()
        combo_box2 = StringVar()
        combo_box3 = StringVar()
        blocks = []
        rooms = []

        # db connection
        conn = sqlite3.connect("C:/Users/Kumble/Workspace/Projects/PROJECT (4)/Database/BTS.sqlite")
        c = conn.cursor()
        query = f'select "B_CODE" from "BLOCK" where "B_H_ID" = (select "H_ID" from "HOSPITAL" where "H_NAME" = "{hospitalName}")'
        c.execute(query)
        blockResult = c.fetchall()

        for i in range(len(blockResult)):
            blocks.append(blockResult[i][0])

        # elements
        self.mainFrame = Frame(root).grid(row=0, column=0, padx=70)
        self.label1 = Label(self.mainFrame, text="Patient Details", font=self.headerFont, bg="#ffdd9e").grid(
            row=0, column=0, columnspan=4, pady=13, padx=90)

        self.label2 = Label(self.mainFrame, text="Unique ID", width=10, font=self.labelFont, bg="#ffdd9e").grid(
            row=1, column=0, pady=10)
        self.txtBox1 = Entry(
            root, width=15, bg='#ffdd9e', font=self.labelFont, textvariable=UID).grid(row=1, column=1, ipady=3)

        self.label3 = Label(self.mainFrame, text="Enter Name", width=10, font=self.labelFont, bg="#ffdd9e").grid(
            row=2, column=0, pady=10)
        self.txtBox2 = Entry(
            root, width=15, bg='#ffdd9e', font=self.labelFont, textvariable=fname).grid(row=2, column=1, ipady=3)
        self.txtBox3 = Entry(
            root, width=15, bg='#ffdd9e', font=self.labelFont, textvariable=mname).grid(row=2, column=2, ipady=3, padx=40)
        self.txtBox4 = Entry(
            root, width=15, bg='#ffdd9e', font=self.labelFont, textvariable=lname).grid(row=2, column=3, ipady=3, padx=40)

        self.label5 = Label(self.mainFrame, text="Age", width=10,
                            font=self.labelFont, bg="#ffdd9e").grid(row=3, column=0)

        self.txtBox6 = Entry(
            root, width=15, bg='#ffdd9e', font=self.labelFont, textvariable=age).grid(row=3, column=1, ipady=3)

        self.label6 = Label(self.mainFrame, text="Address", width=10, font=self.labelFont, bg="#ffdd9e").grid(
            row=4, column=0, pady=10)
        self.txtBox7 = Entry(
            root, width=65, bg='#ffdd9e', font=self.labelFont, textvariable=address).grid(row=4, column=1, columnspan=3, ipady=3)

        self.label8 = Label(self.mainFrame, text="Phone", width=10, font=self.labelFont, bg="#ffdd9e").grid(
            row=3, column=2, pady=10)
        self.txtBox9 = Entry(
            root, width=15, bg='#ffdd9e', font=self.labelFont, textvariable=phno).grid(row=3, column=3, ipady=3)

        self.label9 = Label(self.mainFrame, text="Gender", width=10, font=self.labelFont, bg="#ffdd9e").grid(
            row=6, column=0, pady=10)
        self.rButton1 = Radiobutton(self.mainFrame, text="Male", variable=gender,
                                    value='Male', width=10, bg='#ffdd9e', cursor='hand2', font=self.labelFont).grid(row=6, column=1, padx=20)
        self.rButton2 = Radiobutton(self.mainFrame, text="Female", variable=gender,
                                    value='Female', width=10, bg='#ffdd9e', cursor='hand2', font=self.labelFont).grid(row=6, column=2)

        self.label11 = Label(
            self.mainFrame, text="Dependent", width=10, font=self.headerFont, bg="#ffdd9e").grid(row=8, column=0, columnspan=4, pady=13)
        self.label12 = Label(self.mainFrame, text="Name", width=10, font=self.labelFont, bg="#ffdd9e").grid(
            row=9, column=0, pady=3)
        self.txtBox11 = Entry(
            root, width=15, bg='#ffdd9e', font=self.labelFont, textvariable=dname).grid(row=9, column=1, ipady=3)
        self.label13 = Label(
            self.mainFrame, text="Relationship", width=10, font=self.labelFont, bg="#ffdd9e").grid(row=9, column=2)
        self.txtBox12 = Entry(
            root, width=15, bg='#ffdd9e', font=self.labelFont, textvariable=drelation).grid(row=9, column=3, ipady=5)
        self.label14 = Label(
            self.mainFrame, text="Contact No.", width=10, font=self.labelFont, bg="#ffdd9e").grid(row=10, column=0, pady=10)
        self.txtBox13 = Entry(
            root, width=15, bg='#ffdd9e', font=self.labelFont, textvariable=dphno).grid(row=10, column=1, ipady=5)

        self.label15 = Label(self.mainFrame, text="HOSPITAL-DETAILS",
                             width=20, font=self.headerFont, bg="#ffdd9e").grid(row=11, column=0, columnspan=4, pady=20)

        self.label16 = Label(self.mainFrame, text="Select Block", width=10, font=self.labelFont, bg="#ffdd9e").grid(
            row=12, column=0, pady=10)
        com_box1 = ttk.Combobox(
            self.mainFrame, width=15, textvariable=combo_box1, state='readonly', values=blocks)
        com_box1.grid(row=12, column=1)

        self.label17 = Label(
            self.mainFrame, text="Select Room", width=10, font=self.labelFont, bg="#ffdd9e").grid(row=12, column=2)
        com_box2 = ttk.Combobox(
            self.mainFrame, width=15, textvariable=combo_box2, state='readonly', values=rooms)
        com_box2.grid(row=12, column=3)

        self.label18 = Label(
            self.mainFrame, text="Select Bed", width=10, font=self.labelFont, bg="#ffdd9e").grid(row=13, column=0)
        com_box3 = ttk.Combobox(
            self.mainFrame, width=15, textvariable=combo_box3, state='readonly', values=('Normal', 'Ventilator', 'ICU'))
        com_box3.grid(row=13, column=1, pady=10)

        self.Button1 = Button(root, text="SAVE", font=self.labelFont,
                              bg="#ffdd9e", width=10, cursor="hand2", command=save).grid(row=14, column=0, pady=20)

        self.Button2 = Button(root, text="UPDATE", font=self.labelFont,
                              bg="#ffdd9e", width=10, cursor="hand2", command=update).grid(row=14, column=1, pady=20)

        self.Button3 = Button(root, text="DELETE", font=self.labelFont,
                              bg="#ffdd9e", width=10, cursor="hand2", command=delete).grid(row=14, column=2, pady=20)

        self.Button4 = Button(root, text="BACK", font=self.labelFont,
                              bg="#ffdd9e", width=10, cursor="hand2", command=returnToHome).grid(row=14, column=3, pady=20)

        Button5 = Button(root, text="Assign Doctor", font=self.labelFont,
                         bg="#ffdd9e", state=DISABLED, width=30, cursor="hand2", command=assignDoctor)
        Button5.grid(row=15, column=0, columnspan=4, pady=20)


class IntException(Exception):
    def __init__(self, error) -> None:
        self.message = error
        super().__init__(self.message)


class StringException(Exception):
    def __init__(self, error):
        super().__init__(self, error)


def init(hospName):
    global hospitalName, root
    hospitalName = hospName
    root = Tk()
    root.geometry('700x730+350+0')
    root.title('PATIENT-DETAILS')
    #root.iconbitmap(
    #    "D:/4th sem/python/playground/project/images/GIT__LOGO.ico")
    root.config(bg='#ffce73')
    p = PatientDetails()
    hospitalName = hospName
    com_box1.bind("<<ComboboxSelected>>", setBlock)
    com_box2.bind("<<ComboboxSelected>>", setRoom)
    com_box3.bind("<<ComboboxSelected>>", setBed)
    root.mainloop()


def save():
    try:
        # queries
        query1 = 'insert into "PATIENT"("P_ID","P_FNAME","P_MNAME","P_LNAME","P_AGE","P_PNO", "P_ADDR", "P_GENDER", "P_H_ID") values(?,?,?,?,?,?,?,?,?);'
        query2 = 'insert into "DEPENDENT"("D_P_ID", "D_NAME", "D_REL", "D_PNO") values(?,?,?,?);'
        # query3 = f'update "BLOCK" set "P_ID" = {UID.get()} where "B_CODE" = "{block}"'
        query3 = f'insert into "ALLOCATED_ROOMS" values(?,?)'
        # query4 = f'update "ROOM" set "R_P_ID" = {UID.get()} where "R_NO" = "{room}"'
        query4 = f'insert into "ALLOCATED_BLOCKS" values(?,?)'
        query6 = f'select "B_NO", "B_AVAILABILITY" from "BED" where "B_TYPE" = "{bed}" and "B_H_ID" = (select "H_ID" from "HOSPITAL" where "H_NAME" = "{hospitalName}")'
        query9 = f'insert into "AVAILABILITY"("B_NO", "B_TYPE_NO","B_TYPE", "B_P_ID", "B_R_NO") values(?,?,?,?,?)'
        query10 = f'select "H_ID" from "HOSPITAL" where "H_NAME" = "{hospitalName}"'

        # checks
        if len(str(UID.get())) != 12:
            raise IntException('Please enter valid aadhar number')
        if len(str(phno.get())) != 10 or len(str(dphno.get())) != 10:
            raise IntException('Please enter valid phone number')
        if not isinstance(fname.get(), str):
            raise StringException(
                'Please enter valid information in text fields')
        # db connection
        conn = sqlite3.connect("C:/Users/Kumble/Workspace/Projects/PROJECT (4)/Database/BTS.sqlite")
        c = conn.cursor()

        # prerequisite query
        c.execute(query10)
        hID = c.fetchall()[0][0]

        # data
        pData = (UID.get(), fname.get().strip(), mname.get().strip(),
                 lname.get().strip(), age.get(), phno.get(), address.get().strip(), gender.get(), hID)
        dData = (UID.get(), dname.get().strip(),
                 ((drelation.get()).strip().capitalize()), dphno.get())
        arr = []

        # executing query
        c.execute(query1, pData)
        c.execute(query2, dData)
        c.execute(query3, (room, UID.get()))
        c.execute(query4, (block, UID.get()))
        conn.commit()
        c.execute(query6)
        bedInfo = c.fetchone()
        if bedInfo[1] != 0:
            query7 = f'update "BED" set "B_AVAILABILITY" = {bedInfo[1]-1} where "B_TYPE" = "{bed}" and "B_H_ID" = (select "H_ID" from "HOSPITAL" where "H_NAME" = "{hospitalName}")'
            c.execute(query7)
            conn.commit()
        else:
            raise StringException('BEDS NOT AVAILABLE!!')
        query8 = f'select "B_NO" from "AVAILABILITY" where "B_TYPE_NO" = {bedInfo[0]} and "B_TYPE" = "{bed}"'
        c.execute(query8)
        latestNum = c.fetchall()
        if len(latestNum) != 0:
            for i in latestNum:
                arr.append(i[0])
            c.execute(
                query9, (max(arr) + 1, bedInfo[0], f"{bed}", UID.get(), combo_box2.get()))
        else:
            c.execute(
                query9, (1, bedInfo[0], f"{bed}", UID.get(), combo_box2.get()))
        conn.commit()
        messagebox.showinfo('Record Inserted',
                            'Record has been inserted successfully..')
        Button5['state'] = NORMAL

    except IntException as e:
        messagebox.showerror('Error', e.message)
    except OperationalError as e:
        messagebox.showerror('Error', e.args)
    except Exception as e:
        messagebox.showerror('Error', e)


def update():
    try:
        conn = sqlite3.connect("C:/Users/Kumble/Workspace/Projects/PROJECT (4)/Database/BTS.sqlite")
        c = conn.cursor()
        query1 = f'update "PATIENT" set "P_FNAME" = "{fname.get()}", "P_MNAME" = "{mname.get()}", "P_LNAME" = "{lname.get()}", "P_AGE" = {age.get()}, "P_PNO" = {phno.get()}, "P_ADDR" = "{address.get()}", "P_GENDER" = "{gender.get()}" where "P_ID" = {UID.get()}'
        query2 = f'update "DEPENDENT" set "D_NAME" = "{dname.get()}", "D_REL" = "{drelation.get().capitalize()}", "D_PNO" = {dphno.get()}'
        c.execute(query1)
        conn.commit()
        c.execute(query2)
        conn.commit()

        messagebox.showinfo(
            'Success', f'Record for {fname.get()} updated successfully!')
    except Exception as e:
        messagebox.showerror('Failure', e)


def delete():
    try:
        conn = sqlite3.connect("C:/Users/Kumble/Workspace/Projects/PROJECT (4)/Database/BTS.sqlite")
        c = conn.cursor()
        query0 = f'update "DOCTOR" set "D_AVAILABILITY" = "YES" where D_ID = (select "P_D_ID" from "PATIENT" where "P_ID" = {UID.get()})'
        query1 = f'delete from "PATIENT" where "P_ID" = {UID.get()}'
        query2 = f'delete from "DEPENDENT" where "D_P_ID" = {UID.get()}'
        query3 = f'update "BLOCK" set "P_ID" = NULL where "P_ID" = {UID.get()}'
        query4 = f'update "ROOM" set "R_P_ID" = NULL where "R_P_ID" = {UID.get()}'
        c.execute(query0)
        c.execute(query1)
        c.execute(query2)
        c.execute(query3)
        c.execute(query4)
        conn.commit()
        messagebox.showinfo('Success', 'Record deleted successfully!')
    except Exception as e:
        messagebox.showerror('Failure', e)


def returnToHome():
    root.destroy()
    Nurse__menu.init(hospitalName)


def assignDoctor():
    root.destroy()
    Doctor__assign.init(hospitalName, UID.get())


def setBlock(event):
    global block
    block = combo_box1.get()
    rooms = []
    conn = sqlite3.connect("C:/Users/Kumble/Workspace/Projects/PROJECT (4)/Database/BTS.sqlite")
    c = conn.cursor()
    query = f'select "R_NO" from "ROOM" where "R_B_CODE" = "{block}"'
    c.execute(query)
    roomResult = c.fetchall()
    for i in range(len(roomResult)):
        rooms.append(roomResult[i][0])
    com_box2['values'] = rooms


def setRoom(event):
    global room
    room = combo_box2.get()


def setBed(event):
    global bed
    bed = combo_box3.get()


if __name__ == '__main__':
    hospName = str
    init(hospName)
