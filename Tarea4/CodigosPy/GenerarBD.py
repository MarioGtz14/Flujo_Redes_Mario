import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
import time

'''
------------------------------------------------------------
Parametros
------------------------------------------------------------
'''
base=3
inicio=3
ordebase=5
orden=[pow(base,i) for i in range(inicio,inicio+ordebase)]

cantidadgrafos=10

media=15
desviacion=5

parejas=5

repeticiones=100



f=open('ReporteT4.txt','w')
f.write('Generador' + '\t' + 'Orden' + '\t' + 'Solucion' + '\t' + 'Pareja' +'\t' + 'Replica' + '\n')
f.close()

for x1 in orden:
   
   for x2 in range(cantidadgrafos):
      
      for x3 in range(parejas):
         #Tiempo para el algoritmo generador a1, en el orden x1, en el grafo x2
         #en el orden de parejas x3, sumando el tiempo de las repeticiones
         #hecho por el algoritmo de sol. a2
         
         T11=[]
         T12=[]
         T13=[]
         T21=[]
         T22=[]
         T23=[]
         T31=[]
         T32=[]
         T33=[]
         
         
         for x4 in range(repeticiones):
      
            '''
            ------------------------------------
            '''
            
            
            #Crear grafo 1
            t1i=time.time()
            G = nx.grid_graph(dim=[x1, x1])
            t1f=time.time()
            
            K=[_ for _ in G.edges()]
            
            #Generar pesos normales y positivos
            Pesos=[max(0.1,random.gauss(media,desviacion)) for _ in range(len(K))]
            
            #Actualizar el grafo
            e=[]
            for i in range(len(G.edges())):
               
               a=(K[i][0],K[i][1],Pesos[i])  
               e.append(a)
            
            G.add_weighted_edges_from(e)
            
            
            #Seleccionar nodo fuente y nodo destino 
            buscar=True
            while buscar:
               
               origen1=random.randint(0, x1-1)
               origen2=random.randint(0, x1-1)
               destino1=random.randint(0, x1-1)
               destino2=random.randint(0, x1-1)
               
               if origen1==destino1 and origen2==destino2:
                  buscar=True
               else:
                  buscar=False
            
            
            
            
            #Aplicar el primer algoritmo
            t11i=time.time()
            Max_Flujo, Flujo_Arcos = nx.maximum_flow(G, (origen1,origen2),(destino1,destino2), capacity='weight')
            t11f=time.time()
            
            #Aplicar el primer algoritmo
            t12i=time.time()
            cut_value = nx.minimum_cut_value(G, (origen1,origen2),(destino1,destino2),capacity='weight')            
            t12f=time.time()
            
            #Aplicar el primer algoritmo
            t13i=time.time()
            flow_value = nx.maximum_flow_value(G, (origen1,origen2),(destino1,destino2),capacity='weight')
            t13f=time.time()
            
            tcreacion1 = t1f-t1i
            
            ta1a1=t11f-t11i
            ta1a2=t12f-t12i
            ta1a3=t13f-t13i
            
            T11.append(tcreacion1 + ta1a1)
            T12.append(tcreacion1 + ta1a2)
            T13.append(tcreacion1 + ta1a3)
            
            '''
            ------------------------------------
            '''
            
            
            '''
            ------------------------------------
            '''
            
            
            #Crear grafo 2
            t2i=time.time()
            H = nx.complete_graph(x1)
            t2f=time.time()
            
            K=[_ for _ in H.edges()]
            
            #Generar pesos normales y positivos
            Pesos=[max(0.1,random.gauss(media,desviacion)) for _ in range(len(K))]
            
            #Actualizar el grafo
            e=[]
            for i in range(len(H.edges())):
               
               a=(K[i][0],K[i][1],Pesos[i])  
               e.append(a)
            
            H.add_weighted_edges_from(e)
            
            #Seleccionar nodo fuente y nodo destino 
            buscar=True
            while buscar:
               
               origen2=random.randint(0, x1-1)
               destino2=random.randint(0, x1-1)
               
               if origen2==destino2:
                  buscar=True
               else:
                  buscar=False
                  
            
            
            #Aplicar el primer algoritmo
            t21i=time.time()
            Max_Flujo, Flujo_Arcos = nx.maximum_flow(H, origen2,destino2, capacity='weight')
            t21f=time.time()
            
            #Aplicar el primer algoritmo
            t22i=time.time()
            cut_value = nx.minimum_cut_value(H, origen2,destino2,capacity='weight')            
            t22f=time.time()
            
            #Aplicar el primer algoritmo
            t23i=time.time()
            flow_value = nx.maximum_flow_value(H,origen2,destino2,capacity='weight')
            t23f=time.time()
            
            tcreacion2 = t2f-t2i
            
            ta2a1=t21f-t21i
            ta2a2=t22f-t22i
            ta2a3=t23f-t23i
            
            T21.append(tcreacion2 + ta2a1)
            T22.append(tcreacion2 + ta2a2)
            T23.append(tcreacion2 + ta2a3)
            
            '''
            ------------------------------------
            '''
            
                  
            '''
            ------------------------------------
            '''
            
            
            
            #Crear grafo 3
            t3i=time.time()
            W= nx.circular_ladder_graph(x1)
            t3f=time.time()
            
            K=[_ for _ in W.edges()]
            
            #Generar pesos normales y positivos
            Pesos=[max(0.1,random.gauss(media,desviacion)) for _ in range(len(K))]
            
            #Actualizar el grafo
            e=[]
            for i in range(len(W.edges())):
               
               a=(K[i][0],K[i][1],Pesos[i])  
               e.append(a)
            
            W.add_weighted_edges_from(e)
            
            #Seleccionar nodo fuente y nodo destino 
            buscar=True
            while buscar:
               
               origen2=random.randint(0, x1-1)
               destino2=random.randint(0, x1-1)
               
               if origen2==destino2:
                  buscar=True
               else:
                  buscar=False
                  
            
            
            
            #Aplicar el primer algoritmo
            t31i=time.time()
            Max_Flujo, Flujo_Arcos = nx.maximum_flow(W, origen2,destino2, capacity='weight')
            t31f=time.time()
            
            #Aplicar el primer algoritmo
            t32i=time.time()
            cut_value = nx.minimum_cut_value(W, origen2,destino2,capacity='weight')            
            t32f=time.time()
            
            #Aplicar el primer algoritmo
            t33i=time.time()
            flow_value = nx.maximum_flow_value(W,origen2,destino2,capacity='weight')
            t33f=time.time()
            
            tcreacion3 = t3f-t3i
            
            ta3a1=t31f-t31i
            ta3a2=t32f-t32i
            ta3a3=t33f-t33i
            
            T31.append(tcreacion3 + ta3a1)
            T32.append(tcreacion3 + ta3a2)
            T33.append(tcreacion3 + ta3a3)
            
         
         media11=np.sum(T11)
         media12=np.sum(T12)
         media13=np.sum(T13)
         
         media21=np.sum(T21)
         media22=np.sum(T22)
         media23=np.sum(T23)
         
         media31=np.sum(T31)
         media32=np.sum(T32)
         media33=np.sum(T33)
         
         
         #Aqui se pegarian las cosas en el reporte 
         f=open('ReporteT4.txt','a')
         f.write(str(1) + '\t' + str(x1) + '\t' + str(1) + '\t' + str(x3) + '\t' + str(x2) +'\t' + str(media11) +'\n')
         f.write(str(1) + '\t' + str(x1) + '\t' + str(2) + '\t' + str(x3) + '\t' + str(x2) +'\t' + str(media12)+ '\n')
         f.write(str(1) + '\t' + str(x1) + '\t' + str(3) + '\t' + str(x3) + '\t' + str(x2) +'\t' + str(media13)+ '\n')
         f.write(str(2) + '\t' + str(x1) + '\t' + str(1) + '\t' + str(x3) + '\t' + str(x2) +'\t' + str(media21)+ '\n')
         f.write(str(2) + '\t' + str(x1) + '\t' + str(2) + '\t' + str(x3) + '\t' + str(x2) +'\t' + str(media22)+ '\n')
         f.write(str(2) + '\t' + str(x1) + '\t' + str(3) + '\t' + str(x3) + '\t' + str(x2) +'\t' + str(media23)+ '\n')
         f.write(str(3) + '\t' + str(x1) + '\t' + str(1) + '\t' + str(x3) + '\t' + str(x2) +'\t' + str(media31)+ '\n')
         f.write(str(3) + '\t' + str(x1) + '\t' + str(2) + '\t' + str(x3) + '\t' + str(x2) +'\t' + str(media32)+ '\n')
         f.write(str(3) + '\t' + str(x1) + '\t' + str(3) + '\t' + str(x3) + '\t' + str(x2) +'\t' + str(media33)+ '\n')
         f.close()   

