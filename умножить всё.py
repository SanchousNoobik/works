a='1564, 45542, 6664, 7775'
f=1
b=[]
def hi(a,f):
   for i in range(len(a)):
       if a[i]!=" " and a[i]!=",":
           n=int(a[i])
           b.append(n)      
   print(b)   
   for i in b:
       f=f*i
   print(f)
hi(a,f)