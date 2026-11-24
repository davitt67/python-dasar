# ===== LIST (mutable) =====
buah = ["apel", "jeruk", "mangga"]

# Akses elemen
print(buah[0])  # apel

# Menambah elemen
buah.append("pisang")

# Mengubah elemen
buah[1] = "anggur"

# Menghapus elemen
buah.remove("mangga")

print(buah)  # ['apel', 'anggur', 'pisang']


# ===== TUPLE (immutable) =====
warna = ("merah", "hijau", "biru")

# Akses elemen
print(warna[1])  # hijau

# Tuple tidak bisa diubah
# warna[0] = "kuning"  # Error: TypeError

# Tapi bisa dibaca dengan loop
for w in warna:
    print(w)


# ===== SET (unik, tidak berurutan) =====
angka = {1, 2, 3, 3, 4, 5}
print(angka)  # {1, 2, 3, 4, 5} (duplikat otomatis hilang)

# Menambah dan menghapus elemen
angka.add(6)
angka.remove(2)
print(angka)  # {1, 3, 4, 5, 6}

# Operasi himpunan
ganjil = {1, 3, 5, 7}
genap = {2, 4, 6, 8}

print(ganjil | genap)  # Union: {1, 2, 3, 4, 5, 6, 7, 8}
print(ganjil & genap)  # Intersection: set()
print(ganjil - genap)  # Difference: {1, 3, 5, 7}


# Variasi sendiri: hapus duplikat dari list memakai set
nilai = [80, 90, 80, 70, 90, 100]
nilai_unik = list(set(nilai))
print("Nilai unik:", sorted(nilai_unik))  # [70, 80, 90, 100]

# Variasi sendiri: ubah tuple menjadi list lalu tambah elemen
hari = ("senin", "selasa")
hari_list = list(hari)
hari_list.append("rabu")
print(hari_list)  # ['senin', 'selasa', 'rabu']