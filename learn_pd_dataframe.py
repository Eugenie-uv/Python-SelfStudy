# -*- coding: utf-8 -*-
"""
学习pandas DataFrame
__________________________________
https://towardsdatascience.com/pandas-dataframe-a-lightweight-intro-680e3a212b96
_ _ _ _ _ \_ *^!^* _/ _ _ _ _ _
Created on Monday Oct 31 2018
@author:github.com/Eugenie-uv
"""

import pandas as pd
import numpy as np 

#  Creating a Pandas DataFrame from a dict
# =============================================================================
my_dict = {
    'name' : ["a", "b", "c", "d", "e", "f", "g"],
    'age' : [20, 27, 35, 55, 18, 21, 35],
    'designation' : ["VP", "CEO", "CFO", "VP", "VP", "CEO", "MD"]
}

df = pd.DataFrame(my_dict) # python implements dictionary as hash and doesn’t guarantee to preserve the sequence.
print(df) #python将字典实现为哈希，并不保证保留序列
#Python automatically generates a sequence (0…6) as row index.

# __________Index___________
# Add our own index with index parameter
df = pd.DataFrame(my_dict, index=[1,2,3,4,5,6,7])
print(df)

# Use stings act as index
df = pd.DataFrame(
    my_dict,
    index=["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh"]
)
print(df)

#  that Index are homogeneous in nature 
# which means we can also use NumPy arrays as Index.
np_arr = np.array([10, 20, 30, 40, 50, 60, 70])
df = pd.DataFrame(my_dict, index=np_arr)
print(df)

# Using Column as Row Index: pandas DataFrame allows setting any existing column or set of column as row index
df = pd.DataFrame(my_dict)
df.set_index("name", inplace=False)
print('use name as index')
print(df)

df.set_index(["name","age"])#, inplace=True)
print('use multiple columns as index')
print(df)


# __________check the data type of a column in two ways_________
# 1. Dictionary like syntax
df['age'].dtype
print(df['age'].dtype)

# 2. Adding the column name using DataFrame
df.age.dtype
df.name.dtype
print(df.age.dtype)
print(df.name.dtype)

# data types of all columns
print(df.dtypes)

# ______View the data of a DataFrame_______
# Use head() and tail() functions to show the first or last fice rows
print(df.head())

print(df.tail())

# Show specific number of rows from top or bottom
print( df.head(2) ) #Displays 1st tow rows

print( df.tail(1) ) #Displays last 1 row

# To show Row indexex and Columns name
print( df.index )

print( df.columns )

# _______load selectives columns in DataFrame_____________
df0 = pd.DataFrame( my_dict, columns = ["name", "age"] )
print( df0 )

# ___Delete Rows and Columns form DataFrame______
del df0['name']


# ______Pandas DataFrame Columns Helper Functions__________
# unique : provide unique elements from a column by removing duplicates.
print( df.designation.unique() )

# mean : priovide the mean value of all the items in the column
print( df.age.mean() )

# Drop : delete Columns as well as Rows
# the second argument in the drop function: 1 - delete column; 0 - delete row
# Delete Clounm "age"
df1 = df
df1.drop( 'age', 1 )
# Delete Row with Index "3"
df1.drop( 3, 0)

# Delete multiple Rows and Columns
df2 = df
df2.drop( ['name', 'age'], 1 )
# Delete rows with index "2", "3", "4"
df2.drop( [2,3,4], 0 )


#  Creating a Pandas DataFrame from a list
# =============================================================================
my_list = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
    [17,18,19,20]
]

df = pd.DataFrame( my_list )
print(df)

# Pass the Row Indexes and Column names to DataFrame
df = pd.DataFrame(
    my_list,
    index = ["1:", "2:", "3:", "4:", "5:"],
    columns = ["A", "B", "C", "D"]
)
print (df)

#  Creating a Pandas DataFrame from Numpy arrays
# =============================================================================
np_arr = np.array(
    [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16],
        [17,18,19,20]
    ]
)

df3 = pd.DataFrame(np_arr)
print(df3)

#  Mathematical Operations on DataFrame
# =============================================================================
# Multiplications
print( df * df )
print( df * 10 )

# Addition / Subtraction
print( df + 100 )

# BitWise Operation - And& Or| etc
print( df & 0 )