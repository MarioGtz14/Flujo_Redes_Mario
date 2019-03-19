import networkx as nx
import time

'''
---------------------------------------------------------------------------
Parametros
---------------------------------------------------------------------------
'''
Replicas = 5
Repeticiones = 70000

f = open ('Reportef.txt','w')
f.write("Corrida" + "\t" + "Replica" + "\t" + "TPE" + "\n")
f.close()

'''
---------------------------------------------------------------------------
Grafos
---------------------------------------------------------------------------
'''
G1=nx.DiGraph()

Arcos=[(0,1,{'peso':4}),(0,2,{'peso':2}),(1,3,{'peso':3}),
       (1,4,{'peso':10}),(2,3,{'peso':9}),(3,4,{'peso':5})]
G1.add_edges_from(Arcos)
pos1=nx.spectral_layout(G1)

tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      Algoritmo = nx.all_shortest_paths(G1, source=0, 
                                        target=4, weight = 'peso')
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
         
   tiempos.append(T)  
   f = open ('Reportef.txt','a')
   f.write("0" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()



G2 = nx.DiGraph()

Arcos=[(0,1,{'peso':7}),(0,4,{'peso':4}),(1,2,{'peso':3}),
       (3,2,{'peso':8}),(4,3,{'peso':5})]
G2.add_edges_from(Arcos)
pos2=nx.spectral_layout(G2)
      
tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      Algoritmo = nx.all_shortest_paths(G2, source=0, target=2, weight = 'peso')
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
      
   tiempos.append(T) 
   f = open ('Reportef.txt','a')
   f.write("1" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()


G3 = nx.DiGraph()
      
Arcos=[(0,1,{'peso':3}),(0,3,{'peso':4}),(0,4,{'peso':12}),
       (1,2,{'peso':6}),(1,4,{'peso':6}),(2,4,{'peso':2}),
       (3,2,{'peso':5}),(3,4,{'peso':9})]
G3.add_edges_from(Arcos)

pos3=nx.spectral_layout(G3)

tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      Algoritmo = nx.all_shortest_paths(G3,source=0,target=4,weight='peso')
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
      
      
   tiempos.append(T) 
   f = open ('Reportef.txt','a')
   f.write("2" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()



G4 = nx.DiGraph()
      
Arcos=[(0,3,{'peso':4}),(1,2,{'peso':8}),(3,1,{'peso':6}),
       (3,2,{'peso':11}),(3,4,{'peso':2}),(4,0,{'peso':9}),
       (4,2,{'peso':7})]
G4.add_edges_from(Arcos)

pos4=nx.spectral_layout(G4)

tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      Algoritmo = nx.all_shortest_paths(G4, source=3, target=2, weight = 'peso')
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T) 
   f = open ('Reportef.txt','a')
   f.write("3" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()
   
   
G5 = nx.DiGraph()
      
Arcos=[(0,1,{'peso':11}),(0,2,{'peso':9}),(1,2,{'peso':2}),
       (2,3,{'peso':4}),(3,4,{'peso':2}),(3,5,{'peso':13}),
       (4,5,{'peso':5})]
G5.add_edges_from(Arcos)

pos5=nx.circular_layout(G5)

tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      Algoritmo = nx.all_shortest_paths(G5, source=0, target=5, weight = 'peso')
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T)
   f = open ('Reportef.txt','a')
   f.write("4" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()
   
   
   
G6 = nx.DiGraph()
      
Arcos=[(0,1),(0,2),(1,3),(1,4),(2,3),(3,4)]
G6.add_edges_from(Arcos)

#Posicion asignada (Proporcionada por el algoritmo de acomodo)
pos6=nx.spectral_layout(G6)

tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      Coeficientes = nx.betweenness_centrality(G6,normalized=True)
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T)
   f = open ('Reportef.txt','a')
   f.write("5" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()
   
G7 = nx.DiGraph()
      
Arcos=[(0,1),(0,4),(1,2),(3,2),(4,3)]
G7.add_edges_from(Arcos)

pos7=nx.spectral_layout(G7)

tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      Coeficientes = nx.betweenness_centrality(G7,normalized=True)
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T) 
   f = open ('Reportef.txt','a')
   f.write("6" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()
   
G8 = nx.DiGraph()
      
Arcos=[(0,1),(0,3),(0,4),(1,2),(1,4),(2,4),(3,2),(3,4)]
G8.add_edges_from(Arcos)

pos8=nx.spectral_layout(G8)

tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      Coeficientes = nx.betweenness_centrality(G8,normalized=True)
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T)
   f = open ('Reportef.txt','a')
   f.write("7" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()
   
G9 = nx.DiGraph()
      
Arcos=[(0,3),(1,2),(3,1),(3,2),(3,4),(4,0),(4,2)]
G9.add_edges_from(Arcos)

pos9=nx.spectral_layout(G9)

tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      Coeficientes = nx.betweenness_centrality(G9,normalized=True)
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T)
   f = open ('Reportef.txt','a')
   f.write("8" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()
   
G10 = nx.DiGraph()
      
Arcos=[(0,1),(0,2),(1,2),(2,3),(3,4),(3,5),(4,5)]
G10.add_edges_from(Arcos)

pos10=nx.circular_layout(G10)

tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      Coeficientes = nx.betweenness_centrality(G10,normalized=True)
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T)
   f = open ('Reportef.txt','a')
   f.write("9" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()


G11 = nx.Graph()
      
Arcos=[(0,1),(0,2),(1,3),(1,4),(2,3),(3,4)]
G11.add_edges_from(Arcos)

#Posicion asignada (Proporcionada por el algoritmo de acomodo)
pos11=nx.spectral_layout(G11)

tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      d = nx.coloring.greedy_color(G11, strategy='largest_first')
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T)
   f = open ('Reportef.txt','a')
   f.write("10" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()
   
G12 = nx.Graph()
      
Arcos=[(0,1),(0,4),(1,2),(3,2),(3,4)]
G12.add_edges_from(Arcos)

pos12=nx.spectral_layout(G12)

tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      d = nx.coloring.greedy_color(G12, strategy='largest_first')
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T)
   f = open ('Reportef.txt','a')
   f.write("11" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()
         
G13 = nx.Graph()
      
Arcos=[(0,1),(0,3),(0,4),(1,2),(1,4),(2,3),(2,4),(3,4)]
G13.add_edges_from(Arcos)

pos13=nx.spectral_layout(G13)

tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      d = nx.coloring.greedy_color(G13, strategy='largest_first')
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T) 
   f = open ('Reportef.txt','a')
   f.write("12" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()

   
G14 = nx.Graph()
      
Arcos=[(0,3),(1,2),(3,1),(3,2),(3,4),(4,0),(4,2)]
G14.add_edges_from(Arcos)

pos14=nx.spectral_layout(G14)

tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      d = nx.coloring.greedy_color(G14, strategy='largest_first')
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T) 
   f = open ('Reportef.txt','a')
   f.write("13" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()
         
G15 = nx.Graph()
      
Arcos=[(0,1),(0,2),(1,2),(2,3),(3,4),(3,5),(4,5)]
G15.add_edges_from(Arcos)

pos15=nx.circular_layout(G15)

tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      d = nx.coloring.greedy_color(G15, strategy='largest_first')
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T) 
   f = open ('Reportef.txt','a')
   f.write("14" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()


G16 = nx.DiGraph()
      
Arcos=[(0,1,{'capacidad':4}),(0,2,{'capacidad':2}),(1,3,{'capacidad':3}),
       (1,4,{'capacidad':10}),(2,3,{'capacidad':9}),(3,4,{'capacidad':5})]
G16.add_edges_from(Arcos)

pos16=nx.spectral_layout(G16)

tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      Max_Flujo, Flujo_Arcos = nx.maximum_flow(G16, 0,4, capacity='capacidad')
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T)   
   f = open ('Reportef.txt','a')
   f.write("15" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()
         
         
G17 = nx.DiGraph()
      
Arcos=[(0,1,{'capacidad':7}),(0,4,{'capacidad':4}),(1,2,{'capacidad':3}),
       (3,2,{'capacidad':8}),(4,3,{'capacidad':5})]
G17.add_edges_from(Arcos)

pos17=nx.spectral_layout(G17)

#Calcular tiempo de replicas y promedio 
tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      Max_Flujo, Flujo_Arcos = nx.maximum_flow(G17, 0,2, capacity='capacidad')
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T)   
   f = open ('Reportef.txt','a')
   f.write("16" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()
         

G18 = nx.DiGraph()
      
Arcos=[(0,1,{'capacidad':3}),(0,3,{'capacidad':4}),(0,4,{'capacidad':12}),
       (1,2,{'capacidad':6}),(1,4,{'capacidad':6}),(2,4,{'capacidad':2}),
       (3,2,{'capacidad':5}),(3,4,{'capacidad':9})]
G18.add_edges_from(Arcos)

pos18=nx.spectral_layout(G18)

#Calcular tiempo de replicas y promedio 
tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      Max_Flujo, Flujo_Arcos = nx.maximum_flow(G18, 0,4, capacity='capacidad')
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T)   
   f = open ('Reportef.txt','a')
   f.write("17" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()
         
         
G19 = nx.DiGraph()
      
Arcos=[(0,3,{'capacidad':4}),(1,2,{'capacidad':8}),(3,1,{'capacidad':6}),
       (3,2,{'capacidad':11}),(3,4,{'capacidad':2}),(4,0,{'capacidad':9}),
       (4,2,{'capacidad':7})]
G19.add_edges_from(Arcos)

pos19=nx.spectral_layout(G19)

#Calcular tiempo de replicas y promedio 
tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      Max_Flujo, Flujo_Arcos = nx.maximum_flow(G19, 3,2, capacity='capacidad')
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T) 
   f = open ('Reportef.txt','a')
   f.write("18" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()
         
         
G20 = nx.DiGraph()
      
Arcos=[(0,1,{'capacidad':11}),(0,2,{'capacidad':9}),(1,2,{'capacidad':2}),
       (2,3,{'capacidad':4}),(3,4,{'capacidad':2}),(3,5,{'capacidad':13}),
       (4,5,{'capacidad':5})]
G20.add_edges_from(Arcos)

pos20=nx.circular_layout(G20)

#Calcular tiempo de replicas y promedio 
tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      Max_Flujo, Flujo_Arcos = nx.maximum_flow(G20, 0,5, capacity='capacidad')
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T) 
   f = open ('Reportef.txt','a')
   f.write("19" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()
         
         
G21 = nx.Graph()
      
Arcos=[(0,1,{'weight':4}),(0,2,{'weight':2}),(1,3,{'weight':3}),
       (1,4,{'weight':10}),(2,3,{'weight':9}),(3,4,{'weight':5})]

G21.add_edges_from(Arcos)
pos21=nx.spectral_layout(G21)

tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      Tm = nx.minimum_spanning_tree(G21,algorithm='kruskal')
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T)   
   f = open ('Reportef.txt','a')
   f.write("20" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()
         
         
G22 = nx.Graph()

Arcos=[(0,1,{'peso':7}),(0,4,{'peso':4}),(1,2,{'peso':3}),
       (3,2,{'peso':8}),(4,3,{'peso':5})]
G22.add_edges_from(Arcos)

pos22=nx.spectral_layout(G22)

tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      Tm = nx.minimum_spanning_tree(G22,algorithm='kruskal')
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T) 
   f = open ('Reportef.txt','a')
   f.write("21" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()
         
         
G23 = nx.Graph()

Arcos=[(0,1,{'weight':3}),(0,3,{'weight':4}),(0,4,{'weight':12}),
       (1,2,{'weight':6}),(1,4,{'weight':6}),(2,4,{'weight':2}),
       (3,2,{'weight':5}),(3,4,{'weight':9})]
G23.add_edges_from(Arcos)

pos23=nx.spectral_layout(G23)

tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      Tm = nx.minimum_spanning_tree(G23,algorithm='kruskal')
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T) 
   f = open ('Reportef.txt','a')
   f.write("22" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()
         
         
G24 = nx.Graph()

Arcos=[(0,3,{'weight':4}),(1,2,{'weight':8}),(3,1,{'weight':6}),
       (3,2,{'weight':11}),(3,4,{'weight':2}),(4,0,{'weight':9}),
       (4,2,{'weight':7})]
G24.add_edges_from(Arcos)

pos24=nx.spectral_layout(G24)

tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      Tm = nx.minimum_spanning_tree(G24,algorithm='kruskal')
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T)  
   f = open ('Reportef.txt','a')
   f.write("23" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()
         
         
G25 = nx.Graph()
      
Arcos=[(0,1,{'weight':11}),(0,2,{'weight':9}),(1,2,{'weight':2}),
       (2,3,{'weight':4}),(3,4,{'weight':2}),(3,5,{'weight':13}),
       (4,5,{'weight':5})]
G25.add_edges_from(Arcos)

pos25=nx.circular_layout(G25)

tiempos=[]
for i in range(Replicas):
   T=0
   for j in range(Repeticiones):
      inicio = time.time()
      Tm = nx.minimum_spanning_tree(G25,algorithm='kruskal')
      final = time.time()
      T = T + final - inicio
      T=round(T,4)
   
   tiempos.append(T)  
   f = open ('Reportef.txt','a')
   f.write("24" + "\t" + str(i) + "\t" + str(T) + "\n")
   f.close()