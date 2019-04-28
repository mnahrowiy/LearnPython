# dictionary

member1 = {"ID":101,
           "Nama":"Faqihza Mukhlish",
           "Pekerjaan":"Mahasiswa",
           "Status member":"Gold"
           }


member2 = {"ID":102,
           "Nama":"Ujang Pintu",
           "Pekerjaan": "reprasi pintu",
           "Status member":"Berlian"
           }
member_list = {101:member1,102:member2}

# print(member1["Pekerjaan"])
# print(member1.keys())
# print(member1.values())
# print(member1.items())

# dia mengambil data dari data 101
print(member_list[101]) # ini bisa menjadi sebuah database