my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict)

#for printing a particular value
print(my_dict['key2']) #make sure that the key is a string and its in a square bracket

#for adding a new key value pair
my_dict['key3'] = 'value3' #again keep in mind to use square brackets
print(my_dict)
# We can also use the same method to easily overwrite an existing key value pair.
my_dict['key3'] = 'new-value'
print(my_dict)


price_lookup = {'apple':300, 'banana': 100, 'berries': ['straw', 'rasp', 'blue'], 'veggies' : {'tomato':50, 'potato':60}}
print(price_lookup['apple'])
print(price_lookup['berries'])
print(price_lookup['berries'][2])
print(price_lookup['veggies']['potato'])
print(price_lookup['berries'][1].upper())
print(price_lookup.keys()) # Method to return a list of all keys 
print(price_lookup.values()) # Method to grab all values
print(price_lookup.items()) # Method to return tuples of all items
price_lookup['apple'] = price_lookup['apple'] -100
print(price_lookup)
price_lookup['banana'] -= 50
print(price_lookup)


