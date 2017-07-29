import pandas as pd
import numpy as np
import random
import string

def UserPrompt():
    print("Hello, User.")
    user_response1 = int(input(print("\nPlease enter the number of rows in your dataset")))
    user_response2 = int(input(print("\nPlease enter the number of columns in your dataset")))
    return user_response1, user_response2

def ColumnGenerator(number_of_columns):
    columns_list = []
    columns_counter = range(0, number_of_columns)
    columns_headers = string.ascii_uppercase
    for each in columns_counter:
        columns_list.append(columns_headers[each])
    return columns_list


def RowGenerator(number_of_rows, row_length):
    rows_list = []
    for number in range(number_of_rows):
        group_list = []
        for value in range(row_length):
            value = random.randrange(1, 10000)
            group_list.append(value)
        rows_list.append(group_list)
    return rows_list

size = UserPrompt()
rows = size[0]
cols = size[1]
print("Rows = " + str(rows))
print("Columns = " + str(cols))

data_set = RowGenerator(rows, cols)
headers = ColumnGenerator(cols)
df = pd.DataFrame(np.array(data_set), columns=headers)
print(df)
#print(df.loc[:, "A"])
print(np.std(df))
