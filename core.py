import config

def forward(obj,space,direction): #Here direction is symbol!!!
    #per item in space: [symbol,value], obj是主角，space是包含空間一系列的座標陣列，spaceIndex是空間座標
    oldIndex = obj.get()
    newIndex = obj.forward_(direction)
    if newIndex[0]==None or newIndex[1]==None or space[obj.index(*newIndex)][1]>=1 or newIndex==oldIndex: return None
    
    obj.position = newIndex
    
    space[obj.get()][0] = obj.symbol
    space[oldIndex][0] = 0
    
    #obj.power += 1
    #space[newIndex][1]-=1
    
    return True

def get_1d(spaceRoot,position_2d): #position_2d is [c,r] aka [w,h]
    space = spaceRoot.data
    if None in position_2d: return [None,None]
    spaceIndex = spaceRoot.index(position_2d[0],position_2d[1]) #2d to 1d index
    value = space[spaceIndex][1]
    return [spaceIndex,value]

def prettyPrint(e):
    return str(e[0])

def prettyPrint_(e):
    if e[1]>9:return "a"
    return str(e[1])

def update(root,c,spaceRoot,*labels):
    index = [c1.position for c1 in c]+[c[0].lastIndex]
    texts = [spaceRoot.print(prettyPrint,index,"●"),spaceRoot.print(prettyPrint_),0,c[0].power]
    labels[0].config(text=texts[0])
    labels[1].config(text=texts[1],index=index)
    #labels[3].config(text=texts[3])
    if config.stop: labels[2].config(text="你贏了")
    else: labels[2].config(text="--")
    root.after(10,update,root,c,spaceRoot,*labels)