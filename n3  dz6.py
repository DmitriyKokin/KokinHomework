def encrypt(text, key):
    """Функция на вход получает строку и ключ
       На основе которого будет выполнено шифрование XOR
       Возвращает закодированну/раскодированную строку
       """
    encript_str = ""
    for letter in text:
        encript_str += chr(ord(letter) ^ key)
    return  encript_str   
mytext = ''
try:
    a = open('input3.txt', 'r')
    mytext = a.read()
except Exception:
    print(f'file not found')
    exit()
a.close()
print(f'Текст, прочитанный из файла:\n{mytext}\n')
try:
    key = int(input(f'Введите ключ шифрования..(int)'))
except Exception:
    print(f'Unknown Error')
    exit()
e = encrypt(mytext, key)
out = open('output3.txt', 'w')
out.write(f'{e}')
print(f'encrypt(x2):\n{encrypt(e, key)}')
out.close()



