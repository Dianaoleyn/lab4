from dataclasses import dataclass
import socket, struct, threading, time
import json
from msg import *
from server import *

HOST = 'localhost'
PORT = 12345

def ProcessReceive():
    while True:
        try:
            print('Messages: ' + GetList(Message.ClientID)['m'])
        except Exception:
            pass
        time.sleep(10)

def Client():
    Message.SendMessage(M_BROKER, M_INIT)

    t = threading.Thread(target=ProcessReceive)
    t.start()
    while True: 
        n = int(input("1. Отправить клиенту \n2. Отправить всем \n3. Получить сообщения\n"))
        if (n == 1):
            id = int(input("Введите id \n"))
            s = input("Введите сообщение\n")
            SendMsg(Message.ClientID, s, id)
        elif (n == 2):
            s = input("Введите сообщение\n")
            SendMsg(Message.ClientID, s, M_ALL)
        elif (n == 3):
            print('Messages' + GetList(Message.ClientID)['m'])
Client()