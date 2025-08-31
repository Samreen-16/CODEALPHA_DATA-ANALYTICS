import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 
data = np.random.randn(1000) 
sns.histplot(data, kde=True) 
plt.title('Random Data Distribution') 
plt.show() 
