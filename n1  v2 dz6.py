def encoder(arr):
    """Функция кодирует строку, переданную в качестве аргумента
       Возвращает закодированную версию строки
       """
    for i in range(len(arr)):
        arr[i] = arr[i].encode('utf-8')
    return arr
def decoder(arr):
    """Функция декодирует строку, переданную в качестве аргумента
       Возвращает раскодированную версию строки
       """
    for i in range(len(arr)):
        arr[i] = arr[i].decode('utf-8')
    return arr
try:
    n = int(input(f'n = '))
except Exception:
    print('usererror')
    exit()
a = []
for i in range(n):
    a.append(input(f'str № {i+1} = '))
b = encoder(a)
print(f'byte string:\n{b}')
b = decoder(b)
print(f'decode string:\n{b}')
