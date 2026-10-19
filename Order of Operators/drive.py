age = int(input("Enter your age: "))
has_license = input("Do you have a driver's license? (yes/no): ").lower()

if has_license == "yes":
    has_license = True
else:
    has_license = False

# AND - both must be true
can_drive = age >= 18 and has_license
print(can_drive)


myage = 25
has_licensee = False

can_driveCar = myage >= 18 and has_licensee
print(can_driveCar)
