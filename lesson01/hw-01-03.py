# 3 Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def input_coord(coords):
    coord = [0] * coords
    for i in range(coords):
        is_OK = False
        while not is_OK:
            try:
                number = float(input(f"Enter {i+1} coordinate: "))
                coord[i] = number
                is_OK = True
                if coord[i] == 0:
                    is_OK = False
                    print("Coordinate must be not equal 0 ")
            except ValueError:
                print("Please enter the number")
    return coord


def check_coordinates(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    print(f"The point is in the {text} quarter of the plane")


coordinate = input_coord(2)
check_coordinates(coordinate)
