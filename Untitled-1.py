
ROWS = 10
COLS = 10

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
        dx = int(input("Введіть зміщення за горизонталлю (-1, 0, або 1): "))
        dy = int(input("Введіть зміщення за вертикаллю (-1, 0, або 1): "))
    except:
        print("Введіть коректні значення.")
        continue
    
    if -1 <= x + dx < ROWS-2 and -1 <= y + dy < COLS-2:
        x += dx
        y += dy
    else:
        print("Некоректне зміщення. Спробуйте ще раз.")