person = {"name": "Alice", "age": 22, "City": "New York"}

# Get values by key
print(person["name"])   # "Alice"

print(person["age"]) # 30

# Safer with get()

print(person.get("job"))  # None (no error)

print(person.get("job", "Unknow"))   # "Unknow" (default)

