# Задача 44: В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид.
# Сделать без встроенных ф-ций, например,get_dummies?

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

# 1
data.loc[data['whoAmI'] == 'robot', 'robot_group'] = '1'
data.loc[data['whoAmI'] != 'robot', 'robot_group'] = '0'
data.loc[data['whoAmI'] == 'human', 'human_group'] = '1'
data.loc[data['whoAmI'] != 'human', 'human_group'] = '0'
print(data)
