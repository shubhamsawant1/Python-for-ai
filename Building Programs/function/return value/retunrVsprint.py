# Understanding the differnce is crucial:

def get_greeting_print(name):
  print(f"Hellow, {name}!") #just display

def get_greeting_return(name):
  return f"hello, {name}! " # Gives back value

# can't use print version's output

message = get_greeting_print("Alice") # Prints but returns None
print(message) # None

# can use returns version's output

message = get_greeting_return("Alice") # return the setting 
print(message.upper()) # HELLO, ALICE!

# use return when you need to use the result elsewhere. Use print when you just want to display information.

