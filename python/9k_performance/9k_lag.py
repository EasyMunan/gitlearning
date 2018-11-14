import os
import sys


fp = open("./9k_lag_perfomance.txt","w+")

fp.write('configure\n')

for i  in range(2,33):
    fp.write('interface %d\n' % i)
    fp.write('routing\n')
    fp.write('split 10000\n')
    fp.write('exit\n') 
fp.write('interface lag 1\n')
fp.write('no routing\n')
fp.write('no shutdown\n')
fp.write('exit\n')
for i in range(12,33):
    for j in range(1,5):
        fp.write('interface %d-%d\n' %(i,j))
        fp.write('no routing\n')
        fp.write('no shutdown\n')
        fp.write('force_tx on\n')
        fp.write('lag 1\n')   
        fp.write('exit\n')
fp.write('access-list ipv4 acl2\n2 forward lag lag1 any any any\nsync access-list\n')

for i in range(2,11):
    for j in range(1,5):
        fp.write('interface %d-%d\n' %(i,j))
        fp.write('loopback on\n')
        fp.write('egroup 1\n') 
        fp.write('apply access-list ip acl2 in\n') 
        fp.write('exit\n')
fp.write('access-list ipv4 acl1\n1 forward egroup egroup1 any any any\nsync access-list\ninterface 1\napply access-list ip acl1 in\n')

fp.close()
