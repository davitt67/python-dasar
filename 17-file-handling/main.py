# Menulis ke file (mode "w": buat file baru atau timpa file lama)
file = open("data.txt", "w")
file.write("Halo, ini data baru!\n")
file.write("Baris kedua...\n")
file.close()

# Membuka dan membaca seluruh isi file (mode "r")
file = open("data.txt", "r")
print(file.read())
file.close()

# Membaca file baris per baris
file = open("data.txt", "r")
for baris in file:
    print(baris.strip())  # strip() untuk hapus newline
file.close()

# Menambah data di akhir file (mode "a")
file = open("data.txt", "a")
file.write("Baris tambahan...\n")
file.close()

# Menggunakan with (best practice, file otomatis tertutup)
with open("data.txt", "r") as file:
    isi = file.read()
    print(isi)


# Contoh program lengkap
# Menulis file
with open("contoh.txt", "w") as file:
    file.write("Belajar Python itu menyenangkan!\n")

# Menambah data
with open("contoh.txt", "a") as file:
    file.write("Tambahan baris kedua.\n")

# Membaca file
with open("contoh.txt", "r") as file:
    for baris in file:
        print(baris.strip())


# Variasi sendiri: menyimpan daftar ke file lalu membacanya dengan nomor baris
buah = ["apel", "jeruk", "mangga"]

with open("buah.txt", "w") as file:
    for item in buah:
        file.write(item + "\n")

with open("buah.txt", "r") as file:
    for nomor, baris in enumerate(file, start=1):
        print(f"{nomor}. {baris.strip()}")


# Variasi sendiri: membaca file yang tidak ada dengan exception handling
try:
    with open("tidak_ada.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File tidak ditemukan!")