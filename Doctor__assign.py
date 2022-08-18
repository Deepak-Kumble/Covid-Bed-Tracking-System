from tkinter import *
from tkinter import ttk
import tkinter.font as font
from tkinter import messagebox
import sqlite3
import Patient__Registration


class DoctorAssign:
    def __init__(self, root, hospName, doctors):
        self.labelFont = font.Font(family="Ubuntu", size=11, weight="bold")
        self.label1font = font.Font(family='Ubuntu', size=16, weight="bold")
        self.headerFont = font.Font(family="Ubuntu", size=17, weight="bold")
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", selectBackground="#ffdd9e",
                        background="#ffdd9e")

        global combo_box1
        combo_box1 = StringVar()

        self.header = Label(root, text=hospName, font=self.label1font,
                            bg="#ffdd9e", width=30, wraplength=400).place(x=50, y=20)

        self.label1 = Label(root, text="Assign Doctor to patient",
                            font=self.labelFont, bg="#ffdd9e", width=30).place(x=105, y=75)

        self.label1 = Label(root, text="Select Doctor",
                            font=self.labelFont, bg="#ffdd9e", width=20).place(x=20, y=160)

        self.cobox2 = ttk.Combobox(
            root, width=20, font=self.labelFont, state="readonly", textvariable=combo_box1, values=doctors).place(x=250, y=160)

        self.button1 = Button(root, text="OK", width=20,
                              bg="#ffdd9e", font=self.labelFont, cursor="hand2", activebackground="#ffdd9f", command=addDoc).place(x=150, y=220)

        self.button2 = Button(root, text="BACK", width=10, bg="#ffdd9e",
                              font=self.labelFont, activebackground="#ffdd9f", cursor="hand2", command=back).place(x=350, y=290)


def addDoc():
    try:
        conn = sqlite3.connect("C:/Users/Kumble/Workspace/Projects/PROJECT (4)/Database/BTS.sqlite")
        c = conn.cursor()
        query1 = f'update "PATIENT" set "P_D_ID" = (select "D_ID" from "DOCTOR" where "D_NAME" = "{combo_box1.get()}") where "P_ID" = {ID}'
        query2 = f'update "DOCTOR" set "D_AVAILABILITY" = "NO" where "D_ID" = (select "D_ID" from "DOCTOR" where "D_NAME" = "{combo_box1.get()}")'
        query3 = f'select "P_FNAME" from "PATIENT" where "P_ID" = {ID}'
        c.execute(query1)
        conn.commit()
        c.execute(query2)
        conn.commit()
        c.execute(query3)
        name = c.fetchall()
        conn.close()
        messagebox.showinfo(
            'Success', f'Doctor {combo_box1.get()} assigned to {name[0][0]}')
    except Exception as e:
        messagebox.showerror('Failure', e)


def back():
    root.destroy()
    Patient__Registration.init(hospitalName)


def init(hospName, id):
    # initializers
    global root, hospitalName, ID
    hospitalName = hospName
    ID = id

    # connection to database
    conn = sqlite3.connect("C:/Users/Kumble/Workspace/Projects/PROJECT (4)/Database/BTS.sqlite")
    c = conn.cursor()
    query = f'select "D_NAME" from "DOCTOR", "HOSPITAL" where "DOCTOR"."H_ID" = "HOSPITAL"."H_ID" and "H_NAME" = "{hospName}"and "D_AVAILABILITY" = "YES"'
    c.execute(query)
    doctors = c.fetchall()

    # tkinter variables
    root = Tk()
    root.geometry('500x350+450+200')
    root.title('PATIENT-DETAILS')
    #root.iconbitmap(
    #    "D:/4th sem/python/playground/project/images/GIT__LOGO.ico")
    root.config(bg='#ffce73')
    p = DoctorAssign(root, hospName, doctors)
    root.mainloop()


if __name__ == '__main__':
    hospName = str
    ID = int
    init(hospName, ID)
