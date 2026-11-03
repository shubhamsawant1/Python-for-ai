# Nested if statements inside other if statements:
def ticket(has_ticket):
  if has_ticket == "Yes":
    return True
  else:
    return False
  
has_ticket = input("Enter you have a ticket: (yes/no)").title().strip()
age = int(input("Enter Your Age: "))

if ticket(has_ticket):
  if age >= 18:
    print("Enjoy the movie!")
  else: 
    print("Need adult supervision ")
else:
  print("Buy a ticket first")