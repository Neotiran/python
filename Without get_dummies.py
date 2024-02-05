import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())

uni_val = list(set(lst))
one_hot = pd.DataFrame(columns=uni_val)

for value in uni_val:
    one_hot[value] = [1 if x == value else 0 for x in lst]

data = pd.concat([data, one_hot], axis=1)
data = data.drop('whoAmI', axis=1)
print(data.head())