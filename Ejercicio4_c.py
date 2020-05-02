import xlrd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_excel('BI_Clientes.xlsx',sheet_name="Hoja1")

CantGen=data.groupby('Gender')['YearlyIncome'].mean()
print(CantGen)
CantGen.plot(kind="pie",autopct="%0.1f %%")
plt.title('Ingreso Promedio Anual  por Genero')
plt.legend(['Femenino','Masculino'])
plt.show()