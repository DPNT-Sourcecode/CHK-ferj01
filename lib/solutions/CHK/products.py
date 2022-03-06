class Product:
    """A shopping item"""

    item_price = 0
    offers = {}
    freebies = {}

    group_offers = {3: ()}

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
            total += in_offer * self.offers[offer_num]

        return total + (remaining * self.item_price)


class ProductA(Product):
    item_price = 50
    offers = {3: 130, 5: 200}


class ProductB(Product):
    item_price = 30
    offers = {2: 45}


class ProductC(Product):
    item_price = 20


class ProductD(Product):
    item_price = 15


class ProductE(Product):
    item_price = 40
    freebies = {2: "B"}


class ProductF(Product):
    item_price = 10
    offers = {3: 20}


class ProductG(Product):
    item_price = 20


class ProductH(Product):
    item_price = 10
    offers = {5: 45, 10: 80}


class ProductI(Product):
    item_price = 35


class ProductJ(Product):
    item_price = 60


class ProductK(Product):
    item_price = 80
    offers = {2: 150}


class ProductL(Product):
    item_price = 90


class ProductM(Product):
    item_price = 15


class ProductN(Product):
    item_price = 40
    freebies = {3: "M"}


class ProductO(Product):
    item_price = 10


class ProductP(Product):
    item_price = 50
    offers = {5: 200}


class ProductQ(Product):
    item_price = 30
    offers = {3: 80}


class ProductR(Product):
    item_price = 50
    freebies = {3: "Q"}


class ProductS(Product):
    item_price = 20


class ProductT(Product):
    item_price = 20


class ProductU(Product):
    item_price = 40
    offers = {4: 120}


class ProductV(Product):
    item_price = 50
    offers = {2: 90, 3: 130}


class ProductW(Product):
    item_price = 20


class ProductX(Product):
    item_price = 17


class ProductY(Product):
    item_price = 20


class ProductZ(Product):
    item_price = 21


PRODUCT_MAP = {
    "A": ProductA(),
    "B": ProductB(),
    "C": ProductC(),
    "D": ProductD(),
    "E": ProductE(),
    "F": ProductF(),
    "G": ProductG(),
    "H": ProductH(),
    "I": ProductI(),
    "J": ProductJ(),
    "K": ProductK(),
    "L": ProductL(),
    "M": ProductM(),
    "N": ProductN(),
    "O": ProductO(),
    "P": ProductP(),
    "Q": ProductQ(),
    "R": ProductR(),
    "S": ProductS(),
    "T": ProductT(),
    "U": ProductU(),
    "V": ProductV(),
    "W": ProductW(),
    "X": ProductX(),
    "Y": ProductY(),
    "Z": ProductZ(),
}