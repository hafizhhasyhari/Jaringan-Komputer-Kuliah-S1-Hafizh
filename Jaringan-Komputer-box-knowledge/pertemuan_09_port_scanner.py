# pertemuan_09_port_scanner.py
import socket

target = "127.0.0.1"
port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((target, port))
if result == 0:
    print(f"Port {port} terbuka di {target}")
else:
    print(f"Port {port} tertutup di {target}")
sock.close()
