import os
import sys
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
fp = open('./pl.txt', 'w')
for i in range(1, 7):
    fp.write('interface %d\napply access-list ip acl%d in\n'%(i+48,i+48))
  
    #if (i%2 == 1):
        #fp.write('access-list ipv4 acl%d\n%d forward port %s any any any\nsync access-list\n' %(i+48, i+48, l2[i]))
        #fp.write('access-list ipv4 acl%d\n%d forward port %s any any any\nsync access-list\n' %(i+48+1, i+48+1, l2[i-1]))
    #fp.write('interface %d\napply access-list ip acl%d in\n'%(i,i))
    #if (i%2 == 1):
        #fp.write('access-list ipv4 acl%d\n%d forward port %d any any any\nsync access-list\n' %(i, i, i+1))
        #fp.write('access-list ipv4 acl%d\n%d forward port %d any any any\nsync access-list\n' %(i+1, i+1, i))
        #fp.write('interface %d\n' %i)
        #fp.write('lag 1\n')
        #fp.write('no vxlanterminated enable\n')
        #fp.write('no access-list ip acl%d\n' % i)
        #fp.write('no shutdown\nno routing\nvlan access 1\n')
#for i in range(1,37):
#    fp.write('interface %d\nvlan access %d\ninterface %d\nvlan access %d\n'%(i,i,i+16,i))
    
fp.close()
