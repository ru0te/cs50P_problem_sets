def math_interpreter():
    user_input = input("Enter math expression: ")
    expression = tuple(user_input.split(" "))
    x, y, z = expression
    match y:
        case "+":
            print(float(x) + float(z))
        case "-":
            print(float(x) - float(z))
        case "*":
            print(float(x) * float(z))
        case "/":
            print(float(x) / float(z))


math_interpreter()
