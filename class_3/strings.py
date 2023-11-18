# String formatting

mini_str = 'sky'

max_str = "The is  {} very clear".format(mini_str)

# print(max_str)

# F Strings 

mini_str2 = "Friends"

max_str2 = f"When the sitcom {mini_str2} end ?"

# print(max_str2)


# String Slicing: refers a process of extracting portions of an iterable or string

# Slicing syntax: <iterable>[start:stop:step]

alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

new_str = alphas[-20:-10:2]
neww_str2 ="FGHIJ"
print(new_str)