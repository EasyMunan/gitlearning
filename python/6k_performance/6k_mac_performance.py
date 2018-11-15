import os
import sys

fp = open('./6k_mac_performance.txt', 'w')
<<<<<<< HEAD

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

=======
for i in range(1, 17):
    fp.write('mac-address static 00:00:00:00:00:%d interface %d vlan 1\n' % (i+10, i+32))

for i,j,l in range((17, 37),(49, 55),(1, 5)):
    fp.write('mac-address static 00:00:00:00:00:%d interface %d-%d vlan 1\n' % (i+10, j, l))
>>>>>>> a06b80c9c81b5b3d6c9194649b2b00c968d0fff8
fp.close()