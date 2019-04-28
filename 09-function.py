"""
# function ini untuk membuat program yang sama tidak berulang-ulang

# ini dalah cara mendefinisikan fungsi
def fungsi():
    print('ini adalah fungsi')

# manggil fungsi
fungsi()
fungsi()
fungsi()
"""

# membuat fungsi sederhana

def suaraAyam():
    print('kukuruyuuk!!!')

def hargaAyam():
    suaraAyam()
    print("harga ayam per 1 kg adalah Rp. 20.000")

# membuat fungsi dengan input argument

def hargaTotalAyam(kg):
    suaraAyam()
    harga = 20000
    hargaTotal = kg*harga
    print('harga ',kg,'ayam adalah',hargaTotal)

hargaAyam()
hargaTotalAyam(2)
hargaTotalAyam(4)
hargaTotalAyam(5)
hargaTotalAyam(0.5)

