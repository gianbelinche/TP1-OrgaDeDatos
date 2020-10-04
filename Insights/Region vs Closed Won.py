#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
datos = pd.read_csv("Entrenamieto_ECI_2020.csv")
datos.loc[datos["Region"] == "Middle East",:]["Stage"].value_counts(normalize=True)


# In[149]:


gp = datos[["Region","Stage"]].groupby("Region")["Stage"].value_counts(normalize=True)
gp = gp.filter(like = "Closed Won")
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
gp.plot(kind="bar",color=(1,0.3,0.6,0.7))
style.use("seaborn")
plt.title("Region vs Closed Won")
plt.xlabel("Region")
plt.ylabel("Closed Won %")
plt.xticks(np.arange(5),("APAC","America","EMEA","Japan","Middle East"))
plt.show()


# In[ ]:





# In[ ]:




