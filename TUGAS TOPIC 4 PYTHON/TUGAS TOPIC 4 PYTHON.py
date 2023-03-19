#!/usr/bin/env python
# coding: utf-8

# In[1]:


# nama lengkap
nama_lengkap = "DIAH MUNICA NAWANG"

# hitung jumlah huruf dari nama lengkap
jumlah_huruf = len(nama_lengkap) - nama_lengkap.count(' ')

# hitung jumlah huruf vocal dari nama lengkap
huruf_vokal = 0
for huruf in nama_lengkap:
    if huruf.lower() in ['a', 'i', 'u', 'e', 'o']:
        huruf_vokal += 1

# hitung jumlah huruf konsonan dari nama lengkap
huruf_konsonan = 0
for huruf in nama_lengkap:
    if huruf.lower() not in ['a', 'i', 'u', 'e', 'o'] and huruf != ' ':
        huruf_konsonan += 1

# cetak hasil
print("Jumlah huruf dari nama lengkap DIAH MUNICA NAWANG adalah", jumlah_huruf)
print("Jumlah huruf vocal dari nama lengkap DIAH MUNICA NAWANG adalah", huruf_vokal)
print("Jumlah huruf konsonan dari nama lengkap DIAH MUNICA NAWANG adalah", huruf_konsonan)


# In[ ]:




