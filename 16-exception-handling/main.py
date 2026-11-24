# Menangani exception dengan try-except
# (Contoh tanpa exception handling akan menghentikan program, jadi dijadikan komentar)
# angka = 10
# hasil = angka / 0   # ZeroDivisionError: division by zero

try:
    angka = 10
    hasil = angka / 0
    print("Hasil:", hasil)
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")


# Menangani banyak jenis error
try:
    data = int("abc")  # akan memicu ValueError
except ValueError:
    print("Error: Data tidak valid!")
except ZeroDivisionError:
    print("Error: Tidak boleh membagi dengan nol!")


# Menggunakan else dan finally
try:
    angka = 10 / 2
except ZeroDivisionError:
    print("Error: Tidak bisa bagi nol!")
else:
    print("Perhitungan berhasil, hasil:", angka)  # dijalankan jika tidak ada error
finally:
    print("Selesai memproses.")  # selalu dijalankan


# Membuat exception sendiri dengan raise
def cek_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif!")
    else:
        print("Umur valid:", umur)


try:
    cek_umur(-5)
except ValueError as e:
    print("Error:", e)


# Variasi sendiri: input angka dari pengguna dengan validasi
try:
    angka_input = int(input("Masukkan sebuah angka: "))
    print("Kuadrat:", angka_input ** 2)
except ValueError:
    print("Input harus berupa angka!")
finally:
    print("Program selesai.")


# Variasi sendiri: menangkap beberapa error sekaligus
def bagi(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError) as e:
        print("Terjadi error:", e)
        return None


print(bagi(10, 2))     # 5.0
print(bagi(10, 0))     # Terjadi error: division by zero -> None
print(bagi(10, "a"))   # Terjadi error: unsupported operand type(s)... -> None


# Variasi sendiri: custom exception class
class SaldoTidakCukupError(Exception):
    pass


def tarik_saldo(saldo, jumlah):
    if jumlah > saldo:
        raise SaldoTidakCukupError("Saldo tidak mencukupi!")
    return saldo - jumlah


try:
    tarik_saldo(1000, 5000)
except SaldoTidakCukupError as e:
    print("Error:", e)