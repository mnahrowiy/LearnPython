"""
while argumen:
     statement
"""

angka = 0

while angka < 5:
    print('nilai angka adalah : ',angka)
    angka = angka + 1

print('di luar while')

# tipe while dengan boolean

start = True
angka = 0

while start:
    print("di dalam while")
    if angka is 100:
        start = False
        print('oke angka 100 ditemukan')
    angka +=1