def main():
    print("Program Menghitung Volume dan Luas Permukaan Bangun Ruang")
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    print("4. Kerucut")
    print("5. Limas Segiempat")
    print("6. Prisma Segitiga")

pilihan = int(input("Tentukan pilihan bangun ruang:\n1. Kubus\n2. Balok\n3. Tabung\n4. Kerucut\n5. Limas segiempat\n6. Prisma segitiga\n\nPilihan: "))

if pilihan == 1:
    sisi = float(input("Masukkan panjang sisi kubus: "))
    volume = sisi ** 3
    print("Volume kubus adalah", volume)
elif pilihan == 2:
    panjang = float(input("Masukkan panjang balok: "))
    lebar = float(input("Masukkan lebar balok: "))
    tinggi = float(input("Masukkan tinggi balok: "))
    volume = panjang * lebar * tinggi
    print("Volume balok adalah", volume)
elif pilihan == 3:
    jari_jari = float(input("Masukkan jari-jari tabung: "))
    tinggi = float(input("Masukkan tinggi tabung: "))
    volume = 3.14 * jari_jari ** 2 * tinggi
    print("Volume tabung adalah", volume)
elif pilihan == 4:
    jari_jari = float(input("Masukkan jari-jari kerucut: "))
    tinggi = float(input("Masukkan tinggi kerucut: "))
    volume = 1/3 * 3.14 * jari_jari ** 2 * tinggi
    print("Volume kerucut adalah", volume)
elif pilihan == 5:
    alas = float(input("Masukkan panjang alas limas: "))
    tinggi_segitiga = float(input("Masukkan tinggi segitiga pada alas limas: "))
    tinggi_limas = float(input("Masukkan tinggi limas: "))
    volume = 1/3 * alas ** 2 * tinggi_segitiga * tinggi_limas
    print("Volume limas adalah", volume)
elif pilihan == 6:
    alas = float(input("Masukkan panjang alas prisma: "))
    tinggi_alas = float(input("Masukkan tinggi alas prisma: "))
    tinggi_prisma = float(input("Masukkan tinggi prisma: "))
    volume = alas * tinggi_alas * tinggi_prisma
    print("Volume prisma adalah", volume)
