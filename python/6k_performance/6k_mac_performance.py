import os
import sys

fp = open('./6k_mac_performance.txt', 'w')

l1 = range(1, 49)
l2 = range(49, 55)
l3 = range (1, 5)
l4 = list(range(0, 24))

l= 0
for i in range(49, 55):
    for j in range(1, 5):
        l4[l] =  '%d-%d' % (i, j)
        l += 1
l5 = l1 + l4
l = 0
for i in range(1, 72):
    if i %2 == 1:
        fp.write('vlan %d\nno shutdown\n'%(i/2+2))
for i in range(1, 72):
    if i %2 == 1:
        fp.write('interface %s\nvlan access %d\n'%(l5[l], (i/2+2)))
        l += 1 
        fp.write('interface %s\nvlan access %d\n'%(l5[l], (i/2+2)))
        l += 1  
l = 0       
for i in range(1, 72):
    if i %2 == 1:
        fp.write('mac-address static 00:00:00:00:00:02 interface %s vlan %d\n' % (l5[l],(i/2+2) ))
        l += 1 
        fp.write('mac-address static 00:00:00:00:00:01 interface %s vlan %d\n' % (l5[l],(i/2+2) ))
        l += 1 

fp.close()