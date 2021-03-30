class Matrix:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        sum_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(self.data)):
            for j in range(len(other.data)):
                sum_matrix[i][j] = self.data[i][j] + other.data[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in sum_matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.data]))


new_matrix_1 = Matrix([[1, 3, 4], [10, 20, 50], [3, 5, 7]])
new_matrix_2 = Matrix([[10, 23, 3], [11, 7, 5], [93, 65, 70]])
print(new_matrix_1, '\n')
print(new_matrix_2, '\n')
print('Результат сложения:\n')
print(new_matrix_1 + new_matrix_2)
