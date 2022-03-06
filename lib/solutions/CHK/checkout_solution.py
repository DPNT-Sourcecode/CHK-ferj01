# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter 

class InvalidItem(Exception):
    """Invalid item"""

class Product:
    """A shopping item"""
    item_price = 0
    offers = {}
    freebies = {}


    def calculate_price(self, count, freebie_count):
        """Calculate the price"""
        original_price = self._get_price(count)
        if not freebie_count:
            return original_price

        new_count = count - freebie_count
        if new_count < 0:
            new_count = 0

        new_price = self._get_price(new_count)
        return min(original_price, new_price)

    def get_freebies(self, count):
        """Get any freebies on offer"""
        free = {}
        for num, item in self.freebies.items():
            product_count = int(count / num)
            free[item] = product_count

        return free

    def _get_price(self, count):
        """Get the price"""
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
            remaining = remaining % offer_num
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

class ProductD(Product):
    """D"""
    item_price = 15

class ProductE(Product):
    """E"""
    item_price = 40
    freebies = {2: "B"}

PRODUCT_MAP = {
    "A": ProductA(),
    "B": ProductB(),
    "C": ProductC(),
    "D": ProductD(),
    "E": ProductE(),
}


def checkout(skus):
    items = Counter([i for i in skus])
    try:
        _check_for_invalid_item(items)
    except InvalidItem:
        return -1

    freebies = _get_freebies(items)
    total = 0
    for k, count in items.items():
        product = PRODUCT_MAP[k]
        total += product.calculate_price(count, freebies.get(k, 0))

    return total

def _get_freebies(items):
    """Get the freebies"""
    total_freebies = []
    for k, count in items.items():
        product = PRODUCT_MAP[k]
        total_freebies.append(product.get_freebies(count))

    freebies = {}
    for free in total_freebies:
        freebies = dict(Counter(freebies) + Counter(free))
    return freebies

def _check_for_invalid_item(items):
    """Checking for any invalid items"""
    for k in items.keys():
        if k not in list(PRODUCT_MAP.keys()):
            raise InvalidItem()


assert checkout("A") == 50
assert checkout("AA") == 100
assert checkout("AAA") == 130
assert checkout("AAAA") == 180
assert checkout("AAAAA") == 200
assert checkout("AAAAAA") == 250

assert checkout("AAAAAAAA") == 330
assert checkout("AAAAAAAAA") == 380
assert checkout("AAAAAEEBAAABB") == 455

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

assert checkout("E") == 40
assert checkout("EE") == 80
assert checkout("EEE") == 120
assert checkout("EEEE") == 160

assert checkout("AABBCCDD") == 100 + 45 + 40 + 30
assert checkout("BEE") == 80
assert checkout("BBEE") == 80 + 30
