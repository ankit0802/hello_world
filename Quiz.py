
import future
import sys
import json
import tkinter
from tkinter import *
from tkinter import messagebox
from datetime import datetime

with open('./dataa.json') as f:
    data = json.load(f)

    #converting JSON array into python list
q=(data['ques'])
options=(data['options'])
a=(data['ans'])
'''
print(questions)
print(options)
print(answers)
'''

class Quiz:
    global newroot
    def __init__(self):
        self.qn = 0
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        #self.update()
        self.correct = 0

    #def clock(self):
     #   minutes=
      #  sec=
    def update(self):
        newroot.config(bg="green")
        t = Label(newroot, text="TIME OVER CLICK TO GENERATE RESULT", width=70, bg="blue", fg="white",
                  font=("times", 32, "bold"))
        t.place(x=300,y=200)
        button=Button(newroot,text="SHOW RESULT",width=20,command=self.display_result)
        button.pack(x=400,y=300)
    def question(self, qn):
        t = Label(newroot, text="Quiz in Python Programming", width=70, bg="blue", fg="white", font=("times", 32, "bold"))
        t.place(x=0, y=2)
        qn = Label(newroot, text=q[qn], width=58, bg="#00ae9f",font=("times", 30, "bold"), anchor="w")
        qn.place(x=60, y=120)
        return qn

    def radiobtns(self):
        val = 0
        b = []
        yp = 220
        while val < 4:
            btn = Radiobutton(newroot,bg="#00ae9f", text=" ", variable=self.opt_selected, value=val + 1, font=("verdana", 22,"bold"))
            b.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 90
        return b

    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[val]['text'] = op
            val += 1

    def buttons(self):
        nbutton = Button(newroot, text="Next", command=self.nextbtn, width=15, bg="Blue", fg="white",
                         font=("times", 16, "bold"))
        nbutton.place(x=1200, y=680)
        quitbutton = Button(newroot, text="Quit", command=newroot.destroy, width=15, bg="red", fg="white",
                            font=("times", 16, "bold"))
        quitbutton.place(x=1330, y=60)
        submitbutton = Button(newroot, text="Submit", command=self.display_result, width=15, bg="green", fg="white",
                            font=("times", 16, "bold"))
        submitbutton.place(x=800, y=680)

    def checkans(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True

    def nextbtn(self):
        if self.checkans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(q):
            self.display_result()
        else:
            self.display_options(self.qn)

    def display_result(self):
        global correct,wrong,score,end_time,newroot
        score = int(self.correct / len(q) * 100)
        score = str(score)
        wc = len(q) - self.correct
        correct =  str(self.correct)
        wrong =   str(wc)
        end_time=datetime.now()
        self.store_data()
        self.show()

    def show(self):
        global correct, wrong, score, end_time,newroot
        newroot.destroy()
        win=Toplevel(root)
        win.title("RESULT")
        win.geometry("2050x790+0+0")
        #win.resizable()
        win.config(bg="cyan")

        res=Label(win,width=100,font=("Comic sans MS ", 70, "bold"),text="  RESULT  ",fg="red",bg="blue")
        res.place(x=0,y=120)
        res.pack()

        scorelabel=Label(win,width=50, font=("Comic sans MS ", 40, "bold"),text="SCORED \n"+score+"%",fg="yellow",bg="cyan")
        scorelabel.place(x=40,y=190)
        #scorelabel.pack()

        correctlabel=Label(win,width=30, font=("Comic sans MS ", 35, "bold"),text="CORRECT \n"+correct,fg="green",bg="cyan")
        correctlabel.place(x=800,y=430)
        #correctlabel.pack()

        wronglabel=Label(win,width=30, font=("Comic sans MS ", 35, "bold"),text="WRONG \n"+wrong,fg="red",bg="cyan")
        wronglabel.place(x=10,y=430)
        #wronglabel.pack()

        win.mainloop()

    def store_data(self):
        global score, correct, wrong, end_time, file_name
        end_time = str(end_time)
        score = str(score)
        correct = str(correct)
        wrong = str(wrong)
        file = open(file_name, "a")
        data = '\nSCORE:   ' + score + '\nCORRECT:  ' + correct + '\nWRONG:   ' + wrong + '\nEND TIME:   ' + end_time + '\n\n'
        file.write(data)
        file.close()

def file():
    global file_name,roll_text
    label_instruction.destroy()
    button_enter.destroy()
    roll=roll_text.get()
    name=name_text.get()
    time=datetime.now()
    time=str(time)
    file_name = roll +'_'+ name + '.txt'
    file = open(file_name, "a")
    data = '\nROLL NO:' + roll + '\nNAME   :' + name+'\nSTART TIME:   '+time
    file.write(data)
    file.close()
    global newwindow
    newwindow.destroy()
    enter_command()

def enter_command():
    #root.destroy()
    label_instruction.destroy()
    label_text.destroy()
    label_image.destroy()
    button_enter.destroy()
    label_instruction.destroy()
    root.configure(bg="blue")
    global label_instruction1,label_Rules,button_start_quiz
    label_instruction1 = Label(root, bg="orange", font=("Comic sans MS ", 30, "bold"),text="INSTRUCTIONS",)
    label_instruction1.pack(pady=(10, 0))

    label_Rules = Label(root,width=100,height=20,background="black",foreground="white",font=("Comic sans MS",17,),text="1.Be wise to your answers.\n"
                                                                                                                       "2.There will be 5 Python programming questions.\n"
                                                                                                                       "3.you will get sufficient time take your full time .\n"
                                                                                                                       "4.Think before choosing answer.,"
                                                                                                                       "clicking on option would make it submit ,So be aware!!!")
    label_Rules.pack()

    button_start_quiz = Button(root, text="START QUIZ ", bg="yellow", activebackground="white", width=14,
                               height=2, font=("Comic sans MS", 15, "bold"),command=start_quiz )
    button_start_quiz.pack(pady=(0, 0))

def start_quiz():
    global label_instruction1, label_Rules, button_start_quiz,quiz
    label_instruction1.destroy()
    label_Rules.destroy()
    button_start_quiz.destroy()
    global newroot
    newroot=Toplevel(root)
    newroot.geometry("2050x790+0+0")
    newroot.config(bg="#00ae9f")
    quiz=Quiz()


def clear():
    global newwindow
    newwindow.destroy()


def enter_roll():

        global newwindow
        newwindow=Toplevel(root)
        newwindow.geometry("400x200+400+280")
        newwindow.config(bg="blue")
        global name_text,roll_text

        label_instruction=Label(newwindow,bg="blue",fg="red",font=("Comic sans MS ", 15, "bold"),text="ROLL NO:")
        label_instruction.place(x=10,y=10)
        roll = tkinter.Entry(newwindow,width="35", textvariable=roll_text)
        roll.place(x=160,y=10)

        label_instruction=Label(newwindow,bg="blue",fg="red",font=("Comic sans MS ", 15, "bold"),text="NAME:     ")
        label_instruction.place(x=10,y=45)
        user = tkinter.Entry(newwindow,width="35", textvariable=name_text)
        user.place(x=160,y=50)

        button_start = Button(newwindow, bg="light green", text="Start", font=("Comic sans MS", 13, "bold"),
                         command=file)
        button_start.place(x=300,y=140)

        button_cancel = Button(newwindow, bg="red", text="Cancel", font=("Comic sans MS", 12, "bold"), command=clear)
        button_cancel.place(x=45,y= 140)

        newwindow.mainloop()

                                        ####### PROGRAM STARTS##########
                                        #######HOME PAGE##########

root = tkinter.Tk()
name_text=tkinter.StringVar()
roll_text =tkinter.StringVar()
root.configure(bg="orange")
root.geometry("2050x790+0+0")

root.title("AB QUIZ")
photo = tkinter.PhotoImage(file = 'prepster-icon.png')
root.iconphoto(True,photo)

image1 = tkinter.PhotoImage(file = 'prepster-icon.png')

label_text = Label(root,fg="blue",text = "LETS QUIZ",font = ("Comic sans MS",56,"bold"),background = "orange")
label_text.pack(pady = (70,0))

label_image = Label(root,bg = "orange",image = image1)
label_image.pack(pady = (100,0))

button_enter = Button(root,text="START >>>",bg="light green",fg="white",activebackground="light green",width=14,height=1,font=("Comic sans MS",20,"bold"),command=enter_roll)
button_enter.pack(pady=(50,0))

label_instruction = Label(root,fg="purple",bg="orange",font=("Comic sans MS ",20,"bold"),text="Life is not a multiple choice test,\n"
                                                                                " it's an open-book essay exam.  ",)
label_instruction.pack(pady=(60,30))

root.mainloop()



