# Remove duplicates

names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]

unique_names = list(set(names))
print(unique_names)

# Fast membership testing

allowed_users = {"alice", "bob", "charlie"}

if "alice" in allowed_users: # very fast!
  print("Access granted")