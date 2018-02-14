require 'byebug'
array = [1, 7, 3, 4]

def get_product(list)
  sum = 1
  list.each do |el|
    sum *= el
  end
  sum
end

def get_product2(list)
  list.inject(&:*)
end

byebug
