# Menggunakan package
from my_package import operasi, geometri

print(operasi.kurang(10, 4))      # 6
print(geometri.luas_persegi(5))   # 25


# Import fungsi tertentu dari package
from my_package.operasi import kurang
from my_package.geometri import luas_persegi

print(kurang(20, 7))     # 13
print(luas_persegi(8))   # 64


# Package di Python Standard Library
import os
import datetime

print(os.getcwd())             # Menampilkan direktori kerja saat ini
print(datetime.date.today())   # Menampilkan tanggal hari ini


# Variasi sendiri: memakai fungsi tambahan dari package
print(operasi.tambah(3, 9))                      # 12
print(geometri.luas_persegi_panjang(6, 4))       # 24


# Variasi sendiri: package json bawaan Python
import json

data = {"nama": "Budi", "umur": 20}
teks_json = json.dumps(data)
print(teks_json)                    # {"nama": "Budi", "umur": 20}
print(json.loads(teks_json)["nama"])  # Budi


# Variasi sendiri: daftar isi folder dengan os
print(os.listdir("."))