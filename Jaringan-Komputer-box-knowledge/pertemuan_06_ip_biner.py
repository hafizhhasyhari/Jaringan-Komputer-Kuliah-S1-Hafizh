# pertemuan_06_ip_biner.py
def ip_to_binary(ip):
    return '.'.join(format(int(octet), '08b') for octet in ip.split('.'))

ip_address = '192.168.1.1'
print(f"IP Address: {ip_address}")
print(f"Binary: {ip_to_binary(ip_address)}")
