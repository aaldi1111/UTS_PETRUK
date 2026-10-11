def buat_file_menu(nama_file):
    #Mode 'x' untuk membuat file baru pertama kali sekaligus menangani FileExistsError jika file sudah ada.
    try:
        with open(nama_file, "x") as file:
            file.write("NamaMenu;Kategori;Harga\n")
        print(f"File '{nama_file}' berhasil dibuat.")
    except FileExistsError:
        print(f"Informasi: File '{nama_file}' sudah ada sebelumnya.")

def tambah_menu_file(nama_file, teks_data):
    #Mode 'a' (append) untuk menambahkan baris data menu baru di bagian akhir file tanpa menghapus data lama.
    with open(nama_file, "a") as file:
        file.write(teks_data + "\n")

def baca_menu_file(nama_file):
    """ Mode 'r' untuk membaca file secara iteratif (baris demi baris).
       ada try-except untuk menangani FileNotFoundError dan ValueError (baris rusak)."""
    daftar_menu = []
    try:
        with open(nama_file, "r") as file:
            for baris in file: 
                baris = baris.strip()
                if not baris or baris.startswith("NamaMenu"):
                    continue # Lewati baris header atau baris kosong
                parts = baris.split(";")
                if len(parts) == 3:
                    try:
                        # Konversi string harga ke float, tangani ValueError jika gagal
                        harga_num = float(parts[2])
                        daftar_menu.append({
                            "nama": parts[0].strip(),
                            "kategori": parts[1].strip(),
                            "harga": harga_num
                        })
                    except ValueError:
                        #.Debugging: Baris rusak dilewati (continue), program tidak crash
                        print(f"Peringatan: Baris data rusak dilewati -> {baris}")
                        continue
    except FileNotFoundError:
        # Menangani pesan error jika file belum ada di direktori
        print(f"Error: File '{nama_file}' belum ada atau belum dibuat.")
    return daftar_menu

def tulis_laporan_file(nama_file_laporan, isi_laporan):
    """Alur: Mode 'w' (write) untuk menulis hasil ringkasan laporan 
       ke dalam file teks baru."""
    with open(nama_file_laporan, "w") as file:
        file.write(isi_laporan)
    print(f"Laporan menu berhasil ditulis ke '{nama_file_laporan}'.")