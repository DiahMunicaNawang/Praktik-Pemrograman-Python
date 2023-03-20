#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Membuat fungsi untuk menghitung FPB dua bilangan
def hitung_fpb(a, b):
    if b == 0:
        return a
    else:
        return hitung_fpb(b, a % b)

# Membuat fungsi untuk menghitung KPK dua bilangan
def hitung_kpk(a, b):
    kpk = a*b // hitung_fpb(a, b)
    return kpk

# Memulai program
print("Pilih operasi FPB atau KPK")
print("1. FPB")
print("2. KPK")

# Meminta input dari user
pilihan = int(input("Masukkan pilihan (1 atau 2): "))
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))

# Menampilkan hasil sesuai pilihan
if pilihan == 1:
    print("FPB dari", a, "dan", b, "adalah:", hitung_fpb(a, b))
elif pilihan == 2:
    print("KPK dari", a, "dan", b, "adalah:", hitung_kpk(a, b))
else:
    print("Pilihan tidak valid")


# In[2]:


# Membuat fungsi untuk menghitung FPB dua bilangan
def hitung_fpb(a, b):
    if b == 0:
        return a
    else:
        return hitung_fpb(b, a % b)

# Membuat fungsi untuk menghitung KPK dua bilangan
def hitung_kpk(a, b):
    kpk = a*b // hitung_fpb(a, b)
    return kpk

# Memulai program
print("Pilih operasi FPB atau KPK")
print("1. FPB")
print("2. KPK")

# Meminta input dari user
pilihan = int(input("Masukkan pilihan (1 atau 2): "))
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))

# Menampilkan hasil sesuai pilihan
if pilihan == 1:
    print("FPB dari", a, "dan", b, "adalah:", hitung_fpb(a, b))
elif pilihan == 2:
    print("KPK dari", a, "dan", b, "adalah:", hitung_kpk(a, b))
else:
    print("Pilihan tidak valid")


# In[ ]:




