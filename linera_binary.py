def linear_search(lst, target) :
    for index, element in enumerate(lst):
        if element == target:
            return index
    return -1   # return -1 if not found

my_list = linear_search([1, 3, 5, 7, 9],5)
print(my_list)