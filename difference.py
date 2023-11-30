# define sum_of_squares = 0
sum_of_squares = 0
# define sum = 0
sum = 0


# while i <= 100
for i in range(1, 101):
    # sum_of_squares = sum_of_squares + i * i
    sum_of_squares += i * i
    # sum = sum + i
    sum += i


# square_of_sum = sum * sum
square_of_sum = sum ** 2
# diff = square_of_sum - sum_of_squares
diff = square_of_sum - sum_of_squares
# display diff
print(diff)