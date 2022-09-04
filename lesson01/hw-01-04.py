# 4 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def get_quarter_number(input_text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{input_text}"))
            is_OK = True
        except ValueError:
            print("The value is not a number!")
    return number

def get_coord_range(num):
    if num < 1 or num > 4:
        print('Please, enter correct quarter number from 1 to 4 ')
    elif num == 1:
        print(
            f'coordinates range in quarter {num} is: x > 0 and y > 0')
    elif num == 2:
        print(
            f'coordinates range in quarter {num} is: x < 0 and y > 0')
    elif num == 3:
        print(
            f'coordinates range in quarter {num} is: x < 0 and y < 0')
    elif num == 4:
        print(
            f'coordinates range in quarter {num} is: x > 0 and y < 0')

num = get_quarter_number("Enter number of quarter ")
get_coord_range(num)