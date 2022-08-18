from tkinter import *
from tkinter import ttk
import tkinter.font as font
import Patient__Enquiry
import Patient__Registration
import discharge


class NurseMenu:

    def __init__(self, root, hospName):
        global occupation
        occupation = IntVar()
        occupation.set(0)
        self.labelFont = font.Font(family="Ubuntu", size=12, weight="bold")
        self.headerFont = font.Font(family="Ubuntu", size=15, weight="bold")

        self.label1 = Label(root, text=hospName, font=self.headerFont,
                            bg="#ffdd9e", width=30, wraplength=400).grid(row=0, column=0, columnspan=1, pady=30, ipady=15)
        self.rButton1 = Radiobutton(
            root, text="Patient Registration", variable=occupation, value=1, width=20, bg='#ffdd9e', cursor='hand2', font=self.labelFont)
        self.rButton2 = Radiobutton(
            root, text="Patient Enquiry", variable=occupation, value=2, width=20, bg='#ffdd9e', cursor='hand2', font=self.labelFont)
        self.rButton3 = Radiobutton(
            root, text="Discharge", variable=occupation, value=3, width=20, bg='#ffdd9e', cursor='hand2', font=self.labelFont)
        self.button1 = Button(root, text="Proceed!",
                              cursor='hand2', bg='#ffdd9e', font=self.labelFont, command=patientEnquiry)

        self.rButton1.grid(row=1, column=0, pady=20, padx=110)
        self.rButton2.grid(row=2, column=0, pady=20, padx=110)
        self.rButton3.grid(row=3, column=0, pady=20, padx=110)
        # self.rButton4.grid(row=4, column=0, pady=20, padx=110)
        self.button1.grid(row=5, column=0, columnspan=2, pady=20)


def patientEnquiry():
    if occupation.get() == 1:
        root.destroy()
        Patient__Registration.init(hospitalName)
    elif occupation.get() == 2:
        root.destroy()
        Patient__Enquiry.init(hospitalName)
    elif occupation.get() == 3:
        root.destroy()
        discharge.init(hospitalName)


def init(hospName):
    global root, hospitalName
    root = Tk()
    root.geometry('450x400+450+100')
    root.title('NURSE-MENU')
    #root.iconbitmap(
    #    "D:/4th sem/python/playground/project/images/GIT__LOGO.ico")
    root.config(bg='#ffce73')
    hospitalName = hospName
    n = NurseMenu(root, hospName)
    root.mainloop()


if __name__ == '__main__':
    hospName = str
    init(hospName)
