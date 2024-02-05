import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())

one_hot = pd.get_dummies(data['whoAmI'], dtype=int)
data = data.drop('whoAmI', axis=1)
data = data.join(one_hot)
print(data.head())