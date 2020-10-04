#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
datos = pd.read_csv("Entrenamieto_ECI_2020.csv")
gp = datos.groupby("Size")["Stage"].value_counts()
gp


# In[ ]:


#Esto me indica que la columna size no da informacion valida sobre el modelo, ya que cuando no se conoce el tamaño
#El resultado no esta definido, pero al conocerse el tamaño el resultado es siempre perdido, esto no tiene sentido alguno
#Ya que aun en los casos en que el tamaño es "None", debe ser alguno de los tamaños posibles
#Por lo que intuyo que es un resultado del azar y no que el hecho de conocer el tamaño implique que el caso sera perdido

