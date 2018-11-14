import os
import sys
fp = open('./6k_sx1.txt', 'w+')
l1 = (range(48))
l2 = range(0, 24)
tmp =0
for i in range (49, 55):
    for j in range (1, 5):
        l2[tmp] = '%d-%d'%(i,j)
        tmp = tmp+1
cnt = 37
l3 = l1+l2
loop = 1
fp.write('configure\n')
for i in range(1, 36):
 
    for j in range(1,5):
        fp.write('mac-address static 00:00:00:00:00:%d interface %s vlan 2\n' % (j+10+loop, l3[cnt]))
        loop +=1
    cnt = cnt +1

fp.close()
