class MenuTidakValidError(Exception):
    """untuk menangani data menu yang tidak valid."""
    def __init__(self, pesan):
        super().__init__(pesan)

def validasi_harga(harga):
    """Alur: Memastikan harga berupa angka positif dan tidak bernilai negatif."""
    if harga < 0:
        raise MenuTidakValidError("Error: Harga menu tidak boleh bernilai negatif!")
    return True

def validasi_teks(teks):
    """Alur: Memastikan string nama atau kategori tidak kosong atau spasi kosong."""
    if not teks or not teks.strip():
        raise MenuTidakValidError("Error: Kolom nama menu atau kategori tidak boleh kosong!")
    return teks.strip()