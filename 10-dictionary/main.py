# Membuat dictionary
mahasiswa = {
    "nama": "Budi",
    "umur": 20,
    "jurusan": "Informatika"
}

print(mahasiswa)  # {'nama': 'Budi', 'umur': 20, 'jurusan': 'Informatika'}


# Mengakses data
print(mahasiswa["nama"])       # Budi
print(mahasiswa.get("umur"))   # 20

# get() mengembalikan None jika key tidak ada (tidak error)
print(mahasiswa.get("alamat"))  # None


# Menambah dan mengubah data
mahasiswa["angkatan"] = 2023  # Menambah data baru
mahasiswa["umur"] = 21        # Mengubah value umur

print(mahasiswa)
# {'nama': 'Budi', 'umur': 21, 'jurusan': 'Informatika', 'angkatan': 2023}


# Menghapus data
mahasiswa.pop("jurusan")  # Menghapus dengan key
del mahasiswa["nama"]     # Menghapus dengan del

print(mahasiswa)  # {'umur': 21, 'angkatan': 2023}


# Iterasi dictionary
for key, value in mahasiswa.items():
    print(key, ":", value)


# Nested dictionary
kampus = {
    "mahasiswa1": {"nama": "Budi", "umur": 21},
    "mahasiswa2": {"nama": "Siti", "umur": 22}
}

print(kampus["mahasiswa1"]["nama"])  # Budi


# Variasi sendiri: hitung frekuensi huruf dalam sebuah kata
kata = "python"
frekuensi = {}
for huruf in kata:
    frekuensi[huruf] = frekuensi.get(huruf, 0) + 1
print("Frekuensi huruf:", frekuensi)

# Variasi sendiri: cek apakah key ada
if "umur" in mahasiswa:
    print("Key 'umur' ada, nilainya:", mahasiswa["umur"])