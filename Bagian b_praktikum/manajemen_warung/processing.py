from manajemen_warung.validasi import validasi_harga, validasi_teks

class WarungBahari:
    """Class induk untuk menyimpan data dasar menu warung."""
    def __init__(self, nama_warung):
        self.nama_warung = nama_warung
        self.katalog_menu = []

    def tambah_menu(self, nama, kategori, harga):
        #Alur: Melakukan validasi input, assert, lalu memasukkan data ke list katalog.
        validasi_teks(nama)
        validasi_teks(kategori)
        validasi_harga(harga)
        
        # Alur Debugging: Assert untuk memastikan harga valid secara internal
        assert harga >= 0, "Harga tidak boleh negatif"
        
        self.katalog_menu.append({
            "nama": nama,
            "kategori": kategori,
            "harga": harga
        })

    def hitung_total_harga_paket(self, *args):
        #Alur: Menggunakan *args untuk menerima argumen harga tak terbatas dan mengembalikan total jumlahnya.
        return sum(args)

class AnalisisMenu(WarungBahari):
    # Class (Inheritance) untuk melakukan analisis, filter, dan sorting menu.

    def filter_berdasarkan_kategori(self, data_menu, **kwargs):
        # Alur: Menggunakan **kwargs dan ekspresi lambda untuk menyaring menu berdasarkan kategori tertentu secara fleksibel."""
        kategori_dicari = kwargs.get("kategori")
        if kategori_dicari:
            return list(filter(lambda x: x["kategori"].lower() == kategori_dicari.lower(), data_menu))
        return data_menu

    def urutkan_menu_berdasarkan_harga(self, data_menu, ascending=True):
        """Alur: Menggunakan fungsi sorted() dengan lambda key untuk mengurutkan menu berdasarkan harga."""
        return sorted(data_menu, key=lambda x: x["harga"], reverse=not ascending)