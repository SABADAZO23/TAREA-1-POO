import math

class CuerpoPlanetario:
    G = 6.67430e-11  
    _id_counter = 1

    def __init__(self, nombre, masa, densidad, diametro, distancia_al_sol):
        self.id = CuerpoPlanetario._id_counter
        CuerpoPlanetario._id_counter += 1
        self.nombre = nombre
        self.masa = masa  
        self.densidad = densidad  
        self.diametro = diametro  
        self.distancia_al_sol = distancia_al_sol 

    def __str__(self):
        return (f"ID: {self.id}, Nombre: {self.nombre}, Masa: {self.masa} kg, "
                f"Densidad: {self.densidad} kg/m^3, Diámetro: {self.diametro} m, "
                f"Distancia al Sol: {self.distancia_al_sol} m")

    def atraccion_gravitatoria(self, otro):
        # Calcula la fuerza gravitatoria entre este cuerpo y otro
        distancia = abs(self.distancia_al_sol - otro.distancia_al_sol)
        if distancia == 0:
            distancia = (self.diametro + otro.diametro) / 2  
        fuerza = CuerpoPlanetario.G * self.masa * otro.masa / distancia**2
        return fuerza

tierra = CuerpoPlanetario("Tierra", 5.972e24, 5514, 12742, 1.496e11)
marte = CuerpoPlanetario("Marte", 6.417e23, 3933, 6779, 2.279e11)

print(tierra)
print(marte)
print(f"Atracción gravitatoria Tierra-Marte: {tierra.atraccion_gravitatoria(marte):.2e}")


