try:
    a = open('input2.txt','r')
except:
    print(f'file not found')
str = []
for i in a:
    str.append(i.split(' '))
a.close()
try:
    c = int(str[0][0])
    h = int(str[0][1])
    o = int(str[0][2])
except:
    print('usrerror')
    exit()
out = open('output.txt', 'w')
ans = min(c//2, h//6, o) 
out.write(f'{ans}')
out.close()
print(f'{ans}')
