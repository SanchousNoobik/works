import math
ax=1
bx=1
ay=1
by=2
def triugolnik(ax,bx,ay,by):
    n=math.sqrt(((bx-ax)**2)+((by-ay)**2))
    n=round(n,0)
    print(n)
triugolnik(ax,bx,ay,by)
