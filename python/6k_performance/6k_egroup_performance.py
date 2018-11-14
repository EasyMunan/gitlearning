fp = open("./6k_megroup_perfomance.txt","w"
          )

fp.write('configure\n')

fp.write('interface 1\n')
fp.write('no routing\n')
fp.write('no shutdown\n')
fp.write('vlan access 1\n')
fp.write('rx on\n')

for i  in range(49,55):
    fp.write('interface %d\n' % i)
    fp.write('routing\n')
    fp.write('split 10000\n')
    fp.write('exit\n') 

fp.write('interface megroup 1\n')
fp.write('exit\n')



for i in range(2,49):
    fp.write('interface %d\n' % i)
    fp.write('no routing\n')
    fp.write('no shutdown\n')
    fp.write('vlan access 1\n')
    fp.write('megroup 1\n')   
    fp.write('exit\n')

for i in range(49,55):
    for j in range(1,5):
        fp.write('interface %d-%d\n' % (i,j))
        fp.write('no routing\n')
        fp.write('no shutdown\n')
        fp.write('megroup 1\n')   
        fp.write('exit\n')

        
fp.write('access-list ipv4 acl1\n')
fp.write('1 forward megroup egroup1 any any any\n')
fp.write('sync access-list\n')
fp.write('interface 1\n')
fp.write('no routing\n')
fp.write('no shutdown\n')
fp.write('rx on\n')
fp.write('apply access-list ip acl1 in\n')




fp.close()
