from __test import *
from multiprocessing import Process
from time import time

jobs = []

tm = time()

# for i in range(10):
#     p = Process(target=count, args=(1, 1))
#     jobs.append(p)
#     p.start()
#
# for i in jobs:
#     i.join()
#
# print("Process CPU:", time() - tm)  # Process CPU: 4.836609840393066

for i in range(10):
    p = Process(target=io)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()

print("Process IO:", time() - tm)
