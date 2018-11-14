#!/usr/bin/env python3
# coding: utf-8
import os
import sys

par = sys.argv[1]

if par == '--help':
    print ('This test is designed to test performance of elag on PF6000\nplease type like this:\n\tpython 6k_elag_performance.py -gtp\n\tpython 6k_elag_performance.py -mpls\n\tpython 6k_elag_performance.py -vxlan\n\tpython 6k_elag_performance.py -erspan\n\tpython 6k_elag_performance.py -vntag\n\t')
else:        
    fp = open("./6k_elag_performance.txt","w")
    fp.write('configure\n')
    if par == 'gtp' or 'mpls'or'vxlan'or'erspan'or'vntag':
        par3 = par
        par2 = par
    for i  in range(49,55):
        fp.write('interface %d\nrouting\nsplit 10000\nexit\n' % i)
    
    fp.write('interface elag 1\nexit\ninterface 1\nelag 1\n')
        
    for i in range(1,49):
        fp.write('interface %d\nno routing\nno shutdown\nelag 1\n' % i)  
       # if  par3:
       #   fp.write('%sterminated enable\n' % par2)
    fp.write('access-list ipv4 acl1\n1 forward elag elag1 any any any\nsync access-list\n')
    for i in range(49,55):
        for j in range(1,5):
            fp.write('interface %d-%d\nno routing\nno shutdown\nelag 1\n' % (i,j))
    for i in range(1,49):
        fp.write('interface %d\napply access-list ip acl1 in\nexit\n' % i)  
    fp.close()
        