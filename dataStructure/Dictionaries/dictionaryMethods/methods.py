person = {"name": "Alice", "age": 30, "city": "Kolhapur"}

# Get all keys , values, or items

print(person.keys()) # dict_keys(['name' , 'age' 'city'])

print(person.values()) # dict_valuese(['Alice' 30 , 'New York'])

print(person.items())  # dict_items([('name', 'Alice'), ....])

# Check if key exists 
if 'name' in person:
  print("Name Found! ")

# Update multiple values

person.update({"age": 22, "job": "Engineer"})

print(person)
