class Mascota:
    def __init__(self, nombre, edad, energia):
        self.nombre = nombre
        self.edad = edad
        self.__energia = energia  # atributo privado

    # Getter
    def get_energia(self):
        return self.__energia

    # Setter
    def set_energia(self, nueva_energia):
        if nueva_energia >= 0:
            self.__energia = nueva_energia
        else:
            print("La energía no puede ser negativa")

    # Método 1
    def jugar(self, tiempo):
        self.__energia -= tiempo * 5
        if self.__energia < 0:
            self.__energia = 0
        return f"{self.nombre} jugó y ahora tiene {self.__energia} de energía"

    # Método 2
    def dormir(self, horas):
        self.__energia += horas * 10
        return f"{self.nombre} durmió y ahora tiene {self.__energia} de energía"

    # Método 3
    def edad_humana(self):
        return self.edad * 7


# Instanciación de objetos
mascota1 = Mascota("Firulais", 3, 80)
mascota2 = Mascota("Luna", 5, 60)

# Uso de métodos con mascota1
print("=== Mascota 1 ===")
print(mascota1.jugar(4))
print(mascota1.dormir(2))
print("Edad humana:", mascota1.edad_humana())
print("Energía actual:", mascota1.get_energia())

# Uso del setter
mascota1.set_energia(90)
print("Nueva energía:", mascota1.get_energia())

# Uso de métodos con mascota2
print("\n=== Mascota 2 ===")
print(mascota2.jugar(3))
print(mascota2.dormir(1))
print("Edad humana:", mascota2.edad_humana())
print("Energía actual:", mascota2.get_energia())

# Uso del setter
mascota2.set_energia(70)
print("Nueva energía:", mascota2.get_energia())
