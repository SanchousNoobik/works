a=[0,5,4,6,110,82]
o=0
def hi(a,o):
    for i in range(len(a)-1):
        if a[i]<a[i+1]:
            o=o+1
    if o>=(len(a)-1):
        print('возрастаит')
    else:
        print('не возрастаит')
hi(a,o)