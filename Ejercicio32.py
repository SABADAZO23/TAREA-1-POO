#¿Es posible ejecutar un programa en java que contenga varias clases con métodos
#main? En caso positivo, ¿cómo se determina el punto de entrada a un programa?

if __name__ == "__main__":
    main()
''' en Python puedes tener varios archivos (o clases) con funciones llamadas main, pero no existe un punto de entrada fijo como en Java. Solo el archivo que ejecutas como principal ejecutará su bloque if __name__ == "__main__":.
Los demás archivos pueden tener su propia función main, pero no se ejecutarán automáticamente.'''