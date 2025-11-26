# add and subtract two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2
diff = num1 - num2
mult = num1 * num2

if num2 == 0:
    div = "Cannot divide by zero"
else:
    div = num1 / num2

print("Sum of two numbers:", sum)
print("Difference of two numbers:", diff)
print("Multiplication of two numbers:", mult)
print("Division of two numbers:", div)