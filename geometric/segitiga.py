from geometric.bangun_datar import BangunDatar


class SegiTiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi


    def info(self):
        return f"Ini adalah object segitiga dengan panjang alas {self.alas} dan tinggi {self.tinggi}"

    def hitung_luas(self):
        return f"Luas segitiga tersebut adalah {self.alas * self.tinggi * 0.5}"