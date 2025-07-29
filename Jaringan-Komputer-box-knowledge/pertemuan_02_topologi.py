# pertemuan_02_topologi.py
topologi = {
    "Bus": "Satu kabel utama digunakan untuk menghubungkan semua perangkat.",
    "Ring": "Setiap perangkat terhubung melingkar.",
    "Star": "Semua perangkat terhubung ke switch atau hub pusat.",
    "Mesh": "Setiap perangkat terhubung langsung ke semua perangkat lainnya."
}

for nama, penjelasan in topologi.items():
    print(f"{nama}: {penjelasan}")
