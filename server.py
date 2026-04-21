import socket
import threading
import sys
import pygame

HOST = "192.168.0.170"
PORT = 6767
ADDR = HOST, PORT

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"pripojeno: {addr} pripojen i guess")

    connected = True
    while connected:
        msg = conn.recv(1024)
        print(msg)

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args=(conn,addr))
        thread.start()
        print(f"aktivni pripojeni: {threading.active_count()-1}")


print("SERVER STARTUJE ....")
start()
