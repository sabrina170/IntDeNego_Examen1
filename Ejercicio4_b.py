import xlrd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_excel('BI_Clientes.xlsx',sheet_name="Hoja1")

CantGen=data.groupby('Gender')['YearlyIncome'].sum()
print(CantGen)
CantGen.plot(kind="barh")
plt.title('Ingreso Anual Acumulado por Genero')
plt.ylabel('Generos')
plt.xlabel('Millones')
plt.show()






