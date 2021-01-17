import random as rnd
import pickle


class Cell:
    def __init__(self):
        self.changeable = True
        self.number = -1
        self.possible_numbers = possible_numbers = {1, 2, 3, 4, 5, 6}


class Field:
    def __init__(self):
        self.cells = [[Cell() for i in range(6)] for j in range(6)]

    def try_place(self, x, y, v):
        return v in self.cells[x][y].possible_numbers

    def try_remove(self, x, y):
        return self.cells[x][y].number != -1 and self.cells[x][y].changeable

    def update_possible_numbers(self):
        for i in range(6):
            for j in range(6):
                self.cells[i][j].possible_numbers = {1, 2, 3, 4, 5, 6}
        for i in range(6):
            for j in range(6):
                if self.cells[i][j].number != -1:
                    self.place(i, j, self.cells[i][j].number)

    def place(self, x, y, v):
        for i in range(6):
            self.cells[i][y].possible_numbers.discard(v)
            self.cells[x][i].possible_numbers.discard(v)
        block_x = x // 2
        block_y = y // 3
        for i in range(block_x * 2, block_x * 2 + 2):
            for j in range(block_y * 3, block_y * 3 + 3):
                self.cells[i][j].possible_numbers.discard(v)
        self.cells[x][y].number = v
        self.cells[x][y].possible_numbers = set()

    def remove(self, x, y):
        self.cells[x][y].number = -1
        self.update_possible_numbers()

    def generate(self):
        for j in range(rnd.randrange(6, 11)):
            x = rnd.randrange(6)
            y = rnd.randrange(6)
            while not(len(self.cells[x][y].possible_numbers)):
                x = rnd.randrange(6)
                y = rnd.randrange(6)
            sz = len(self.cells[x][y].possible_numbers)
            self.cells[x][y].changeable = False
            self.place(x, y, list(self.cells[x][y].possible_numbers)[rnd.randrange(sz)])

    def __str__(self):
        result = ""
        for i in range(6):
            for j in range(6):
                v = self.cells[i][j].number
                result += (str(v) if v != -1 else "-") + " "
                if j == 2:
                    result += " "
            result += "\n"
            if i == 1 or i == 3:
                result += "\n"
        return result


class Game:
    def __init__(self):
        self.field = Field()
        self.field.generate()
        game_mode = int(input("""Выберите режим:
1 - начать новую игру
2 - загрузить игру"""))
        if game_mode == 2:
            while 1:
                try:
                    self.load_game()
                except FileNotFoundError:
                    print('Неверный путь к файлу\n')
                break
        print("""Каждый ход задаётся тремя числами - позицией строки, столбца и числом,
которое нужно поставить на эту позицию. Верхняя левая ячейка имеет координаты (1, 1).
Чтобы удалить число введите -1 вместо числа.

Число можно поставить только в том случае, если в одном столбце, в одной
строке и в одном блоке нет такого же числа, а также если число в этой ячейке
не было сгенерировано изначально.

Удалить число из ячейки можно только если там уже есть какое-то число,
и это число не было сгенерировано изначально.

После каждого хода игра автоматически сохраняется в файл save.pkl.""")
        print(self.field)
        while True:
            x, y, v = map(int, input("Введите ход ").split())
            try:
                if v == -1:
                    if not(self.field.try_remove(x - 1, y - 1)):
                        print('Невозможно удалить это число')
                        continue
                    self.field.remove(x - 1, y - 1)
                else:
                    if not(self.field.try_place(x - 1, y - 1, v)):
                        print('Невозможно поставить это число')
                        continue
                    self.field.place(x - 1, y - 1, v)
            except IndexError:
                print('индексы ячеек лежат в диапозоне от 1 до 6 включительно')
                continue
            print(self.field)
            with open("save_file.pkl", "wb") as save_file:
                pickle.dump(self.field, save_file)

    def load_game(self):
        path = input("Ведите полный путь до файла сохранения\n")
        with open(path, 'rb') as save_file:
            self.field = pickle.load(save_file)


g = Game()
