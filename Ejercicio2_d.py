import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
archivo="WEO_Data.csv"
data=pd.read_csv(archivo,thousands=',',decimal='.')
print(data)
data.rename(columns={'Country':'Pais'},inplace=True)
data.set_index('Pais',inplace=True)
def grafico1():
    top10 = data.sort_values(by='2020', ascending=True, inplace=True)
    top10 = data['2019'].tail(10)
    top10.plot(kind='barh')
    plt.title('10 paises con mayor PBI del 2019')
    plt.ylabel('Paises')
    plt.xlabel('Millones')
    plt.show()
grafico1()