#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#LIBRERIAS
import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns
import pandas as pd
import time
import numpy as np
import random
#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
class Instancia:
   #-------------------------------------------------------------------------------------------
   #-------------------------------------------------------------------------------------------
   def __init__(self,x1,x2,x3,x4,x5,x6,x7):
      #----------------------------------------------------------
      #Parametros
      #----------------------------------------------------------
      orden = x1
      conexiones = x2
      media = x3
      desviacion = x4
      repeticiones = x5
      replicas = x6
      numero = x7
      #----------------------------------------------------------
      #Crear Grafo
      #----------------------------------------------------------
      G = nx.barabasi_albert_graph(orden,conexiones)
      self.G=G
      pos=nx.kamada_kawai_layout(G)
      #----------------------------------------------------------
      #Crear y asignar pesos
      #----------------------------------------------------------
      K=[_ for _ in G.edges()]
      Pesos=[round(max(0.1,random.gauss(media,desviacion)),2) for _ in range(len(K))]
      e=[]
      for i in range(len(G.edges())):
         
         a=(K[i][0],K[i][1],Pesos[i])  
         e.append(a)
      
      G.add_weighted_edges_from(e)
      
      Capacidad=nx.get_edge_attributes(G,'weight')
      #----------------------------------------------------------
      #buscar nodo fuente y sumidero
      #----------------------------------------------------------
      buscar = True
      while buscar:
         inicio = random.randint(0,orden-1)
         final = random.randint(0,orden-1)
         
         if inicio != final:
            buscar=False
      
      Txt='Inicio: {} Final {}'
      print(Txt.format(inicio,final))
      #----------------------------------------------------------
      #Algoritmo de solucion
      #----------------------------------------------------------
      Max_Flujo, Flujo_Arcos = nx.maximum_flow(G, inicio,final, capacity='weight')
      print(Max_Flujo)
      objetivo=Max_Flujo
      #----------------------------------------------------------
      #Graficar instancia y solucion
      #----------------------------------------------------------
      Grosor_capacidad=[]
      Grosor_flujo=[]
      
      for (i,j) in nx.get_edge_attributes(G,'weight').keys():
         Grosor_capacidad.append(Capacidad[(i,j)]*.5)
         if Flujo_Arcos[i][j]>0: #Depende el orden de salida, ya que python los toma de menor a mayor
            Grosor_flujo.append(Flujo_Arcos[i][j]*.5)
         else:
            Grosor_flujo.append(Flujo_Arcos[j][i]*.5)
            
      
      nx.draw_networkx_nodes(G,pos,nodelist=G.nodes(),node_color='teal',node_size=200,node_shape='o')
      nx.draw_networkx_nodes(G,pos,nodelist=[inicio],node_color='fuchsia', node_shape='s',node_size=500)
      nx.draw_networkx_nodes(G,pos,nodelist=[final],node_color='r', node_shape='s',node_size=500)  
      nx.draw_networkx_edges(G,pos,edgelist=G.edges(),edge_color='lightgray',width=Grosor_capacidad)
      
      
      plt.axis('off')
      plot_margin = 0.05
      x0, x1, y0, y1 = plt.axis()
      plt.axis((x0 - plot_margin,x1 + plot_margin,y0 - plot_margin,y1 + plot_margin))
      plt.tight_layout()
      nombre = "G_" + str(numero) + "_1"+ ".eps"
      plt.savefig(nombre)
      plt.show()
      
      
      nx.draw_networkx_nodes(G,pos,nodelist=G.nodes(),node_color='teal',node_size=200,node_shape='o')
      nx.draw_networkx_nodes(G,pos,nodelist=[inicio],node_color='fuchsia', node_shape='s',node_size=500)
      nx.draw_networkx_nodes(G,pos,nodelist=[final],node_color='r', node_shape='s',node_size=500)  
      nx.draw_networkx_edges(G,pos,edgelist=G.edges(),edge_color='lightgray',width=Grosor_capacidad)
      nx.draw_networkx_edges(G,pos,edge_color='dodgerblue',width=Grosor_flujo, style='--')
      nx.draw_networkx_labels(G,pos,font_color='w')
      
      plt.axis('off')
      plot_margin = 0.05
      x0, x1, y0, y1 = plt.axis()
      plt.axis((x0 - plot_margin,x1 + plot_margin,y0 - plot_margin,y1 + plot_margin))
      plt.tight_layout()
      plt.show()
      
      #----------------------------------------------------------
      #Tamaño
      #----------------------------------------------------------
      Coeficientes1 = nx.betweenness_centrality(G, normalized=True)
      Coeficientes2 = nx.closeness_centrality(G)
      Coeficientes3 = nx.clustering(G)
      Coeficientes4 = nx.load_centrality(G)
      
      tamaño1 =  [w1 for w1 in Coeficientes1.values()]
      tamaño2 =  [w2 for w2 in Coeficientes2.values()]
      tamaño3 =  [w3 for w3 in Coeficientes3.values()]
      tamaño4 =  [w4 for w4 in Coeficientes4.values()]
      
      #Normalizar
      #--------------------------------------
      suma1=0
      suma2=0
      suma3=0
      suma4=0
      for i in G.nodes():
         suma1=suma1+tamaño1[i]
         suma2=suma2+tamaño2[i]
         suma3=suma3+tamaño3[i]
         suma4=suma4+tamaño4[i]
         
      tamaño=[]
      for i in G.nodes():
         
         w1=tamaño1[i]/suma1
         w2=tamaño2[i]/suma2
         w3=tamaño3[i]/suma3
         w4=tamaño4[i]/suma4
         
         tamaño.append(1000*(w1+w2+w3+w4))
      #----------------------------------------------------------
      #Graficar solucion con caracteristicas de nodos 
      #----------------------------------------------------------
      nx.draw_networkx_nodes(G,pos,nodelist=G.nodes(),node_color='teal',node_size=tamaño,node_shape='o')
      nx.draw_networkx_nodes(G,pos,nodelist=[inicio],node_color='fuchsia', node_shape='s',node_size=tamaño[inicio])
      nx.draw_networkx_nodes(G,pos,nodelist=[final],node_color='r', node_shape='s',node_size=tamaño[final])  
      nx.draw_networkx_edges(G,pos,edgelist=G.edges(),edge_color='lightgray',width=Grosor_capacidad)
      nx.draw_networkx_edges(G,pos,edge_color='dodgerblue',width=Grosor_flujo, style='--')
      
      
      plt.axis('off')
      plot_margin = 0.05
      x0, x1, y0, y1 = plt.axis()
      plt.axis((x0 - plot_margin,x1 + plot_margin,y0 - plot_margin,y1 + plot_margin))
      plt.tight_layout()
      nombre = "G_" + str(numero) + "_2"+ ".eps"
      plt.savefig(nombre)
      plt.show()
      #----------------------------------------------------------
      #Variar el nodo t
      #----------------------------------------------------------
      aux=final
      BD1=[]
      mejores_t=[]
      for i in G.nodes():
         if i!=inicio:
            final=i
            for k in range(repeticiones):
               t_inicial = time.time()
               for j in range(replicas):
                  Max_Flujo, Flujo_Arcos = nx.maximum_flow(G, inicio,final, capacity='weight')
               t_final = time.time()
               BD1.append([inicio,final,round(t_final-t_inicial,4),round(Max_Flujo,4)])
            if round(Max_Flujo,4)-objetivo>.1:
               mejores_t.append(final)
      final=aux
      BD1=pd.DataFrame(BD1,columns=['I', 'F', 'TE','FO'])
      #----------------------------------------------------------
      #Variar el nodo s
      #----------------------------------------------------------
      print('')
      aux=inicio
      BD2=[]
      mejores_s=[]
      for i in G.nodes():
         if i!=final:
            inicio=i
            for k in range(repeticiones):
               t_inicial = time.time()
               for j in range(replicas):
                  Max_Flujo, Flujo_Arcos = nx.maximum_flow(G, inicio,final, capacity='weight')
               t_final = time.time()
               BD2.append([inicio,final,round(t_final-t_inicial,4),round(Max_Flujo,4)])
            if round(Max_Flujo,4)-objetivo>.1:
               mejores_s.append(inicio)
      inicio=aux
      BD2=pd.DataFrame(BD2,columns=['I', 'F', 'TE','FO'])
      #----------------------------------------------------------
      #Eliminar un nodo y resolver el problema para
      #detectar cuello de botella
      #----------------------------------------------------------
      print('')
      BD3=[]
      mejores_elim=[]
      for i in G.nodes(): 
         if i!= inicio and i != final:
            Gaux=G.copy()
            Gaux.remove_node(i)
            
            for k in range(repeticiones):
               t_inicial = time.time()
               for j in range(replicas):
                  Max_Flujo, Flujo_Arcos = nx.maximum_flow(Gaux, inicio,final, capacity='weight')
               t_final = time.time()
               BD3.append([i,round(t_final-t_inicial,4),round(Max_Flujo,4)])
            if round(Max_Flujo,4)-objetivo>.1:
               mejores_elim.append(i)
      BD3=pd.DataFrame(BD3,columns=['El', 'TE','FO'])
      
      #----------------------------------------------------------
      #Graficar solucion con buenos nodos fuente y sumidero
      #----------------------------------------------------------
      
      nodos1=[]
      nodos2=[]
      nodos3=[]
      nodos4=[]
      
      color1=[]
      color2=[]
      color3=[]
      color4=[]
      
      tamaño1=[]
      tamaño2=[]
      tamaño3=[]
      tamaño4=[]
      
      for i in G.nodes():
         if i!=inicio and i!=final:
            if i in mejores_s and i not in mejores_t:
               nodos1.append(i)
               color1.append('limegreen')
               tamaño1.append(tamaño[i])
            if i in mejores_t and i not in mejores_s:
               nodos2.append(i)
               color2.append('limegreen')
               tamaño2.append(tamaño[i])
            if i in mejores_s and i in mejores_t:
               nodos3.append(i)
               color3.append('darkgreen')
               tamaño3.append(tamaño[i])
            if i not in mejores_s and i not in mejores_t:
               nodos4.append(i)
               color4.append('teal')
               tamaño4.append(tamaño[i])
               
      #mejores s pero no t
      nx.draw_networkx_nodes(G,pos,nodelist=nodos1,node_color=color1,node_size=tamaño1,node_shape='o')
      nx.draw_networkx_nodes(G,pos,nodelist=nodos1,node_color='b',node_size=[i*.5 for i in tamaño1],node_shape='o')
      #mejores t pero no s
      nx.draw_networkx_nodes(G,pos,nodelist=nodos2,node_color=color2,node_size=tamaño2,node_shape='o')
      nx.draw_networkx_nodes(G,pos,nodelist=nodos2,node_color='indigo',node_size=[i*.5 for i in tamaño2],node_shape='o')
      #mejores s y t
      nx.draw_networkx_nodes(G,pos,nodelist=nodos3,node_color=color3,node_size=tamaño3,node_shape='o')
      #sin mejora
      nx.draw_networkx_nodes(G,pos,nodelist=nodos4,node_color=color4,node_size=tamaño4,node_shape='o')
      #inicio
      nx.draw_networkx_nodes(G,pos,nodelist=[inicio],node_color='fuchsia', node_shape='s',node_size=tamaño[inicio])
      #final
      nx.draw_networkx_nodes(G,pos,nodelist=[final],node_color='r', node_shape='s',node_size=tamaño[final])  
      #capacidad
      nx.draw_networkx_edges(G,pos,edgelist=G.edges(),edge_color='lightgray',width=Grosor_capacidad)
      #flujo
      nx.draw_networkx_edges(G,pos,edge_color='dodgerblue',width=Grosor_flujo, style='--')
      #nx.draw_networkx_labels(G,pos,font_color='w')
      
      plt.axis('off')
      plot_margin = 0.05
      x0, x1, y0, y1 = plt.axis()
      plt.axis((x0 - plot_margin,x1 + plot_margin,y0 - plot_margin,y1 + plot_margin))
      plt.tight_layout()
      nombre = "G_" + str(numero) + "_3"+ ".eps"
      plt.savefig(nombre)
      plt.show()
      
      #----------------------------------------------------------
      #Grafica de comparacion de tiempo de ejecucion variando
      #el nodo destino
      #----------------------------------------------------------
      
      bplot=sns.boxplot(y='TE', x='F', data=BD1, width=0.4,palette="colorblind")      
      bplot=sns.swarmplot(y='TE', x='F',data=BD1, color='black',alpha=0.0)
      bplot.axes.set_title("Tiempo de ejecución cambiando\n el nodo destino partiendo del nodo "+str(inicio),fontsize=13)
      
      
      j=0
      for c_nodo in range(orden):
         if c_nodo!=inicio:
            BD_aux1 = BD1.loc[BD1.F == c_nodo]
            BD_array = np.asarray(BD_aux1['TE'])
            
            if max(np.asarray(BD_aux1['FO'])) - objetivo >0.1:
               plt.text(j-0.3,max(BD_array)+0.0007 , max(np.asarray(BD_aux1['FO'])),color='r',size=7)
            else:
               plt.text(j-0.3,max(BD_array)+0.0007 , max(np.asarray(BD_aux1['FO'])),color='b',size=7)
            j=j+1
            
      
      bplot.set_xlabel("Nodo destino", fontsize=11)
      bplot.set_ylabel("Tiempo(segs.)",fontsize=11)
      bplot.tick_params(labelsize=9)
      nombre = "CD_" + str(numero) + ".eps"
      plt.savefig(nombre)
      plt.show()
      
      #----------------------------------------------------------
      #Grafica de comparacion de tiempo de ejecucion variando
      #el nodo fuente
      #----------------------------------------------------------
      
      bplot=sns.boxplot(y='TE', x='I', data=BD2, width=0.4,palette="colorblind")      
      bplot=sns.swarmplot(y='TE', x='I',data=BD2, color='black',alpha=0.0)
      bplot.axes.set_title("Tiempo de ejecución cambiando\n el nodo fuente llegando al nodo "+str(final),fontsize=13)
      
      j=0
      for c_nodo in range(orden):
         if c_nodo!=final:
            BD_aux2 = BD2.loc[BD2.I == c_nodo]
            BD_array = np.asarray(BD_aux2['TE'])
            
            if max(np.asarray(BD_aux2['FO'])) - objetivo>0.1:
               plt.text(j-0.3,max(BD_array)+0.0007 , max(np.asarray(BD_aux2['FO'])),color='r',size=7)
            else:
               plt.text(j-0.3,max(BD_array)+0.0007 , max(np.asarray(BD_aux2['FO'])),color='b',size=7)
            j=j+1
      
      bplot.set_xlabel("Nodo fuente", fontsize=11)
      bplot.set_ylabel("Tiempo(segs.)",fontsize=11)
      bplot.tick_params(labelsize=9)
      nombre = "CF_" + str(numero) + ".eps"
      plt.savefig(nombre)
      plt.show()
      
      #----------------------------------------------------------
      #Grafica de comparacion de tiempo de ejecucion variando
      #un nodo intermedio que se elimina
      #----------------------------------------------------------
      
      bplot=sns.boxplot(y='TE', x='El', data=BD3, width=0.4,palette="colorblind")      
      bplot=sns.swarmplot(y='TE', x='El',data=BD3, color='black',alpha=0.0)
      bplot.axes.set_title("Tiempo de ejecución cambiando\n el nodo intermedio eliminado",fontsize=13)
      
      j=0
      for c_nodo in range(orden):
         if c_nodo!=final and c_nodo!=inicio:
            BD_aux3 = BD3.loc[BD3.El == c_nodo ]
            BD_array = np.asarray(BD_aux3['TE'])
            
            
            if max(np.asarray(BD_aux3['FO'])) - objetivo >0.1:
               plt.text(j-0.3,max(BD_array)+0.0004 , max(np.asarray(BD_aux3['FO'])),color='r',size=7)
            else:
               plt.text(j-0.3,max(BD_array)+0.0004 , max(np.asarray(BD_aux3['FO'])),color='b',size=7)
            j=j+1
      
      bplot.set_xlabel("Nodo eliminado", fontsize=11)
      bplot.set_ylabel("Tiempo(segs.)",fontsize=11)
      bplot.tick_params(labelsize=9)
      nombre = "CE_" + str(numero) + ".eps"
      plt.savefig(nombre)
      plt.show()
      
      
def Comparacion_caracteristicas(Arreglo_Inst):
   
   A1=[]       #Guardara las listas de los ranking de nodos para cada grafo con el algoritmo 1
   A2=[]       #Guardara las listas de los ranking de nodos para cada grafo con el algoritmo 2
   A3=[]       #Guardara las listas de los ranking de nodos para cada grafo con el algoritmo 3
   A4=[]       #Guardara las listas de los ranking de nodos para cada grafo con el algoritmo 4
   A5=[]       #Guardara las listas de los ranking de nodos para cada grafo con el algoritmo 5
   A6=[]       #Guardara las listas de los ranking de nodos para cada grafo con el algoritmo 6
   
   for instancia in Arreglo_Inst:
      
      #Algoritmo 1 - nx.degree_centrality(G)      
      a1=[i for i in nx.degree_centrality(instancia.G).values()]
      
      #Algoritmo 2 - nx.closeness_centrality(G)      
      a2=[i for i in nx.closeness_centrality(instancia.G).values()]
      
      #Algoritmo 3 - nx.clustering(G)      
      a3=[i for i in nx.clustering(instancia.G).values()]
      
      #Algoritmo 4 - nx.load_centrality(G)      
      a4=[i for i in nx.load_centrality(instancia.G).values()]
      
      #Algoritmo 5 - nx.eccentricity(G)      
      a5=[i for i in nx.eccentricity(instancia.G).values()]
      
      #Algoritmo 6 - nx.pagerank(G)      
      a6=[i for i in nx.pagerank(instancia.G).values()]
   
      
      A1.append(a1)
      A2.append(a2)
      A3.append(a3)
      A4.append(a4)
      A5.append(a5)
      A6.append(a6)
      #print(instancia.G.nodes())
      

   
   #Boxplots
   BDA1 = [[1,i,j, A1[i][j]] for i in range(len(Arreglo_Inst)) for j in range(len(A1[i]))]
   BDA2 = [[2,i,j, A2[i][j]] for i in range(len(Arreglo_Inst)) for j in range(len(A2[i]))]
   BDA3 = [[3,i,j, A3[i][j]] for i in range(len(Arreglo_Inst)) for j in range(len(A3[i]))]
   BDA4 = [[4,i,j, A4[i][j]] for i in range(len(Arreglo_Inst)) for j in range(len(A4[i]))]
   BDA5 = [[5,i,j, A5[i][j]] for i in range(len(Arreglo_Inst)) for j in range(len(A5[i]))]
   BDA6 = [[6,i,j, A6[i][j]] for i in range(len(Arreglo_Inst)) for j in range(len(A6[i]))]
   
   BDA1=pd.DataFrame(BDA1,columns=['A', 'G','N','R']) #Algoritmo,Grafo,Nodo,Ranking
   BDA2=pd.DataFrame(BDA2,columns=['A', 'G','N','R'])
   BDA3=pd.DataFrame(BDA3,columns=['A', 'G','N','R'])
   BDA4=pd.DataFrame(BDA4,columns=['A', 'G','N','R'])
   BDA5=pd.DataFrame(BDA5,columns=['A', 'G','N','R'])
   BDA6=pd.DataFrame(BDA6,columns=['A', 'G','N','R'])
   
   bplot=sns.boxplot(y='R', x='G', data=BDA1, width=0.4,palette="colorblind")      
   bplot.axes.set_title("Comparación por grafo \n para el algoritmo degree_centrality",fontsize=13)
   bplot.set_xlabel("Grafo", fontsize=11)
   bplot.set_ylabel("Ranking",fontsize=11)
   bplot.tick_params(labelsize=9)
   plt.xticks(range(0, len(Arreglo_Inst)), range(1, len(Arreglo_Inst)+1))
   plt.savefig("CA_1.eps")
   plt.show()
   
   bplot=sns.boxplot(y='R', x='G', data=BDA2, width=0.4,palette="colorblind")      
   bplot.axes.set_title("Comparación por grafo \n para el algoritmo closeness_centrality",fontsize=13)
   bplot.set_xlabel("Grafo", fontsize=11)
   bplot.set_ylabel("Ranking",fontsize=11)
   bplot.tick_params(labelsize=9)
   plt.xticks(range(0, len(Arreglo_Inst)), range(1, len(Arreglo_Inst)+1))
   plt.savefig("CA_2.eps")
   plt.show()
   
   bplot=sns.boxplot(y='R', x='G', data=BDA3, width=0.4,palette="colorblind")      
   bplot.axes.set_title("Comparación por grafo \n para el algoritmo clustering",fontsize=13)
   bplot.set_xlabel("Grafo", fontsize=11)
   bplot.set_ylabel("Ranking",fontsize=11)
   bplot.tick_params(labelsize=9)
   plt.xticks(range(0, len(Arreglo_Inst)), range(1, len(Arreglo_Inst)+1))
   plt.savefig("CA_3.eps")
   plt.show()
   
   bplot=sns.boxplot(y='R', x='G', data=BDA4, width=0.4,palette="colorblind")      
   bplot.axes.set_title("Comparación por grafo \n para el algoritmo load_centrality",fontsize=13)
   bplot.set_xlabel("Grafo", fontsize=11)
   bplot.set_ylabel("Ranking",fontsize=11)
   bplot.tick_params(labelsize=9)
   plt.xticks(range(0, len(Arreglo_Inst)), range(1, len(Arreglo_Inst)+1))
   plt.savefig("CA_4.eps")
   plt.show()
   
   bplot=sns.boxplot(y='R', x='G', data=BDA5, width=0.4,palette="colorblind")      
   bplot.axes.set_title("Comparación por grafo \n para el algoritmo eccentricity",fontsize=13)
   bplot.set_xlabel("Grafo", fontsize=11)
   bplot.set_ylabel("Ranking",fontsize=11)
   bplot.tick_params(labelsize=9)
   plt.xticks(range(0, len(Arreglo_Inst)), range(1, len(Arreglo_Inst)+1))
   plt.savefig("CA_5.eps")
   plt.show()
   
   bplot=sns.boxplot(y='R', x='G', data=BDA6, width=0.4,palette="colorblind")      
   bplot.axes.set_title("Comparación por grafo \n para el algoritmo pagerank",fontsize=13)
   bplot.set_xlabel("Grafo", fontsize=11)
   bplot.set_ylabel("Ranking",fontsize=11)
   bplot.tick_params(labelsize=9)
   plt.xticks(range(0, len(Arreglo_Inst)), range(1, len(Arreglo_Inst)+1))
   plt.savefig("CA_6.eps")
   plt.show()
   
   '''
   #Histogramas
   Algoritmo1 = [A1[j] for j in range(len(Arreglo_Inst))]
   Algoritmo2 = [A2[j] for j in range(len(Arreglo_Inst))]
   Algoritmo3 = [A3[j] for j in range(len(Arreglo_Inst))]
   Algoritmo4 = [A4[j] for j in range(len(Arreglo_Inst))]
   Algoritmo5 = [A5[j] for j in range(len(Arreglo_Inst))]
   Algoritmo6 = [A6[j] for j in range(len(Arreglo_Inst))]
   
   
   Algoritmos=[Algoritmo1,Algoritmo2,Algoritmo3,Algoritmo4,Algoritmo5,Algoritmo6]
   
   for i in range(len(Algoritmos)):
      
      bins = np.linspace(0, 1, 5)
      
      for j in range(len(Arreglo_Inst)):
         nombre='Inst'+str(j+1)
         plt.hist(Algoritmos[i][j], bins, alpha=0.3, label=nombre)

      plt.legend(loc='upper right') 
      plt.show() 
   '''

   
   '''
   import matplotlib
   pyplot.show()
   
   import matplotlib.pyplot as plt
   plt.show()
   '''
      
   