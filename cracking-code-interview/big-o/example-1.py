# The runtime will be O(n), the fact that it does run for twice won't matter, gets rid of constants


def sum_and_product(list):
    sum = 0
    product = 1
    for el in list:
        sum += el
    for el in list:
        product *= el
    print ("sum = %s, product = %s" % (sum, product))
    return [sum, product]


list = [1, 5, 8, 9, 11, 13, 15, 19, 21]
sum_and_product(list)
