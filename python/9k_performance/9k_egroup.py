fp = open("./9k_egroup_perfomance.txt","w+")

fp.write('configure\n')

for i  in range(2,33):
    fp.write('interface %d\n' % i)
    fp.write('routing\n')
    fp.write('split 10000\n')
    fp.write('exit\n') 
fp.write('interface egroup 1\n')
fp.write('exit\n')

for i in range(2,33):
    for j in range(1,5):
        fp.write('interface %d-%d\n' %(i,j))
        fp.write('no routing\n')
        fp.write('no shutdown\n')
        fp.write('force_tx on\n')
        fp.write('vlan access 1\n')
        fp.write('egroup 1\n')   
        fp.write('exit\n')


fp.write('access-list ipv4 acl2\n2 forward egroup egroup1 any any any\nsync access-list\n')



fp.close()
