# pertemuan_07_dns.py
import socket

domain = 'www.google.com'
ip = socket.gethostbyname(domain)
print(f"Domain: {domain}")
print(f"Alamat IP: {ip}")
