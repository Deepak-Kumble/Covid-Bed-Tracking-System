from tkinter import *
import tkinter.font as font


class Login:
    def __init__(self, root) -> None:
        self.labelFont = font.Font(family="Ubuntu", size=12, weight="bold")
        self.label1 = Label(root, text="Enter Username",
                            font=self.labelFont, bg='#ffdd9e')
        self.txtBox1 = Entry(root, font=self.labelFont,
                             width=17, bg='#ffdd9e')
        self.label2 = Label(root, text="Enter Password",
                            font=self.labelFont, bg='#ffdd9e')
        self.txtBox2 = Entry(root, font=self.labelFont, width=17, bg='#ffdd9e')
        self.button1 = Button(root, width=20, height=2,
                              text="Login", font=self.labelFont, bg='#ffdd9e', activebackground='#ffdfa3', cursor='hand2')
        self.label1.grid(row=0, column=0, padx=20, pady=60)
        self.txtBox1.grid(row=0, column=1, ipady=5)
        self.label2.grid(row=1, column=0)
        self.txtBox2.grid(row=1, column=1, ipady=5)
        self.button1.grid(row=2, column=0, columnspan=2, pady=60, padx=50)


def init():
    global root
    root = Tk()
    root.geometry("360x400+500+200")
    root.title('Login')
    root.config(bg='#ffce73')
    #root.iconbitmap(
    #    "D:/4th sem/python/playground/project/images/GIT__LOGO.ico")
    lgn = Login(root)
    root.mainloop()


if __name__ == '__main__':
    init()
# ------------------------------------------------------------------------------------------------------------------

# root = Tk()
# root.geometry("375x400+500+200")
# root.title('Login')
# root.config(bg='#ffce73')
# root.iconbitmap("D:/4th sem/python/playground/project/images/GIT__LOGO.ico")
# # lgn = Login(root)

# labelFont = font.Font(family="Ubuntu", size=12, weight="bold")
# buttonFrame = Frame()
# label1 = Label(text="Enter Username", font=labelFont, bg='#ffdd9e')
# txtBox1 = Entry(font=labelFont, width=17, bg='#ffdd9e')
# label2 = Label(text="Enter Password", font=labelFont, bg='#ffdd9e')
# txtBox2 = Entry(font=labelFont, width=17, bg='#ffdd9e')
# button1 = Button(buttonFrame, width=20, height=2, text="Login", font=labelFont,
#                  bg='#ffdd9e', activebackground='#ffdfa3', cursor='hand2')

# label1.grid(row=0, column=0, padx=20, pady=60)
# txtBox1.grid(row=0, column=1, ipady=5)
# label2.grid(row=1, column=0)
# txtBox2.grid(row=1, column=1, ipady=5)
# buttonFrame.grid(row=2, column=0, columnspan=2, pady=60, padx=67)
# button1.pack()


# root.mainloop()
