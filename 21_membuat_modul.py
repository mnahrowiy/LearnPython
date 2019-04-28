# # singkat penulisan modul dengan as
# import matematika as m
#
# m.tambah(2,4)
# m.kurang(7,2)

# from matematika import tambah # hanya tambah
# from matematika import kurang # hanya kurang
# from matematika import tambah,kurang # jika ingin menambah fungsi dari dalam modul
# from matematika import kurang as k # menyingkat nama
from matematika import tambah as t
t(3,7)
t(2,4)

