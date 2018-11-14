fp = open("./6k_acl_perfomance_v6.txt","w")

fp.write('configure\n')

fp.write('interface 1\n')
fp.write('rx on\n')

fp.write('interface 48\n')
fp.write('rx on\n')


for i in range(1,49):
    if i%2 !=0:
        fp.write('access-list ipv6 acl%d\n%d forward port %d any any any\nsync access-list\n' % (i,i+100,i+1))
for i in range(1,49):
    if i%2 !=0:
        fp.write('interface %d\napply access-list ip acl%d in\n' %(i,i))
for i in range(48,0,-1):
    if i%2 == 0:
        fp.write('access-list ipv6 acl%d\n%d forward port %d any any any\nsync access-list\n' % (i,i+100,i-1))
for i in range(48,0,-1):
    if i%2 == 0:
        fp.write('interface %d\napply access-list ip acl%d in\n' %(i,i))            
 
fp.close()
