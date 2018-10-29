import os
from tweetHashtagPuller import hashAnalysis

class hashtag (object):
    def __init__(self,has):
        self.exists = True
        self.output = ''
        self.hash = has
    def name(self):
        return self.hash   
    def __str__(self):
        return self.output

from tkinter import Tk, Label, Frame, Entry, Button
from tkinter.messagebox import showinfo
class ui(Tk):
    def __init__(self,parent=None):
        Tk.__init__(self,parent)
        self.title('Personality Analysis')
        self.make_widgets()
    def calc_reponse(self):
        self.tweet = hashtag(self.hashT.get())
        if(str(self.hashT.get())[:1] != '#'):
            showinfo(message = str(self.hashT.get())+' is not a valid hashtag'+ str(self.tweet))
        else:
            hashAnalysis(str(self.hashT.get()))
    def make_widgets(self):
        Label(self, text='Hashtag to search:',width=40).pack()
        self.hashT = Entry(self, width = 40)
        self.hashT.pack()
        Button(self,text='Submit', command=lambda:self.calc_reponse()).pack()
                
ui().mainloop()
