class Libro:
    def __init__(self,titulo,autor,año):
        self.titulo= titulo
        self.autor= autor
        self.año= año
    def mostrar_libros(self):
        print(f"Titulo: {self.titulo} | Autor: {self.autor} | Año de publicacion: {self.año}")
def agregar_libro():
    try:
        titulo= input("Ingrese el titulo del libro: ")
        autor= input("Ingrese el autor del libro: ")
        año_publicacion= int(input("Ingrese el año de publicacion: "))
    except ValueError:
        print("Error: el año de publicacion debe ser un numero entero.")
    except Exception as e:
        print(f"Ocurrio un error inesperado: ",e)