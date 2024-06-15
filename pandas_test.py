import pandas as pd



## checking version ####

print(pd.__version__)

### example for Pandas Series ###

arr = [1,2,3,4,5]
ser_arr = pd.Series(arr, index = ['a','b','c','d','e'])
print(ser_arr)

### dictionary as series 

my_dict = {'1':'Monday', '2':'Tuesday', '3':'Wednesday'}
ser_my_dict = pd.Series(my_dict)
print(ser_my_dict)

ser_half_my_dict = pd.Series(my_dict, ['1','3'])
print(ser_half_my_dict)


### exmaple dataset for DataFrame ####

custom_dataset = {
    'Name' : ['Ash', 'Naruto', 'Levi'],
    'Age' : ['12','25','26']
}

df_custom = pd.DataFrame(custom_dataset)

print("\n",df_custom)

print("\n",df_custom.loc[0])

print("\n",df_custom.loc[[0,2]])