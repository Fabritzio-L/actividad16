class Libro:
    def __init__(self,titulo,autor,año):
        self.titulo= titulo
        self.autor= autor
        self.año= año
    def mostrar_detalles(self):
        print(f"Titulo: {self.titulo} | Autor: {self.autor} | Año de publicacion: {self.año}")
libros=[]
def agregar_libro():
    try:
        while True:
            titulo= input("Ingrese el titulo del libro: ")
            if not titulo:
                print("El titulo no puede estar vacio")
            else:
                break
        while True:
            autor= input("Ingrese el autor del libro: ")
            if not autor:
                print("El autor no puede estar vacio")
            else:
                break
        año_publicacion= int(input("Ingrese el año de publicacion: "))
        libro= Libro(titulo,autor,año_publicacion)
        libros.append(libro)
        print("Libro agregado")
    except ValueError:
        print("Error: el año de publicacion debe ser un numero entero.")
    except Exception as e:
        print(f"Ocurrio un error inesperado: ",e)
def mostrar_libros():
    if libros:
        print("\nLista de libros")
        i=1
        for libro in libros:
            print(f"{i}.",end="")
            libro.mostrar_detalles()
            i+=1
    else:
        print("No hay libros registrados")
def eliminar_libro():
    titulo_buscado= input("Ingrese el titulo del libro a eliminar: ")
    libro_encontrado = False
    for libro in libros:
        if libro.titulo.lower()== titulo_buscado.lower():
            libros.remove(libro)
            print("Libro eliminado")
            libro_encontrado=True
            break
        else:
            print("Libro no encontrado")
while True:
    print("-----MENU-----")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Eliminar libro")
    print("4. Salir")
    opcion= input("Ingrese una de las opciones: ")
    match opcion:
        case "1":
            agregar_libro()
        case "2":
            mostrar_libros()
        case "3":
            eliminar_libro()
        case "4":
            print("Saliendo del programa...")
            break
        case _:
            print("Ingrese una opcion valida")