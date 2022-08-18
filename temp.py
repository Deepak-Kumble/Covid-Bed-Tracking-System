import tkinter as tk
from tkinter import StringVar, ttk
# # conn = sqlite3.connect('./DataBase/BTS.sqlite')
# c = conn.cursor()
# query1 = f'select "P_ID", "P_FNAME", "P_LNAME", "P_GENDER", "P_AGE" from "PATIENT" where "P_ID" = {641660306254}'
# query2 = f'select "D_NAME" from "DOCTOR" where "D_ID" = (select "P_D_ID" from "PATIENT" where "P_ID" = {641660306254})'
# c.execute(query1)
# pdata = c.fetchone()
# c.execute(query2)
# ddata = c.fetchone()
# data = []
# for i in pdata:
#     data.append(i)
# data.append(ddata[0])
# print(data)

# , "D_NAME" from "PATIENT", "DOCTOR" where "PATIENT"."P_D_ID" = "DOCTOR"."D_ID" and "P_ID" = {641660306254}

# from tkinter import *

# fenster = Tk()
# fenster.title("Window")


# def switch():
#     if b1["state"] == "normal":
#         b1["state"] = "disabled"
#         b2["text"] = "enable"
#     else:
#         b1["state"] = "normal"
#         b2["text"] = "disable"


# #--Buttons
# b1 = Button(fenster, text="Button", height=5, width=7)
# b1.grid(row=0, column=0)

# b2 = Button(text="disable", command=switch)
# b2.grid(row=0, column=1)

# fenster.mainloop()

# query1 = f'select "P_ID", "P_FNAME", "P_LNAME", "P_GENDER", "P_AGE", "D_NAME" from "PATIENT", "DOCTOR" where "PATIENT"."P_D_ID" = "DOCTOR"."D_ID" and "P_ID" = {regID.get()}'


# def func(event):
#     comVal.set(comVal.get())


# root = tk.Tk()
# root.geometry('250x250+300+150')
# comVal = tk.StringVar()
# comVal.trace("w", lambda name, index, mode, comVal=comVal: func(comVal))
# button = tk.Entry(root, width=15, textvariable=comVal)
# button1 = tk.Entry(root, width=15, textvariable=comVal)
# button.place(x=60, y=60)
# button1.place(x=60, y=90)
# root.mainloop()

# def callbackFunc(event):
#     print("New Element Selected")
# root = tk.Tk()
# root.geometry('200x100+300+150')
# comVal = StringVar()
# comboExample = ttk.Combobox(root, width=15,textvariable=comVal,state='readonly', values=[
#                             "January", "February", "March", "April"]).place(x=50, y=60)
# comboExample.current(1)
# comboExample.bind("<<ComboboxSelected>>", callbackFunc)
# root.mainloop()

import sqlite3
arr = []
conn = sqlite3.connect('./DataBase/BTS.sqlite')
c = conn.cursor()
query12 = f'select "B_NO" from "BED" where "B_TYPE" = "" and "B_H_ID" = (select "H_ID" from "HOSPITAL" where "H_NAME" = "")'
c.execute(query12)
latestNum = c.fetchall()
print(latestNum)
# for i in latestNum:
#     arr.append(i[0])
# print(max(arr)+1)
