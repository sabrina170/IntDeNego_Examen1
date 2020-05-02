import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
archivo="WEO_Data.csv"
data=pd.read_csv(archivo,thousands=',',decimal='.')
print(data)
data.rename(columns={'Country':'Pais'},inplace=True)
data.set_index('Pais',inplace=True)
periodo=list(map(str,range(2000,2024)))
def grafico1():
    china=data.loc['China',periodo]
    EU=data.loc['United States',periodo]
    print(china,EU)
    china.plot(kind="line")
    EU.plot(kind="line")

    plt.title('PBI de los paises China y Estados unidos')
    plt.legend(['China','Estados Unidos'])
    plt.ylabel('Millones')
    plt.xlabel('Años')
    plt.show()
grafico1()