from tkinter import *
from tkinter import ttk
import tkinter.font as font
from tkinter import messagebox
import sqlite3
import Nurse__menu
import Doctor


class Hosp:
    def __init__(self, root):
        global combo_box, textEntry1, textEntry2
        combo_box = StringVar()
        textEntry1 = StringVar()
        textEntry2 = StringVar()
        self.labelFont = font.Font(family="Ubuntu", size=12, weight="bold")
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", selectBackground="#ffdd9e",
                        background="#ffdd9e")
        self.label1 = Label(root, text="User Role",
                            font=self.labelFont, bg='#ffdd9e')
        self.comboBox = ttk.Combobox(
            root, width=27, textvariable=combo_box, state='readonly', values=('NURSE', 'DOCTOR'))
        self.comboBox.current(0)
        self.label2 = Label(root, text="Username",
                            font=self.labelFont, bg='#ffdd9e')
        self.txtBox1 = Entry(root, font=self.labelFont,
                             width=20, bg='#ffdd9e', textvariable=textEntry1)
        self.label3 = Label(root, text="Password",
                            font=self.labelFont, bg='#ffdd9e')
        self.txtBox2 = Entry(root, font=self.labelFont,
                             width=20, bg='#ffdd9e', textvariable=textEntry2)
        self.button1 = Button(root, width=20, height=2,
                              text="Login", font=self.labelFont, bg='#ffdd9e', activebackground='#ffdfa3', cursor='hand2', command=nextGUI)

        self.label1.grid(row=0, column=0, padx=70, pady=50)
        self.comboBox.grid(row=0, column=1, ipady=10)
        self.label2.grid(row=1, column=0)
        self.txtBox1.grid(row=1, column=1, ipady=5)
        self.label3.grid(row=2, column=0, pady=30)
        self.txtBox2.grid(row=2, column=1, pady=30, ipady=5)
        self.button1.grid(row=3, column=0, columnspan=3)


def nextGUI():
    conn = sqlite3.connect("C:/Users/Kumble/Workspace/Projects/PROJECT (4)/Database/BTS.sqlite")
    c = conn.cursor()
    query = 'select "L_PASSWORD", "L_H_NAME" from LOGIN where L_NAME = "' + \
        textEntry1.get() + '" and L_OCCUPATION = "' + combo_box.get() + '";'
    c.execute(query)
    result = c.fetchall()
    if len(result) and result[0][0] == textEntry2.get() and combo_box.get() == 'NURSE':
        root.destroy()
        Nurse__menu.init(result[0][1])
    elif len(result) and result[0][0] == textEntry2.get() and combo_box.get() == 'DOCTOR':
        root.destroy()
        Doctor.init(result[0][1])
    else:
        messagebox.showerror('Error', 'Invalid Login Credentials')


def init():
    global root
    root = Tk()
    root.geometry('450x350+450+100')
    root.title('Hospital-Login')
    #root.iconbitmap(
    #    "D:/4th sem/python/playground/project/images/GIT__LOGO.ico")
    root.config(bg='#ffce73')
    h = Hosp(root)
    root.mainloop()


if __name__ == '__main__':
    init()
