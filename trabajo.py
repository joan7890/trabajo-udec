#ejercicio 1: Desarrollar un programa que permita solicitar 15 valores al usuario mostrar el resultado de la suma de los mismos y su promedio. print("hola, ingresa 15 valores")
print("hola,ingrese 15 valores")

numeros=[]
for i in range(15):
   valor =float(input("ingresa el valor {}: ".format(i+1)))
   numeros.append(valor)

#calcular la suma de los valores
sumatotal=sum(numeros)

#calcular el promedio de los valores
promedio=sumatotal / len(numeros)

#mostrar resultado
print("el promedio de los valores es: ",sumatotal)
print("El promedio de los valores es:", promedio)

#ejercicio 2: La alcaldía de Fusagasuga tiene puntos de reparto de vacunas contra el covid-19, se pretende que funcionen de la sigu
def reparto_vacunas():
    inventario = 1000
    while inventario > 0:
      print("Inventario actual de vacunas:", inventario)    
   
      if inventario < 200:
         print("El inventario es menor a 200 unidades.")
  
      entregas = int(input("ingrese la cantidad de vacunas entregadas hoy (o para salir): "))
   
      if entregas == 0:
         print("saliendo del programa")
         break
      inventario -= entregas
print("el inventario de vacunas ha llegado a cero. Fin del programa")
if __name__ =="__main__":
   reparto_vacunas()