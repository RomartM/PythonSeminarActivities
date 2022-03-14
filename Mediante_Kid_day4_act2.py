# Init

want_to_continue = True

# Process

while want_to_continue:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    print("The sum of %d and %d is %d" % (n1, n2, n1 + n2))
    is_continue = str(input("Would you like to continue? [Y/N]")).lower()
    if(is_continue == 'n'):
        print("Thank You!")
        want_to_continue = False
        break;
