#class Usuario:
 #   nombre = "Enzo"
  #  apellido = "Quiroz"
#usuario = Usuario()
#print (usuario.nombre, usuario.apellidclass Animal:

# Definición de la clase padre (Superclase)
class Animal:
    def __init__(self, nombre, onomatopeya):
        # Se guardan los atributos básicos al crear el objeto
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        # Accede a 'self.tipo' (definido en la subclase) y a sus propios atributos
        print("Hola, soy un", self.tipo, "y hago un", self.onomatopeya)

# Subclase que hereda de Animal
class Gato(Animal):
    tipo = 'gato' # Atributo de clase específico para Gato

# Subclase que hereda de Animal
class Perro(Animal):
    tipo = 'perro' # Atributo de clase específico para Perro

# Crear una instancia de Gato
gato = Gato("Michi", "Miau")
gato.saludo()

# Crear una instancia de Perro
perro = Perro("Firulais", "Guau")
perro.saludo()

# Crear una instancia de Vaca
vaca = Vaca("Marta", "muu")
vaca.saludo()


