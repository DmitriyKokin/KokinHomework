def encrypt(text, key):
    encript_str = ""
    for letter in text:
        encript_str += chr(ord(letter) ^ key )
    return  encript_str   
mytext = ''
try:
    a = open('input3.txt','r')
    mytext = a.read()
except:
    print(f'file not found')
    exit()
a.close()
print(f'Текст, прочитанный из файла:\n{mytext}\n')
try:
    key = int(input(f'Введите ключ шифрования..(int)'))
except:
    print(f'Unknown Error')
    exit()
e = encrypt(mytext, key)
out = open('output3.txt', 'w')
out.write(f'{e}')
print(f'encrypt(x2):\n{encrypt(e, key)}')
out.close()



