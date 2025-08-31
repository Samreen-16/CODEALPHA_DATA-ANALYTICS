import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
df = sns.load_dataset('titanic') 
print(df.info()) 
sns.countplot(x='survived', data=df) 
plt.title('Survival Count') 
plt.show() 
