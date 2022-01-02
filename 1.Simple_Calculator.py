 print("simple calculator,operation with two arguments")


def add(a, b):
    print(f'{a} + {b} =', a + b)


def sub(a, b):
    print(f'{a} - {b} =', a - b)


def multi(a, b):
    print(f'{a} * {b} is', a * b)


def div(a, b):
    print(f'{a} / {b} =', a / b)


while True:
    print("calculation choices are \n+ for press 1. \n- for press 2. \n* for press 3. \n/ for press 4.")
    user_wish = input("enter your choice(1/2/3/4):")
    if user_wish in ['1', '2', '3', '4']:
        num1 = float(input("enter a first number:"))
        num2 = float(input("enter a second number:"))
        if user_wish == '1':
            add(num1, num2)

        elif user_wish == '2':
            sub(num1, num2)

        elif user_wish == '3':
            multy(num1, num2)

        else:
            div(num1, num2)
    else:
        print("Invalid choice,Enter a valid choice")

    next_calculation = input("Do you want to calculate again?(press yes = 'y'/ press no = 'n'):")
    if next_calculation == 'n':
        break
