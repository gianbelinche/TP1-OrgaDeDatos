#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
datos = pd.read_csv("Entrenamieto_ECI_2020.csv")
gp = datos[["Bureaucratic_Code_0_Approval","Bureaucratic_Code_0_Approved","Stage"]]
gp = gp.groupby(["Bureaucratic_Code_0_Approval","Bureaucratic_Code_0_Approved"])
gp = gp["Stage"].value_counts(normalize = True)
gp = gp.filter(like = "Closed Won")
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
gp.plot(kind="bar",color=(1,0.6,0.3,0.7))
style.use("seaborn")
plt.title("Bureaucratic Code vs Closed Won")
plt.xlabel("Bureaucratic Code")
plt.ylabel("Closed Won %")
plt.xticks(np.arange(3),("Not Necesarry","Not Approved","Approved"))
plt.show()


# In[ ]:




