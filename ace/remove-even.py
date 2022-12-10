def remove_even(lst):
    even_count = 0  # does not initilize another array
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_count += 1
        else:
            lst[i - even_count] = lst[i]
    return lst[0:len(lst)-even_count]

# can also use list comprehension but this allocates a new list but is nice

# return [number for number in lst if number % 2 != 0]


my_list = [1, 2, 4, 5, 10, 6, 3]  # my_list = [1,5,3]

print(remove_even(my_list))
