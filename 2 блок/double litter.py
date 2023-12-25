a='рассказыsdlfhjsdlfsdlflhhhhfhfhdвать'
def hi(a):
    for i in range(len(a)-1): 
        f=a[i]
        g=a[i+1]
        if f==g:
            print('True')
hi(a)