from tkinter import *


class Calc():
	def __init__(self,master):
		"""Constructor method"""
		master.title('Calulator') 
		master.geometry()
		self.e = Entry(master)
		self.e.grid(row=0,column=0,columnspan=9,pady=1)
		self.e.focus_set() #Sets focus on the input text area

		self.div='÷'
		#self.newdiv=self.div.decode('utf-8')

		#Generating Buttons
		Button(master,text="=",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
		Button(master,text='AC',width=3,command=lambda:self.clearall()).grid(row=1, column=4)
		Button(master,text='C',width=3,command=lambda:self.clear1()).grid(row=1, column=5)
		Button(master,text="+",width=3,command=lambda:self.action('+')).grid(row=4, column=3)
		Button(master,text="x",width=3,command=lambda:self.action('x')).grid(row=2, column=3)
		Button(master,text="-",width=3,command=lambda:self.action('-')).grid(row=3, column=3)
		Button(master,text="÷",width=3,command=lambda:self.action(self.newdiv)).grid(row=1, column=3) 
		Button(master,text="%",width=3,command=lambda:self.action('%')).grid(row=4, column=2)
		Button(master,text="7",width=3,command=lambda:self.action('7')).grid(row=1, column=0)
		Button(master,text="8",width=3,command=lambda:self.action(8)).grid(row=1, column=1)
		Button(master,text="9",width=3,command=lambda:self.action(9)).grid(row=1, column=2)
		Button(master,text="4",width=3,command=lambda:self.action(4)).grid(row=2, column=0)
		Button(master,text="5",width=3,command=lambda:self.action(5)).grid(row=2, column=1)
		Button(master,text="6",width=3,command=lambda:self.action(6)).grid(row=2, column=2)
		Button(master,text="1",width=3,command=lambda:self.action(1)).grid(row=3, column=0)
		Button(master,text="2",width=3,command=lambda:self.action(2)).grid(row=3, column=1)
		Button(master,text="3",width=3,command=lambda:self.action(3)).grid(row=3, column=2)
		Button(master,text="0",width=3,command=lambda:self.action(0)).grid(row=4, column=0)
		Button(master,text=".",width=3,command=lambda:self.action('.')).grid(row=4, column=1)
		Button(master,text="(",width=3,command=lambda:self.action('(')).grid(row=2, column=4)
		Button(master,text=")",width=3,command=lambda:self.action(')')).grid(row=2, column=5)
		Button(master,text="√",width=3,command=lambda:self.squareroot()).grid(row=3, column=4)
		Button(master,text="x^n",width=3,command=lambda:self.exponent()).grid(row=3, column=5)


	def equals(self):
		return

	def clearall(self):
		return
	def clear1(self):
		return
	def action(self,arg):
		return
	def squareroot(self):
		return
	def exponent(self):
		return

root = Tk()
calc = Calc(root)
root.mainloop()

