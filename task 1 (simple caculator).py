def simple_calculator():
    print("Simple Calculator")
    
    # Prompt the user to input two numbers
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    # Display operation choices
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Prompt the user to choose an operation
    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ['1', '2', '3', '4']:
            break
        else:
            print("Invalid choice! Please enter a valid operation (1/2/3/4).")

    # Perform the calculation and display the result
    if choice == '1':
        result = num1 + num2
        operation = '+'
    elif choice == '2':
        result = num1 - num2
        operation = '-'
    elif choice == '3':
        result = num1 * num2
        operation = '*'
    elif choice == '4':
        if num2 == 0:
            print("Error! Division by zero.")
            return
        result = num1 / num2
        operation = '/'

    print(f"{num1} {operation} {num2} = {result}")

# Call the simple_calculator function to run the calculator
simple_calculator()
