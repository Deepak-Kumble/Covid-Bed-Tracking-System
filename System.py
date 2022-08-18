from tkinter import *
import tkinter.font as font
from Govt__login import Login
import Hospital__login
import user


class System:
    def __init__(self, root):
        self.myFont = font.Font(family="Ubuntu",
                                size=16, weight="bold", underline=1)
        self.headerFont = font.Font(family="Ubuntu", size=30, weight="bold")

        self.header = Label(root, text="Bed Tracking System for Covid Patients",
                            font=self.headerFont, bg="#ffdd9e", width=45).pack(side=TOP, pady=30)

        self.frame1 = Frame(root, bg='blue', cursor='hand2')
        self.frame1.pack(side=LEFT, padx=50, pady=50)

        self.frame2 = Frame(root, bg='yellow', cursor='hand2')
        self.frame2.pack(side=LEFT, padx=50, pady=50)

        self.frame3 = Frame(root, bg='green', cursor='hand2')
        self.frame3.pack(side=LEFT, padx=75, pady=50)

       

        self.button2 = Button(self.frame2, text='HOSPITAL', command=hospLogin,
                              relief=FLAT, bg='yellow', activebackground='yellow', font=self.myFont)
        self.button2.pack(ipadx=50, ipady=91, pady=20, padx=20)

        self.button3 = Button(self.frame3, width=10, text='USER',
                              command=userGUI, relief=FLAT, bg='green', activebackground='green', font=self.myFont)
        self.button3.pack(ipadx=45, ipady=90, pady=20, padx=20)


def hospLogin():
    global root
    root.destroy()
    Hospital__login.init()


def userGUI():
    root.destroy()
    user.init()


def init():
    global root
    root = Tk()
    root.geometry('1150x500+100+100')
    root.title('SYSTEM')
    #root.iconbitmap(
    #    "C:\Users\SanjanaKumble\Desktop\Workspace\4\PYTHON LAB\PROJECT\GIT__LOGO.jpe")
    root.config(bg='#ffce73')
    sys = System(root)
    root.mainloop()


if __name__ == '__main__':
    init()