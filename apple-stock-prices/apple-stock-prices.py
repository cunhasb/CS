stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
stock_prices_yesterday = [12, 13, 5, 6, 17, 20, 19, 15, 30]
stock_prices_yesterday = [12, 5, 15, 4, 5, 6, 7, 1, 13]
stock_prices_yesterday = [15, 14, 13, 10, 9, 8, 3, 10, 13, 20]
stock_prices_yesterday = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6]


def get_max_profit(list):
    smallest = list[0]
    biggest = list[0]

    for el in list:

        if el < smallest:
            smallest = el
            biggest = el
        else:
            if el > biggest:
                biggest = el

    return biggest - smallest


print(get_max_profit(stock_prices_yesterday))
