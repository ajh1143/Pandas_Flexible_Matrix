# Pandas Flexible Matrix

#### Imports
```Python3
from itertools import count, product, islice
import pandas as pd
import numpy as np
import random
import string
```
#### Class
```Python3
class MatrixPermutation(object)
```

#### User Input
```Python3

    def UserPrompt(self):
        print("Hello, User.")
        print("\nPlease enter the number of rows in your dataset")
        user_rows = int(input())
        print("\nPlease enter the number of columns in your dataset")
        user_columns = int(input())
        return user_rows, user_columns
```

#### Generate Headers
```Python3
    def ColumnHeaderGenerator(self):
        columns_headers = string.ascii_uppercase
        for each in count(1):
            for all in product(columns_headers, repeat=each):
               yield ''.join(all)
```
#### Generate Rows
```Python3
    def RowGenerator(self, number_of_rows, row_length):
        rows_list = []
        for number in range(number_of_rows):
            group_list = []
            for value in range(row_length):
                value = random.randrange(1, 10000)
                group_list.append(value)
            rows_list.append(group_list)
        return rows_list
```

#### Generate DataFrame & Calculate Standard Deviation Per Group
```Python3
    def DataFrameGenerator(self, Data, Headers):
        df = pd.DataFrame(np.array(Data), columns=Headers)
        print(df)
        print(np.std(df).round(2))
```

#### Running it
```Python3
if __name__ == '__main__':
    a = MatrixPermutation()
    size = a.UserPrompt()
    rows = size[0]
    cols = size[1]
    print("Rows = " + str(rows))
    print("Columns = " + str(cols))
    data_set = a.RowGenerator(rows, cols)
    headers = list(islice(a.ColumnHeaderGenerator(), cols))
    a.DataFrameGenerator(data_set, headers)
```
