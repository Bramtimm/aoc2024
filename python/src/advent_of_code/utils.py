from typing import Any
import itertools


class Matrix:
    def __init__(self, nrow: int, ncol: int, data: Any | None, fill: str = ""):
        self.nrow = nrow
        self.ncol = ncol

        if data is None:
            self.data = [[fill for _ in range(ncol)] for _ in range(nrow)]
        else:
            self.data = data

    def __getitem__(self, key):
        if isinstance(key, int):
            row_index = key
            return self.data[row_index]

        if isinstance(key, tuple) and len(key) == 2:
            row_index, col_index = key

            if isinstance(row_index, int) and isinstance(col_index, int):
                return self.data[row_index][col_index]

            if isinstance(row_index, slice):
                row_indices = range(*row_index.indices(self.nrow))
                row_sliced = [self.data[i] for i in row_indices]
            elif isinstance(row_index, int):
                row_sliced = [self.data[row_index]]

            if isinstance(col_index, slice):
                col_indices = range(*col_index.indices(self.nrow))
                result_data = [[row[j] for j in col_indices] for row in row_sliced]
            elif isinstance(col_index, int):
                result_data = [row[col_index] for row in row_sliced]

            cls = type(self)
            return cls(len(result_data), len(result_data), result_data)

    def __setitem__(self, index, value):
        row_index, col_index = index
        self.data[row_index][col_index] = value

    def get_diagonal(self):
        self.diagonal = []
        for diag_index in range(0, self.nrow):
            self.diagonal.append(self.data[diag_index][diag_index])

        return self.diagonal

    def get_reverse_diagonal(self):
        self.reverse_diagonal = []

        for diag_index in range(0, self.nrow):
            self.reverse_diagonal.append(
                self.data[diag_index][self.ncol - diag_index - 1]
            )
        return self.reverse_diagonal

    def get_column(self, col_index):
        self.column = []
        for i in range(0, self.nrow):
            self.column.append(self.data[i][col_index])

        return self.column

    def get_unique_items(self, exclude=[]):
        self.unique_items = []
        for row in self.data:
            for item in row:
                if item not in self.unique_items and item not in exclude:
                    self.unique_items.append(item)
        return self.unique_items

    def count_nr_of_item(self, item):
        self.count = 0
        for row in self.data:
            for i in row:
                if i == item:
                    self.count += 1
        return self.count

    def flatten(self):
        return list(itertools.chain.from_iterable(self.data))

    def __repr__(self):
        return f"Matrix(\n{self.data})"

    def __str__(self):
        for rows in self.data:
            print(rows)
