import core, config
import tkinter as tk

def changeL(label,text):
    label.config(text=text)

class Label1(tk.Frame):
    def __init__(self,w,h,tconfig,*args,**kargs):
        super().__init__(*args,**kargs)
        self.elements = []
        self.w = w
        self.h = h
        config = self.config
        self.config = self.config_
        self.config_ = config
        for i in range(h):
            f = tk.Frame(self)
            self.elements.append([])
            for i_ in range(w):
                l = tk.Label(f, **tconfig)
                l.pack(side="left")
                self.elements[-1].append(l)
            f.pack(side="top")
    def config_(self,text="",index=[[0,0]]):
        text = text.replace("\n","")
        if len(text)!=self.h*self.w:
            print()
            raise AssertionError(len(text),"len(text)!=self.h*self.w",text)
        for i in range(self.h):
            for i_ in range(self.w):
                text_ = text[self.w*i+i_]
                background="#fff"
                if [i_,i] in index: background = "#999"
                self.elements[i][i_].config(text=text_,background=background)

def event(obj,space,e):
    #print(e.keycode)
    if config.stop: return 3
    # ["←","-","→","↙","↓","↘","↖","↑","↗"]
    #                     37  38  39  40               49  50    52  53               97  98    100 101
    direction = [0]*1000
    direction[37] = direction[51] = direction[51+48] = "←"
    direction[38] = direction[55] = direction[55+48] = "↑"
    direction[39] = direction[54] = direction[54+48] = "→"
    direction[40] = direction[56] = direction[56+48] = "↓"
    direction[49] = direction[49+48] = "↙"
    direction[50] = direction[50+48] = "↘"
    direction[52] = direction[52+48] = "↖"
    direction[53] = direction[53+48] = "↗"
    direction = direction[e.keycode]
    if direction==0: return 2
    core.forward(obj,space,direction)
    if obj.position==obj.lastIndex: config.stop = 1

def reset(obj,spaceRoot):
    config.stop = 0
    spaceRoot.data[obj.get()][0] = 0
    obj.reset()
    #spaceRoot.set(lambda:[0,config.fun.get()%10])