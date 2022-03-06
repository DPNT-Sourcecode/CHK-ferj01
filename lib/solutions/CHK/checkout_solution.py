# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter 

class InvalidItem(Exception):
    """Invalid item"""

class Product:
    """A shopping item"""

    item_price = 50
    offer_num = 3
    offer_price = 130

    def get_price(self, count):
        """Get the price, including any offers"""
        price = count * self.item_price
        if self.offer_num:
            price = self._calculate_offers(count)
        return price

    def _calculate_offers(self, count):
        """Calculate the offers"""
        mod = count / self.offer_num
        rem = count % self.offer_num
        return (mod * self.offer_price) + (rem * self.item_price)

        

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





