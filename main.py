from geometric.persegipanjang import PersegiPanjang
from geometric.segitiga import SegiTiga

print('Menggunakan OOP')

p1 = PersegiPanjang(10, 3)
print(f'\n{p1.info()}')
print(p1.hitung_luas())


s1 = SegiTiga(8, 6)
print(f'\n{s1.info()}')
print(s1.hitung_luas())


# polymorphism: kemampuan object untuk merespon berbeda terhadap pemanggilan method yg sama

daftar_bangun_datar =[]
daftar_bangun_datar.append(p1)
daftar_bangun_datar.append(s1)

print('\nPolymorphism:')
for bangun_datar in daftar_bangun_datar:
    print('\n' + bangun_datar.info())
    print(bangun_datar.hitung_luas())
