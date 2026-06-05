import random


class Matrix:
    """Класс для работы с матрицами строконаправленными"""

    def __init__(self, rows, column, start_volume = 0, end_volume = 1000):
        self.rows = rows
        self.column = column
        self.matrix = [random.randint(start_volume, end_volume) for i in range(rows * column)]
        print(len(self.matrix))


    def __str__(self):
        result = []
        for i in range(self.column):
            temp = []
            for j in range(self.rows):
                temp.append(self._find_value(i, j))

            result.append(' '.join(list(map(str, temp))))
        return '\n'.join(result)




    def insert_matrix(self, row, column, value, matrix=None) -> None:
        self.matrix[row * self.rows + column] = value




    def norm(self, ntype = "e"):

        if ntype == 'e':
            return self._evklid()
        elif ntype == '1':
            return self._max_sum_column()
        elif ntype == 'inf':
            return self._max_sum_rows()
        else:
            return "None type"


    def _max_sum_rows(self):
        """Максимальная сумма значений строки"""
        maxi = 0

        for i in range(self.rows):
            row = []
            for j in range(self.column):
                row.append(self.matrix[i * self.rows + j])

            if sum(row) > maxi: maxi = sum(row)

        return maxi



    def _max_sum_column(self):
        """Максимальная сумма значений столбца"""
        maxi = 0

        for i in range(self.rows):
            column = []
            for j in range(i, len(self.matrix), self.rows):
                column.append(self.matrix[j])

            if sum(column) > maxi : maxi = sum(column)

        return maxi






    def _evklid(self):
        """Корень квадратный из квадратов всех ячеек матрицы"""
        return sum([i**2 for i in self.matrix])**0.5



    def _find_value(self, row, column):
        """Находит значение в определенной ячейке"""
        return self.matrix[row * self.rows + column]




    def transponir(self):
        """Меняет строки и столбцы местами"""

        mass = [0 for i in range(self.column * self.rows)]

        for i in range(self.rows):
            for j in range(self.column):
                mass[j * self.column + i] = self._find_value(i, j)

        self.matrix = mass
        trash = self.column
        self.column = self.rows
        self.rows = trash
