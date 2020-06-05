from functools import reduce

my_list = [el for el in range(100, 1002) if el % 2 == 0]

sum_all = reduce(lambda x,y: x + y, my_list)

print(sum_all)
