# Polymorphism pada method
class Kucing:
    def suara(self):
        return "Meow"


class Anjing:
    def suara(self):
        return "Guk guk"


# Polymorphism di dalam loop
hewan = [Kucing(), Anjing()]

for h in hewan:
    print(h.suara())


# Polymorphism dengan inheritance
class Hewan:
    def suara(self):
        return "Hewan bersuara"


class KucingTurunan(Hewan):
    def suara(self):
        return "Meow"


class AnjingTurunan(Hewan):
    def suara(self):
        return "Guk guk"


# Semua objek diperlakukan sebagai 'Hewan'
daftar_hewan = [KucingTurunan(), AnjingTurunan(), Hewan()]

for h in daftar_hewan:
    print(h.suara())


# Polymorphism dengan function
def cetak_suara(hewan):
    print(hewan.suara())


cetak_suara(Kucing())
cetak_suara(Anjing())


# Polymorphism dengan built-in function
print(len("Python"))                   # 6
print(len([1, 2, 3]))                  # 3
print(len({"a": 1, "b": 2, "c": 3}))   # 3


# Variasi sendiri: polymorphism pada bangun datar
class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2


class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return 3.14 * self.jari_jari ** 2


bangun = [Persegi(4), Lingkaran(7)]
for b in bangun:
    print(f"Luas {type(b).__name__}: {b.luas()}")


# Variasi sendiri: operator + untuk tipe data berbeda
print(5 + 3)          # 8 (penjumlahan angka)
print("Py" + "thon")   # Python (penggabungan string)
print([1, 2] + [3])    # [1, 2, 3] (penggabungan list)