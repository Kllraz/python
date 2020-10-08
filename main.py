from abc import abstractmethod


class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        """Возвращает новый объект матрицы, получившийся в результате их сложения"""

        new_matrix = []

        if isinstance(other, Matrix):
            for i in zip(self.matrix, other.matrix):
                temp = []
                for j in zip(i[0], i[1]):
                    temp.append(sum(j))
                new_matrix.append(temp)
            return Matrix(new_matrix)
        else:
            return 0

    def __str__(self):
        """Возвращает строку, привучную для просмотра матрицы"""

        res = ''
        for i in self.matrix:
            res += f'{i}\n'
        return res


my_matrix = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]
]

my_matrix_2 = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]
]

matrix = Matrix(my_matrix)
matrix_2 = Matrix(my_matrix_2)

print(matrix)
print(matrix + matrix_2)


class Clothes(object):
    @abstractmethod
    def fabric_counting(self):
        """Возвращает расход ткани"""
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def fabric_counting(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def fabric_counting(self):
        return 2 * self.h + 3


coat = Coat(20)
suit = Suit(30)
print(coat.fabric_counting, suit.fabric_counting)


class Cell(object):
    def __init__(self, val):
        self.num_cells = [i for i in range(1, val + 1)]

    def __add__(self, other):
        """Возвращает новый объект, в котором кол-во ячеек равно сумме кол-во ячеек двух клеток"""
        if isinstance(other, Cell):
            count = len(self.num_cells) + len(other.num_cells)

            return Cell(count)

    def __sub__(self, other):
        """Возвращает объект, в котором кол-во клеток равно разности кол-во ячеек двух клеток.
         Если результат отрицательный, то выводится ошибка"""

        if isinstance(other, Cell):
            count = len(self.num_cells)
            count_other = len(other.num_cells)

            result = count - count_other
            if result > 0:
                return Cell(result)
            else:
                print("Отрицательный результат не допустим!")

    def __mul__(self, other):
        """Возвращает объект, в котором кол-во ячеек является произведение кол-во ячеек двух клеток"""

        if isinstance(other, Cell):
            count = len(self.num_cells)
            count_other = len(other.num_cells)
            result = count * count_other

            return Cell(result)

    def __truediv__(self, other):
        """Возвращает объект, в котором кол-во ячеек равно целочисленному результату от деления вух клеток"""

        if isinstance(other, Cell):
            count = len(self.num_cells)
            count_other = len(other.num_cells)
            result = round(count / count_other)

            return Cell(result)

    def make_order(self, rows):
        """Возвращает строку, где количество ячеек между \n равно переданному аргументу"""

        res = ''
        new_list = [self.num_cells[i:i + len(self.num_cells) // rows]
                    for i in range(0, len(self.num_cells), len(self.num_cells) // rows)]

        for i in new_list:
            temp = ' '.join(map(str, i))
            res += f'{temp}\n'

        return res


cell = Cell(20)

cell_2 = Cell(25)

print(cell + cell_2)
print(cell - cell_2)
print(cell * cell_2)
print(cell / cell_2)
print(cell.make_order(4))
