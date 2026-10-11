import unittest
from analisis_suhu import baca_suhu, analisis_suhu

class TestAnalisisSuhu(unittest.TestCase):

    def setUp(self):
        self.data = [
            {"hari": "Senin", "suhu": 31},
            {"hari": "Selasa", "suhu": 33},
            {"hari": "Rabu", "suhu": 29},
            {"hari": "Kamis", "suhu": 35},
            {"hari": "Jumat", "suhu": 32},
            {"hari": "Sabtu", "suhu": 30},
            {"hari": "Minggu", "suhu": 28},
        ]

    def test_rata_rata(self):
        hasil = analisis_suhu(self.data)
        self.assertAlmostEqual(hasil["rata_rata"], 218 / 7, places=2)

    def test_suhu_tertinggi(self):
        hasil = analisis_suhu(self.data)
        self.assertEqual(hasil["tertinggi"]["hari"], "Kamis")

    def test_suhu_terendah(self):
        hasil = analisis_suhu(self.data)
        self.assertEqual(hasil["terendah"]["hari"], "Minggu")

    def test_jumlah_hari_panas(self):
        hasil = analisis_suhu(self.data, batas_panas=32)
        self.assertEqual(hasil["jumlah_panas"], 3)

    def test_data_kosong(self):
        self.assertIsNone(analisis_suhu([]))

if __name__ == "__main__":
    unittest.main()