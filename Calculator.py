operator = input("Enter the operation: add, subtract, divide, multiply").lower()
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if operator == 'add':
    output = num1 + num2
    print(output)
elif operator == 'subtract':
    output = num1 - num2
    print(output)
elif operator == 'divide':
    output = num1/num2
    print(output)
    
elif operator == 'multiply':
    output = num1 * num2
    print(output)