# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter 

def checkout(skus):
    items = [i for i in skus]
    print(Counter(items))



checkout("ABACDDD")


