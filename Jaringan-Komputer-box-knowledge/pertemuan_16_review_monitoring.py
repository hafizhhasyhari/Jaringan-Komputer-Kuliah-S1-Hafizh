# pertemuan_16_review_monitoring.py
import psutil

net = psutil.net_io_counters()
print(f"Bytes terkirim: {net.bytes_sent}")
print(f"Bytes diterima: {net.bytes_recv}")
