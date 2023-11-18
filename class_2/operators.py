# What are Operators?

# Operators are special characters or symbols that are used to perform arithmetic and logical 
# operations/computations on values and variables

# Arithmetic Operators

# Operator         Name               Example
#  +               Addition             5 + 5 = 10
#  -               Subtraction          5 - 5 = 0
#  *               Multiplication       5 * 5 = 25
#  /               Division             25 / 5 = 5
#  %               Modulus               34 % 5 = 4
#  //              Floor Division       23 // 4 = 5
#  **              Exponential           6 ** 3 = 216
#  =               Equal to              a = 2
#  +=              increment              a += 2
#  -=              decrement              a -= 2
#  *=              multiplied_increment   a *= 2
#  /=              divisional_decrement   a /= 2
#  %=              a   %= 2              a = a % 2
#  //=              a   //= 2              a = a // 2
#  **=              a   **= 2              a = a ** 2


# Comparison Operators

# ==             Equal or same as           a == b 
# !=             Not Equal or not same as   a != b
# >              Greater than               a > b
# <              less than                  a < b
# >=             Greater than or qual to    a >= b
# <=             less than or qual to       a <= b


# Logical Opeartors

# or             returns True if at least one of the statements true             a<29 or a>54
# and             returns True if both statements  are true                      a>5 and  a>54
# not           reverses the result, if True is returned , it reverses to false      not(a>5 and  a>54)
# is           returns True if both variables are the same object                p is q
# is not           returns False if both variables are  not the same object                p is not q
# in           returns True if specified value is present in the object               p in q
# not in           returns True if specified value is not present in the object               p not in q


# Practical Examples of Logical

mylist = ['1','2','3']

str1 = '1'

# print(str1 is mylist)
# print(str1 is not mylist)
# print(not(str1 is mylist))
# print(not(str1 is not mylist))

# print(str1  in mylist)
# print(str1 not in mylist)

# Strings 

# String Concatenation : This the concept of joining or combining separate or different strings and turning them 
# into one string

str2 = "Beautiful"
str3 = " city"

str4 = str2 + " " + str3
# print(str4)

# String Index: This is the process of referencing string characters using numbers as indexes

# print(str2[0])
print(str2[3])

# Negative Indexing: strings can be indexed using negative numbers. The last character has an index of -1

print(str2[-1])












