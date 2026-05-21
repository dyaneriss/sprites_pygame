class Personaje:

    def __init__(self):
        self.NOMBRE = "nombre por defecto"
        self.Tipo = "tipo por defecto"

    def Cantar(self):
        print("El personaje llamado " + self.NOMBRE + " canta.")
class Druida(Personaje):

    def __init__(self, nombre, nivel):
        self.NOMBRE = nombre
        self.Tipo = "DRUIDA"
        self.NIVEL_DRUIDA = nivel

    def InventarPocion(self):
        print("El druida llamado " + self.NOMBRE + " inventa una poción.")
pygamix = Druida("Pygamix", 5)
pygamix.Cantar()
pygamix.InventarPocion()


# definicion de la clase del vehiculo 
class Vehiculo:
    # Constructor de la clase Veniculo
    def __init__(self, matricula, color, numeroPuertas):
        self.MATRICULA = matricula
        self. COLOR = color
        self. NUMERO = numeroPuertas
        self.AVANZA = False
        print ("Constucción de un vehículo : " + self. MATRICULA)

    # Metodo Avanzar
    def Avanzar(self):
        self.AVANZA = True
        print(self.MATRICULA + " avanza. ")
    # Metodo Detenerse
    def Detenerse(self):
        self. AVANZA = False
        print (self. MATRICULA + " se detiene.")
# Construcción de una primera instancia
vehiculol = Vehiculo("AR123", "rojo", 3)
# Construccion de una segunda instancia
vehiculo2 = Vehiculo("FR456", "verde", 5)
# EL priner vehiculo avanza
vehiculol.Avanzar()

# El primer vehículo se detiene
vehiculol.Detenerse()
