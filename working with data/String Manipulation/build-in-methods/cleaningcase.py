messy = "  Hellow World  "
clean_messy = messy.strip() # removes Leading and trailing whitedspace

price = "$19.99"
clean_price = price.strip("$") # removes Leading and trailing $ sign

print(clean_messy) # Outputt: Hellow World
print(clean_price) # Output: 19.99

