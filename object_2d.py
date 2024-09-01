class object_2d:
    def __init__(self,width,height,initfun=lambda:0,*initargs):
        self.data = [initfun(*initargs) for i in range(width*height)]
        self.width = width
        self.height = height
    def index(self,column,row):
        return row*self.width+column
    def print(self,pretty=lambda x:str(x), index=[[None,None]], symbol=""):
        s = ""
        for r in range(self.height):
            for c in range(self.width):
                p = self.index(c,r)
                t = pretty(self.data[p])
                if [c,r] in index: t=symbol
                s += t
            s+="\n"
        return s
    def set(self,initfun=lambda:0,*initargs):
        self.data = [initfun(*initargs) for i in range(self.width*self.height)]

class character_2d:
    def __init__(self,symbol,width,height,power=8,position=[0,0],near_=["-"]):
        #                w,h
        self.position = [0,0]
        self.width = width
        self.height = height
        self.symbol = symbol
        # symbol:[left,right,up,down]
        self.near_search = {"↖":[1,0,1,0],
                            "↑":[0,0,1,0],
                            "↗":[0,1,1,0],
                            "←":[1,0,0,0],
                            "-":[0,0,0,0],
                            "→":[0,1,0,0],
                            "↙":[1,0,0,1],
                            "↓":[0,0,0,1],
                            "↘":[0,1,0,1]}
        self.near_ = ["↖","↑","↗","←","-","→","↙","↓","↘"]
        
        #self.life = 9
        self.power = power
        self.position = position
        self.near_ = near_
        self.original = position
        return None
    def index(self,c,r):
        return self.width*r+c
    def get(self):
        return self.index(self.position[0],self.position[1])
    def set(self,c,r):
        self.position = [c,r]
    def add(self,v,lastIndex,return_=0):
        if v==lastIndex: return return_
        return v+1
    def nadd(self,v,lastIndex,return_="last"):
        if v==0 and return_=="last": return lastIndex
        if v==0: return return_
        return v-1
    def forward_(self,direction):#direction:"↖","↑","↗",symbols...
        left,right,up,down = self.near_search[direction]
        if left and right:
            left = 0
            right = 0
        if up and down:
            up = 0
            down = 0
        c = self.position[0]; r = self.position[1];
        lw = self.width-1; lh = self.height-1;
        add = self.add; nadd = self.nadd;
        if left:c=nadd(c,lw,None)
        if right: c=add(c,lw,None)
        if up: r=nadd(r,lh,None)
        if down: r=add(r,lh,None)
        return [c,r]
    def forward(self,direction_index):
        ##print(self.position)
        # [left,right,up,down]
        direction = self.get_direction(direction_index)
        self.position = self.forward_(direction)
        ##print(*direction)
        ##print(self.position)
        return self.get()
    def near(self):
        return [self.forward_(i) for i in self.near_] #[[c,r],[c,r]...] aka [[w,h],...]
    def get_direction(self,index):
        return self.near_[index]
    def reset(self):
        self.position = self.original

if __name__=="__main__":
    from cycle import cycle
    a2d = object_2d(9,4,lambda x:[0,cycle(1,2,1)],3)
    a2d.data[0][1].add()
    a2d.print(lambda x:str(x[0])+str(x[1])+" ")
    b2d = object_2d(9,4,lambda:1)
    b2d.print()
    #0  1  2  3  4  5  6  7  8
    #9 10 11 12 13 14 15 16 17
    cd2d = character_2d(None,9,2)
    print(cd2d.get())
    print(cd2d.forward_(0,1,1,0))