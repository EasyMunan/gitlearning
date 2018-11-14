import os
import sys

fp = open('./6k_mac_performance.txt', 'w')
for i in range(1, 17):
    fp.write('mac-address static 00:00:00:00:00:%d interface %d vlan 1' % (i+10, i+32))

for i,j,l in range((17, 37),(49, 55),(1, 5)):
    fp.write('mac-address static 00:00:00:00:00:%d interface %d-%d vlan 1' % (i+10, j, l))
fp.close()