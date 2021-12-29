from __test import *
from time import time

tm = time()

for i in range(10):
    # count(1, 1)
    io()

# print("Signal CPU:", time() - tm)  # Signal CPU: 6.685747861862183
print("Signal IO:", time() - tm)  # Signal IO: 9.449385404586792
