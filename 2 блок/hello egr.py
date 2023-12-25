a=['egr1','egr2','egr3','egr4','egr5']
def HelloSlave(a):
    for i in range(len(a)):
        c=a[i]
        s='Welcome to the club, '+str(c )
        print(s)
HelloSlave(a)