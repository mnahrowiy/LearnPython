# set, himpunan
# isi set bisa campuran
superHero = set()

superHero.add("wiro sableng")
superHero.add("gundala")
superHero.add("saras 008")
superHero.add(212)

print(superHero)
# print(superHero[1]) tidak bisa di-index

ganjil = {1,3,5,7,9}
genap  = {2,4,6,8,10}
prima  = {2,3,5,7}

# metode himpunan seperti gabungan, irisan dll
print(ganjil.union(genap)) # union gabungan
print(genap.intersection(prima)) # irisan