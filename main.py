def rata2(arr):
    hasil = 0
    for i in arr:
        hasil += i
    return hasil / len(arr)


def sum(arr):
    hasil = 0
    for i in arr:
        hasil += i
    return hasil


container = []
while True:
    ipt = input('masukkan nilai : ')
    try:
        ipt = int(ipt)
    except Exception:
        print('galat hanya bisa input bilangan')
        continue
    if ipt == 0:
        break
    container.append(ipt)

print('inputan = ',container)
print('total = ', sum(container))
print('banyak inputan = ',len(container))
print('rata2 = ',rata2(container))

