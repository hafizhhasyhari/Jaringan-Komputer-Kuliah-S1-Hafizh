# pertemuan_04_protokol.py
protokol = {
    "TCP": "Transmission Control Protocol - koneksi handal",
    "UDP": "User Datagram Protocol - koneksi tidak handal",
    "ICMP": "Internet Control Message Protocol - digunakan untuk diagnosa seperti ping"
}

for nama, deskripsi in protokol.items():
    print(f"{nama}: {deskripsi}")
