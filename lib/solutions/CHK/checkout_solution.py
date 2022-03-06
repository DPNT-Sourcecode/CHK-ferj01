# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter 

class InvalidItem(Exception):
    """Invalid item"""

class Product:
    """A shopping item"""
    item_price = 0
    offers = {}

    def get_price(self, count):
        """Get the price, including any offers"""
        price = count * self.item_price
        if self.offers:
            price = self._calculate_offers(count)
        return price

    def _calculate_offers(self, count):
        """Calculate the offers"""
        offer_nums = list(self.offers.keys())
        offer_nums = sorted(offer_nums, key=int, reverse=True)

        remaining = count
        total = 0
        for offer_num in offer_nums:
            if remaining < offer_num:
                continue

            in_offer = int(remaining / offer_num)
            remaining = count % offer_num
            total += (in_offer * self.offers[offer_num])


        return total + (remaining * self.item_price)

class ProductA(Product):
    """A"""
    item_price = 50
    offers = {3: 130, 5:200}

class ProductB(Product):
    """B"""
    item_price = 30
    offers = {2: 45}

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

PRODUCT_MAP = {
    "A": ProductA(),
    "B": ProductB(),
    "C": ProductC(),
    "D": ProductD(),
}


def checkout(skus):
    items = Counter([i for i in skus])
    try:
        _check_for_invalid_item(items)
    except InvalidItem:
        return -1

    total = 0
    for k, count in items.items():
        product = PRODUCT_MAP[k]
        total += product.get_price(count)

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
assert checkout("AAAAA") == 200
assert checkout("AAAAAA") == 250

assert checkout("B") == 30
assert checkout("BB") == 45
assert checkout("BBB") == 75
assert checkout("BBBB") == 90
assert checkout("BBBBB") == 120

assert checkout("C") == 20
assert checkout("CC") == 40
assert checkout("CCC") == 60
assert checkout("CCCC") == 80

assert checkout("D") == 15
assert checkout("DD") == 30
assert checkout("DDD") == 45
assert checkout("DDDD") == 60

assert checkout("AABBCCDD") == 100 + 45 + 40 + 30





