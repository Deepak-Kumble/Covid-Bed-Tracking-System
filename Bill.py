from tkinter import *
from tkinter import ttk
import tkinter.font as font
import datetime
import Nurse__menu


class Bill:
    def __init__(self, root, data, billID):
        x = datetime.datetime.now()
        self.labelFont = font.Font(family="Ubuntu", size=11, weight="bold")
        self.headerFont = font.Font(family="Ubuntu", size=15, weight="bold")

        self.label1 = Label(root, text="BILL", font=self.headerFont,
                            width=55, height=2, bg="#ffdd9e").place(x=185, y=20)
        self.label2 = Label(root, text="Bill No.: ", font=self.labelFont,
                            width=10, height=1, bg="#ffdd9e").place(x=810, y=80)
        self.subBillLabel = Label(root, text=billID, font=self.labelFont,
                                  width=5, height=1, bg="#ffdd9e").place(x=925, y=80)

        self.label3 = Label(root, text="Name of the Patient", font=self.labelFont,
                            width=20,  bg="#ffdd9e").place(x=30, y=150)

        self.label4 = Label(root, text="Name of the Doctor", font=self.labelFont,
                            width=20, bg="#ffdd9e").place(x=30, y=180)

        self.label5 = Label(root, text="Registration Number", font=self.labelFont,
                            width=20, bg="#ffdd9e").place(x=30, y=210)

        self.label6 = Label(root, text="Gender", font=self.labelFont,
                            width=20, bg="#ffdd9e").place(x=600, y=150)

        self.label7 = Label(root, text="Contact Number", font=self.labelFont,
                            width=20, bg="#ffdd9e").place(x=600, y=180)

        self.label8 = Label(root, text="Date", font=self.labelFont,
                            width=20, bg="#ffdd9e").place(x=600, y=210)

        self.txtBox1 = Label(root, font=self.labelFont,
                             bg="#ffdd9e", width=20, text=data[0])
        self.txtBox1.place(x=250, y=150)
        # self.txtBox1.set()

        self.txtBox2 = Label(root, font=self.labelFont,
                             bg="#ffdd9e", width=20, text=data[2])
        self.txtBox2.place(x=250, y=180)

        self.txtBox3 = Label(root, font=self.labelFont,
                             bg="#ffdd9e", width=20, text=data[4])
        self.txtBox3.place(x=250, y=210)

        self.txtBox4 = Label(root, font=self.labelFont,
                             bg="#ffdd9e", width=20, text=data[1])
        self.txtBox4.place(x=820, y=150)
        self.txtBox5 = Label(root, font=self.labelFont,
                             bg="#ffdd9e", width=20, text=data[3])
        self.txtBox5.place(x=820, y=180)
        self.txtBox6 = Label(root, font=self.labelFont,
                             bg="#ffdd9e", width=20, text=(x.strftime("%x")))
        self.txtBox6.place(x=820, y=210)
        self.billFrame = Frame(
            root, bg="#ffdd9e", width=955, height=270).place(x=30, y=260)

        self.frame1 = Frame(self.billFrame, bg="#ffce98",
                            width=150, height=250).place(x=40, y=270)

        self.frame2 = Frame(self.billFrame, bg="#ffd587",
                            width=625, height=250).place(x=192, y=270)

        self.frame3 = Frame(self.billFrame, bg="#ffce98",
                            width=150, height=250).place(x=820, y=270)

        self.sublabel1 = Label(self.frame1, text="SI No.",
                               font=self.labelFont, width=15, bg="#ffc14d").place(x=44, y=280)

        self.sublabel2 = Label(self.frame2, text="Particulars",
                               font=self.labelFont, width=68, bg="#ffc14d").place(x=195, y=280)

        self.sublabel3 = Label(self.frame3, text="Amount",
                               font=self.labelFont, width=15, bg="#ffc14d").place(x=824, y=280)

        self.sublabel4 = Label(self.frame2, text="01",
                               font=self.labelFont, width=15, bg="#ffc457").place(x=44, y=320)

        self.sublabel5 = Label(self.frame2, text="HOSPITAL FEE",
                               font=self.labelFont, width=68, bg="#ffc14d").place(x=195, y=320)

        self.txtBox7 = Entry(self.frame3, font=self.labelFont,
                             bg="#ffdd9e", width=15)
        self.txtBox7.place(x=832, y=320)
        self.txtBox7.insert(0, data[5])
        self.txtBox7['state'] = DISABLED

        self.sublabel6 = Label(self.frame2, text="02",
                               font=self.labelFont, width=15, bg="#ffc457").place(x=44, y=360)

        self.sublabel7 = Label(self.frame2, text="LAB TEST",
                               font=self.labelFont, width=68, bg="#ffc14d").place(x=195, y=360)

        self.txtBox8 = Entry(self.frame3, font=self.labelFont,
                             bg="#ffdd9e", width=15)
        self.txtBox8.place(x=832, y=360)
        self.txtBox8.insert(0, data[6])
        self.txtBox8['state'] = DISABLED

        self.sublabel8 = Label(self.frame2, text="03",
                               font=self.labelFont, width=15, bg="#ffc457").place(x=44, y=400)

        self.sublabel9 = Label(self.frame2, text="CONSULTATION FEE",
                               font=self.labelFont, width=68, bg="#ffc14d").place(x=195, y=400)

        self.txtBox9 = Entry(self.frame3, font=self.labelFont,
                             bg="#ffdd9e", width=15)
        self.txtBox9.place(x=832, y=400)
        self.txtBox9.insert(0, data[7])
        self.txtBox9['state'] = DISABLED

        self.sublabel10 = Label(self.frame2, text="04",
                                font=self.labelFont, width=15, bg="#ffc457").place(x=44, y=440)

        self.sublabel11 = Label(self.frame2, text="MEDICINE FEE",
                                font=self.labelFont, width=68, bg="#ffc14d").place(x=195, y=440)

        self.txtBox10 = Entry(self.frame3, font=self.labelFont,
                              bg="#ffdd9e", width=15)
        self.txtBox10.place(x=832, y=440)
        self.txtBox10.insert(0, data[8])
        self.txtBox10['state'] = DISABLED
        self.sublabel12 = Label(self.frame2, text="Total",
                                font=self.labelFont, width=15, bg="#ffc14d").place(x=670, y=480)

        self.txtBox10 = Label(self.frame3, font=self.labelFont,
                              bg="#ffdd9e", width=12, text=(data[5] + data[6] + data[7] + data[8])).place(x=834, y=480)

        self.button = Button(root, text="Back to HOME", font=self.labelFont,
                             bg="#ffdd9e", command=back, cursor='hand2').place(x=834, y=550)


def back():
    root.destroy()
    Nurse__menu.init(hospitalName)


def init(data, billID, hospName):
    global hospitalName, root
    hospitalName = hospName
    root = Tk()
    root.geometry('1020x600+150+100')
    root.title('PATIENT-DETAILS')
    #root.iconbitmap(
    #    "D:/4th sem/python/playground/project/images/GIT__LOGO.ico")
    root.config(bg='#ffce73')
    p = Bill(root, data, billID)
    root.mainloop()


if __name__ == '__main__':
    data = ()
    billID = int
    hospName = str
    init(data, billID, hospName)
