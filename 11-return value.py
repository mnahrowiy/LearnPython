# fungsi dengan return
def kuadrat(argumen):
    total = argumen**2
    print('nilai kuadrat dari argument adalah ',total)
    return total

a = kuadrat(3)
print(a)

print("+"*100)

def tambah(argumen1,argumen2):
    total = argumen1 + argumen2
    print(argumen1,"+",argumen2,'=',total)
    return total

def kali(argumen1,argumen2):
    total = argumen1 * argumen2
    print(argumen1,"*",argumen2,'=',total)
    return total

a = kali(4,tambah(3,tambah(3,4)))
print(a)