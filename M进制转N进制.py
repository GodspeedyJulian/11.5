def basetra(b):
    if b =="A":
        return 10
    elif b == "B":
        return 11
    elif b=="C":
        return 12
    elif b=="D":
        return 13
    elif b=="E":
        return 14
    elif b=="F":
        return 15
    else:
        return b
while True:
    M=int(input("input the base transfer from: "))
    N=int(input("input the base transfer to: "))
    if 2<=N <=16 and 2<=M <=16:
        break
a=input("input the number: ")
a10=0
for i in range (len(a)):
    a10 += basetra(a[i])* (M**(len(a)-i))
index=0
while True :
    
    if a10 >= N**index:
        index+=1
    else:
        break
aN=""
for i in range (index+1):
    aN+=str(a10//N**index)
    a10= a10%N**index
    i-=1
print(aN)
