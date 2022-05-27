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
def check_win():
    if ((A[1][1] == '0' and A[1][2] == '0' and A[1][3] == '0')
            or (A[2][1] == '0' and A[2][2] == '0' and A[2][3] == '0')
            or (A[3][1] == '0' and A[3][2] == '0' and A[3][3] == '0')
            or (A[1][1] == '0' and A[2][1] == '0' and A[3][1] == '0')
            or (A[1][2] == '0' and A[2][2] == '0' and A[3][2] == '0')
            or (A[1][3] == '0' and A[2][3] == '0' and A[3][3] == '0')
            or (A[1][1] == '0' and A[2][2] == '0' and A[3][3] == '0')
            or (A[1][3] == '0' and A[2][2] == '0' and A[3][1] == '0')):
        print('ВЫИГРАЛ "0"')
        return 0

    if ((A[1][1] == 'x' and A[1][2] == 'x' and A[1][3] == 'x')
            or (A[2][1] == 'x' and A[2][2] == 'x' and A[2][3] == 'x')
            or (A[3][1] == 'x' and A[3][2] == 'x' and A[3][3] == 'x')
            or (A[1][1] == 'x' and A[2][1] == 'x' and A[3][1] == 'x')
            or (A[1][2] == 'x' and A[2][2] == 'x' and A[3][2] == 'x')
            or (A[1][3] == 'x' and A[2][3] == 'x' and A[3][3] == 'x')
            or (A[1][1] == 'x' and A[2][2] == 'x' and A[3][3] == 'x')
            or (A[1][3] == 'x' and A[2][2] == 'x' and A[3][1] == 'x')):
        print('ВЫИГРАЛ "x"')
        return  0

    if (A[1][1] != '-' and A[1][2] != '-' and A[1][3] != '-' and
            A[2][1] != '-' and A[2][2] != '-' and A[2][3] != '-' and
            A[3][1] != '-' and A[3][2] != '-' and A[3][3] != '-'):
        print('НИЧЬЯ!')
        return 0

# цикл ходов
turn = 'x'
draw_matrix(A)

while True:
    if turn == '0':
        print('---------------------')
        print()
        print('ХОДИТ "0"')
        y = int(input('введите координату y:'))
        x = int(input('введите координату x:'))
        if A[y + 1][x + 1] == '-':
            A[y + 1][x + 1] = '0'
            draw_matrix(A)
            if check_win() == 0: break
            turn = 'x'
        else:
            print('Неверный ход!')
    if turn == 'x':
        print('---------------------')
        print()
        print('ХОДИТ "Х"')
        y = int(input('введите координату y:'))
        x = int(input('введите координату x:'))
        if A[y + 1][x + 1] == '-':
            A[y + 1][x + 1] = 'x'
            draw_matrix(A)
            if check_win() == 0: break
            turn = '0'
        else:
            print('Неверный ход!')


