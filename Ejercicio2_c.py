import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
archivo="WEO_Data.csv"
data=pd.read_csv(archivo,thousands=',',decimal='.')
data.rename(columns={'Country':'Pais'},inplace=True)
data.set_index('Pais', inplace=True)

EEUU=data.loc['United States','2019']
China=data.loc['China','2019']
Japan= data.loc['Japan', '2019']
Germany = data.loc['Germany', '2019']
France = data.loc['France', '2019']
Brazil = data.loc['Brazil', '2019']
Peru = data.loc['Peru', '2019']
paises=([EEUU,China,Japan,Germany,France,Brazil,Peru])
x=np.arange(7)
names=['EEUU','China','Japòn','Alemania','Francia','Brasil','Perù']
plt.bar(x,paises,tick_label=names)
plt.title('PBI del 2019')
plt.ylabel('Millones')
plt.xlabel('Paises')
plt.show()
print(EEUU,China,Japan,Germany,France,Brazil,Peru, paises)
