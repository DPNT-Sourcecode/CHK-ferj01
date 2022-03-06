# noinspection PyUnusedLocal
from collections import Counter

from solutions.CHK.products import PRODUCT_MAP


class InvalidItem(Exception):
    """Invalid item"""


def checkout(skus):
    items = Counter([i for i in skus])
    try:
        _check_for_invalid_item(items)
    except InvalidItem:
        return -1

    freebies = _get_freebies(items)
    groups = _get_groups(items)
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


def _get_groups(items):
    """Get the item groups"""
    grouped = []
    for k, count in items.items():
        if k in ["S", "T", "X", "Y", "Z"]:
            grouped.extend([PRODUCT_MAP[k] for _ in range(count)])

    print(grouped)


assert checkout("STXYZ") == 50

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

assert checkout("F") == 10
assert checkout("FF") == 20
assert checkout("FFF") == 20
assert checkout("FFFF") == 30
assert checkout("FFFFF") == 40
assert checkout("FFFFFF") == 40

assert checkout("HHHHH") == 45
assert checkout("HHHHHHHHHH") == 80

assert checkout("KK") == 150

assert checkout("MNNN") == 120

assert checkout("PPPPP") == 200
assert checkout("PPPPPPPPPP") == 400

assert checkout("QQQ") == 80

assert checkout("QRRR") == 150
assert checkout("QQQRRR") == 150 + 60

assert checkout("UUUU") == 120

assert checkout("VV") == 90
assert checkout("VVV") == 130

assert checkout("AABBCCDD") == 100 + 45 + 40 + 30
assert checkout("BEE") == 80
assert checkout("BBEE") == 80 + 30

