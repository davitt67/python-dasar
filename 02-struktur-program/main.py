# Contoh statement dan output dasar
print("Hello, Python!")  # Fungsi print untuk mencetak teks

# Ini adalah komentar satu baris

"""
Ini komentar multi-baris.
Biasa dipakai untuk dokumentasi.
"""

# Indentasi: blok kode ditandai spasi (4 spasi)
if True:
    print("Kode ini berada di dalam blok if")
    print("Masih di dalam blok if")
print("Kode ini sudah di luar blok if")

# Input dan output dasar
nama = input("Masukkan nama Anda: ")
print("Halo,", nama)


# Struktur program dengan fungsi main
def main():
    print("Hello dari fungsi main!")


if __name__ == "__main__":
    main()