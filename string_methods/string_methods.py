# String title method : This method converts the first letters of string to Uppercase it returns a new string

mystr = "regular expression"
new_mystr = mystr.title()

# print(new_mystr)

# String upper method : This method converts all the letters in a string into capital . It returns a new string

mystr2 = mystr.upper()

# print(mystr2)

# String lower method : This methods converts all the letters of a string to lowercase

mystr3 = mystr2.lower()

# print(mystr3)

# String startswith method : This method returns true if the string starts with the specific character

check1 = mystr2.startswith('r')

# print(check1)

# String endswith method : This method returns true if the string starts with the specific character

check2 = mystr.endswith('n')

# print(check2)

# String index method : This method is used to returns the index of the first occurence of a substring 
substrX= mystr[1:]
lookup = mystr.index('r')
# lookup2 = substrX.index('z')

# print(lookup)

# String find method : This method is used to returns the index of the first occurence of a substring 
# Note : The difference btwn the index method and the find is in their error handling. Index method throws an error
#        when it doesn't get a matching substring while find method returns a -1 if it doesn't get a matching substr
#        Also the find method is only used on strings


lookup3 = mystr.find('r')
email = "winsomeGmail.com"
lookup2 = email.find('@')
# print(substrX)
# print(lookup2)

# String isspace : This method returns true if all the charcters in a string are whitespaces

user_name = " "
check3 = user_name.isspace()


# print(check3)

# String islower method : This method returns true if all chars are lowercase .

check4 = email.islower()

# print(check4)

# String isupper method : This method returns true if all chars are uppercase .

person = "ABBA"

check5 = person.isupper()

# print(check5)

# String split method : This method splits a string at the specified separator and returns a list

mystr4 = "a,b,c,d"

mystr4_list = mystr4.split(',',2)

# print(mystr4_list )

# String join method : This method returns a string of combined list items

newStr = ",".join(mystr4_list)

# print(newStr)
# String count method : This method returns the number of times a specified value occurs in string

newStr2 = mystr.count('r')

# print(newStr2)

# String replace method : This method is used to replace a char in a String

newStr3 = mystr.replace('r','z')

print(newStr3)