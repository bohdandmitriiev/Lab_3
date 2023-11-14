
ROWS = 10
COLS = 20

x, y = 1, 1


sym = [['.', 'X', '.'],['X', 'X', 'X'], ['.', 'X', '.']]
def print_field():
    for i in range(ROWS):
        for j in range(COLS):
            if (i == x or i == x+1 or i == x+2) and (j == y or j == y+1 or j == y+2):
                print(sym[i-x][j-y], end=' ')
            else:
                print(".", end=' ')
        print()

while True:

    print_field()
    
    try:
        ctrl_input = input("Введіть зміщення(w,s,a,d): ")
        if  ctrl_input == "w":
            dx = -1
            dy = 0
        elif ctrl_input == "s":
            dx = 1
            dy = 0
        elif ctrl_input == "a":
            dy = -1
            dx = 0
        elif ctrl_input == "d":
            dy = 1
            dx = 0

    except:
        print("Введіть коректні значення.")
        continue
    
    if 0 <= x + dx < ROWS-2 and 0 <= y + dy < COLS-2:
        x += dx
        y += dy
    else:
        print("Некоректне зміщення. Спробуйте ще раз.")