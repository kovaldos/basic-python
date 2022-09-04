# 1-Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("The value is not a number!")
    return number


def checkNumber(num):
    if 6 <= num <= 7:
        print("Is it a day off? Yes")
    elif 0 < num < 6:
        print("Is it a day off? No")
    else:
        print("The value is not between 1 and 7!")


num = InputNumbers("Enter a number from 1 to 7: ")
checkNumber(num)
