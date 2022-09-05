# 1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

def input_numbers(input_text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{input_text}"))
            is_OK = True
        except ValueError:
            print("The value is not a number!")
    return number


def check_number(num):
    if 6 <= num <= 7:
        print("Is it a day off? Yes")
    elif 0 < num < 6:
        print("Is it a day off? No")
    else:
        print("The value is not between 1 and 7!")

num = input_numbers("Enter a number from 1 to 7: ")
check_number(num)
