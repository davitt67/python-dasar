# Operator Aritmatika
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3 (pembagian bulat)
print(a % b)   # 1 (sisa bagi)
print(a ** b)  # 1000 (pangkat)

# Operator Perbandingan
x = 5
y = 10

print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= y)  # False
print(x <= y)  # True

# Operator Logika
p = True
q = False

print(p and q)  # False
print(p or q)   # True
print(not p)    # False

# Operator Penugasan
n = 10

n += 5
print(n)  # 15

n -= 3
print(n)  # 12

n *= 2
print(n)  # 24

n /= 4
print(n)  # 6.0

# Operator Keanggotaan (Membership)
buah = ["apel", "jeruk", "mangga"]

print("apel" in buah)       # True
print("pisang" not in buah)  # True

# Operator Identitas
m = [1, 2, 3]
k = m
c = [1, 2, 3]

print(m is k)   # True (menunjuk objek yang sama)
print(m is c)   # False (objek berbeda walau isinya sama)
print(m == c)   # True (nilai isinya sama)

# Variasi sendiri: cek bilangan genap dan dalam rentang
angka = 18
print("Genap:", angka % 2 == 0)
print("Dalam rentang 10-20:", angka >= 10 and angka <= 20)