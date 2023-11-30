# User inputs 3 numbers: a, b, c
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
# If a > b
if a > b:
    # if a > c
    if a > c:
        #display a
        print(a)
    # else
    else:
        #display c
        print(c)
# else
else:
    # if b > c
    if b> c:
        # display b
        print(b)
    # else
    else:
        # display c
        print(c)