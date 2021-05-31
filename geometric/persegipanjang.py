from geometric.bangun_datar import BangunDatar


class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar


    def info(self):
        return f"Ini adalah object persegi panjang dengan panjang {self.panjang} dan lebar {self.lebar}"


    def hitung_luas(self):
        return f'Luas persegi panjang adalah {self.panjang * self.lebar}'



