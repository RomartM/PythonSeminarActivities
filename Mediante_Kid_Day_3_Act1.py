# Init

bunos = 0

# Input

number_of_years = int(input("Enter Number of Years: "))
name_of_office = str(input("Enter Name of Office: ")).lower()

# Process

if name_of_office == 'it':
    if number_of_years >= 10:
        bunos = 10000
    else:
        bunos = 5000
elif name_of_office == 'acct':
    if number_of_years >= 10:
        bunos = 12000
    else:
        bunos = 6000
elif name_of_office == 'hr':
    if number_of_years >= 10:
        bunos = 15000
    else:
        bunos = 7500
else:
    print(f"\nNo offices matched for '{name_of_office}'");

# Output


if bunos != 0:
    print(f"\nYour claimable bunos is : {bunos}")
