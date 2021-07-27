from tkinter import*
import os

from PIL import ImageTk,Image
from tkinter import messagebox
class Login_System:
    def login(self):
        if self.uname.get()=="" and self.pass_.get()=="":
            messagebox.showerror("Error","All Fields are Required")
        elif self.uname.get()=="@ankit" and self.pass_.get()=="123456":
            root.destroy()
            import Quiz
           # messagebox.showinfo("Successfull Login",f"welcome {self.uname.get()}")
        else:
            messagebox.showerror("Error","Invalid Username or Password")

    def __init__(self,root):

        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("2050x750+0+0")
        icone = Image.open("question-marks-quiz-doubt-survey-faq-public-poll-question-marks-scattered-white-background-quiz-doubt-poll-survey-faq-142410058.jpg")
        icone = icone.resize((2050,850), Image.ANTIALIAS)
        self.bg_image=ImageTk.PhotoImage(icone)
        bg_images = Label(self.root, image=self.bg_image).place(x=0, y=0)
        #======================================
        icon = Image.open("login_logo.png")
        icon = icon.resize((200, 200), Image.ANTIALIAS)

        self.bg_icon =ImageTk.PhotoImage(icon)

       # self.bg_icon = self.bg_icon.width(30)

        # self.logo_icon = PhotoImage(file="logoo.jpg")
        self.uname=StringVar()
        self.pass_=StringVar()
        bg_label = Label(self.root, image=self.bg_icon).place(x=670,y=100)

        title=Label(self.root,text="LOGIN",font=("times new roman",40,"bold"),bg="orange",fg="green",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="grey",relief=GROOVE)
        Login_Frame.place(x=540,y=350,)
        logolbl=Label(Login_Frame,bd=1).grid(row=0,columnspan=8,pady=20)

        lbluser=Label(Login_Frame,text="username",compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(Login_Frame,textvariable=self.uname,bd=5,relief=GROOVE,font=("",15),).grid(row=1,column=1,padx=20)

        lblpass=Label(Login_Frame,text="Password",compound=LEFT,font=("times new roman",20,"bold"),bg="white",).grid(row=2,column=0,padx=20,pady=10)
        txtpass=Entry(Login_Frame,textvariable=self.pass_,bd=5,show='*',relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)

        btn_log=Button(Login_Frame,text="Login",width=15,font=("times new roman",14,"bold"),bg="light green",fg="black",command=self.login).grid(row=6,column=1,pady=40)

global root
root=Tk()
obj=Login_System(root)
root.mainloop()