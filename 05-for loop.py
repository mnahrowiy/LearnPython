gorengan = ['bakwan','cireng','tahu isi','tempe goreng','ubi goreng']

# for isi in gorengan: # g itu variabel baru
#     print(isi)
#     print(len(isi))
#
# # string sebagai iterable
#
# bakwan = 'bakwan'
# for i in bakwan:
#     print(i)


# for di dalam for

buah  = ['semangka','jeruk','apel','anggur']
sayur = ['kangkung','wortel','tomat','kentang']

DaftarBelanja = [gorengan,buah,sayur]

for subDaftarBelanja in DaftarBelanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)




# hanya perbandingan
# bahasa c++
# for (int 1=0; i<gorengan.length;i++){
#     cout << gorengan[i];
#
# }

