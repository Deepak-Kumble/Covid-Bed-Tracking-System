from os import read
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font
import sqlite3
import Hospital__login


class Doctor:
    def __init__(self, root, hospName):
        self.regID = IntVar()
        self.name = StringVar()
        self.doctor = StringVar()
        self.medicine = StringVar()
        self.dosage = StringVar()
        self.quantity = IntVar()
        self.amount = IntVar()
        self.uyc = 305
        self.ryc = 305

        self.labelFont = font.Font(family="Ubuntu", size=11, weight="bold")
        self.headerFont = font.Font(family="Ubuntu", size=17, weight="bold")
        self.header = Label(root, text=hospName, bg="#ffdd9e",
                            width=60, font=self.headerFont).place(x=90, y=20)
        self.optionFrame = Frame(root, bg="#ffdd9e", width=1000, height=200).grid(
            row=0, columnspan=5, pady=75, padx=20)

        self.label1 = Label(self.optionFrame, text="Reg ID",
                            bg="#ffc14d", width=10, font=self.labelFont).place(x=40, y=90)

        self.txtBox1 = Entry(root, width=20, font=self.labelFont,
                             bg="#ffc14d", textvariable=self.regID).place(x=150, y=90)

        self.label2 = Label(self.optionFrame, text="Name",
                            bg="#ffc14d", width=10, font=self.labelFont).place(x=350, y=90)

        self.txtBox2 = Entry(root, width=20, font=self.labelFont,
                             bg="#ffc14d", textvariable=self.name).place(x=460, y=90)

        self.label3 = Label(self.optionFrame, text="Doctor",
                            bg="#ffc14d", width=10, font=self.labelFont).place(x=660, y=90)

        self.txtBox3 = Entry(root, width=20, font=self.labelFont,
                             bg="#ffc14d", textvariable=self.doctor).place(x=770, y=90)

        self.label4 = Label(self.optionFrame, text="Medicine",
                            bg="#ffc14d", width=10, font=self.labelFont).place(x=40, y=150)

        self.txtBox4 = Entry(root, width=20, font=self.labelFont,
                             bg="#ffc14d", textvariable=self.medicine).place(x=150, y=150)

        self.label5 = Label(self.optionFrame, text="Dosage",
                            bg="#ffc14d", width=10, font=self.labelFont).place(x=350, y=150)

        self.txtBox5 = Entry(root, width=20, font=self.labelFont,
                             bg="#ffc14d", textvariable=self.dosage).place(x=460, y=150)

        self.label6 = Label(self.optionFrame, text="Quantity",
                            bg="#ffc14d", width=10, font=self.labelFont).place(x=660, y=150)

        self.txtBox6 = Entry(root, width=20, font=self.labelFont,
                             bg="#ffc14d", textvariable=self.quantity).place(x=770, y=150)

        self.label7 = Label(self.optionFrame, text="Amount",
                            bg="#ffc14d", width=10, font=self.labelFont).place(x=40, y=200)

        self.txtBox7 = Entry(root, width=20, font=self.labelFont,
                             bg="#ffc14d", textvariable=self.amount).place(x=150, y=200)

        self.Button1 = Button(
            self.optionFrame, font=self.labelFont, text="Prescribe Medicine", width=15, bg="#ffc14d", cursor='hand2', activebackground='#ffdd9e', command=prescribeMed, state=DISABLED)
        self.Button1.place(x=350, y=230)

        self.Button3 = Button(
            self.optionFrame, font=self.labelFont, text="Medicine Record", width=15, bg="#ffc14d", cursor='hand2', activebackground='#ffdd9e', command=readMed).place(x=500, y=230)

        self.frame1 = Frame(root, bg="#ffdd9e", width=1000, height=100).grid(
            row=3, columnspan=8, pady=20, padx=20)

        self.frame2 = Frame(self.frame1, bg="#ffce98", width=250, height=300).place(
            x=20, y=300)

        self.frame3 = Frame(self.frame1, bg="#ffdd9e", width=250, height=300).place(
            x=270, y=300)

        self.frame4 = Frame(self.frame1, bg="#ffce98", width=250, height=300).place(
            x=520, y=300)

        self.frame5 = Frame(self.frame1, bg="#ffdd9e", width=250, height=300).place(
            x=770, y=300)

        self.sublabel1 = Label(
            self.frame2, text="Medicine", width=25, bg="#ffc14d", font=self.labelFont).place(x=25, y=305)

        self.sublabel2 = Label(
            self.frame3, text="Dosage", width=25, bg="#ffc14d", font=self.labelFont).place(x=276, y=305)

        self.sublabel3 = Label(
            self.frame4, text="Quantity", width=25, bg="#ffc14d", font=self.labelFont).place(x=527, y=305)

        self.sublabel4 = Label(
            self.frame5, text="Amount", width=25, bg="#ffc14d", font=self.labelFont).place(x=778, y=305)

        self.Button2 = Button(root, text="UPDATE", font=self.labelFont,
                              bg="#ffdd9e", width=15, cursor="hand2", command=update, state=DISABLED)
        self.Button2.place(x=720, y=610)

        self.Button3 = Button(root, text="BACK", font=self.labelFont,
                              bg="#ffdd9e", width=15, cursor="hand2", command=back)
        self.Button3.place(x=870, y=610)


class IntException(Exception):
    def __init__(self, error) -> None:
        self.message = error
        super().__init__(self.message)


class StringException(Exception):
    def __init__(self, error):
        super().__init__(error)


class GeneralException(Exception):
    def __init__(self, error):
        super().__init__(error)


def back():
    root.destroy()
    Hospital__login.init()


def update():
    messagebox.showinfo(
        'Success', f'Drug data for {p.name.get()} updated successfully')
    root.destroy()
    Hospital__login.init()


def readMed():
    global readLabel
    xc = 50
    p.ryc += 40
    i = 0
    readLabel = []
    try:
        if p.regID.get() == 0 or len(str(p.regID.get())) < 12:
            raise IntException('Please enter valid ID')
        elif p.name.get() == "" or p.doctor.get() == "":
            raise StringException('Invalid Patient Name or Doctor Name')

        query1 = f'select "P_FNAME", "P_D_ID" from "PATIENT" where "P_ID" = {p.regID.get()}'
        query2 = f'select "D_NAME" from "DOCTOR" where "D_ID" = ?'
        query3 = f'select "M_NAME", "M_DOSE", "M_QTY", "M_AMOUNT" from "MEDICINE" where "M_P_ID" = {p.regID.get()}'
        conn = sqlite3.connect("C:/Users/Kumble/Workspace/Projects/PROJECT (4)/Database/BTS.sqlite")
        c = conn.cursor()
        c.execute(query1)
        pData = c.fetchall()

        if not pData:
            raise StringException('Patient Record not found.')

        if pData[0][0].lower() != (p.name.get()).lower():
            raise StringException('ID and Name does not match.')

        c.execute(query2, (pData[0][1],))
        dData = c.fetchall()
        if not dData or (dData[0][0].lower() != p.doctor.get().lower()):
            raise StringException('No such patient assigned to you.')
        c.execute(query3)
        medData = c.fetchall()
        if not medData:
            raise GeneralException('No Drug data found')
        for medRecord in medData:
            for info in medRecord:
                readLabel.append(Label(root, text=info, width=20,
                                       bg="#ffc14d", font=p.labelFont))
                readLabel[i].place(x=xc, y=p.ryc)
                xc += 251
                i += 1
            p.ryc += 40
            xc = 50
        p.Button1['state'] = NORMAL

    except IntException as e:
        messagebox.showerror('Failure', e.message)

    except StringException as e:
        messagebox.showerror('Error', e)

    except GeneralException as e:
        messagebox.showerror('Error', e)
        p.Button1['state'] = NORMAL

    except Exception as e:
        messagebox.showerror('Failure', e)


def prescribeMed():
    global prescLabel
    xc = 25
    p.uyc += 40
    for i in readLabel:
        i.after(1, i.destroy())
    try:
        if p.regID.get() == 0:
            raise IntException('Please enter valid ID')
        elif p.name.get() == "" or p.doctor.get() == "":
            raise StringException('Invalid Patient Name or Doctor Name')
        elif p.medicine.get() == "" or p.dosage.get == "" or p.quantity.get() == 0 or p.amount.get == 0:
            raise StringException('Please enter valid medicine details')
        query1 = f'select "P_D_ID" from "PATIENT" where "P_ID" = {p.regID.get()}'
        query2 = 'insert into "MEDICINE"("M_NAME", "M_QTY", "M_DOSE", "M_AMOUNT", "M_P_ID", "M_D_ID") values(?,?,?,?,?,?)'
        conn = sqlite3.connect("C:/Users/Kumble/Workspace/Projects/PROJECT (4)/Database/BTS.sqlite")
        c = conn.cursor()
        c.execute(query1)
        dID = c.fetchone()
        data = (p.medicine.get(), p.quantity.get(), p.dosage.get(),
                p.amount.get(), p.regID.get(), dID[0])
        dispData = [p.medicine.get(), p.dosage.get(),
                    p.quantity.get(), p.amount.get()]
        c.execute(query2, data)
        conn.commit()
        p.Button2['state'] = NORMAL
        for info in dispData:
            prescLabel = Label(root, text=info, width=25,
                               bg="#ffc14d", font=p.labelFont)
            prescLabel.place(x=xc, y=p.uyc)
            xc += 251

    except IntException as e:
        messagebox.showerror('Failure', e)

    except StringException as e:
        messagebox.showerror('Failure', e)

    except Exception as e:
        messagebox.showerror('Failure', e)


def init(hospName):
    global root, p
    root = Tk()
    root.geometry('1050x650+150+50')
    root.title('PATIENT-DETAILS')
    #root.iconbitmap(
    #    "D:/4th sem/python/playground/project/images/GIT__LOGO.ico")
    root.config(bg='#ffce73')
    p = Doctor(root, hospName)
    root.mainloop()


if __name__ == '__main__':
    hospName = str
    init(hospName)
