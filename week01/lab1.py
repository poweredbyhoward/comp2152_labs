# Sample Coding Questions 01 Week 01
# Howard Huang

# [] creates a list
some_array_aka_list = [1, 4, 7, 9]


# Order of operations
# ** (exponents/powers) - FIRST
# *, /, //, % (multiply, divide, floor divide, modulo) - SECOND
# +, - (add, subtract) - THIRD

# ** = power/exponent (example: 2 ** 3 means 2³ = 8)
# // = floor division (divides and rounds DOWN to whole number)
# % = modulo (gives the remainder after division)

a = 1
b = 2
c = 3
d = 4
# TASK: bracketed version of ---> e = a - b ** c // d + a % c
e = ((a - ((b ** c) // d)) + (a % c))
print("Q3 answer with brackets: ", e)
f = a - b ** c // d + a % c
print("Q3 asnwer without brackets: ", f)

temp = 32.6
second_temp = 42.1
print("The temp today is: {:.3f} degrees Celsius... testing {:.5f}".format(temp, second_temp))
print(f"Lorem ipsum {temp:.2f} something something {second_temp:.2f}")

some_num = int(input("Enter a random number to be added with 5: "))
some_num += 5
print(some_num)