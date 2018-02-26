# The runtime will be O(n), the fact that it does run for twice won't matter, gets rid of constants
def sum_and_product(array)
  sum = 0
  product = 1

  array.each do |el|
    sum += el
  end
  array.each do |el|
    product *= el
  end
  puts("sum = #{sum}, product = #{product}")
  [sum, product]
end

array = [1, 5, 8, 9, 11, 13, 15, 19, 21]
sum_and_product(array)
