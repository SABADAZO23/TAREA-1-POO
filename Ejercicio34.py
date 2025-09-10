class Vehiculo:
    def __init__(self, num_pasajeros, tripulacion, num_ruedas, fecha_matriculacion, medio):
        self.num_pasajeros = num_pasajeros
        self.tripulacion = tripulacion
        self.num_ruedas = num_ruedas
        self.fecha_matriculacion = fecha_matriculacion
        self.medio = medio

    def __str__(self):
        return (f"Pasajeros: {self.num_pasajeros}, "
                f"Tripulación: {'Sí' if self.tripulacion else 'No'}, "
                f"Ruedas: {self.num_ruedas}, "
                f"Fecha matriculación: {self.fecha_matriculacion}, "
                f"Medio: {self.medio}")

def leer_vehiculo():
    num_pasajeros = int(input("Número de pasajeros: "))
    tripulacion = input("¿Tiene tripulación? (s/n): ").strip().lower() == 's'
    num_ruedas = int(input("Número de ruedas: "))
    fecha_matriculacion = input("Fecha de matriculación (dd/mm/aaaa): ")
    medio = input("Medio de desplazamiento: ")
    return Vehiculo(num_pasajeros, tripulacion, num_ruedas, fecha_matriculacion, medio)

def main():
    vehiculos = []
    print("Ingrese los datos de 10 vehículos:")
    for i in range(10):
        print(f"\nVehículo {i+1}:")
        vehiculo = leer_vehiculo()
        vehiculos.append(vehiculo)

    print("\nListado de vehículos:")
    for i, v in enumerate(vehiculos, 1):
        print(f"{i}. {v}")

if __name__ == "__main__":
    main()