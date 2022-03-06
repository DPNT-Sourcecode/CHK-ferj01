"""Store product details """

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

class ProductF(Product):
    """F"""
    item_price = 10
    offers = {3: 20}