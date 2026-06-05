from matrix_project.matrix import Matrix




class SquareMatrix(Matrix):

    def __init__(self, rows, column):
        super().__init__(rows, column)
        self.rows = rows
        self.column = rows
        self.matrix = [0 for i in range(rows * self.column)]




    def one_matrix_line(self) -> None:
        """Создает единичную матрицу"""
        for i in range(self.rows):
            self.matrix[i*self.rows + i] = 1
