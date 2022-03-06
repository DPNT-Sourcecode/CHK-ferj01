# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter 

class InvalidItem(Exception):
    """Invalid item"""

class Product:
    """A shopping item"""
    item_price = 0
    offer_num = 0
    offer_price = 0

    def get_price(self, count):
        """Get the price, including any offers"""
        price = count * self.item_price
        if self.offer_num:
            price = self._calculate_offers(count)
        return price

    def _calculate_offers(self, count):
        """Calculate the offers"""
        in_offer = int(count / self.offer_num)
        out_offer = count % self.offer_num
        return (in_offer * self.offer_price) + (out_offer * self.item_price)

class ProductA(Product):
    """A"""
    item_price = 50
    offer_num = 3
    offer_price = 130

class ProductB(Product):
    """B"""
    item_price = 30
    offer_num = 2
    offer_price = 45

class ProductC(Product):
    """C"""
    item_price = 20
    offer_num = 0
    offer_price = 0

class ProductD(Product):
    """D"""
    item_price = 15
    offer_num = 0
    offer_price = 0

        

def checkout(skus):
    items = Counter([i for i in skus])
    try:
        _check_for_invalid_item(items)
    except InvalidItem:
        return -1

    total = 0
    for k, count in items.items():
        product = Product()
        price = product.get_price(count)
        total += price

    return total

def _check_for_invalid_item(items):
    """Checking for any invalid items"""
    for k in items.keys():
        if k not in ["A", "B", "C", "D"]:
            raise InvalidItem()



assert checkout("A") == 50
assert checkout("AA") == 100
assert checkout("AAA") == 130
assert checkout("AAAA") == 180
assert checkout("AAAAAA") == 260

