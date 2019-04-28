from PIL import Image

im = Image.open("saya.jpg")

print("format file: ", im.format)
print("ukuran file: ", im.size)
print("mode file  : ", im.mode)

im.show()
