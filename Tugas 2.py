# Input nilai alas, tinggi segitiga, dan tinggal limas
alas = int(input("Masukkan nilai alas segitiga: "))
tinggi_segitiga =  int(input("Masukkan nilai tinggi limas: "))

# Hitung volume limas segitiga
volume = (1/3) * (alas ** 2) * tinggi_segitiga * tinggi_segitiga

# Output hasil perhitungan
print("Volume limas segitiga adalah", volume)



# Input nilai jari-jari dan tinggi kerucut
jari_jari = int(input("Masukkan nilai jari-jari kerucut: "))
tinggi = int(input("Masukkan nilai jari-jari kerucut: "))

# Hitung volume kerucut
phi = 3.14
volume = (1/3) * (jari_jari ** 2) * tinggi

# Output hasil perhitungan
print("Volume kerucut adalh", volume)