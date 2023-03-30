def main():
    pilihan = int(input("Masukkan pilihan bangun datar yang ingin di hitung luasnya: "))

    if pilihan == 1:
        sisi = float(input("Masukkan panjang sisi persegi: "))
        luas = sisi ** 2
        print("Luas persegi adalah", luas)

    elif pilihan == 2:
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        luas = panjang * lebar
        print("Luas persegi panjang adalah", luas)

    elif pilihan == 3:
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = 0.5 * alas * tinggi
        print("Luas segitiga adalah", luas)

    elif pilihan == 4:
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        luas = 3.14 * jari_jari ** 2
        print("Luas lingkaran adalah", luas)

    elif pilihan == 5:
        alas = float(input("Masukkan panjang alas jajar genjang: "))
        tinggi = float(input("Masukkan tinggi jajar genjang: "))
        luas = alas * tinggi
        print("Luas jajar genjang adalah", luas)

    elif pilihan == 6:
        sisi_sejajar1 = float(input("Masukkan panjang sisi sejajar 1 trapesium: "))
        sisi_sejajar2 = float(input("Masukkan panjang sisi sejajar 2 trapesium: "))
        tinggi = float(input("Masukkan tinggi trapesium: "))
        luas = 0.5 * (sisi_sejajar1 + sisi_sejajar2) * tinggi
        print("Luas trapesium adalah", luas)

    else:
        print("Pilihan tidak valid")


if __name__ == '__main__':
    main()
