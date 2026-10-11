import unittest
from manajemen_warung.processing import WarungBahari, AnalisisMenu
from manajemen_warung.validasi import validasi_harga, MenuTidakValidError

class TestDaftarMenuWarung(unittest.TestCase):

    def setUp(self):
        """Alur: Menyiapkan data sampel sebelum setiap fungsi test dijalankan."""
        self.warung = WarungBahari("Warung Bahari")
        self.analisis = AnalisisMenu("Warung Bahari")
        self.sampel_menu = [
            {"nama": "Nasi Goreng", "kategori": "Makanan", "harga": 15000},
            {"nama": "Es Teh Manis", "kategori": "Minuman", "harga": 5000},
            {"nama": "Ayam Geprek", "kategori": "Makanan", "harga": 18000}
        ]

    def test_hitung_total_paket_args(self):
        """Alur Test 1: Menguji perhitungan total harga menggunakan *args."""
        total = self.warung.hitung_total_harga_paket(15000, 5000, 18000)
        self.assertEqual(total, 38000)

    def test_validasi_harga_normal(self):
        """Alur Test 2: Menguji validasi harga normal yang bernilai positif."""
        self.assertTrue(validasi_harga(12000))

    def test_validasi_harga_negatif_raises_error(self):
        """Alur Test 3: Menguji custom exception (raise) saat harga bernilai negatif."""
        with self.assertRaises(MenuTidakValidError):
            validasi_harga(-2000)

    def test_filter_kategori_lambda(self):
        """Alur Test 4: Menguji keyword argument (**kwargs) dan filter lambda."""
        hasil = self.analisis.filter_berdasarkan_kategori(self.sampel_menu, kategori="Makanan")
        self.assertEqual(len(hasil), 2)

    def test_sorting_harga_lambda(self):
        """Alur Test 5: Menguji fungsi sorted() dengan key lambda untuk harga termurah."""
        hasil_urut = self.analisis.urutkan_menu_berdasarkan_harga(self.sampel_menu, ascending=True)
        self.assertEqual(hasil_urut[0]["harga"], 5000)

if __name__ == "__main__":
    unittest.main()