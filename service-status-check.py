import os
service = ['service mongod status', 'service chat-service status']

for i in service: 
    stat = os.system(i)
    if stat == 0:
        print('{0} is running'.format(i))
    elif stat == 768:
        print('{0} is not running'.format(i))