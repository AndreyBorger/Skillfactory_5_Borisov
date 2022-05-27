A = [[' ', '0', '1', '2'],
     ['0', '-', '-', '-'],
     ['1', '-', '-', '-'],
     ['2', '-', '-', '-']
     ]


# функция отрисовки игрового поля
def draw_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end='  ')
        print()
    return


# функция проверки выигрыша
def check_win(draw_matrix):
    c = True
    if ((A[1][1] == '0' and A[1][2] == '0' and A[1][3] == '0')
            or (A[2][1] == '0' and A[2][2] == '0' and A[2][3] == '0')
            or (A[3][1] == '0' and A[3][2] == '0' and A[3][3] == '0')
            or (A[1][1] == '0' and A[2][1] == '0' and A[3][1] == '0')
            or (A[1][2] == '0' and A[2][2] == '0' and A[3][2] == '0')
            or (A[1][3] == '0' and A[2][3] == '0' and A[3][3] == '0')
            or (A[1][1] == '0' and A[2][2] == '0' and A[3][3] == '0')
            or (A[1][3] == '0' and A[2][2] == '0' and A[3][1] == '0')):
        c = 0
        print('ВЫИГРАЛ "0"')

    if ((A[1][1] == 'x' and A[1][2] == 'x' and A[1][3] == 'x')
            or (A[2][1] == 'x' and A[2][2] == 'x' and A[2][3] == 'x')
            or (A[3][1] == 'x' and A[3][2] == 'x' and A[3][3] == 'x')
            or (A[1][1] == 'x' and A[2][1] == 'x' and A[3][1] == 'x')
            or (A[1][2] == 'x' and A[2][2] == 'x' and A[3][2] == 'x')
            or (A[1][3] == 'x' and A[2][3] == 'x' and A[3][3] == 'x')
            or (A[1][1] == 'x' and A[2][2] == 'x' and A[3][3] == 'x')
            or (A[1][3] == 'x' and A[2][2] == 'x' and A[3][1] == 'x')):
        print('ВЫИГРАЛ "x"')
        c = 0
    if (A[1][1] != '-' and A[1][2] != '-' and A[1][3] != '-' and
            A[2][1] != '-' and A[2][2] != '-' and A[2][3] != '-' and
            A[3][1] != '-' and A[3][2] != '-' and A[3][3] != '-' and c != 0):
        print('НИЧЬЯ!')
        c = 0

    return (c)

# цикл ходов
count = 0
while check_win(draw_matrix(A)) != 0:
    count += 1
    if count % 2 == 0:
        print('---------------------')
        print()
        print('ХОДИТ "0"')
        y = int(input('введите координату y:'))
        x = int(input('введите координату x:'))
        if A[y + 1][x + 1] == '-':
            A[y + 1][x + 1] = '0'
        else:
            print('Неверный ход!')
    if count % 2 != 0:
        print('---------------------')
        print()
        print('ХОДИТ "Х"')
        y = int(input('введите координату y:'))
        x = int(input('введите координату x:'))
        if A[y + 1][x + 1] == '-':
            A[y + 1][x + 1] = 'x'
        else:
            print('Неверный ход!')


