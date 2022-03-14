# Init

f1 = 0
f2 = 0
f3 = 0
f4 = 0

# Input

n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))
n3 = int(input("Enter Third Number: "))
n4 = int(input("Enter Fourth Number: "))

# Process

if n1 > n2 and n1 > n3 and n1 > n4:
    f4 = n1
    if n2 > n3 and n2 > n4:
        f3 = n2
        if n3 > n4:
            f2 = n3
            f1 = n4
        else:
            f2 = n4
            f1 = n3
    elif n3 > n4 and n3 > n2:
        f3 = n3
        if n4 > n2:
            f2 = n4
            f1 = n2
        else:
            f2 = n2
            f1 = n4
    elif n4 > n2 and n4 > n3:
        f3 = n4
        if n2 > n3:
            f2 = n2
            f1 = n3
        else:
            f2 = n3
            f1 = n2
elif n2 > n3 and n2 > n4 and n2 > n1:
    f4 = n2
    if n3 > n4 and n3 > n1:
        f3 = n3
        if n4 > n1:
            f2 = n4
            f1 = n1
        else:
            f2 = n1
            f1 = n4
    elif n4 > n3 and n4 > n1:
        f3 = n4
        if n3 > n1:
            f2 = n3
            f1 = n1
        else:
            f2 = n1
            f1 = n3
    elif n1 > n4 and n1 > n3:
        f3 = n1
        if n4 > n3:
            f2 = n4
            f1 = n3
        else:
            f2 = n3
            f1 = n4
elif n3 > n4 and n3 > n1 and n3 > n2:
    f4 = n3
    if n4 > n1 and n4 > n2:
        f3 = n4
        if n1 > n2:
            f2 = n1
            f1 = n2
        else:
            f2 = n2
            f1 = n1
    elif n1 > n4 and n1 > n2:
        f3 = n1
        if n4 > n2:
            f2 = n4
            f1 = n2
        else:
            f2 = n2
            f1 = n4
    elif n2 > n4 and n2 > n1:
        f3 = n2
        if n4 > n1:
            f2 = n4
            f1 = n1
        else:
            f2 = n1
            f1 = n4
elif n4 > n1 and n4 > n2 and n4 > n3:
    f4 = n4
    if n1 > n2 and n1 > n3:
        f3 = n1
        if n2 > n3:
            f2 = n3
            f1 = n2
        else:
            f2 = n2
            f1 = n3
    elif n2 > n1 and n2 > n3:
        f3 = n2
        if n1 > n3:
            f2 = n1
            f1 = n3
        else:
            f2 = n3
            f1 = n1
    elif n3 > n1 and n3 > n2:
        f3 = n3
        if n1 > n2:
            f2 = n1
            f1 = n2
        else:
            f2 = n2
            f1 = n1

# Output
print(f"Result: {f4} {f3} {f2} {f1}")
