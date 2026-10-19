age = int(input("Enter your age: "))
has_license = input("Do you have a driver's license? (yes/no): ").lower() == "yes"

# AND - both must be true
can_drive = age >= 18 and has_license
print(can_drive)