nama_barang = input('Masukkan nama barang: ')
harga_barang_1 = float(input("Masukkan harga barang 1: "))
harga_barang_2 = float(input("Masukkan harga barang 2: "))
total_belanja = float(input("Total belanja: "))


harga_barang = {
    'apel': 7000,
    'mangga': 8000,
    'durian': 9000
}

print(f"Nama Barang: {nama_barang}")
print(f"Harga Barang 1: {harga_barang_1}")
print(f"Harga Barang 2: {harga_barang_2}")
print(f"Total Belanja: {total_belanja}")

# Check if the item is in the harga_barang dictionary
if nama_barang in harga_barang:
    print(f"Harga {nama_barang}: {harga_barang[nama_barang]}")
else:
    print(f"{nama_barang} tidak ditemukan dalam daftar harga.")
nama_barang = input('Masukkan nama barang: ')
harga_barang_1 = float(input("Masukkan harga barang 1: "))
harga_barang_2 = float(input("Masukkan harga barang 2: "))
total_belanja = float(input("Total belanja: "))


harga_barang = {
    'apel': 7000,
    'mangga': 8000,
    'durian': 9000
}


print(f"Nama Barang: {nama_barang}")
print(f"Harga Barang 1: {harga_barang_1}")
print(f"Harga Barang 2: {harga_barang_2}")
print(f"Total Belanja: {total_belanja}")


if nama_barang in harga_barang:
    print(f"Harga {nama_barang}: {harga_barang[nama_barang]}")
else:
    print(f"{nama_barang} tidak ditemukan dalam daftar harga.")