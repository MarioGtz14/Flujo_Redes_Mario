from Clase1 import Instancia,Comparacion_caracteristicas
import warnings

warnings.simplefilter("ignore")

def main():
   
   Inst1 = Instancia(8,2,10,3,40,100,1) #ultimos, 3 y 50
   Inst2 = Instancia(8,3,10,3,40,100,2)
   Inst3 = Instancia(8,4,10,3,40,100,3)
   Inst4 = Instancia(16,2,10,3,40,100,4)
   Inst5 = Instancia(16,3,10,3,40,100,5)
   
   
   Comparacion_caracteristicas([Inst1,Inst2,Inst3,Inst4,Inst5])
   
main()   