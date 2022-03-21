import random
def ltn(li):
    l = len(li)
    nu = 0
    for i in range(1,l+1):
        nu = nu + li[i-1]*(10**(4-i))
    return nu
def ntl(nu):
    return list(map(int,str(nu)))
def test(real,inn,car,cbr):
    lis = ntl(real)
    while len(lis) != 4:
            lis.insert(0,0)
    liinn = ntl(inn)
    ca,cb = 0,0
    for i in range(1,5):
        for j in range(1,5):
            if liinn[j-1] == lis[i-1]:
                if i == j :
                    ca += 1
                else :
                    cb += 1
    if ca == int(car) and cb == int(cbr) :
        return 1
    else:
        return 0
relist = list(range(10000))
while True:
    inn = input()
    if inn == 'B' :
        break
    car = input()
    cbr = input()
    brelist = relist.copy()
    l = len(brelist)
    for i in range(l):
        if i == 1000:
            a = 0
        real = relist[i]
        if test(real,inn,car,cbr) == 0:
            relist[i] = 0
for i in range(len(relist)):
    if relist[i] != 0:
        print(relist[i])    
input()