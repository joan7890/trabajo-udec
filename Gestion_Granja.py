class Cultivo:
    def __init__(self, nombre, tipo, area, rendimiento):
        self.nombre = nombre
        self.tipo = tipo
        self.area = area
        self.rendimiento = rendimiento

class Animal:
    def __init__(self, especie, raza, edad, peso):
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.peso = peso

class Produccion:
    def __init__(self):
        self.cultivos = []
        self.animales = []

    def agregar_cultivo(self, cultivo):
        self.cultivos.append(cultivo)

    def eliminar_cultivo(self, nombre):
        self.cultivos = [c for c in self.cultivos if c.nombre != nombre]

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def eliminar_animal(self, especie):
        self.animales = [a for a in self.animales if a.especie != especie]

    def calcular_produccion_cultivos(self):
        total = sum(c.rendimiento * c.area for c in self.cultivos)
        return total

    def calcular_produccion_ganado(self):
        total = sum(a.peso for a in self.animales)
        return total

class Granja:
    def __init__(self, produccion):
        self.produccion = produccion

    def calcular_produccion_total(self):
        produccion_cultivos = self.produccion.calcular_produccion_cultivos()
        produccion_ganado = self.produccion.calcular_produccion_ganado()
        produccion_total = produccion_cultivos + produccion_ganado
        return produccion_total

def gestionar_cultivos(produccion):
    while True:
        print("\n### Gestionar Cultivos ###")
        print("1. Agregar cultivo")
        print("2. Eliminar cultivo")
        print("3. Calcular producción total de cultivos")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del cultivo: ")
            tipo = input("Tipo del cultivo: ")
            area = float(input("Área de cultivo (en hectáreas): "))
            rendimiento = float(input("Rendimiento del cultivo (en kg/hectárea): "))
            produccion.agregar_cultivo(Cultivo(nombre, tipo, area, rendimiento))
            print("Cultivo agregado con éxito.")

        elif opcion == "2":
            nombre = input("Nombre del cultivo a eliminar: ")
            produccion.eliminar_cultivo(nombre)
            print("Cultivo eliminado con éxito.")

        elif opcion == "3":
            produccion_total = produccion.calcular_produccion_cultivos()
            print("Producción total de cultivos:", produccion_total)

        elif opcion == "4":
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def gestionar_ganado(produccion):
    while True:
        print("\n### Gestionar Ganado ###")
        print("1. Agregar animal")
        print("2. Eliminar animal")
        print("3. Calcular producción total del ganado")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            especie = input("Especie del animal: ")
            raza = input("Raza del animal: ")
            edad = int(input("Edad del animal (en meses): "))
            peso = float(input("Peso del animal (en kg): "))
            produccion.agregar_animal(Animal(especie, raza, edad, peso))
            print("Animal agregado con éxito.")

        elif opcion == "2":
            especie = input("Especie del animal a eliminar: ")
            produccion.eliminar_animal(especie)
            print("Animal eliminado con éxito.")

        elif opcion == "3":
            produccion_total = produccion.calcular_produccion_ganado()
            print("Producción total del ganado:", produccion_total)

        elif opcion == "4":
            break

        else:
            print("Opción no válida. Por favor, seleccione otra.")

if __name__ == "__main__":
    produccion = Produccion()
    granja = Granja(produccion)

    while True:
        print("\n### Menú Principal ###")
        print("1. Gestionar cultivos")
        print("2. Gestionar ganado")
        print("3. Calcular producción total de la granja")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            gestionar_cultivos(produccion)

        elif opcion == "2":
            gestionar_ganado(produccion)

        elif opcion == "3":
            produccion_total = granja.calcular_produccion_total()
            print("Produccion total de la granja:", produccion_total)

        elif opcion == "4":
            print("A Pronto")
            break

        else:
            print("Opción no válida, seleccione otra.")
