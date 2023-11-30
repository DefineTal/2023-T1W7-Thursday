# Input numerator as n and denominator as d
n = int(input("Enter Numerator: "))
d = int(input("Enter Denominator: "))

# If d is greater then 0 calculate the value of q as d/n
# then display value of q
if d > 0:
    q = n / d
    print(q)

# if d is equal to 0 display "Denominator cant be zero"
else:
    print("Denominator cant be zero or lower")


