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

print(count_check)
