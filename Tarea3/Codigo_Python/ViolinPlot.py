import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Datos = pd.read_csv('Tiempos.csv')
#Datos = np.array(Datos)
#print(Datos[:,0])

plt.figure(figsize=(6,12))
sns.violinplot(x=Datos['Tiempo'] ,y=Datos['Algoritmo'],hue= Datos['Grafo'] )
plt.savefig('grafica.eps')