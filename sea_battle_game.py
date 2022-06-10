from random import randint
from random import choice

# Родительский класс ошибок BoardErrors(наследует класс Python Exception) и дочерние классы игровых ошибок
class BoardErrors(Exception):
    pass


class BoardOutError(BoardErrors):
    def __str__(self):
        return "Доска игры не такая большая!"


class BoardUsedError(BoardErrors):
    def __str__(self):
        return "В эту клетку нельзя стрелять!"


class BoardWrongShipError(BoardErrors):
    pass


# Класс точек с методом сравнения точек __eq__и методом __repr__ вывода объекта строкой в форме создания
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"


# Класс корабля с методом dots возвращает список всех точек корабля
class Ship:
    def __init__(self, nose_dot, size_of_ship, position):
        self.nose_dot = nose_dot
        self.size_of_ship = size_of_ship
        self.position = position
        self.rest_of_lives = size_of_ship

    @property
    def dots(self):
        dots_of_ship = []
        for i in range(self.size_of_ship):
            now_x = self.nose_dot.x
            now_y = self.nose_dot.y

            if self.position == 'h':
                now_x += i
            elif self.position == 'v':
                now_y += i
            dots_of_ship.append(Dot(now_x, now_y))
        return dots_of_ship


# Класс Игровой доски
class Board:
    def __init__(self, size=7, display=False):
        self.count = 0
        self.size = size
        self.display = display
        self.board_list = [[' '] * self.size for _ in
                           range(self.size)]
        self.ships = []
        self.busy = []
        self.y_coords = 1

# метод класса Board отрисовки игрового поля (доски)
    def draw_board(self):
        # v = [str(x + 1) for x in range(self.size)]
        print('\t')
        #print('  |  '.join(v), end='  |  ')
        print('    1     2     3     4     5     6  ')
        print('--------------------------------------')
        for y in range(len(self.board_list)):
            print(str(self.y_coords) + ' |', end=' ')
            for x in range(len(self.board_list[y])):
                print(self.board_list[x][y], end='  |  ')
            print()
            print()
            self.y_coords += 1
        self.y_coords = 1

# метод класса Board скрытия кораблей
    def hidden(self):
        for i in range(len(self.board_list)):
            for j in range(len(self.board_list[i])):
                if self.board_list[i][j] == "■" and not self.display:
                    self.board_list[i][j] = " "

# метод класса Board определяющий выход за пределы игровой доски (not!)
    def out(self, point):
        return not (
                    (0 <= point.x < self.size) and
                    (0 <= point.y < self.size)
                   )

# метод класса Board контура корабля
    def contour(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for point in ship.dots:
            for pointx, pointy in near:
                now = Dot(point.x + pointx, point.y +
                          pointy)
                if not ((self.out(now)) and
                        now not in self.busy):
                    if verb:
                        self.board_list[now.x][now.y] = "*"
                    self.busy.append(now)

# метод класса Board, добавляющий корабль на игровую доску
    def add_ship(self, ship):
        for point in ship.dots:
            if self.out(point) or point in self.busy:
                raise BoardWrongShipError()
        for point in ship.dots:
            self.board_list[point.x][point.y] = "■"
            self.busy.append(point)

        self.ships.append(ship)
        self.contour(ship)

# метод класса Board - выстрел
    def shot(self, point):
        if self.out(point):
            raise BoardOutError()

        if point in self.busy:
            raise BoardUsedError()

        self.busy.append(point)

        for ship in self.ships:
            if point in ship.dots:
                ship.rest_of_lives -= 1
                self.board_list[point.x][point.y] = "X"
                if ship.rest_of_lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("Потоплен!")
                    return False
                else:
                    print("Ранен!")
                    return True

        self.board_list[point.x][point.y] = "*"
        print("Мимо!")
        return False
# метод класса Board, обнуление занятых клеток
    def begin(self):
        self.busy = []

# Класс игрока
class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardErrors as e:
                print(e)


# Класс игрока - компьютер (наследует класс Player)
class AI(Player):
    def ask(self):
        point = Dot(randint(0, 5), randint(0, 5))
        print(f"Комп ходит: {point.x + 1} {point.y + 1}")
        return point


# Класс игрока - человек(наследует класс Player)
class User(Player):
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:
                print(" Введите 2 координаты! ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Введите числа! ")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)


# Класс Игры формирование, игровых досок
class Game:
    def try_board(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size),
                                randint(0, self.size)), l
                            , choice('hv'))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipError:
                    pass
        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

# метод класса Game - конструктор
    def __init__(self, size = 6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.display = True

        self.ai = AI(co, pl)
        self.us = User(pl, co)

# метод класса Game -приветствие
    def greet(self):
        print(" Приветствуем Вас в игре 'Морской бой'")
        print("--------------------------------------")
        print(" формат ввода: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")

# метод класса Game - игровой цикл
    def loop(self):
        num = 0
        while True:
            print("-" * 38)
            print("Ваша доска:")
            self.us.board.draw_board()
            print("-" * 38)
            print("Доска компьютера:")
            self.ai.board.hidden()
            self.ai.board.draw_board()
            print("-" * 38)
            if num % 2 == 0:
                print("Вы ходите!")
                repeat = self.us.move()
            else:
                print("Компьютер ходит!")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.count == 7:
                print("-" * 38)
                print("ВЫ выиграли!")
                break

            if self.us.board.count == 7:
                print("-" * 38)
                print("Компьютер выиграл!")
                break
            num += 1

# метод класса Game - стартуем
    def start(self):
        self.greet()
        self.loop()

# создаем экземпляр  класса Game и запускам
g = Game()
g.start()
