import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
titanic = sns.load_dataset('titanic')

#print(titanic['deck'])
#titanic['deck'] = titanic['deck'].cat.add_categories('Unknown')
#print(titanic['deck'])
#titanic['deck'].fillna('Unknown', inplace=True)
#print(titanic['deck'])
#print(titanic.info())
gender_survival=titanic.groupby(by='sex')['survived'].mean().reset_index()
print(gender_survival)
print(gender_survival.info())
print(titanic['survived'])

# sns.countplot(data=titanic,x='survived')
# plt.title('Survived ( 0=NO,1=YES)')
# plt.xlabel('survived')
# plt.ylabel('count')
plt.show()
