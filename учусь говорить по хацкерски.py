a='arcana on pudge'
def pudge(a):
    while 'a' in a:
        a=a.replace('a','4')
    while 'n' in a:
        a=a.replace('n','3')
    print(a)
pudge(a)