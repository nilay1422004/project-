import tkinter
from tkinter import *
from random import randint
root = Tk()

#geometry
root.geometry("500x500")

#title
#background for window
root["bg"]="#264E86"

yscore=0
root.title("project battle")

#ran=randint(0,99)
#number=num_var.set(random.randint(0,99))
def choice(mychoice):
	global yscore
	#ls=["52 Up","52","52 Down"]
	ran=randint(0,99)
	num_var.set(ran)
	#conditions=[ 
	#	ls[ran]=="52 Up" and mychoice <=52,
     #   ls[ran] == "52" and mychoice == 52,
      #  ls[ran] == "52 Down" and mychoice >=52
	#]
	if mychoice=="52 Up" and ran>=52:
		yscore+=1
	elif mychoice=="52" and ran==52:
		yscore+=1
	elif mychoice=="52 Down" and ran<=52:
		yscore+=1
	else:
		yscore+=0
	score_var.set(yscore)






boder_frame = Frame(root,width=480, height=20 ,bg="#5E88FC")
boder_frame.pack(padx=5,pady=10)

home =Label( boder_frame,text="52 Up / 52 Down",font=("Times New Roman",30),bg="#74DBEF")
home.pack(padx=5,pady=5)

frame1 = Frame(root,width=480, height=40 ,bg="#5E88FC")
frame1.pack(padx=5,pady=10)

#\nyou need to bet out of the following options \nif the displayed number matches your condition then you get a point "

rule =Label(frame1,text="rules:",font=("Times New Roman",10),bg="#74DBEF")
rule.pack(padx=5,pady=5,side =LEFT,anchor="w")

rule1=Label(frame1,text="you need to bet out of the following options \nif the displayed number matches your condition then you get a point ",font=("Times New Roman",10),bg="#74DBEF")
rule1.pack(padx=5,pady=5,side =LEFT,anchor="w")
'''
grade_label = Label(frame2, text="Grade", width=20,bg="#fce2d7")
grade_label.grid(row=5, column=0,padx=35,pady=10)

grade_var=StringVar()
grade_label_value_display = Label(frame2, width=20,textvariable=grade_var,bg="#fce2d7")
grade_label_value_display.grid(row=5, column=1,padx=35,pady=10)
'''
num_frame=Frame(root,width=480, height=40 ,bg="#5E88FC")
num_frame.pack(padx=5,pady=10)

num_var=IntVar()
num_display = Label(num_frame, width=25,height=2,textvariable=num_var,bg="#fce2d7")
num_display.pack(padx=5,pady=10)

button_frame=Frame(root,width=480, height=50 ,bg="#5E88FC")
button_frame.pack(padx=5,pady=10)

up_button = Button(button_frame,text="52 Up",width=20,command=lambda:choice("52 Up"))
up_button.grid(row=0, column=1,padx=5,pady=10)

jackpot_button = Button(button_frame,text="52",width=20,command=lambda:choice("52"))
jackpot_button.grid(row=0, column=2,padx=5,pady=10)

down_button = Button(button_frame,text="52 Down",width=20,command=lambda:choice("52 Down"))
down_button.grid(row=0, column=3,padx=5,pady=10)

#score_frame=Frame(root,width=480, height=50 ,bg="#5E88FC")

#score
score = Label(root)
score.configure(text="Score:",font=("Times New Roman",10),bg="#65d2fe",fg="#004220")
score.place(x=60,y=300)


#my score 
your_score=Label(root,text="your score:-",font=("Times New Roman",20),bg="#65d2fe",fg="#004220")
your_score.place(x=100,y=345)

'''
score_var=IntVar()
score_display=Label(root,text=score_var,bg="#65d2fe")
score_display.place(x=270,y=350)

'''
score_var=IntVar()
score_display = Label(root, width=25,height=2,textvariable=score_var,bg="#fce2d7")
score_display.place(x=270,y=345)















































































root.mainloop()