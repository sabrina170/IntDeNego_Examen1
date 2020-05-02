import pandas as pd
import numpy as np

data=pd.read_excel('BI_Clientes.xlsx',sheet_name="Hoja1")
grupo1=data['YearlyIncome']
grupo2=data['TotalChildren']

def MedidaCentral1():
    m1=grupo1.mean()
    mo1=grupo1.mode()
    me1=grupo1.median()
    print('Media de YearlyIncome: ',m1)
    print('Moda de YearlyIncome: ',mo1)
    print('Mediana de YearlyIncome: ',me1)
def MedidaCentral2():
    m2=grupo2.mean()
    mo2=grupo2.mode()
    me2=grupo2.median()
    print('Media de TotalChildren: ',m2)
    print('Moda de TotalChildren: ',mo2)
    print('Mediana de TotalChildren: ',me2)
MedidaCentral1()
MedidaCentral2()

