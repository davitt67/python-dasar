from abc import ABC, abstractmethod


# Abstraction dengan abstract class
class Hewan(ABC):
    @abstractmethod
    def suara(self):
        pass


# Subclass wajib mengimplementasikan method abstract
class Kucing(Hewan):
    def suara(self):
        return "Meow"


class Anjing(Hewan):
    def suara(self):
        return "Guk guk"


# Tidak bisa membuat objek dari abstract class
# h = Hewan()  # Error: TypeError

# Hanya subclass yang bisa dibuat objeknya
k = Kucing()
a = Anjing()

print(k.suara())
print(a.suara())


# Abstraction di dunia nyata: sistem pembayaran
class Pembayaran(ABC):
    @abstractmethod
    def bayar(self, jumlah):
        pass


class Gopay(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} menggunakan GoPay")


class Dana(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} menggunakan Dana")


# Menggunakan abstraction
def proses_pembayaran(pembayaran, jumlah):
    pembayaran.bayar(jumlah)


# Mengirim metode bayar berbeda
proses_pembayaran(Gopay(), 50000)
proses_pembayaran(Dana(), 75000)


# Variasi sendiri: abstract class bangun datar
class BangunDatar(ABC):
    @abstractmethod
    def luas(self):
        pass

    def info(self):  # method biasa tetap boleh ada di abstract class
        print(f"Luas {type(self).__name__}: {self.luas()}")


class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar


class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi


PersegiPanjang(8, 5).info()  # Luas PersegiPanjang: 40
Segitiga(6, 4).info()        # Luas Segitiga: 12.0


# Variasi sendiri: buktikan abstract class tidak bisa diinstansiasi
try:
    h = Hewan()
except TypeError as e:
    print("Error:", e)