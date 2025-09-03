def calculator():
    # Ask user for two numbers
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    
    # Ask user for the operation
    operation = input('Enter the operation (+, -, *, /): ')
    
    # Perform the operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        # Handle division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operation entered. Please use +, -, *, or /.")
        return
    
    # Print the result
    print(f'{num1} {operation} {num2} = {result}')

# Run the calculator function
calculator()