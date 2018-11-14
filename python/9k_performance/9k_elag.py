import os
import sys


par = sys.argv[1] 

if  par == '-help':
    print ('python par1 par2\npar1:split_start\npar2 split_end\n')
    exit
else:
    fp = open("./9k_elag_perfomance.txt","w")
    fp.write('configure\n')
    par1 = int(par)
    print par1
    par2 = sys.argv[1]
    for i  in range(2,33):
        fp.write('interface %d\n' % i)
        fp.write('routing\n')
        fp.write('split 10000\n')
        fp.write('exit\n') 
    fp.write('interface elag 1\n')
    fp.write('exit\n')
        
    for i in range(par1,33):
        for j in range(1,5):
            fp.write('interface %d-%d\n' %(i,j))
            fp.write('force_tx on\n')
            fp.write('elag 1\n')   
            fp.write('exit\n')
        
        
        fp.write('access-list ipv4 acl2\n2 forward elag elag1 any any any\nsync access-list\n')
        
        
    for i in range(2,par1):
        for j in range(1,5):
            fp.write('interface %d-%d\n' %(i,j))
            fp.write('loopback on\n')
            fp.write('egroup 1\n') 
            fp.write('apply access-list ip acl2 in\n') 
            fp.write('exit\n')
        
        fp.write('access-list ipv4 acl1\n1 forward egroup egroup1 any any any\nsync access-list\ninterface 1\napply access-list ip acl1 in\n')
        fp.write('interface elag 1\n')
        
    for i in range(par1,33):
        for j in range(1,5):
            fp.write('interface %d-%d\n' %(i,j))
            fp.write('force_tx on\n')
            fp.write('elag 1\n')   
            fp.write('exit\n')
fp.close()
        