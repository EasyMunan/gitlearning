import os
import sys
fp = open('./pl.txt', 'w')
for i in range(1,49):
    #fp.write('interface %d\n' %i)
    #fp.write('no vxlanterminated enable\n')
    fp.write('no access-list ip acl%d\n' % i)

    
fp.close()
