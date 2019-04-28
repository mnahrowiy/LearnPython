# scope variabel : local
# berguna untuk proteksi variabel

namaKucing = 'cassandra' # global

def rubahNamaKucing(namaBaru):
    global namaKucing
    namaKucing = namaBaru
    print('saya rubah nama kucing menjadi ',namaKucing)

def kasihMakanKucing(makanan,nama):
    global namaKucing, makananKucing
    namaKucing    = nama
    makananKucing = makanan



rubahNamaKucing('katie')

kasihMakanKucing('universal','alex')

print('nama kucing saya menjadi ',namaKucing,' dan makan ',makananKucing)