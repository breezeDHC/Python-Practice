#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.weightLabel = Label(self, text='体重(kg)')
        self.weightLabel.pack()
        self.weightInput = Entry(self)
        self.weightInput.pack()
        self.heightLabel = Label(self, text='身高(cm)')
        self.heightLabel.pack()
        self.heightInput = Entry(self)
        self.heightInput.pack()
        self.alertButton = Button(self, text='result',command=self.result)
        self.alertButton.pack()

    def result(self):
        weight = int(self.weightInput.get())
        height = int(self.heightInput.get())
        height = height/100
        BMI = weight/(height*height)
        if BMI < 18.5:
            messagebox.showinfo('BMI指数','BMI: %.2f  您的体重过轻' % BMI)
        elif BMI < 24:
            messagebox.showinfo('BMI指数','BMI: %.2f  您的体重正常' % BMI)
        elif BMI < 28:
            messagebox.showinfo('BMI指数','BMI: %.2f  您的体重过重' % BMI)
        elif BMI < 32:
            messagebox.showinfo('BMI指数','BMI: %.2f  您的体重肥胖' % BMI)
        else:
            messagebox.showinfo('BMI指数','BMI: %.2f  您的体重非常胖' % BMI)


app = Application()
app.master.title('BMI')
app.mainloop()
