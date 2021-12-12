import random
import numpy as np
a = np.random.random((3, 3))
print(f'Матрица 3х3 со случайными значениями:\n{a}')
a = a.transpose()
print(f'Транспонированая матрица:\n{a}')