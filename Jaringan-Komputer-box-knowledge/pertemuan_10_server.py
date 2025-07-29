# pertemuan_10_server.py
import socket

server = socket.socket()
server.bind(('localhost', 9999))
server.listen(1)
print("Menunggu koneksi...")
conn, addr = server.accept()
print(f"Terkoneksi dengan {addr}")
conn.send(b"Halo Client!")
conn.close()
