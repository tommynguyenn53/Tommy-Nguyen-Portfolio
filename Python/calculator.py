import art


def add(n1, n2):
    result = n1 + n2
    rounded_result = round(result, 2)
    return rounded_result


def sub(n1, n2):
    result = n1 - n2
    rounded_result = round(result, 2)
    return rounded_result


def mul(n1, n2):
    result = n1 * n2
    rounded_result = round(result, 2)
    return rounded_result


def div(n1, n2):
    result = n1 / n2
    rounded_result = round(result, 2)
    return rounded_result


print(art.logo1)
print("Welcome to the calculator program")

user_continuation = True

while user_continuation:
    first_number = int(input("What's the first number? "))
    operation = input("+\n-\n*\n/\nPick an operation: ")
    second_number = int(input("What's the second number? "))

    if operation == "+":
        answer = add(n1=first_number, n2=second_number)

    elif operation == "-":
        answer = sub(n1=first_number, n2=second_number)

    elif operation == "*":
        answer = mul(n1=first_number, n2=second_number)

    elif operation == "/":
        answer = div(n1=first_number, n2=second_number)

    else:
        print("Calculation Failed. Try again")

    print(f'{first_number} {operation} {second_number} = {answer}\n')

    user_choice = input(f'Type \'y\' to continue calculating, or type \'n\' to exit. ')

    if user_choice == 'n':
        user_continuation = False

print("Thank you for using this calculator app")
