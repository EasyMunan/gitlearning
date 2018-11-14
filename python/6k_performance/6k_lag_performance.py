#!/usr/bin/env python3
# coding: utf-8
import os
import sys
 
fp = open("./6k_lag_performance.txt","w")
fp.write('configure\n')

fp.write('interface lag 1\nno routing\ninterface 25\nlag 1\n')
fp.write('access-list ipv4 acl1\n1 forward lag lag1 any any any\nsync access-list\n')    
for i in range(1,25):
    fp.write('interface %d\napply access-list ip acl1 in\n' % i)  
for i in range(25,49):
    fp.write('interface %d\nno routing\nno shutdown\nlag 1\n' % i)
for i in range(49,55):
    for j in range(1,5):
        fp.write('interface %d-%d\nlag 1\n' % (i,j))
fp.close()
    