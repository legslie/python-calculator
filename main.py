import sys


def menu_items():
    print("Calculator")
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    print("5. exit")


def method(uinput):
    if uinput == 1:
        num_1 = int(input("Enter your first number: "))
        num_2 = int(input("Enter your second number: "))
        print(str(num_1) + "+" + str(num_2) + "=" + str(num_1 + num_2))
        menu_items()
        user_input = int(input("Please choose another method: "))
        method(user_input)
    elif uinput == 2:
        num_1 = int(input("Enter your first number: "))
        num_2 = int(input("Enter your second number: "))
        print(str(num_1) + "-" + str(num_2) + "=" + str(num_1 - num_2))
        menu_items()
        user_input = int(input("Please choose another method: "))
        method(user_input)
    elif uinput == 3:
        num_1 = int(input("Enter your first number: "))
        num_2 = int(input("Enter your second number: "))
        print(str(num_1) + "x" + str(num_2) + "=" + str(num_1 * num_2))
        menu_items()
        user_input = int(input("Please choose another method: "))
        method(user_input)
    elif uinput == 4:
        num_1 = int(input("Enter your first number: "))
        num_2 = int(input("Enter your second number: "))
        if num_2 == 0:
            print("Nonono Mr. Peter, I quit")
            sys.exit()
        print(str(num_1) + "/" + str(num_2) + "=" + str(num_1 / num_2))
        menu_items()
        user_input = int(input("Please choose another method: "))
        method(user_input)
    elif uinput == 5:
        sys.exit()
    else:
        print("error")


def main():
    menu_items()
    user_input = int(input("Please choose method: "))
    method(user_input)

if __name__ == '__main__':
    main()