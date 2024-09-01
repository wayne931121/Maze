import tkinter as tk
import threading
import core, config
from uitools import *
from object_2d import object_2d, character_2d

# [[0,?],[symbol of c,?],[0,?],[0,?]...]
w,h = space_length = config.space_length
spaceRoot = object_2d(*space_length, lambda:[0,config.fun.get()%10])

c1 = character_2d("●",*space_length,power=18,position=[0,0],near_=config.preference)
c1.lastIndex = [space_length[0]-1,space_length[1]-1]
objects = [c1]

root = tk.Tk()
root.geometry("1002x702")
root.tk.call('tk', 'scaling', 3)
frame = tk.Frame(root)
frame1 = tk.Frame(root)

label = tk.Label(frame, text="1", padx=10, pady=10,font=('Helvetica', 15))
label1 = Label1(w,h,{"padx":-100, "pady":0,"font":('Helvetica', 13),"width":0}, frame, background=None)
label2 = tk.Label(frame1, text="--", padx=10, pady=10,font=('Helvetica', 15))
label3 = tk.Label(frame1, text="--", padx=10, pady=10,font=('Helvetica', 15))
label4 = tk.Label(frame1, text="--", padx=10, pady=10,font=('Helvetica', 15))
b1 = tk.Button(frame1, text="重置", padx=10, pady=10,font=('Helvetica', 15),command=lambda:reset(c1,spaceRoot))

label.pack(side="top")
label1.pack(side="top")
label2.pack(side="top")
#label3.pack(side="top")
#label4.pack(side="top")
b1.pack(side="top")
["←","-","→","↙","↓","↘","↖","↑","↗"]
frame.place(relx=0,y=0,relwidth=0.5)
frame1.place(relx=0.5,y=0,relwidth=0.5)
spaceRoot,""

root.bind("<KeyPress>",lambda e:event(c1,spaceRoot.data,e))
core.update(root,objects,spaceRoot,label,label1,label2,label3,label4)
root.mainloop()