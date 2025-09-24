y_root = lambda x,y : x**(1/y)
print(y_root(25,2))

sort = lambda a : sorted(a)
print (sort([6,2,3,9,1,5]))

list1 = [2,6,8,10,11,4,12,7,13,17,0,3,21]
filtered_list = filter(lambda x: x > 9, list1)
print(list(filtered_list))

list2 = [2,6,8,10,11,4,12,7,13,17,0,3,21]
mapped_list = map(lambda a: a%2, list2)
print(list(mapped_list))