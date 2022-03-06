# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter 

class InvalidItem(Exception):
    """Invalid item"""

def checkout(skus):
    items = Counter([i for i in skus])


    try:
        _check_for_invalid_item(items)
    except InvalidItem:
        return -1

    return 0

def _check_for_invalid_item(items):
    """Checking for any invalid items"""
    for k in items.keys():
        if k not in ["A", "B", "C", "D"]:
            raise InvalidItem()



print(checkout("ABACDDD"))



