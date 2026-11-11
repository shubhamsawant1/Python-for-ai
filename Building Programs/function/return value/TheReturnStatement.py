# Use return to send a value back from a function

def calculate_area(width, height):
  area = width * height
  return area

# store the returned value

room_area = calculate_area(10 ,12)
print(f"Room size: {room_area} sq ft")