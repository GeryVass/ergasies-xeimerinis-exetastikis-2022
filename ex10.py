def MtoBinary(a):
    l,m=[],[]
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m

#se periptswsh pou xreiazetai na graftei kwdikas ascii:
#input("Enter ASCII characters:") 

#se periptswsh pou xreiazetai na eisagete arxeio me kwdika ascii:
file=open("two_cities_ascii.txt", "r")
txt=file.read()
bin=MtoBinary(txt)
dgts=[]
for i in range(len(bin)):
    x=[int(d) for d in str(bin[i])]
    while len(x) < 7:
        x.insert(0, 0)
    dgts.append(x)
print(dgts)
for i in range(len(dgts)):
    dgts[i] = dgts[i][0], dgts[i][1], dgts[i][5], dgts[i][6]
print(dgts)