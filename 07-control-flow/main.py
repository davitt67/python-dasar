# Percabangan (if, elif, else)
nilai = 85

if nilai >= 90:
    print("A")
elif nilai >= 75:
    print("B")
else:
    print("C")
# Output: B

# Perulangan for
buah = ["apel", "jeruk", "mangga"]

for item in buah:
    print(item)

# Perulangan while
count = 0

while count < 5:
    print("Hitung:", count)
    count += 1

# Break dan Continue
for i in range(1, 6):
    if i == 3:
        continue  # lewati angka 3
    if i == 5:
        break     # hentikan loop saat i == 5
    print(i)
# Output: 1, 2, 4

# Variasi sendiri: cek bilangan genap/ganjil dari 1 sampai 10
for angka in range(1, 11):
    if angka % 2 == 0:
        print(angka, "genap")
    else:
        print(angka, "ganjil")

# Variasi sendiri: jumlahkan angka dengan while
total = 0
n = 1
while n <= 5:
    total += n
    n += 1
print("Total 1 sampai 5:", total)  # 15