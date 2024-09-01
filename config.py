import world

n2t = {"0":"𝟘","1":"𝟙","2":"𝟚","3":"𝟛","4":"𝟜","5":"𝟝","6":"𝟞","7":"𝟟","8":"𝟠","9":"𝟡"}
t2n = {"𝟘":"0","𝟙":"1","𝟚":"2","𝟛":"3","𝟜":"4","𝟝":"5","𝟞":"6","𝟟":"7","𝟠":"8","𝟡":"9"}
stop = 0

preference = ["←","-","→","↙","↓","↘","↖","↑","↗"]

map1 = """
010000001001
000101110100
011000101100
000100001100
010001000001
111111111100
"""

map12 = """
010000001
000101110
011000001
000100101
010001000
"""

space_length = [len(map1.split("\n")[1]),len(map1.split("\n"))-2]
print(map1.split("\n"))
fun = world.World()
fun.init(map1.replace("\n",""))