from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import statsmodels.api as sm
import networkx as nx
import seaborn as sns
import pandas as pd
import numpy as np
import time

import random

Datos = pd.read_csv("BDT4.csv",header=None)
Datos.columns = ["Generador", "Orden", "Solucion","Pareja","Grafo", "Densidad", "Tiempo"]

#Grafico de cajas
sns.boxplot(x = 'Generador', y = 'Tiempo', data = Datos) 
plt.savefig("A1.eps")
plt.show()
sns.boxplot(x = 'Orden', y = 'Tiempo', data = Datos) 
plt.savefig("A2.eps")
plt.show()
sns.boxplot(x = 'Solucion', y = 'Tiempo', data = Datos) 
plt.savefig("A3.eps")
plt.show()
sns.boxplot(x = 'Densidad', y = 'Tiempo', data = Datos) 
plt.savefig("A4.eps")
plt.show()


#Modelo de analisis de varianza
modelo_int = ols('Tiempo ~ Generador + Orden + Solucion + Densidad + Generador*Orden + Generador*Solucion+Generador*Densidad + Orden*Solucion + Orden*Densidad + Solucion*Densidad ', \
        data = Datos).fit() 


ANOVA = sm.stats.anova_lm(modelo_int, typ = 2)
print(ANOVA)

for i in range(len(ANOVA)):
    print("{:s} {:s}es significativo".format(ANOVA.index[i], "" if ANOVA['PR(>F)'][i] < 0.05 else "NO "))
    