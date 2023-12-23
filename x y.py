a=[1,2,3,4]
b=[5,6,7,8]
c=[]
def egr(a,b,c):
    for i in range (len(a)):
        h = a[i]
        k = b[i]
        g = str(h)+';'+str(k)
        c.append(g)
    print(c) 
egr(a,b,c)    
