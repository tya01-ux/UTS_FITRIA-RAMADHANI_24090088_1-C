berat_badan = int(input('Masukkan berat badan (kg): '))
tinggi_badan = int(input('Masukkan tinggi badan (cm): '))

bmi_ideal = 22
ideal = bmi_ideal * (tinggi_badan / 100) ** 2

kelebihan_berat_badan = berat_badan - ideal

if berat_badan >= 18.5 and tinggi_badan >= 160 and kelebihan_berat_badan >= 1:
    print('Berat badan ideal')
else:
    print('Berat badan tidak ideal')