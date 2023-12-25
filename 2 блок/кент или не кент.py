a=['кент1','кент2','кент3','impostor']
b=['impostor']
c=[]
for i in range (len(a)):
    t= a[i]
    for y in range (len(b)):
        r=b[y]
        if t!=r:
            c.append(t)
print(c)

    