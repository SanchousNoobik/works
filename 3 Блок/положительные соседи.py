a='+a+b+k+f+s+'
b=[]
o=0
t=1
for i in range (len(a)):
    if a[i]!='+':
        if a[i-1]=='+' and a[i+1]=='+':
            b.append(o)
        else:
            b.append(t)
s=sum(b)
if s==0:
    print('true')
else: 
    print('false')