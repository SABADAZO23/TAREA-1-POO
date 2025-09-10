from Ejercicio37 import CuerpoPlanetario


if __name__ == "__main__":
    tierra = CuerpoPlanetario("Tierra", 5.972e24, 5514, 12742000, 1.496e11)
    marte = CuerpoPlanetario("Marte", 6.39e23, 3933, 6779000, 2.279e11)
    print(tierra)
    print(marte)
    print(f"Atracción gravitatoria Tierra-Marte: {tierra.atraccion_gravitatoria(marte):.2e}")