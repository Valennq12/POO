class Persona:
    def __init__(self,dni,nombre,apellidos,fecha = None): # Constructor sirve para inicializar los atributos de la clase
        self.dni = dni
        self.nombre = nombre
        self.fecha = fecha
        self.apellidos = apellidos
        
    def __str__(self): # Método que se ejecuta cuando se intenta convertir un objeto para poder imprimirlo
        return self.nombre + " " + self.apellidos + " " + self.dni + " " + self.fecha
    
una_persona = Persona("12345678A","Juan","García Pérez","01/01/1970")
print(una_persona)
