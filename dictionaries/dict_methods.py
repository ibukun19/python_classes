car = {
    
    "brand":"Ford",
    "model":"mustang", 
    "year": 1964
    
    }

# Dictionary items method: returns a list of tuples and the tuples have two elements each representing the 
#                           key / value pairs in the dictionary

list_tuple = car.items()
amala = list(list_tuple)

print(amala[1])