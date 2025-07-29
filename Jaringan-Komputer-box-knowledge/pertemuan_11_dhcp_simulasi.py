# pertemuan_11_dhcp_simulasi.py
import random

def assign_ip():
    base = "192.168.1."
    return base + str(random.randint(100, 200))

clients = ["ClientA", "ClientB", "ClientC"]
for client in clients:
    print(f"{client} diberikan IP: {assign_ip()}")
