def baca_suhu(nama_file):

    data = []
    try:
        with open(nama_file, "r") as file:
            for baris in file:
                baris = baris.strip()
                if not baris:
                    continue
                try:
                    hari, suhu = baris.split(";")
                    data.append({
                        "hari": hari.strip(),
                        "suhu": int(suhu.strip())
                    })
                except ValueError:
                    print(f"[PERINGATAN] Baris tidak valid dilewati: {baris}")
    except FileNotFoundError:
        print(f"[ERROR] File '{nama_file}' tidak ditemukan.")
    return data

def analisis_suhu(data, *args, batas_panas=32):
   
    if not data:
        return None

    rata_rata = sum(item["suhu"] for item in data) / len(data)

    tertinggi = max(data, key=lambda x: x["suhu"])
    terendah = min(data, key=lambda x: x["suhu"])

    kategori = list(map(
        lambda x: {
            "hari": x["hari"],
            "suhu": x["suhu"],
            "kategori": "Panas" if x["suhu"] >= batas_panas else "Normal"
        },
        data
    ))

    jumlah_panas = sum(1 for k in kategori if k["kategori"] == "Panas")

    return {
        "rata_rata": rata_rata,
        "tertinggi": tertinggi,
        "terendah": terendah,
        "kategori": kategori,
        "jumlah_panas": jumlah_panas,
    }

def tulis_laporan(nama_file, hasil):
    """
    Tahap 3: Menulis laporan ke file (mode 'w') dan menampilkan di layar.
    """
    with open(nama_file, "w") as file:
        file.write("LAPORAN SUHU MINGGUAN\n")
        file.write(f"Rata-rata suhu     : {hasil['rata_rata']:.2f}\n")
        file.write(f"Suhu tertinggi     : {hasil['tertinggi']['suhu']} "
                   f"({hasil['tertinggi']['hari']})\n")
        file.write(f"Suhu terendah      : {hasil['terendah']['suhu']} "
                   f"({hasil['terendah']['hari']})\n")
        file.write(f"Jumlah hari Panas  : {hasil['jumlah_panas']}\n")
        file.write("\nDetail per hari:\n")
        for k in hasil["kategori"]:
            file.write(f"  {k['hari']:<8}: {k['suhu']} ({k['kategori']})\n")

    with open(nama_file, "r") as file:
        print(file.read())

if __name__ == "__main__":
    print(">>> Menjalankan program analisis suhu...\n")
    data = baca_suhu("suhu.txt")
    hasil = analisis_suhu(data, batas_panas=32)
    if hasil:
        tulis_laporan("laporan_suhu.txt", hasil)
    else:
        print("[INFO] Tidak ada data untuk dianalisis.")