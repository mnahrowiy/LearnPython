# tknik looping

nama_band = ['Payung Teduh',
             'Fourtwnty',
             'Dialog Dini Hari',
             'Mr. Sonjaya',
             'Parahyena',
             'Syahrini' # jika tidak ada temannya maka tidak akan ditampilkan
             ]
kumpulan_lagu = ['Akad',
                'Zona Nyaman',
                'Rumahku',
                'Sang Filsuf',
                'Sindoro',
                'jodohku'
                ]

# menampikan index-nya
# iterasi = 0
# for band in nama_band:
#     print('no:',iterasi,'nama_band',band)
#     iterasi +=1

# enumerate

for index,band in enumerate(nama_band): # nama "index bebas, bisa di ganti dengan otong"
    print(index,':',band)

# zip

for band,lagu in zip(nama_band,kumpulan_lagu):
    print(band,'menyanyikan lagu yang berjudul:',lagu)

# set

playlist ={'baby','ada apa dengan cinta','cenat-cenut','jarangoyang','gorgom','kuda','kucing'}

for lagu in sorted(playlist):
    print(lagu)


# dictionary
print(100*'=')

playlist2 ={'Payung teduh': 'akad',
            'Fourtwnty':'zona nyaman',
            'Dialog Dini Hari':'Rumahku'
            }

for i,v in playlist2.items(): # memasangkan # items untuk semua data
    print(i,'lagunya:',v)

for i in playlist2.keys(): # hanya menampilkan keys saja
    print(i)

for i in playlist2.values(): # hanya menampilkan values atau nilai
    print(i)

# fungsi reversed / membalik, tambahan aja ;-D

for i in reversed(range(1,10,1)): # range(10) ini juga bisa ;-D
    print(i)