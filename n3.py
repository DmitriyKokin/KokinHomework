def fbchi(n):
    if n == 2 or n == 1:
        return 1
    else:
        return fbchi(n-1) + fbchi(n-2)

try:
    print(f'{fbchi(int(input(f"n = ")))}') 
except:
    print(f'usrerror') 
# print(f'{fbchi(1)}')
# print(f'{fbchi(2)}')
# print(f'{fbchi(3)}')
# print(f'{fbchi(4)}')
# print(f'{fbchi(5)}')
# print(f'{fbchi(6)}')
# print(f'{fbchi(7)}')
# print(f'{fbchi(8)}')
# print(f'{fbchi(9)}')
