# fungsi dengan menggunakan argumen sederhana

def siswa(nama):
    print('siswa ini bernama : ',nama)

siswa('mario')

# fungsi dengan menggunakan keywords arguments

def guru(nama,pelajaran):
    print('guru ini bernama : ',nama)
    print('mengajar         : ',pelajaran)

guru(nama='popong',pelajaran='seni rupa')
guru(pelajaran = 'olah raga',nama='endang')
guru('olahraga','raihan') # ini contoh yang salah

# fungsi dengan menggunakan default aruments

def penjagaSekolah(nama,shift='siang',galak='tidak'):
    # kalau tidak punya default maka wajib di isi
    # jika punya defaul bila kosaong maka defaul akan di tampilkan
    print('penjaga sekolah ini bernama : ', nama)
    print('shiftnya                    : ', shift)
    print('galak ?                     : ',galak)

penjagaSekolah('Entis')
penjagaSekolah('Maman',shift='malam')
penjagaSekolah('Asep',galak='sangat')
