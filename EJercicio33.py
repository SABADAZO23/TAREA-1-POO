import random

def mostrar_array(arr):
    print(" ".join(f"{x:.2f}" for x in arr))

def burbuja(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    izquierda = [x for x in arr if x < pivot]
    centro = [x for x in arr if x == pivot]
    derecha = [x for x in arr if x > pivot]
    return quicksort(izquierda) + centro + quicksort(derecha)

def main():
    n = int(input("Ingrese el tamaño del arreglo: "))
    arr = [random.uniform(0, 100) for _ in range(n)]
    print("Arreglo generado:")
    mostrar_array(arr)

    opcion = input("Elija el método de ordenación (1: Burbuja, 2: Quicksort): ")
    if opcion == "1":
        burbuja(arr)
        print("Arreglo ordenado con Burbuja:")
        mostrar_array(arr)
    elif opcion == "2":
        arr = quicksort(arr)
        print("Arreglo ordenado con Quicksort:")
        mostrar_array(arr)
    else:
        print("Opción inválida.")

if __name__ == "__main__":
    main()

