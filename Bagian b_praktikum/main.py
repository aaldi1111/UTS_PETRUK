from manajemen_warung.fileio import buat_file_menu, tambah_menu_file, baca_menu_file, tulis_laporan_file
from manajemen_warung.processing import AnalisisMenu

if __name__ == "__main__":
    file_data = "menu_warung.txt"
    file_laporan = "laporan_menu.txt"

    print("=== APLIKASI DAFTAR MENU WARUNG BAHARI ===")
    
    # Alur File Handling Mode 'x': Membuat file data menu pertama kali
    buat_file_menu(file_data)

    #Alur File Handling Mode 'a': Menambahkan data menu sampel ke file
    tambah_menu_file(file_data, "Nasi Goreng Spesial;Makanan;18000")
    tambah_menu_file(file_data, "Es Teh Manis;Minuman;5000")
    tambah_menu_file(file_data, "Ayam Bakar Madu;Makanan;22000")
    tambah_menu_file(file_data, "Jus Alpukat;Minuman;10000")
    tambah_menu_file(file_data, "Data Rusak Contoh;Makanan;abc") # Simulasi uji error ValueError

    # Alur File Handling Mode 'r': Membaca data secara iteratif dari file
    menu_tercatat = baca_menu_file(file_data)
    print(f"\nBerhasil memuat {len(menu_tercatat)} daftar menu valid dari file.")

    # Inisialisasi Objek Analisis Menu
    analis = AnalisisMenu("Warung Bahari")
    
    # penggunaan *args untuk kalkulasi paket pesanan
    total_paket = analis.hitung_total_harga_paket(18000, 5000, 22000)
    print(f"Simulasi Total Harga Paket Pesanan (*args): Rp {total_paket:,}")

    # Contoh penggunaan **kwargs dan lambda untuk menyaring kategori 'Minuman'
    filter_minuman = analis.filter_berdasarkan_kategori(menu_tercatat, kategori="Minuman")
    print(f"Jumlah menu kategori 'Minuman': {len(filter_minuman)} item.")

    # Alur File Handling Mode 'w': Menulis file laporan akhir ringkasan menu
    isi_laporan = f"""LAPORAN MENU WARUNG

Nama Warung  : {analis.nama_warung}
Total Menu   : {len(menu_tercatat)} item tersedia
----------------------------------------
Daftar Menu Valid:
"""
    for m in menu_tercatat:
        isi_laporan += f"- {m['nama']} ({m['kategori']}) : Rp {m['harga']:,.0f}\n"
    isi_laporan += ""

    tulis_laporan_file(file_laporan, isi_laporan)
    print("\nProgram utama daftar menu warung berhasil dijalankan!")