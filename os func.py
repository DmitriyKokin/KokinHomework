from os import getlogin, listdir
from platform import platform
print(f'your OS platform: {platform()}')
print(f'you: {getlogin()}')
try:
    print(f'list files: {listdir(path = "/root")}')
except Exception:
    print(f'error')
    exit()