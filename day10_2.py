import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
datf = pd.DataFrame({"Season 1": [7, 4, 5, 6, 3],
                    "Season 2": [1, 2, 8, 4, 9]})

p = sns.histplot(data = datf)
p.set(xlabel="X Label Value", ylabel = "Y Label Value")
plt.show()


#######################TASK 3#############

import matplotlib.pyplot as plt
import numpy as np 

np.random.seed(42)
data = np.random.randint(30, 90, 1000)

plt.hist(data, bins = 16, edgecolor='black', color='skyblue')

plt.title('Histogram of Cancer patients')
plt.xlabel('Patient Age')

plt.ylabel('Number of patients')

plt.show()