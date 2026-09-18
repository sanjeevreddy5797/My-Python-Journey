import logo 
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    print(logo.logo)
    number1 = float(input("What's the first number?: "))
    condition = True

    while condition:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        number2 =float(input("What is the second number? "))
        result = operations[operation_symbol](number1,number2)
        print(f"{number1} {operation_symbol} {number2} = {result}")
        continue_calculation = input("Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if(continue_calculation == 'y'):
            number1 = result
        else:
            condition = False
            print("\n" * 20)
            calculator()

calculator()