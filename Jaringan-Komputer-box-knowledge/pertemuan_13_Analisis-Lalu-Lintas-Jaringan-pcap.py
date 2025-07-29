# pertemuan_13_pcap.py
from scapy.all import rdpcap

packets = rdpcap("sample.pcap")
for pkt in packets[:5]:
    print(pkt.summary())
