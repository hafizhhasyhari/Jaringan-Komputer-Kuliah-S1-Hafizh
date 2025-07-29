# pertemuan_08_ping.py
import os

hostname = "8.8.8.8"
response = os.system(f"ping -c 4 {hostname}")

if response == 0:
    print(f"{hostname} dapat dijangkau.")
else:
    print(f"{hostname} tidak dapat dijangkau.")
