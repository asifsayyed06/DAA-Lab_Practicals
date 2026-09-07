def factorial_iterative(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


# User Input
n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial using Iterative Method:", factorial_iterative(n))
