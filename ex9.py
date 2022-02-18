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
seq0=0
seq1=1
for i in range(len(bin)):
    count1=0
    count0=0
    x = [int(d) for d in str(bin[i])]
    for j in range(len(x)):
        if x[j]==1:
            count1=count1+1
            count0=0
            if count1>seq1:
                seq1=count1
        else:
            count0=count0+1
            count1=0
            if count0>seq0:
                seq0=count0
print("Oi megaluteres akolouthies apo midenika einai: %d" %seq0)
print("Oi megaluteres akolouthies apo asous einai: %d" %seq1)
