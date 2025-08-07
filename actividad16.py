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
        titulo= input("Ingrese el titulo del libro: ")
        autor= input("Ingrese el autor del libro: ")
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
        for libro in libros:
            print(f"{libro+1}. {libro.mostrar_detalles()}")
    else:
        print("No hay libros registrados.")
