# Returning multiple Values - Python can return multiple values as a tuple

def get_min_max(numbers):
  return min(numbers), max(numbers)

# get both values
minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"Min: {minimum}, Max: {maximum}") 