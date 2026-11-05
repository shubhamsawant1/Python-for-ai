colors = {"red", "blue"}

# Add items
colors.add("green") # Erroe if not found
colors.discard("yellow") # No error if not found

print(colors)

# check membership 

if  "red" in colors:
  print("Red is available")