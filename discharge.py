import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import Bill


class Discharge:
    def __init__(self, root):
        self.UID = StringVar()
        self.labelFont = font.Font(family="Ubuntu", size=12, weight="bold")
        self.headerFont = font.Font(family="Ubuntu", size=15, weight="bold")
        self.header = Label(root, text=hospitalName, font=self.headerFont,
                            bg="#ffdd9e", width=30, wraplength=400).place(x=65, y=30)

        self.label1 = Label(root, text='Discharge Patient', font=self.labelFont,
                            bg="#ffdd9e", width=15).place(x=170, y=80)

        self.label2 = Label(root, text="Registered ID", font=self.labelFont,
                            width=10, bg="#ffdd9e").place(x=120, y=130)

        self.txtBox = Entry(root, font=self.labelFont, bg='#ffdd9e',
                            width=15, textvariable=self.UID).place(x=260, y=130)

        self.button1 = Button(root, text="Retrieve Record", font=self.labelFont,
                              bg="#ffdd9e", command=retrieveRecord, cursor='hand2')
        self.button1.place(x=190, y=180)

        self.button = Button(root, text="Generate Bill", font=self.labelFont,
                             bg="#ffdd9e", command=generateBill, state=DISABLED, cursor='target')
        self.button.place(x=203, y=230)


class StringException(Exception):
    def __init__(self, error):
        self.message = error
        super().__init__(self, error)


def retrieveRecord():
    global finalData
    query1 = f'select "H_HFEE", "H_LFEE", "H_CFEE", "H_ID" from "HOSPITAL" where "H_NAME" = "{hospitalName}"'
    query2 = f'select "P_FNAME", "P_GENDER", "P_PNO", "P_H_ID" from "PATIENT" where "P_ID" = {d.UID.get()}'
    query3 = f'select "D_NAME" from "DOCTOR" where "D_ID" = (select "P_D_ID" from "PATIENT" where "P_ID" = {d.UID.get()})'
    query4 = f'select "M_AMOUNT" from "MEDICINE" where "M_P_ID" = {d.UID.get()}'
    try:
        conn = sqlite3.connect("C:/Users/Kumble/Workspace/Projects/PROJECT (4)/Database/BTS.sqlite")
        c = conn.cursor()
        c.execute(query1)
        hospRates = c.fetchone()  # [( , , )]
        # print(hospRates)
        c.execute(query2)
        pData = c.fetchone()
        # print(pData)
        if not pData:
            raise StringException('Record not found')
        if hospRates[3] != pData[3]:
            raise StringException(f'Patient not in {hospitalName}')

        c.execute(query3)
        dData = c.fetchone()
        # print(dData)
        c.execute(query4)
        bData = c.fetchall()
        billData = []
        for rate in bData:
            billData.append(rate[0])
        finalData = (pData[0], pData[1], dData[0], pData[2],
                     d.UID.get(), hospRates[0], hospRates[1], hospRates[2], sum(billData))

        d.button['state'] = NORMAL
        d.button['cursor'] = 'hand2'
    except StringException as e:
        messagebox.showerror('Error', e.message)


def generateBill():
    # print(finalData)
    query1 = f'insert into "BILL" ("B_P_ID", "TOTAL") values(?,?)'
    query2 = f'select "B_ID" from "BILL" where "B_P_ID" = {d.UID.get()}'
    query3 = f'delete from "PATIENT" where "P_ID" = {d.UID.get()}'
    query4 = f'select "P_D_ID" from "PATIENT" where "P_ID" = {d.UID.get()}'
    query5 = f'select "H_ID" from "HOSPITAL" where "H_NAME" = "{hospitalName}"'
    query6 = f'insert into "RECORD"("P_ID", "H_ID", "D_ID") values(?,?,?)'
    query8 = f'update "BLOCK" set "P_ID" = NULL where "P_ID" = {d.UID.get()}'
    query9 = f'update "ROOM" set "R_P_ID" = NULL where "R_P_ID" = {d.UID.get()}'
    query10 = f'delete from "DEPENDENT" where "D_P_ID" = {d.UID.get()}'
    query11 = f'update "DOCTOR" set "D_AVAILABILITY" = "YES" where "D_ID" = (select "P_D_ID" from "PATIENT" where "P_ID" = {d.UID.get()})'
    query12 = f'select "AVAILABILITY"."B_TYPE" from "BED", "AVAILABILITY" where "BED"."B_NO" = "AVAILABILITY"."B_TYPE_NO" and "B_P_ID" = {d.UID.get()}'

    conn = sqlite3.connect("C:/Users/Kumble/Workspace/Projects/PROJECT (4)/Database/BTS.sqlite")
    c = conn.cursor()
    c.execute(query1, (d.UID.get(),
              finalData[5] + finalData[6] + finalData[7] + finalData[8]))
    conn.commit()
    c.execute(query2)
    billID = c.fetchone()
    c.execute(query11)
    # conn.commit()
    c.execute(query4)
    dID = c.fetchone()[0]
    # print(dID)
    c.execute(query5)
    hID = c.fetchone()[0]
    # print(hID)
    c.execute(query3)
    # conn.commit()
    c.execute(query6, (d.UID.get(), hID, dID))
    # conn.commit()
    c.execute(query8)
    # conn.commit()
    c.execute(query9)
    # conn.commit()
    c.execute(query10)
    # conn.commit()
    c.execute(query12)
    bed = c.fetchall()[0][0]
    query13 = f'select "B_NO", "B_AVAILABILITY" from "BED" where "B_TYPE" = "{bed}" and "B_H_ID" = (select "H_ID" from "HOSPITAL" where "H_NAME" = "{hospitalName}")'
    c.execute(query13)
    bNO = c.fetchall()
    # print(bNO)
    query14 = f'update "BED" set "B_AVAILABILITY" = {bNO[0][1] + 1} where "B_NO" = {bNO[0][0]}'
    c.execute(query14)
    # conn.commit()
    query15 = f'DELETE FROM "AVAILABILITY" where "B_P_ID" = {d.UID.get()}'
    c.execute(query15)
    conn.commit()
    root.destroy()
    Bill.init(finalData, billID[0], hospitalName)


def init(hospName):
    global root, d, hospitalName
    root = Tk()
    root.geometry('500x300+450+200')
    root.title('DISCHARGE')
    #root.iconbitmap(
    #    "D:/4th sem/python/playground/project/images/GIT__LOGO.ico")
    root.config(bg='#ffce73')
    hospitalName = hospName
    d = Discharge(root)
    root.mainloop()


if __name__ == '__main__':
    hospName = str
    init(hospName)
