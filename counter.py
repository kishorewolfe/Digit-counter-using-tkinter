from tkinter import *
import time

counter=0
def digit_counter(mylabel):
	counter=0
	def digit():
		global counter
		counter+=1
		mylabel.config(text=str(counter))
		mylabel.after(10,digit)
	digit()
count=Tk()
count.title("Digit Counter")
mylabel=Label(fg="blue",font=100)
mylabel.pack()
digit_counter(mylabel)
btn=Button(text='Close Window',width=50,command=count.destroy)
btn.pack()
count.mainloop()
