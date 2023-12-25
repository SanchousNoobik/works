a=[15, 53, 44]
b=[22, 444, 644]
d=[85, 96, 18]
f=1
u=1
g=1
def korobka(a,b,d,f,g,u):
    for i in a:
        f=f*i
    for i in b:
        u=u*i
    for i in d:
        g=g*i
    v=f+u+g
    print(v)
korobka(a,b,d,f,g,u)