import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
archivo="WEO_Data.csv"
data=pd.read_csv(archivo,thousands=',',decimal='.')
print(data)
data.rename(columns={'Country':'Pais'},inplace=True)
data.set_index('Pais',inplace=True)
periodo=list(map(str,range(2014,2019)))
def grafico1():
    peru=data.loc['Peru',periodo]
    print(peru)
    peru.plot(kind="line")
    plt.title('PBI del Peru entre 2014-2019')
    plt.ylabel('Millones')
    plt.xlabel('Años')
    plt.show()
grafico1()