def fbchi(n):
    if n == 2 or n == 1:
        return 1
    else:
        return fbchi(n-1) + fbchi(n-2)
try:
    print(fbchi(int(input(f'n='))))
except Exception:
    print(f'Error')