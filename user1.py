from tkinter import *
from tkinter import ttk
import tkinter.font as font


class PatientDetails:
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
        self.headerLabel = Label(root, text='<hospital name>', bg='#ffdd9e', font=self.headerFont).grid(
            row=0, column=0, columnspan=4, pady=20)
        self.mainFrame = Frame(root).grid(row=1, column=1, padx=70)
        self.label1 = Label(self.mainFrame, text="Patient Details", font=self.headerFont, bg="#ffdd9e").grid(
            row=1, column=0, columnspan=4, pady=13, padx=90)

        self.label2 = Label(self.mainFrame, text="Unique ID", width=10, font=self.labelFont, bg="#ffdd9e").grid(
            row=2, column=0, pady=10, padx=25)
        self.txtBox1 = Entry(
            root, width=15, bg='#ffdd9e', font=self.labelFont).grid(row=2, column=1, ipady=3)

        self.label3 = Label(self.mainFrame, text="Enter Name", width=10, font=self.labelFont, bg="#ffdd9e").grid(
            row=3, column=0, pady=10)
        self.txtBox2 = Entry(
            root, width=15, bg='#ffdd9e', font=self.labelFont).grid(row=3, column=1, ipady=3)
        self.txtBox3 = Entry(
            root, width=15, bg='#ffdd9e', font=self.labelFont).grid(row=3, column=2, ipady=3, padx=40)
        self.txtBox4 = Entry(
            root, width=15, bg='#ffdd9e', font=self.labelFont).grid(row=3, column=3, ipady=3, padx=40)

        self.label4 = Label(self.mainFrame, text="Birth Date", width=10, font=self.labelFont, bg="#ffdd9e").grid(
            row=4, column=0, pady=10)
        self.textBox5 = Entry(
            root, width=15, bg='#ffdd9e', font=self.labelFont).grid(row=4, column=1, ipady=3)

        self.label5 = Label(self.mainFrame, text="Age", width=10,
                            font=self.labelFont, bg="#ffdd9e").grid(row=4, column=2)
        self.txtBox6 = Entry(
            root, width=15, bg='#ffdd9e', font=self.labelFont).grid(row=4, column=3, ipady=3)

        self.label6 = Label(self.mainFrame, text="Address", width=10, font=self.labelFont, bg="#ffdd9e").grid(
            row=5, column=0, pady=10)
        self.txtBox7 = Entry(
            root, width=15, bg='#ffdd9e', font=self.labelFont).grid(row=5, column=1, ipady=3)

        self.label7 = Label(self.mainFrame, text="City", width=10,
                            font=self.labelFont, bg="#ffdd9e").grid(row=5, column=2)
        self.txtBox8 = Entry(
            root, width=15, bg='#ffdd9e', font=self.labelFont).grid(row=5, column=3, ipady=3)

        self.label8 = Label(self.mainFrame, text="Phone", width=10, font=self.labelFont, bg="#ffdd9e").grid(
            row=6, column=0, pady=10)
        self.txtBox9 = Entry(
            root, width=15, bg='#ffdd9e', font=self.labelFont).grid(row=6, column=1, ipady=3)

        self.label9 = Label(self.mainFrame, text="Gender", width=10, font=self.labelFont, bg="#ffdd9e").grid(
            row=7, column=0, pady=10)
        self.rButton1 = Radiobutton(self.mainFrame, text="Male", variable='option',
                                    value=1, width=10, bg='#ffdd9e', cursor='hand2', font=self.labelFont).grid(row=7, column=1, padx=20)
        self.rButton2 = Radiobutton(self.mainFrame, text="Female", variable='option',
                                    value=2, width=10, bg='#ffdd9e', cursor='hand2', font=self.labelFont).grid(row=7, column=2)

        self.label10 = Label(self.mainFrame, text="Blood Group", width=10, font=self.labelFont, bg="#ffdd9e").grid(
            row=8, column=0, pady=10)
        self.comboBox1 = ttk.Combobox(
            self.mainFrame, width=15, textvariable=self.combo_box1, state='readonly', values=('A', 'A+', 'AB+')).grid(row=8, column=1)

        self.label11 = Label(self.mainFrame, text="Symptoms", width=10, font=self.labelFont, bg="#ffdd9e").grid(
            row=9, column=0, pady=10)
        self.txtBox9 = Entry(
            root, width=15, bg='#ffdd9e', font=self.labelFont).grid(row=9, column=1, ipady=3)

        self.label12 = Label(self.mainFrame, text="Bed type", width=15, font=self.labelFont, bg="#ffdd9e").grid(
            row=8, column=2)

        self.comboBox2 = ttk.Combobox(
            self.mainFrame, width=15, textvariable=self.combo_box2, state='readonly', values=('A', 'A+', 'AB+')).grid(row=8, column=3)

        self.button1 = Button(root, text="Register", font=self.labelFont, bg="#ffdd9e",
                              activebackground="#ffdd9f", cursor='hand2', width=20, command=register).grid(row=10, column=0, columnspan=2, pady=20)

        self.button1 = Button(root, text="Cancel", font=self.labelFont, bg="#ffdd9e",
                              activebackground="#ffdd9f", cursor='hand2', width=20, command=cancel).grid(row=10, column=2, columnspan=2, pady=20)


def register():
    pass


def cancel():
    root.destroy()


def init():
    global root
    root = Tk()
    root.geometry('700x580+350+100')
    root.title('PATIENT-DETAILS')
    # root.iconbitmap("D:/4th sem/python/playground/project/images/GIT__LOGO.ico")
    root.config(bg='#ffce73')
    p = PatientDetails(root)
    root.mainloop()


if __name__ == '__main__':
    init()
