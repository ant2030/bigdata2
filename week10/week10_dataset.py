import seaborn as sns
import pandas as pd

# print(sns.get_dataset_names())
# mpg= sns.load_dataset('mpg')
# print(mpg.head().sort_values('mpg'))
#
#
titanic = sns.load_dataset(('titanic'))
# print(titanic.describe())
# print(titanic.head())
# print(len(titanic))
# print(titanic.tail(10))
# print(titanic.info())
# print(titanic['deck'])
titanic['deck'] = titanic ['deck'].cat.add_categories('unknown')
# print(titanic['deck'])
titanic['deck'].fillna('unknown',inplace=True)
print(titanic.info())