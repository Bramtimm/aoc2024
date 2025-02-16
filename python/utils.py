class Matrix:

    def __init__(self, nrow: int, ncol: int, fill: str = ""):
        self.nrow = nrow
        self.ncol = ncol
        self.data = [[fill for _ in range(ncol)] for _ in range(nrow)]

    def __getitem__(self, index):
        row_index, col_index = index
        return self.data[row_index][col_index]
    
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
            self.reverse_diagonal.append(self.data[diag_index][self.ncol-diag_index-1])
        return self.reverse_diagonal

    def get_column(self, col_index):
        
        self.column = []
        for i in range(0, self.nrow):
            self.column.append(self.data[i][col_index])

        return self.column
    
    def get_unique_items(self, exclude = []):
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
    
    def print_matrix(self):
        for rows in self.data:
            print(rows)
  