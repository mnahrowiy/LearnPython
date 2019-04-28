# list
Ganjil = [1,3,5,7,9]

# tuple
Genap = (2,4,6,8,10)

print(type(Ganjil))
print(type(Genap))

"""
tuple tidak bisa diubah nilainya 
fungsi tuple berguna untuk sebuah data 
yang tidak bisa diubah seperti KTP, sensus penduduk, dll
dan ternyata tuple lebih ringan diproses dari pada lsit
"""
# contoh 1 // mencoba mengubah isi

# Ganjil[3] =11
# Genap[2]  =4 # ini tidak bisa, akan error karena ini tuple

# contoh 2 // mencoba dengan append
# Ganjil.append(12)
# Genap.append(11)

# print(Ganjil)
# print(Genap)
print(dir(Ganjil))
print(dir(Genap))

