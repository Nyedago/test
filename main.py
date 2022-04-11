import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('本地ip', 10000))

while True:
    rand = random.randint(1, 10)
    print(rand)
    message, address = serverSocket.recvfrom(1024)
    message_str = message.decode('utf-8')
    if message_str == '学号':
        msg_sent = '姓名'
    if rand < 4:
        continue
    ret = '{' + msg_sent + '}'
    serverSocket.sendto(ret.encode(), address)
