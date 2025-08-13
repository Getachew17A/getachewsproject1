# Ask the user for two numbers
x = float(input("Enter the first number to add:"))
y = float(input("enter the second number to add"))

# Ask the user for the operation
Operation = input("Enter an operation(+, -, *, /): ")

# perform the operation and print the result
if Operation == '+':
    result = x + y
    print(f"{x} + {y} = {result}")
elif Operation == '-':
    result = x - y
    print(f"{x} - {y} = {result}")
elif Operation == '*':
    result = x * y
    print(f"{x} * {y} = {result}")
elif Operation == '/':
    if y !=0:
        result = x / y
        print(f"{x} / {y} = {result}")
    else:
        print("Error: Division by Zero is not allowed")
        
else:
    print("invalid operation. Please Enter one of +, -, *, /.")
    
            

print("this is my first code")