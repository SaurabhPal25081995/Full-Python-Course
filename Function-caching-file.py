import time
from functools import lru_cache

@lru_cache(maxsize=3)
def some_work(n):
    time.sleep(n)
    return n

print("Now running some work")
some_work(3)
print("Done 3 calling again...")
some_work(2)
print("Done 2 calling again...")
some_work(1)
print("Done 1 calling again...")
some_work(3)
print("Done 3 calling again...")
some_work(2)
print("Done 2 calling again...")
some_work(1)
print("Done 1")
some_work(5)
print("Done 5")

