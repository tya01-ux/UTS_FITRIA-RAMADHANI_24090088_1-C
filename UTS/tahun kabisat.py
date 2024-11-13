tahun = int(input('Masukkan tahun: '))

if (tahun / 400 == 0) or (tahun / 4 == 0 and tahun / 100 == 0):
    print(f"{tahun} merupakan tahun kabisat.")
else:
    print(f"{tahun} bukan merupakan tahun kabisat.")