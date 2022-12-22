import math
for x in range(0,360,15):
    d=math.sin(x*3.14/180)
    e=math.cos(x*3.14/180)
    print(str(x)+"---" + str(round(d,4))+str(round(e,4)))
