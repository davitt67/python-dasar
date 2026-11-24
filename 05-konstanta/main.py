# Konvensi penulisan konstanta: HURUF KAPITAL SEMUA
PI = 3.14159
MAX_USERS = 100
APP_NAME = "Aplikasi Belajar Python"

print(PI)
print(MAX_USERS)
print(APP_NAME)

# Konstanta dengan lebih dari satu kata: pakai underscore
MAX_LOGIN_ATTEMPT = 5
print("Maksimum percobaan login:", MAX_LOGIN_ATTEMPT)

# Secara teknis nilai bisa diubah, tapi sebaiknya TIDAK dilakukan
# PI = 3.14  # jangan lakukan ini, hanya konvensi

# Konstanta di dalam module (diimpor dari constants.py)
from constants import PI as PI_MODULE, GRAVITY, MAX_RETRY

print("Nilai PI:", PI_MODULE)
print("Gravitasi:", GRAVITY)
print("Maksimum Percobaan:", MAX_RETRY)

# Contoh penggunaan konstanta untuk perhitungan
TAX_RATE = 0.1  # 10 persen

harga_barang = 50000
total = harga_barang + (harga_barang * TAX_RATE)

print("Total harga:", total)

# Variasi sendiri: hitung luas lingkaran memakai konstanta PI
jari_jari = 7
luas = PI_MODULE * jari_jari ** 2
print("Luas lingkaran:", luas)