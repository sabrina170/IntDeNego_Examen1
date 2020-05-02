import xlrd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_excel('BI_Clientes.xlsx',sheet_name="Hoja1")

CantGen=data.groupby('Gender')['Gender'].count()
print(CantGen)
CantGen.plot(kind='barh')
plt.show()