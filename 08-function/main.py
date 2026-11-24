# Membuat function sederhana
def sapa():
    print("Halo, selamat datang di Python!")

# Memanggil function
sapa()


# Function dengan parameter
def sapa_nama(nama):
    print(f"Halo {nama}, semoga harimu menyenangkan!")

sapa_nama("Budi")
sapa_nama("Siti")


# Function dengan return value
def tambah(a, b):
    return a + b

hasil = tambah(5, 7)
print("Hasil penjumlahan:", hasil)  # 12


# Default parameter
def sapa_orang(nama="Teman"):
    print(f"Halo {nama}!")

sapa_orang("Andi")  # Menggunakan parameter
sapa_orang()        # Menggunakan default


# *args (banyak argumen non-keyword)
def jumlahkan(*angka):
    total = sum(angka)
    print("Total:", total)

jumlahkan(1, 2, 3, 4, 5)  # Bisa input banyak angka


# **kwargs (banyak argumen keyword)
def biodata(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

biodata(nama="Budi", umur=20, kota="Jakarta")


# Variasi sendiri: function untuk menghitung luas persegi panjang
def luas_persegi_panjang(panjang, lebar=1):
    return panjang * lebar

print("Luas:", luas_persegi_panjang(8, 5))  # 40
print("Luas (lebar default):", luas_persegi_panjang(8))  # 8