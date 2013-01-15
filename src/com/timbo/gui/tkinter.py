# -*- coding: utf-8 -*-
'''
Created on 2013-1-14

@author: Administrator
'''
import Tkinter

class App(object):
    def __init__(self, master):
        frame = Tkinter.Frame(master)
        frame.pack()
        
        self.hello = Tkinter.Button(frame, text="Hello",
            command=self.hello)
        self.hello.pack(side=Tkinter.LEFT)
        
        self.quit = Tkinter.Button(frame, text="Quit",
            fg="red", command=frame.quit())
        self.quit.pack(side=Tkinter.RIGHT)
        
    def hello(self):
        print "Hello, World!"
        
root = Tkinter.Tk()
root.wm_title("Hello")
root.wm_minsize(200, 200)

app = App(root)
root.mainloop()