# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:43:54 2019

@author: george
"""

import socket
import threading
import datetime
#import subprocess
now = datetime.datetime.now()
timestamp = str(now.strftime("%Y%m%d_%H-%M-%S"))

def handle_client(client_socket):
    now = datetime.datetime.now()
    timestamp = str(now.strftime("%Y%m%d_%H-%M-%S"))
    req=client_socket.recv(1024)
    print("{}_收到的資料{}\n".format(timestamp,req))
    msg="ACK!"
    client_socket.send(msg.encode('UTF-8'))
    client_socket.close()

        


bind_ip="127.0.0.1"
bind_port=9999
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)
print("{}_監聽{},port:{}".format(timestamp,bind_ip,bind_port))
while True:
#    cmmd=input("input cmmd \n")
    now = datetime.datetime.now()
    timestamp = str(now.strftime("%Y%m%d_%H-%M-%S"))
    resp=server.accept()
    print("{}_server.accept()的內容物: {}\n".format(timestamp,resp))
    client,addr=resp
    print("{}_addr的內容物: {}\n".format(timestamp,addr))
    print("{}_client的內容物: {}\n".format(timestamp,client))
    print("{}_Accepted connection from {}:{}".format(timestamp,addr[0],addr[1]))
    
    client_handler=threading.Thread(target=handle_client,args=(client,))
        
    client_handler.start()
#    if(cmmd=="99"):
#        break
    