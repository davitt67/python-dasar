# Membuat class dan object
class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def sapa(self):
        print(f"Halo, nama saya {self.nama} dari jurusan {self.jurusan}")


# Membuat object dari class Mahasiswa
mhs1 = Mahasiswa("Budi", "Informatika")
mhs2 = Mahasiswa("Siti", "Sistem Informasi")

# Memanggil method
mhs1.sapa()
mhs2.sapa()


# Atribut dan method
class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)


pp = PersegiPanjang(5, 3)
print("Luas:", pp.luas())          # 15
print("Keliling:", pp.keliling())  # 16


# Encapsulation (menyembunyikan data)
class BankAccount:
    def __init__(self, saldo):
        self.__saldo = saldo  # private attribute

    def lihat_saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        self.__saldo += jumlah


akun = BankAccount(1000)
akun.setor(500)
print("Saldo:", akun.lihat_saldo())  # 1500

# Atribut private tidak bisa diakses langsung dari luar class
# print(akun.__saldo)  # Error: AttributeError


# Variasi sendiri: tambah method tarik dengan pengecekan saldo
class Dompet:
    def __init__(self, saldo):
        self.__saldo = saldo

    def tarik(self, jumlah):
        if jumlah > self.__saldo:
            print("Saldo tidak cukup")
        else:
            self.__saldo -= jumlah
            print(f"Berhasil menarik {jumlah}")

    def lihat_saldo(self):
        return self.__saldo


dompet = Dompet(2000)
dompet.tarik(500)   # Berhasil menarik 500
dompet.tarik(5000)  # Saldo tidak cukup
print("Sisa saldo:", dompet.lihat_saldo())  # 1500