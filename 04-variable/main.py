# Membuat variable
nama = "Andi"
umur = 25
tinggi = 170.5
is_active = True

print(nama)       # Andi
print(umur)       # 25
print(tinggi)     # 170.5
print(is_active)  # True

# Aturan penamaan: gunakan snake_case
first_name = "Budi"
total_harga = 10000
print(first_name, total_harga)

# Contoh penamaan yang SALAH (jangan dijalankan, hanya sebagai catatan):
# 2nama = "Salah"        # diawali angka
# class = "Informatika"  # keyword Python

# Multiple assignment
a, b, c = 10, 20, 30
print(a, b, c)  # 10 20 30

# Nilai yang sama untuk beberapa variable
x = y = z = 100
print(x, y, z)  # 100 100 100

# Mengecek tipe data variable
print(type(nama))    # <class 'str'>
print(type(umur))    # <class 'int'>
print(type(tinggi))  # <class 'float'>

# Menghapus variable
p = 10
print(p)  # 10
del p
# print(p)  # Error: variable sudah dihapus

# Variasi sendiri: swap nilai dua variable
m, n = 5, 9
m, n = n, m
print("Setelah ditukar:", m, n)  # 9 5