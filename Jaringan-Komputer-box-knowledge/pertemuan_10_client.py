# pertemuan_10_client.py
import socket

client = socket.socket()
client.connect(('localhost', 9999))
msg = client.recv(1024)
print("Pesan dari server:", msg.decode())
client.close()
