# Menggunakan module buatan sendiri
import matematika

print(matematika.tambah(2, 3))  # 5
print(matematika.kali(4, 5))    # 20


# Import dengan alias
import matematika as m

print(m.tambah(10, 5))  # 15


# Import fungsi tertentu
from matematika import tambah

print(tambah(7, 3))  # 10


# Built-in module: math
import math

print(math.sqrt(16))  # 4.0
print(math.pi)        # 3.141592653589793


# Variasi sendiri: memakai fungsi tambahan dari module sendiri
print(m.kurang(10, 4))  # 6
print(m.kuadrat(9))     # 81


# Variasi sendiri: hitung luas lingkaran dengan math.pi
jari_jari = 7
luas = math.pi * jari_jari ** 2
print("Luas lingkaran:", round(luas, 2))  # 153.94


# Variasi sendiri: built-in module lain
import random
import datetime

print("Angka acak 1-10:", random.randint(1, 10))
print("Tanggal hari ini:", datetime.date.today())