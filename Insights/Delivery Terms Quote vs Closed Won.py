#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
datos = pd.read_csv("Entrenamieto_ECI_2020.csv")
gp = datos[["Pricing, Delivery_Terms_Quote_Appr","Pricing, Delivery_Terms_Approved","Stage"]]
gp = gp.groupby(["Pricing, Delivery_Terms_Quote_Appr","Pricing, Delivery_Terms_Approved"])
gp = gp["Stage"].value_counts(normalize = True)
gp = gp.filter(like = "Closed Won")
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
gp.plot(kind="bar",color=(0,0.8,0.6,0.7))
style.use("seaborn")
plt.title("Delivery Terms Quote vs Closed Won")
plt.xlabel("Delivery Terms Quote")
plt.ylabel("Closed Won %")
plt.xticks(np.arange(3),("Not Necesarry","Not Approved","Approved"))
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




