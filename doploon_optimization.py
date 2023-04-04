from knapsack_dooplons import knapsack

SMALL_DOOPLOONS = 20
MEDIUM_DOOPLOONS = 60
GREAT_DOOPLOONS = 140
POWERFUL_DOOPLOONS = 340


def doploon_optimizator(doploon_quantity, small_price, medium_price, great_price, powerful_price):
    scrolls = [
        (SMALL_DOOPLOONS, small_price),
        (MEDIUM_DOOPLOONS, medium_price),
        (GREAT_DOOPLOONS, great_price),
        (POWERFUL_DOOPLOONS, powerful_price)
    ]

    result = knapsack(scrolls, doploon_quantity)

    small = 0
    total_small_price = 0

    medium = 0
    total_medium_price = 0

    great = 0
    total_great_price = 0

    powerful = 0
    total_powerful_price = 0

    for scroll in result:
        if (scroll[0] == 20): small += 1; total_small_price += scroll[1]
        if (scroll[0] == 60): medium += 1; total_medium_price += scroll[1]
        if (scroll[0] == 140): great += 1; total_great_price += scroll[1]
        if (scroll[0] == 340): powerful += 1; total_powerful_price += scroll[1]


    total_price = total_small_price + total_medium_price + total_great_price + total_powerful_price

    return [
        {"small": small, "total_price": total_small_price},
        {"medium": medium, "total_price": total_medium_price},
        {"great": great, "total_price": total_great_price},
        {"powerful": powerful, "total_price": total_powerful_price},
        {"total": total_price},
    ]