Barang = ['kunci','ember','jaket','ban','mobil']
print(Barang)

# beberapa method yang bisa digunakan u tuk meanipulasi list
# menambah data di ujung
Barang.append('sepeda')
print(Barang)

# fungsi extend pengganti iterebale
Barang.extend('dompet')
print(Barang)

# menambah data dengan meyisipkan urutan yang kita inginkan
# insert
Barang.insert(3,'sepeda')
print(Barang)

# method untuk menghitung anggota
jumlahSepeda = Barang.count('sepeda')
print('Jumlah sepeda adalah : ',jumlahSepeda)

# remove data

Barang.remove('sepeda')
print(Barang)
# remove akan me-remove data yg pertama ditemukan
# maka data di index ke-3 akan hilang

# reverse
# membalik urutan
Barang.reverse()
print(Barang)

# copy
# untuk data tidak saling membagikan reperence
print('='*100)

# stuff = Barang  # ini akan membagi data list yang sama dan akan juga mengubah data pada list Barang
# solusi dengan menggunakan copy()
stuff = Barang.copy() # stuff hanya mencopy data di Barang
stuff.append('gelas') # hanya data stuff yang bertambah
print(stuff)
print(Barang)
