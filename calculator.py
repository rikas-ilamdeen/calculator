import sys

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Can not be divided by zero.")
        return "undefined"

def get_user_input():
    while True:
        menu_display = """
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Back
6. Exit"""
        print(menu_display)

        try:
            operator = int(input("Select an operator (1, 2, 3, 4, 5 or 6): "))
            if operator in [5, 6]:
                return operator, None, None
            elif operator in [1, 2, 3, 4]:
                a = int(input("\nEnter your number 1: "))
                b = int(input("Enter your number 2: "))
                return operator, a, b
        except ValueError:
            print("Integer required!")
            continue

def dictionary_method():
    while True:
        menu = {
            1: addition,
            2: subtraction,
            3: multiplication,
            4: division
        }

        operator, a, b = get_user_input()
        if operator == 5:
            break
        elif operator == 6:
            sys.exit("Exited.") 
        operation = menu.get(operator)

        if operation:
            result = operation(a, b)
            print(f"Answer is {result}")
        else:
            print("Invalid input!")
            continue

def matching_method(operator, a, b):
    while True:
        if operator == 5:
            return
        elif operator == 6:
            sys.exit("Exited.")

        match operator:
            case 1:
                calculation = addition
            case 2:
                calculation = subtraction
            case 3:
                calculation = multiplication
            case 4:
                calculation = division
            case _:
                return

        result = calculation(a, b)
        print(f"Answer is {result}")
        operator, a, b = get_user_input()

def main():
    while True:
        menu_display = """
        ___ C A L C U L A T O R ___   \n
1. Dictionary method
2. Matching method
3. Exit"""
        print(menu_display)

        try:
            menu = int(input("Choose an option (1, 2 or 3): "))

            match menu:
                case 1:
                    print("\nDictionary method selected.")
                    dictionary_method()
                case 2:
                    print("\nMatch-Case method selected.")
                    operator, a, b = get_user_input()
                    matching_method(operator, a, b)
                case 3:
                    print("Exited")
                    break
                case _:
                    print("Invalid selection!")
        except ValueError:
            print("Please choose a valid option.")

if __name__ == "__main__":
    main()