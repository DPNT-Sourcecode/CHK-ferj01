# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter 

class InvalidItem(Exception):
    """Invalid item"""

class Product:
    """A shopping item"""

    item_price = 50
    offer_num = 3

    def __init__(self, count) -> None:
        self.count = count

    def get_price(self):
        """Get the price, including any offers"""
        price = self.count * self.item_price
        

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



assert checkout("ABACDDD") == 0




