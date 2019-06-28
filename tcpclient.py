# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:00:41 2019

@author: george
"""
import socket
from multiprocessing import Pool
from time import sleep
import datetime
import codecs



def send_pack(info):
    now = datetime.datetime.now()
    timestamp = str(now.strftime("%Y%m%d_%H-%M-%S"))
#    t_host=input("連線目標URL\n") #info[0]
#    t_port=input("連線目標PORT\n") #info[1] msg=info[2]
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((info[0],int(info[1])))
    try:
        client.settimeout(15)
#        client.send(info[2].encode('UTF-8'))
#        a=b'testtest'
        client.send(b'testtest')
        resp=client.recv(4096)
        print("{}_收到的訊息:{}".format(timestamp,resp))
    except:
        print("connection time out")
        
        
def send(ip):
    now = datetime.datetime.now()
    timestamp = str(now.strftime("%Y%m%d_%H-%M-%S")) 
    #t_host=input("連線目標URL\n") #info[0]
#    t_port=input("連線目標PORT\n") #info[1] msg=info[2]
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((ip,9999))
    try:
        client.settimeout(15)
        sleep(2)
        client.send("connected".encode('UTF-8'))
        resp=client.recv(4096)
        print("{}_收到的訊息:{}".format(timestamp,resp))
    except:
        print("connection time out")
        

while True:
    cmmd=input("輸入1送訊息,99停止,44多執行\n")
    if(cmmd=="1"):    
        send_pack(["127.0.0.1",9999,"I call you"])
    elif(cmmd=="99"):
        break
    elif(cmmd=="55"):
        msg="123456"
#        msg=codecs.encode(msg, encoding='hex', errors='strict')
        print(codecs.getencoder())
#        print("test"+bytes.formhex(msg))
#        print(bytes.decode(msg))
    if(cmmd=="44"):
       with Pool(6) as p:
            p.map(send,["127.0.0.1","127.0.0.1","127.0.0.1","127.0.0.1","127.0.0.1","127.0.0.1"])