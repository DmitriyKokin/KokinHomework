import time
from random import randint
def decorator(func):
    last = [time.time() - 20]
    def wrapper():
        f = open('out.txt', 'a')
        if time.time() - last[0] < 20:
            print(f'Please, wait ')
            while time.time() - last[0] < 20:
                time.sleep(0.1)
        last[0] = time.time()
        try:
            a = int(input(f'a = '))
            b = int(input(f'b = '))
            startTime = int(round(time.time() * 1000))
            time.sleep(randint(5,10))
            result = func(a, b)
            endTime = int(round(time.time() * 1000))
        except Exception:
            print(f'usrError')
            exit()
        f.write(f'addition was successfully calculated. Result:  {a+b}  Time: {endTime - startTime}ms\n')
        f.close()
        print(f'{endTime - startTime}ms')
        return result
    return wrapper

def sum(a=0, b=0):
    print(f'a = {a}, b = {b}\na + b = {a + b}')

sum_decorated = decorator(sum)
for i in range(3):
    sum_decorated()