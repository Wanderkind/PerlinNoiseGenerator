
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

################

while True:
    S = input('\nInput Seed from 0 to 18,446,744,073,709,551,615 (20 digits) or "R" for random : ')
    
    if str(S) == 'R' or str(S) == 'r' or str(S) == 'ㄱ':
        Seed = random.randrange(0, 18446744073709551616)
        print('Seed =', Seed)
        break
    
    else:
        if int(S) < 0 or 18446744073709551615 < int(S):
            S = input('\nInput Seed from 0 to 18,446,744,073,709,551,615 (20 digits) or "R" for random : ')
            continue
        
        else:
            Seed = int(S)
            print('Seed =', Seed)
            break

Sb = str(bin(Seed)[2:].zfill(64))

def prime(a):
    
    if a < 2:
        return False
    
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0 :
            return False
    
    return True

n = 23
P = []
while True:
    
    if prime(n) == False:
        n += 1
    else:
        P.append(n)
        n += 1
        continue
    
    if len(P) == 256:
        break

x = 0
for i in range(64):
        
    if int(Sb[63 - i]) == 1:
        x += P[((2*Seed + 1)*i)%256]
    
    else:
        x += P[((2*Seed + 9)*(i + 26))%256]

    if int(Sb[i]) == 1:
        x += P[((2*Seed + 5)*(i + 79))%256]

    else:
        x += P[((2*Seed + 13)*(i + 168))%256]

d0 = 0
for u in range(len(str(Seed))):
    b0 = int(str(Seed)[u])
    d0 += b0

d1 = 0
for u in range(len(str(Seed))):
    b1 = int(str(Seed)[u])
    d1 += (2*u + 1)*b1

d2 = 0
for u in range(len(str(Seed))):
    b2 = int(str(Seed)[u])
    d2 += ((-1)**u)*(b2 + u + 2)*b2

d3 = 0
for u in range(len(str(Seed))):
    b3 = int(str(Seed)[u])
    d3 += (u + 3)*(b3//(((13*b3)%11)%5 + 2))

d4 = 0
for u in range(len(str(Seed))):
    b4 = int(str(Seed)[u])
    d4 += (u**3 + 6*u + (b4%23) + 4)*b4

ld = [d0, d1, d2, d3, d4]
Ld = []

for i in range(4, -1, -1):
    k = (Seed%math.factorial(i + 1))//math.factorial(i)
    Ld.append(ld[k])
    del ld[k]

D0 = Ld[0] + Ld[1] + Ld[2] + Ld[3] + Ld[4]
D1 = Ld[0]**3 + Ld[1] + Ld[2] + Ld[3] + Ld[4] + 1
D2 = (Ld[0] + Ld[1])**3 + Ld[2] + Ld[3] + Ld[4] + 2
D3 = (Ld[0] + Ld[1] + Ld[2])**3 + Ld[3] + Ld[4] + 3
D4 = (Ld[0] + Ld[1] + Ld[2] + Ld[3])**3 + Ld[4] + 4
X = round(D0*math.sqrt(abs(D1))) + x

lD = [D0, D1, D2, D3, D4]
LD = []

for i in range(4, -1, -1):
    k = ((Seed + X)%math.factorial(i + 1))//math.factorial(i)
    LD.append(lD[k])
    del lD[k]

################

L64 = []
for i in range(64):

    Lm = []
    Lm.append(P[LD[(4*i)%5]%(256 - 4*i)])
    del P[LD[(4*i)%5]%(256 - 4*i)]
    
    for j in range(1, 4):
        
        Lm.append(P[LD[(4*i + j)%5]%(256 - 4*i - j)])
        del P[LD[(4*i + j)%5]%(256 - 4*i - j)]
    
    L64.append(Lm)

LLa = []
for i in range(64):
    
    Sum = 0
    for j in range(4):
        Sum += (X/L64[i][j])
    
    LLa.append(100*Sum + Seed%X)

LLav = []
for i in range(64):
    x = math.cos(math.radians(LLa[i]))
    y = math.sin(math.radians(LLa[i]))
    LLav.append([x, y])

def fa(x, y):
    
    if 0 <= x <= 7 and 0 <= y <= 7:
        
        x0 = math.floor(x)
        x1 = math.ceil(x)
        y0 = math.floor(y)
        y1 = math.ceil(y)
        
        s = np.dot(np.array(LLav[x0 + 8*y0]), np.array([x - x0, y - y0]))
        t = np.dot(np.array(LLav[x1 + 8*y0]), np.array([x - x1, y - y0]))
        u = np.dot(np.array(LLav[x0 + 8*y1]), np.array([x - x0, y - y1]))
        v = np.dot(np.array(LLav[x1 + 8*y1]), np.array([x - x1, y - y1]))
        
        a = s + (t - s)*(6*((x - x0)**5) - 15*((x - x0)**4) + 10*((x - x0)**3))
        b = u + (v - u)*(6*((x - x0)**5) - 15*((x - x0)**4) + 10*((x - x0)**3))
        
        c = a + (b - a)*(6*((y - y0)**5) - 15*((y - y0)**4) + 10*((y - y0)**3))
        
        return math.sqrt(2)*c

################

n = 23
while True:
    
    if prime(n) == False:
        n += 1
    else:
        P.append(n)
        n += 1
        continue
    
    if len(P) == 256:
        break

L16 = []
for i in range(16):

    Lm = []
    Lm.append(P[LD[(16*i)%5]%(256 - 16*i)])
    del P[LD[(16*i)%5]%(256 - 16*i)]
    
    for j in range(1, 16):
        
        Lm.append(P[LD[(16*i - j)%5]%(256 - 16*i - j)])
        del P[LD[(16*i - j)%5]%(256 - 16*i - j)]
        
    L16.append(Lm)

LLb = []
for i in range(16):
    
    Sum = 0
    for j in range(16):
        Sum += (X/L16[i][j])
    
    LLb.append(100*Sum + Seed%X)

LLbv = []
for i in range(16):
    x = math.cos(math.radians(LLb[i]))
    y = math.sin(math.radians(LLb[i]))
    LLbv.append([x, y])

def fb(x, y):
    
    if 0 <= x <= 3 and 0 <= y <= 3:
        
        x0 = math.floor(x)
        x1 = math.ceil(x)
        y0 = math.floor(y)
        y1 = math.ceil(y)
        
        s = np.dot(np.array(LLbv[x0 + 4*y0]), np.array([x - x0, y - y0]))
        t = np.dot(np.array(LLbv[x1 + 4*y0]), np.array([x - x1, y - y0]))
        u = np.dot(np.array(LLbv[x0 + 4*y1]), np.array([x - x0, y - y1]))
        v = np.dot(np.array(LLbv[x1 + 4*y1]), np.array([x - x1, y - y1]))

        a = s + (t - s)*(6*((x - x0)**5) - 15*((x - x0)**4) + 10*((x - x0)**3))
        b = u + (v - u)*(6*((x - x0)**5) - 15*((x - x0)**4) + 10*((x - x0)**3))
        
        c = a + (b - a)*(6*((y - y0)**5) - 15*((y - y0)**4) + 10*((y - y0)**3))
        
        return math.sqrt(2)*c

################

Va = []
for x in range(351):
    v = []
    for y in range(351):
        v.append(fa(0.02*x, 0.02*y))
    Va.append(v)

Maxa = []
mina = []
for x in range(1, 350):
    for y in range(1, 350):
    
        v = [Va[x][y], Va[x + 1][y], Va[x + 1][y + 1], Va[x][y + 1], Va[x - 1][y + 1], Va[x - 1][y], Va[x - 1][y - 1], Va[x][y - 1], Va[x + 1][y - 1]]
        
        if max(v) == Va[x][y]:
            Maxa.append([x/50, y/50])
        
        if min(v) == Va[x][y]:
            mina.append([x/50, y/50])

LMa = len(Maxa)
Lma = len(mina)

Vb = []
for x in range(151):
    v = []
    for y in range(151):
        v.append(fb(0.02*x, 0.02*y))
    Vb.append(v)

Maxb = []
minb = []
for x in range(1, 150):
    for y in range(1, 150):
    
        v = [Vb[x][y], Vb[x + 1][y], Vb[x + 1][y + 1], Vb[x][y + 1], Vb[x - 1][y + 1], Vb[x - 1][y], Vb[x - 1][y - 1], Vb[x][y - 1], Vb[x + 1][y - 1]]
        
        if max(v) == Vb[x][y]:
            Maxb.append([x/50, y/50])
        
        if min(v) == Vb[x][y]:
            minb.append([x/50, y/50])

LMb = len(Maxb)
Lmb = len(minb)

################

Maxa1S = []
Maxa1S.append(Maxa)

count = 0
while True:
    
    temp = []
    for i in range(LMa):
        
        if Maxa1S[count][i] != ['drop']:
            
            l9 = [
            [Maxa1S[count][i][0], Maxa1S[count][i][1]],
            [round(Maxa1S[count][i][0] + 0.004, 3), Maxa1S[count][i][1]],
            [round(Maxa1S[count][i][0] + 0.004, 3), round(Maxa1S[count][i][1] + 0.004, 3)],
            [Maxa1S[count][i][0], round(Maxa1S[count][i][1] + 0.004, 3)],
            [round(Maxa1S[count][i][0] - 0.004, 3), round(Maxa1S[count][i][1] + 0.004, 3)],
            [round(Maxa1S[count][i][0] - 0.004, 3), Maxa1S[count][i][1]],
            [round(Maxa1S[count][i][0] - 0.004, 3), round(Maxa1S[count][i][1] - 0.004, 3)],
            [Maxa1S[count][i][0], round(Maxa1S[count][i][1] - 0.004, 3)],
            [round(Maxa1S[count][i][0] + 0.004, 3), round(Maxa1S[count][i][1] - 0.004, 3)]]
            
            v = []
            for j in range(9):
                v.append(fa(l9[j][0], l9[j][1]))
            
            co = l9[v.index(max(v))]
            
            if 0 not in co and 7 not in co:
                temp.append(co)
            
            else:
                temp.append(['drop'])
        
        else:
            LMa -= 1
    
    Maxa1S.append(temp)
    
    count += 1
    
    if Maxa1S[count - 1] == Maxa1S[count]:
        break
    
    else:
        continue

Maxa1 = []
[Maxa1.append(x) for x in Maxa1S[count] if x not in Maxa1]
LMaxa1 = len(Maxa1)

################

mina1S = []
mina1S.append(mina)

count = 0
while True:
    
    temp = []
    for i in range(Lma):
        
        if mina1S[count][i] != ['drop']:
        
            l9 = [
            [mina1S[count][i][0], mina1S[count][i][1]],
            [round(mina1S[count][i][0] + 0.004, 3), mina1S[count][i][1]],
            [round(mina1S[count][i][0] + 0.004, 3), round(mina1S[count][i][1] + 0.004, 3)],
            [mina1S[count][i][0], round(mina1S[count][i][1] + 0.004, 3)],
            [round(mina1S[count][i][0] - 0.004, 3), round(mina1S[count][i][1] + 0.004, 3)],
            [round(mina1S[count][i][0] - 0.004, 3), mina1S[count][i][1]],
            [round(mina1S[count][i][0] - 0.004, 3), round(mina1S[count][i][1] - 0.004, 3)],
            [mina1S[count][i][0], round(mina1S[count][i][1] - 0.004, 3)],
            [round(mina1S[count][i][0] + 0.004, 3), round(mina1S[count][i][1] - 0.004, 3)]]
            
            v = []
            for j in range(9):
                v.append(fa(l9[j][0], l9[j][1]))
            
            co = l9[v.index(min(v))]
            
            if 0 not in co and 7 not in co:
                temp.append(co)
            
            else:
                temp.append(['drop'])
        
        else:
            Lma -= 1
    
    mina1S.append(temp)
    
    count += 1
    
    if mina1S[count - 1] == mina1S[count]:
        break
    
    else:
        continue

mina1 = []
[mina1.append(x) for x in mina1S[count] if x not in mina1]
Lmina1 = len(mina1)

################

Maxb1S = []
Maxb1S.append(Maxb)

count = 0
while True:
    
    temp = []
    for i in range(LMb):
        
        if Maxb1S[count][i] != ['drop']:
            
            l9 = [
            [Maxb1S[count][i][0], Maxb1S[count][i][1]],
            [round(Maxb1S[count][i][0] + 0.004, 3), Maxb1S[count][i][1]],
            [round(Maxb1S[count][i][0] + 0.004, 3), round(Maxb1S[count][i][1] + 0.004, 3)],
            [Maxb1S[count][i][0], round(Maxb1S[count][i][1] + 0.004, 3)],
            [round(Maxb1S[count][i][0] - 0.004, 3), round(Maxb1S[count][i][1] + 0.004, 3)],
            [round(Maxb1S[count][i][0] - 0.004, 3), Maxb1S[count][i][1]],
            [round(Maxb1S[count][i][0] - 0.004, 3), round(Maxb1S[count][i][1] - 0.004, 3)],
            [Maxb1S[count][i][0], round(Maxb1S[count][i][1] - 0.004, 3)],
            [round(Maxb1S[count][i][0] + 0.004, 3), round(Maxb1S[count][i][1] - 0.004, 3)]]
            
            v = []
            for j in range(9):
                v.append(fb(l9[j][0], l9[j][1]))
            
            co = l9[v.index(max(v))]
            
            if 0 not in co and 3 not in co:
                temp.append(co)
            
            else:
                temp.append(['drop'])
        
        else:
            LMb -= 1
    
    Maxb1S.append(temp)
    
    count += 1
    
    if Maxb1S[count - 1] == Maxb1S[count]:
        break
    
    else:
        continue

Maxb1 = []
[Maxb1.append(x) for x in Maxb1S[count] if x not in Maxb1]
LMaxb1 = len(Maxb1)

################

minb1S = []
minb1S.append(minb)

count = 0
while True:
    
    temp = []
    for i in range(Lmb):
        
        if minb1S[count][i] != ['drop']:
            
            l9 = [
            [minb1S[count][i][0], minb1S[count][i][1]],
            [round(minb1S[count][i][0] + 0.004, 3), minb1S[count][i][1]],
            [round(minb1S[count][i][0] + 0.004, 3), round(minb1S[count][i][1] + 0.004, 3)],
            [minb1S[count][i][0], round(minb1S[count][i][1] + 0.004, 3)],
            [round(minb1S[count][i][0] - 0.004, 3), round(minb1S[count][i][1] + 0.004, 3)],
            [round(minb1S[count][i][0] - 0.004, 3), minb1S[count][i][1]],
            [round(minb1S[count][i][0] - 0.004, 3), round(minb1S[count][i][1] - 0.004, 3)],
            [minb1S[count][i][0], round(minb1S[count][i][1] - 0.004, 3)],
            [round(minb1S[count][i][0] + 0.004, 3), round(minb1S[count][i][1] - 0.004, 3)]]
            
            v = []
            for j in range(9):
                v.append(fb(l9[j][0], l9[j][1]))
            
            co = l9[v.index(min(v))]
            
            if 0 not in co and 3 not in co:
                temp.append(co)
            
            else:
                temp.append(['drop'])
        
        else:
            Lmb -= 1
    
    minb1S.append(temp)
    
    count += 1
    
    if minb1S[count - 1] == minb1S[count]:
        break
    
    else:
        continue

minb1 = []
[minb1.append(x) for x in minb1S[count] if x not in minb1]
Lminb1 = len(minb1)

################

Maxa2S = []
Maxa2S.append(Maxa1)

count = 0
while True:
    
    temp = []
    for i in range(LMaxa1):
        
        if Maxa2S[count][i] != ['drop']:
            
            l9 = [
            [Maxa2S[count][i][0], Maxa2S[count][i][1]],
            [round(Maxa2S[count][i][0] + 0.0008, 4), Maxa2S[count][i][1]],
            [round(Maxa2S[count][i][0] + 0.0008, 4), round(Maxa2S[count][i][1] + 0.0008, 4)],
            [Maxa2S[count][i][0], round(Maxa2S[count][i][1] + 0.0008, 4)],
            [round(Maxa2S[count][i][0] - 0.0008, 4), round(Maxa2S[count][i][1] + 0.0008, 4)],
            [round(Maxa2S[count][i][0] - 0.0008, 4), Maxa2S[count][i][1]],
            [round(Maxa2S[count][i][0] - 0.0008, 4), round(Maxa2S[count][i][1] - 0.0008, 4)],
            [Maxa2S[count][i][0], round(Maxa2S[count][i][1] - 0.0008, 4)],
            [round(Maxa2S[count][i][0] + 0.0008, 4), round(Maxa2S[count][i][1] - 0.0008, 4)]]
            
            v = []
            for j in range(9):
                v.append(fa(l9[j][0], l9[j][1]))
            
            co = l9[v.index(max(v))]
            
            if 0 not in co and 7 not in co:
                temp.append(co)
            
            else:
                temp.append(['drop'])
        
        else:
            LMaxa1 -= 1
    
    Maxa2S.append(temp)
    
    count += 1
    
    if Maxa2S[count - 1] == Maxa2S[count]:
        break
    
    else:
        continue

Maxa2 = []
[Maxa2.append(x) for x in Maxa2S[count] if x not in Maxa2]
LMaxa2 = len(Maxa2)

################

mina2S = []
mina2S.append(mina1)

count = 0
while True:
    
    temp = []
    for i in range(Lmina1):
        
        if mina2S[count][i] != ['drop']:
            
            l9 = [
            [mina2S[count][i][0], mina2S[count][i][1]],
            [round(mina2S[count][i][0] + 0.0008, 4), mina2S[count][i][1]],
            [round(mina2S[count][i][0] + 0.0008, 4), round(mina2S[count][i][1] + 0.0008, 4)],
            [mina2S[count][i][0], round(mina2S[count][i][1] + 0.0008, 4)],
            [round(mina2S[count][i][0] - 0.0008, 4), round(mina2S[count][i][1] + 0.0008, 4)],
            [round(mina2S[count][i][0] - 0.0008, 4), mina2S[count][i][1]],
            [round(mina2S[count][i][0] - 0.0008, 4), round(mina2S[count][i][1] - 0.0008, 4)],
            [mina2S[count][i][0], round(mina2S[count][i][1] - 0.0008, 4)],
            [round(mina2S[count][i][0] + 0.0008, 4), round(mina2S[count][i][1] - 0.0008, 4)]]
            
            v = []
            for j in range(9):
                v.append(fa(l9[j][0], l9[j][1]))
            
            co = l9[v.index(min(v))]
            
            if 0 not in co and 7 not in co:
                temp.append(co)
            
            else:
                temp.append(['drop'])
        
        else:
            Lmina1 -= 1
    
    mina2S.append(temp)
    
    count += 1
    
    if mina2S[count - 1] == mina2S[count]:
        break
    
    else:
        continue

mina2 = []
[mina2.append(x) for x in mina2S[count] if x not in mina2]
Lmina2 = len(mina2)

################

Maxb2S = []
Maxb2S.append(Maxb1)

count = 0
while True:
        
    temp = []
    for i in range(LMaxb1):
        
        if Maxb2S[count][i] != ['drop']:
            
            l9 = [
            [Maxb2S[count][i][0], Maxb2S[count][i][1]],
            [round(Maxb2S[count][i][0] + 0.0008, 4), Maxb2S[count][i][1]],
            [round(Maxb2S[count][i][0] + 0.0008, 4), round(Maxb2S[count][i][1] + 0.0008, 4)],
            [Maxb2S[count][i][0], round(Maxb2S[count][i][1] + 0.0008, 4)],
            [round(Maxb2S[count][i][0] - 0.0008, 4), round(Maxb2S[count][i][1] + 0.0008, 4)],
            [round(Maxb2S[count][i][0] - 0.0008, 4), Maxb2S[count][i][1]],
            [round(Maxb2S[count][i][0] - 0.0008, 4), round(Maxb2S[count][i][1] - 0.0008, 4)],
            [Maxb2S[count][i][0], round(Maxb2S[count][i][1] - 0.0008, 4)],
            [round(Maxb2S[count][i][0] + 0.0008, 4), round(Maxb2S[count][i][1] - 0.0008, 4)]]
            
            v = []
            for j in range(9):
                v.append(fb(l9[j][0], l9[j][1]))
            
            co = l9[v.index(max(v))]
            
            if 0 not in co and 3 not in co:
                temp.append(co)
            
            else:
                temp.append(['drop'])
        
        else:
            LMaxb1 -= 1
    
    Maxb2S.append(temp)
    
    count += 1
    
    if Maxb2S[count - 1] == Maxb2S[count]:
        break
    
    else:
        continue

Maxb2 = []
[Maxb2.append(x) for x in Maxb2S[count] if x not in Maxb2]
LMaxb2 = len(Maxb2)

################

minb2S = []
minb2S.append(minb1)

count = 0
while True:
    
    temp = []
    for i in range(Lminb1):
        
        if minb2S[count][i] != ['drop']:
            
            l9 = [
            [minb2S[count][i][0], minb2S[count][i][1]],
            [round(minb2S[count][i][0] + 0.0008, 4), minb2S[count][i][1]],
            [round(minb2S[count][i][0] + 0.0008, 4), round(minb2S[count][i][1] + 0.0008, 4)],
            [minb2S[count][i][0], round(minb2S[count][i][1] + 0.0008, 4)],
            [round(minb2S[count][i][0] - 0.0008, 4), round(minb2S[count][i][1] + 0.0008, 4)],
            [round(minb2S[count][i][0] - 0.0008, 4), minb2S[count][i][1]],
            [round(minb2S[count][i][0] - 0.0008, 4), round(minb2S[count][i][1] - 0.0008, 4)],
            [minb2S[count][i][0], round(minb2S[count][i][1] - 0.0008, 4)],
            [round(minb2S[count][i][0] + 0.0008, 4), round(minb2S[count][i][1] - 0.0008, 4)]]
            
            v = []
            for j in range(9):
                v.append(fb(l9[j][0], l9[j][1]))
            
            co = l9[v.index(min(v))]
            
            if 0 not in co and 3 not in co:
                temp.append(co)
            
            else:
                temp.append(['drop'])
        
        else:
            Lminb1 -= 1
    
    minb2S.append(temp)
    
    count += 1
    
    if minb2S[count - 1] == minb2S[count]:
        break
    
    else:
        continue

minb2 = []
[minb2.append(x) for x in minb2S[count] if x not in minb2]
Lminb2 = len(minb2)

################

Maxa3S = []
Maxa3S.append(Maxa2)

count = 0
while True:
    
    temp = []
    for i in range(LMaxa2):
        
        if Maxa3S[count][i] != ['drop']:
            
            l9 = [
            [Maxa3S[count][i][0], Maxa3S[count][i][1]],
            [round(Maxa3S[count][i][0] + 0.0001, 4), Maxa3S[count][i][1]],
            [round(Maxa3S[count][i][0] + 0.0001, 4), round(Maxa3S[count][i][1] + 0.0001, 4)],
            [Maxa3S[count][i][0], round(Maxa3S[count][i][1] + 0.0001, 4)],
            [round(Maxa3S[count][i][0] - 0.0001, 4), round(Maxa3S[count][i][1] + 0.0001, 4)],
            [round(Maxa3S[count][i][0] - 0.0001, 4), Maxa3S[count][i][1]],
            [round(Maxa3S[count][i][0] - 0.0001, 4), round(Maxa3S[count][i][1] - 0.0001, 4)],
            [Maxa3S[count][i][0], round(Maxa3S[count][i][1] - 0.0001, 4)],
            [round(Maxa3S[count][i][0] + 0.0001, 4), round(Maxa3S[count][i][1] - 0.0001, 4)]]
            
            v = []
            for j in range(9):
                v.append(fa(l9[j][0], l9[j][1]))
            
            co = l9[v.index(max(v))]
            
            if 0 not in co and 7 not in co:
                temp.append(co)
            
            else:
                temp.append(['drop'])
        
        else:
            LMaxa2 -= 1
    
    Maxa3S.append(temp)
    
    count += 1
    
    if Maxa3S[count - 1] == Maxa3S[count]:
        break
    
    else:
        continue

Maxa3 = []
[Maxa3.append(x) for x in Maxa3S[count] if x not in Maxa3]
LMaxa3 = len(Maxa3)

################

mina3S = []
mina3S.append(mina2)

count = 0
while True:
    
    temp = []
    for i in range(Lmina2):
        
        if mina3S[count][i] != ['drop']:
            
            l9 = [
            [mina3S[count][i][0], mina3S[count][i][1]],
            [round(mina3S[count][i][0] + 0.0001, 4), mina3S[count][i][1]],
            [round(mina3S[count][i][0] + 0.0001, 4), round(mina3S[count][i][1] + 0.0001, 4)],
            [mina3S[count][i][0], round(mina3S[count][i][1] + 0.0001, 4)],
            [round(mina3S[count][i][0] - 0.0001, 4), round(mina3S[count][i][1] + 0.0001, 4)],
            [round(mina3S[count][i][0] - 0.0001, 4), mina3S[count][i][1]],
            [round(mina3S[count][i][0] - 0.0001, 4), round(mina3S[count][i][1] - 0.0001, 4)],
            [mina3S[count][i][0], round(mina3S[count][i][1] - 0.0001, 4)],
            [round(mina3S[count][i][0] + 0.0001, 4), round(mina3S[count][i][1] - 0.0001, 4)]]
            
            v = []
            for j in range(9):
                v.append(fa(l9[j][0], l9[j][1]))
            
            co = l9[v.index(min(v))]
            
            if 0 not in co and 7 not in co:
                temp.append(co)
            
            else:
                temp.append(['drop'])
        
        else:
            Lmina2 -= 1
    
    mina3S.append(temp)
    
    count += 1
    
    if mina3S[count - 1] == mina3S[count]:
        break
    
    else:
        continue

mina3 = []
[mina3.append(x) for x in mina3S[count] if x not in mina3]
Lmina3 = len(mina3)

################

Maxb3S = []
Maxb3S.append(Maxb2)

count = 0
while True:
    
    temp = []
    for i in range(LMaxb2):
        
        if Maxb3S[count][i] != ['drop']:
            
            l9 = [
            [Maxb3S[count][i][0], Maxb3S[count][i][1]],
            [round(Maxb3S[count][i][0] + 0.0001, 4), Maxb3S[count][i][1]],
            [round(Maxb3S[count][i][0] + 0.0001, 4), round(Maxb3S[count][i][1] + 0.0001, 4)],
            [Maxb3S[count][i][0], round(Maxb3S[count][i][1] + 0.0001, 4)],
            [round(Maxb3S[count][i][0] - 0.0001, 4), round(Maxb3S[count][i][1] + 0.0001, 4)],
            [round(Maxb3S[count][i][0] - 0.0001, 4), Maxb3S[count][i][1]],
            [round(Maxb3S[count][i][0] - 0.0001, 4), round(Maxb3S[count][i][1] - 0.0001, 4)],
            [Maxb3S[count][i][0], round(Maxb3S[count][i][1] - 0.0001, 4)],
            [round(Maxb3S[count][i][0] + 0.0001, 4), round(Maxb3S[count][i][1] - 0.0001, 4)]]
            
            v = []
            for j in range(9):
                v.append(fb(l9[j][0], l9[j][1]))
            
            co = l9[v.index(max(v))]
            
            if 0 not in co and 3 not in co:
                temp.append(co)
            
            else:
                temp.append(['drop'])
        
        else:
            LMaxb2 -= 1
    
    Maxb3S.append(temp)
    
    count += 1
    
    if Maxb3S[count - 1] == Maxb3S[count]:
        break
    
    else:
        continue

Maxb3 = []
[Maxb3.append(x) for x in Maxb3S[count] if x not in Maxb3]
LMaxb3 = len(Maxb3)

################

minb3S = []
minb3S.append(minb2)

count = 0
while True:
    
    temp = []
    for i in range(Lminb2):
        
        if minb3S[count][i] != ['drop']:
            
            l9 = [
            [minb3S[count][i][0], minb3S[count][i][1]],
            [round(minb3S[count][i][0] + 0.0001, 4), minb3S[count][i][1]],
            [round(minb3S[count][i][0] + 0.0001, 4), round(minb3S[count][i][1] + 0.0001, 4)],
            [minb3S[count][i][0], round(minb3S[count][i][1] + 0.0001, 4)],
            [round(minb3S[count][i][0] - 0.0001, 4), round(minb3S[count][i][1] + 0.0001, 4)],
            [round(minb3S[count][i][0] - 0.0001, 4), minb3S[count][i][1]],
            [round(minb3S[count][i][0] - 0.0001, 4), round(minb3S[count][i][1] - 0.0001, 4)],
            [minb3S[count][i][0], round(minb3S[count][i][1] - 0.0001, 4)],
            [round(minb3S[count][i][0] + 0.0001, 4), round(minb3S[count][i][1] - 0.0001, 4)]]
            
            v = []
            for j in range(9):
                v.append(fb(l9[j][0], l9[j][1]))
            
            co = l9[v.index(min(v))]
            
            if 0 not in co and 3 not in co:
                temp.append(co)
            
            else:
                temp.append(['drop'])
        
        else:
            Lminb2 -= 1
    
    minb3S.append(temp)
    
    count += 1
    
    if minb3S[count - 1] == minb3S[count]:
        break
    
    else:
        continue

minb3 = []
[minb3.append(x) for x in minb3S[count] if x not in minb3]
Lminb3 = len(minb3)

################

MaxaF = []
minaF = []
MaxbF = []
minbF = []

for i in range(LMaxa3):
    MaxaF.append(Maxa3[i])

for i in range(LMaxa3 - 1):
    for j in range(i + 1, LMaxa3):
        
        if ((Maxa3[i][0] - Maxa3[j][0])**2 + (Maxa3[i][1] - Maxa3[j][1])**2) < 0.0001:
            print(Maxa3[i], Maxa3[j])
            if Maxa3[i] in MaxaF:
                MaxaF.remove(Maxa3[i])

for i in range(Lmina3):
    minaF.append(mina3[i])

for i in range(Lmina3 - 1):
    for j in range(i + 1, Lmina3):
        
        if ((mina3[i][0] - mina3[j][0])**2 + (mina3[i][1] - mina3[j][1])**2) < 0.0001:
            if mina3[i] in minaF:
                minaF.remove(mina3[i])

for i in range(LMaxb3):
    MaxbF.append(Maxb3[i])

for i in range(LMaxb3 - 1):
    for j in range(i + 1, LMaxb3):
        
        if ((Maxb3[i][0] - Maxb3[j][0])**2 + (Maxb3[i][1] - Maxb3[j][1])**2) < 0.0001:
            if Maxb3[i] in MaxbF:
                MaxbF.remove(Maxb3[i])

for i in range(Lminb3):
    minbF.append(minb3[i])

for i in range(Lminb3 - 1):
    for j in range(i + 1, Lminb3):
        
        if ((minb3[i][0] - minb3[j][0])**2 + (minb3[i][1] - minb3[j][1])**2) < 0.0001:
            if minb3[i] in minbF:
                minbF.remove(minb3[i])

print('\nMax points of a :', len(MaxaF))
print(MaxaF)
print('\nmin points of a :', len(minaF))
print(minaF)
print('\nMax points of b :', len(MaxbF))
print(MaxbF)
print('\nmin points of b :', len(minbF))
print(minbF)

################

Ma = []
for i in range(141):
    ma= []
    for j in range(141):
        ma.append(fa(j/20, i/20))
    Ma.append(ma)

x = np.linspace(0, 7, 141)
X = np.tile(x, (141, 1))
Y = np.transpose(X)
Z = np.array(Ma)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='seismic')
ax.set_zlim(-2.5, 2.5)

fig.colorbar(surf, shrink=0.6, aspect=8)
surf.set_clim(-1.0, 1.0)
plt.tight_layout()

plt.show()

Mb = []
for i in range(121):
    mb = []
    for j in range(121):
        mb.append(fb(j/40, i/40))
    Mb.append(mb)

x = np.linspace(0, 3, 121)
X = np.tile(x, (121, 1))
Y = np.transpose(X)
Z = np.array(Mb)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='seismic')
ax.set_zlim(-1.5, 1.5)

fig.colorbar(surf, shrink=0.6, aspect=8)
surf.set_clim(-1.0, 1.0)
plt.tight_layout()

plt.show()

################

