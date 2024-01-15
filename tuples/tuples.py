# Tuple: This is a datastructure  that can hold multiple values however a tuple umlike a list is immutable

# Tuple items can be accessed by either indexing or slicing

first_tuple = (False, "True", 100)

second_tuple = (1,2,4,4,4)

full_tuple = first_tuple + second_tuple

# print(full_tuple)

# Tuple index : This method returns the position of the value specified

checkindex = full_tuple.index("True")
# print(checkindex)

# Tuple count : This method returns the number of times a value occurs

count_check = second_tuple.count(4)

val = second_tuple[-1]

# print(val)

thistuple = ("apple",)
# print(type(thistuple))

thistuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# print(thistuple2[2:5])

# Tuples are unchangeable once created but here is a simple workaround

convert_to_list = list(thistuple2)

convert_to_list.remove('kiwi')
convert_to_list.append('strawberries')

get_back_tuple = tuple(convert_to_list)

# print(get_back_tuple)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
fruits2 = ("apple", "banana", "cherry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
