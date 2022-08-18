import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter.font as font


class UserDetails:
    def __init__(self, root):

        # Initials
        global stateComBox, distComBox
        self.labelFont = font.Font(family="Ubuntu", size=11, weight="bold")
        self.headerFont = font.Font(family="Ubuntu", size=15, weight="bold")
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", selectBackground="#ffdd9e",
                        background="#ffdd9e")
        stateComBox = StringVar()
        distComBox = StringVar()

        # elements
        self.label1 = Label(root, text="Select State", width=12, font=self.labelFont, bg="#ffdd9e").place(
            x=150, y=30)
        self.comboBox1 = ttk.Combobox(
            root, width=18, textvariable=stateComBox, state='readonly', values=('Karnataka')).place(
            x=300, y=30)

        self.label2 = Label(root, text="Select District", width=12, font=self.labelFont, bg="#ffdd9e").place(
            x=150, y=80)

        self.comboBox2 = ttk.Combobox(
            root, width=18, textvariable=distComBox, state='readonly', values=(f'Belgaum', 'Bengaluru',
                                                                               'Davangere', 'Mandya', 'Mysore', 'Tumkur', 'Udupi', 'Vijaypura')).place(
            x=300, y=80)

        self.button1 = Button(root, text="Check", width=15,
                              bg="#ffdd9e", font=self.labelFont, cursor="hand2", activebackground="#ffdd9e", command=check).place(
            x=220, y=130)

        self.frame2 = Frame(root, bg="#ffce98", width=200, height=250).place(
            x=20, y=240)

        self.frame3 = Frame(root, bg="#ffdd9e", width=150, height=250).place(
            x=220, y=240)

        self.frame4 = Frame(root, bg="#ffce98", width=150, height=250).place(
            x=370, y=240)

        # self.frame5 = Frame(root, bg="#ffdd9e", width=150, height=250).place(
        #     x=520, y=240)

        self.sublabel1 = Label(
            self.frame2, text="HOSPITAL", width=17, bg="#ffc14d", font=self.labelFont).place(x=40, y=250)

        self.sublabel2 = Label(
            self.frame3, text="O2 Availability", width=13, bg="#ffc14d", font=self.labelFont).place(x=234, y=250)

        self.sublabel3 = Label(
            self.frame4, text="BEDS", width=13, bg="#ffc14d", font=self.labelFont).place(x=384, y=250)


def check():
    yc = 250
    i = 0
    hospitals = [['Venugram Hospital', 'Lakeview Hospital', 'KLE Hospital'],
                 ['Victoria Hospital', 'HAL Hospital', 'Apollo Hospital'],
                 ['Chigateri Hospital', 'City Central Hospital', 'Anugraha Hospital'],
                 ['MIMS Hospital', 'Vikram Hospital',
                     'Mandya Multispeciality Hospital'],
                 ['District Hospital', 'Panacea Hospital',
                     'Raman Memorial Hospital'],
                 ['Tumkur District Hospital', 'Dr. Thammaiah Hosptial',
                     'Manipal Tumkur Hospital'],
                 ['Dr. TMA Pai Hospital', 'Kasturba Hospital', 'Gandhi Hopsital'],
                 ['District Hospital', 'Old Government Hospital', 'Al-Ameen Hospital']
                 ]

    if stateComBox.get() == "" and distComBox.get() == "":
        return
    elif stateComBox.get() == "Karnataka" and distComBox.get() == 'Belgaum':
        hospitals = hospitals[0]
    elif stateComBox.get() == 'Karnataka' and distComBox.get() == 'Bengaluru':
        hospitals = hospitals[1]
    elif stateComBox.get() == 'Karnataka' and distComBox.get() == 'Davangere':
        hospitals = hospitals[2]
    elif stateComBox.get() == 'Karnataka' and distComBox.get() == 'Mandya':
        hospitals = hospitals[3]
    elif stateComBox.get() == 'Karnataka' and distComBox.get() == 'Mysore':
        hospitals = hospitals[4]
    elif stateComBox.get() == 'Karnataka' and distComBox.get() == 'Tumkur':
        hospitals = hospitals[5]
    elif stateComBox.get() == 'Karnataka' and distComBox.get() == 'Udupi':
        hospitals = hospitals[6]
    elif stateComBox.get() == 'Karnataka' and distComBox.get() == 'Vijaypura':
        hospitals = hospitals[7]

    conn = sqlite3.connect("C:/Users/Kumble/Workspace/Projects/PROJECT (4)/Database/BTS.sqlite")
    c = conn.cursor()
    query1 = f'select "H_02_AVAIL" from "HOSPITAL" where "H_ADDR" = "{distComBox.get()}"'
    query2 = f'select "H_ID" from "HOSPITAL" where "H_ADDR" = "{distComBox.get()}"'
    c.execute(query1)
    O2data = c.fetchall()
    # print(O2data)
    c.execute(query2)
    bedData = c.fetchall()
    # print(bedData)
    # for hID in bedData:
    #     c.execute(
    #         f'select "B_AVAILABILITY" from "BED" where "B_H_ID" = {hID[0]}')
    #     print(c.fetchall())

    for hospital in hospitals:
        yc += 50
        label1 = Label(
            root, text=hospital, width=17, bg="#ffc14d", wraplength=150, font=font.Font(family="Ubuntu", size=11, weight="bold")).place(x=40, y=yc)

        labe2 = Label(
            root, text=f'{O2data[i][0]} L', width=13, bg="#ffc14d", wraplength=150, font=font.Font(family="Ubuntu", size=11, weight="bold")).place(x=234, y=yc)
    yc = 250
    for hID in bedData:
        yc += 50
        c.execute(
            f'select "B_AVAILABILITY" from "BED" where "B_H_ID" = {hID[0]}')
        availBeds = c.fetchall()
        # print(availBeds)
        combox = ttk.Combobox(
            root, width=13, font=font.Font(family="Ubuntu", size=11, weight="bold"), state='readonly')
        combox.place(x=384, y=yc)
        combox['values'] = [
            f'NORMAL    {availBeds[0][0]}', f'Ventilator    {availBeds[1][0]}', f'ICU               {availBeds[2][0]}']


def init():
    global root
    root = Tk()
    root.geometry('550x500+400+120')
    root.title('SELECT USER DETAILS')
    # root.iconbitmap("D:/4th sem/python/playground/project/images/GIT__LOGO.ico")
    root.config(bg='#ffce73')
    p = UserDetails(root)
    root.mainloop()


if __name__ == '__main__':
    init()


# Belagavi   : Venugram Hospital, Lakeview Hospital , KLE Hospital
# Bengaluru  : 'Victoria Hospital', 'HAL Hospital', 'Apollo Hospital',
# Davangere  : 'Chigateri Hospital', 'City Central Hospital', 'Anugraha Hospital',
# Mandya    : 'MIMS Hospital', 'Vikram Hospital', 'Mandya Multispeciality Hospital',
# Mysore     : 'District Hospital', 'Panacea Hospital', 'Raman Memorial Hospital',
# Tumkur     : 'Tumkur District Hospital', 'Dr. Thammaiah Hosptial', 'Manipal Tumkur Hospital',
# Udupi      :'Dr. TMA Pai Hospital', 'Kasturba Hospital', 'Gandhi Hopsital',
# Vijaypura  : 'District Hospital', 'Old Government Hospital', 'Al-Ameen Hospital',
