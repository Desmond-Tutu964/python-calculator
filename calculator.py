while True:
    print("********* DESMOND PYTHON CALCULATOR ***********")

    num1 = int(input("enter your first number: "))
    num2 = int(input("enter your second number: "))

    operation = input("choose an operation(+, -, *, /)or type q to quit: ")

    if operation == "q":
        break
    if operation == "+":
            print("Result:", num1 + num2)

    elif operation == "-":
            print("Result:", num1 - num2)

    elif operation == "*":
            print("Result:", num1 * num2)

    elif operation == "/":
        if num2 == 0:
            print("cannot divite by zero")
        else:         
            print("Result:", num1 / num2)

    else:
            print("Invalid operation")
  
