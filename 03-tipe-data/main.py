# Integer (int)
umur = 25
print(type(umur))  # <class 'int'>

# Float
tinggi = 170.5
print(type(tinggi))  # <class 'float'>

# String (str)
nama = "Andi"
print(type(nama))  # <class 'str'>

# Boolean (bool)
is_active = True
print(type(is_active))  # <class 'bool'>

# List (mutable, bisa diubah)
buah = ["apel", "jeruk", "mangga"]
print(type(buah))  # <class 'list'>
buah.append("pisang")
print(buah)

# Tuple (immutable, tidak bisa diubah)
warna = ("merah", "hijau", "biru")
print(type(warna))  # <class 'tuple'>

# Dictionary (pasangan key-value)
mahasiswa = {"nama": "Budi", "umur": 21, "jurusan": "Informatika"}
print(type(mahasiswa))  # <class 'dict'>
print(mahasiswa["nama"])

# Set (elemen unik, tanpa duplikat)
angka = {1, 2, 3, 3, 4}
print(angka)  # {1, 2, 3, 4}
print(type(angka))  # <class 'set'>

# Konversi tipe data
x = 10
y = float(x)  # konversi ke float
z = str(x)    # konversi ke string
print(y, type(y))  # 10.0 <class 'float'>
print(z, type(z))  # '10' <class 'str'>

# Variasi sendiri: konversi string ke integer
teks = "123"
angka_int = int(teks)
print(angka_int + 7, type(angka_int))  # 130 <class 'int'>