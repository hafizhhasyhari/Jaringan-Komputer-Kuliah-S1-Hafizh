# pertemuan_05_ip_subnet.py
import ipaddress

ip = ipaddress.IPv4Network('192.168.10.0/24', strict=False)
print("Subnet mask:", ip.netmask)
print("Jumlah host yang tersedia:", ip.num_addresses - 2)
print("Contoh IP yang valid:")
for i, addr in enumerate(ip.hosts()):
    print(addr)
    if i == 4:
        break
