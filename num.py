from ast import While
import random
def ltn(li):
    l = len(li)
    nu = 0
    for i in range(1,l+1):
        nu = nu + li[i-1]*(10**(4-i))
    return nu
def ntl(nu):
    return list(map(int,str(nu)))
def remake(drl):
    for j in range(1,4):
        for i in range(j,4):
            while drl[j-1] == drl[i]:
                drl[i] = random.randint(1,9)
    return drl
lis = []
for i in range(1,5):
    lis.append(random.randint(1,9))
real = ltn(remake(lis))
inn = input()
step = 0
while int(inn) != real :
    liinn = ntl(inn)
    ca,cb = 0,0
    for i in range(1,5):
        for j in range(1,5):
            if liinn[j-1] == lis[i-1]:
                if i == j :
                    ca += 1
                else :
                    cb += 1
    step = step + 1
    print(ca,"A",cb,"B"," ",step)
    inn = input()
print("4 A")
