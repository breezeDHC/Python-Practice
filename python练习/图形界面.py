#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_

from tkinter import *
import  tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    
    def createWidgets(self):
        self.helloLabel = Label(self, text='hello, world')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command = self.quit)
        self.quitButton.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='hello', command=self.hello)
        self.alertButton.pack()
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello,%s' % name)
app = Application()
app.master.title('Hello world')
app.mainloop()
