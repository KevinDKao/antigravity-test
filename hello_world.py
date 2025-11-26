
# request an input for two numbers and add them together

print("Select operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

operation = input("Enter choice (1/2/3/4 or +,-,*,/): ")

print("Enter the first number")
first_number = float(input())

print("Enter the second number")
second_number = float(input())

if operation in ('1', '+'):
    print("The sum is", first_number + second_number)
elif operation in ('2', '-'):
    print("The difference is", first_number - second_number)
elif operation in ('3', '*'):
    print("The product is", first_number * second_number)
elif operation in ('4', '/'):
    if second_number == 0:
        print("Error: Division by zero")
    else:
        print("The quotient is", first_number / second_number)
else:
    print("Invalid operation")