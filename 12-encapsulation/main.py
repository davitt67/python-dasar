# Public, Protected, dan Private
class Contoh:
    def __init__(self):
        self.nama = "Public"         # public: bisa diakses dari mana saja
        self._elemen = "Protected"   # protected: konvensi, jangan diakses dari luar
        self.__saldo = "Private"     # private: tidak bisa langsung diakses dari luar

    def lihat_private(self):
        return self.__saldo


c = Contoh()
print(c.nama)            # Public
print(c._elemen)         # Protected (masih bisa, tapi tidak dianjurkan)
print(c.lihat_private())  # Private (lewat method)
# print(c.__saldo)       # Error: AttributeError


# Contoh encapsulation dengan private attribute
class BankAccount:
    def __init__(self, saldo_awal):
        self.__saldo = saldo_awal  # private attribute

    # getter
    def lihat_saldo(self):
        return self.__saldo

    # setter
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
        else:
            print("Jumlah setor harus positif!")

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup atau jumlah tidak valid!")


# Membuat objek
akun = BankAccount(1000)

# Mengakses saldo lewat method (bukan langsung)
print("Saldo awal:", akun.lihat_saldo())  # 1000

akun.setor(500)
print("Setelah setor:", akun.lihat_saldo())  # 1500

akun.tarik(300)
print("Setelah tarik:", akun.lihat_saldo())  # 1200


# Variasi sendiri: uji validasi
akun.setor(-100)   # Jumlah setor harus positif!
akun.tarik(9999)   # Saldo tidak cukup atau jumlah tidak valid!


# Variasi sendiri: getter dan setter dengan @property
class Siswa:
    def __init__(self, nama, nilai):
        self.__nama = nama
        self.__nilai = nilai

    @property
    def nilai(self):
        return self.__nilai

    @nilai.setter
    def nilai(self, nilai_baru):
        if 0 <= nilai_baru <= 100:
            self.__nilai = nilai_baru
        else:
            print("Nilai harus antara 0 sampai 100")


siswa = Siswa("Andi", 80)
print("Nilai:", siswa.nilai)  # 80
siswa.nilai = 95
print("Nilai baru:", siswa.nilai)  # 95
siswa.nilai = 150             # Nilai harus antara 0 sampai 100