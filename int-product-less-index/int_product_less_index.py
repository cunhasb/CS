array = [1, 7, 3, 4]

# Brute force, helper method o(n), returns product of entire array


def get_product(list):
    sum = 1
    for el in list:
        sum *= el
    return sum

# Using reduce


def get_product_using_reduce(list):
    return reduce((lambda x, y: x * y), list)


# Gets product of entire array from helper method and than appends value to new_array O(n)
def get_products_of_all_ints_except_at_index(list):
    product = get_product(list)
    new_array = []
    for el in list:
        new_array.append(product / el)
    return new_array


# Using map function
def get_products_of_all_ints_except_at_index_using_map(list):
    product = get_product(list)
    return list(map((lambda el: product / el), list))
