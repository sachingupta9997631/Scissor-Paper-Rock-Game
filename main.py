from tkinter import *
import random

win = Tk()
win.title("Scissor Paper Rock")
win.config(bg="white")
win.geometry("900x600+300+50")
win.iconbitmap("file.ico")

img=PhotoImage(file="1.png")
bg_lab=Label(win,image=img)
bg_lab.pack()
bg_lab.place(x=0,y=0)

##############################################variables declared############################
user=str()
comp=str()
res = str()
sc=0
su=0
score = StringVar()
score.set(str("{} : {}".format(su,sc)))
result =StringVar()
####################################################functions defined##########################

def func(a):
    global su,sc,user,comp,img1,img2,img3,res,result,score
    user = a
    if random.randint(1,3)==1:
        comp = "scissor"
        imag1=Label(win,image=img1,borderwidth=0,bg="#28b4e5")
    elif random.randint(1,3)==1:
        comp = "paper"
        imag1=Label(win,image=img2,borderwidth=0,bg="#28b4e5")
    else:
        comp = "rock"
        imag1=Label(win,image=img3,borderwidth=0,bg="#28b4e5")

    imag1.pack()
    imag1.place(x=705,y=250)

    if comp == "scissor" and user =="scissor":
        res = "Game Draw..."
    elif comp == "scissor" and user =="paper":
        res = "Computer Won..."
        sc+=1
    elif comp == "scissor" and user =="rock":
        res = "User Won..."
        su+=1
    elif comp == "paper" and user =="scissor":
        res = "User Won..."
        su+=1
    elif comp == "paper" and user == "paper":
        res = "Game Draw..."
    elif comp == "paper" and user == "rock":
        res = "Computer Won..."
        sc+=1
    elif comp == "rock" and user =="scissor":
        res = "Computer Won..."
        sc+=1
    elif comp == "rock" and user =="paper":
        res = "User Won..."
        su+=1
    elif comp == "rock" and user =="rock":
        res = "Game Draw..."
    else:
        res=""
        
    score.set(str("{} : {}".format(su,sc)))
    result.set(str(res))

def reset():
    global score,result,sc,su
    sc=0
    su=0
    score.set(str("{} : {}".format(su,sc)))
    result.set("")

###############################################################################################

main_l = Label(win,text="Scissor Paper Rock Game",font=("bahnschrift Semibold",30),bg = "#28b4e5",fg="white")
main_l.pack(pady=5)

img1=PhotoImage(file="2.png")
scissor=Button(win,image=img1,borderwidth=0,bg="#28b4e5",command=lambda: func("scissor"))
scissor.pack()
scissor.place(x=5,y=100)

img2=PhotoImage(file="3.png")
paper=Button(win,image=img2,borderwidth=0,bg="#28b4e5",command=lambda: func("paper"))
paper.pack()
paper.place(x=5,y=250)

img3=PhotoImage(file="4.png")
rock=Button(win,image=img3,borderwidth=0,bg="#28b4e5",command=lambda: func("rock"))
rock.pack()
rock.place(x=5,y=370)


lab1=Label(win,text="Your\nChoice",font=("bahnschrift Semibold",18),bg = "#28b4e5",fg="white")
lab1.pack()
lab1.place(x=35,y=485)

lab2=Label(win,text="Computer's\nChoice",font=("bahnschrift Semibold",18),bg = "#28b4e5",fg="white")
lab2.pack()
lab2.place(x=735,y=485)

#showing the result to the screen
lab3=Label(win,textvariable = result,font=("bahnschrift Semibold",18),bg = "#28b4e5",fg="white")
lab3.pack()
lab3.place(x=380,y=485)

lab4=Label(win,text = "Score",font=("bahnschrift Semibold",18),bg = "#28b4e5",fg="white")
lab4.pack()
lab4.place(x=420,y=400)

score_lab = Label(win,textvariable = score,font=("bahnschrift Semibold",18),bg = "#28b4e5",fg="white")
score_lab.pack()
score_lab.place(x=430,y=430)

res_but = Button(text = "R E S E T", font = ("consolas",12),bg="red",fg="white", command = reset)
res_but.pack()
res_but.place(x=5,y=565)

exit_but = Button(text = "E X I T", font = ("consolas",12),bg="red",fg="white", command = lambda: win.destroy())
exit_but.pack()
exit_but.place(x=820,y=565)

win.mainloop()
