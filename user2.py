from tkinter import *
from tkinter import ttk
import tkinter.font as font


class HospitalDetails:
    def __init__(self, root):

        # Initials
        self.labelFont = font.Font(family="Ubuntu", size=11, weight="bold")
        self.headerFont = font.Font(family="Ubuntu", size=15, weight="bold")
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", selectBackground="#ffdd9e",
                        background="#ffdd9e")
        self.combo_box1 = StringVar()
        self.combo_box2 = StringVar()

        # elements

        self.label1 = Label(root, text="NAME OF THE HOSPITAL",
                            width=30, font=self.headerFont, bg="#ffdd9e").grid(row=0, column=0, columnspan=2, pady=20, ipady=5)

        self.label2 = Label(root, text="Select Bed Type", width=15, font=self.labelFont, bg="#ffdd9e").grid(
            row=1, column=0, padx=40)
        self.comboBox1 = ttk.Combobox(
            root, width=15, textvariable=self.combo_box2, state='readonly', values=('Normal', 'Ventilator', 'ICU')).grid(row=1, column=1, padx=60, pady=20)

        self.label3 = Label(root, text="Beds Available", width=15, font=self.labelFont, bg="#ffdd9e").grid(
            row=2, column=0, pady=10)
        self.txtBox1 = Entry(
            root, width=15, bg='#ffdd9e', font=self.labelFont).grid(row=2, column=1)

        self.label4 = Label(root, text="Oxygen Available", width=15, font=self.labelFont, bg="#ffdd9e").grid(
            row=3, column=0, pady=10)
        self.txtBox2 = Entry(
            root, width=15, bg='#ffdd9e', font=self.labelFont).grid(row=3, column=1)

        self.button1 = Button(root, text="Book", font=self.labelFont,
                              bg="#ffdd9e", width=10, activebackground="#ffdd9e").grid(row=4, column=0, columnspan=2, pady=30)


root = Tk()
root.geometry('450x300+500+200')
root.title('HOSPITAL-DETAILS')
# root.iconbitmap("D:/4th sem/python/playground/project/images/GIT__LOGO.ico")
root.config(bg='#ffce73')
h = HospitalDetails(root)
root.mainloop()
