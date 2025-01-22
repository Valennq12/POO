class Persona :
    def __init__(self, dni, nombre, apellidos, edad) :
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
    def __str__(self):
        return self.nombre+' con DNI '+self.dni+' y apellidos '+self.apellidos+' tiene '+self.edad+' años.'
    def mayor_edad(self):
        return self.edad >=18



dni_p1 = input('Dime el DNI de la persona1: ')
nombre_p1 = input('Dime el nombre de la persona1: ')
apellidos_p1 = input('Dime el apellidos de la persona1: ')
edad_p1 = input('Dime la edad de la persona1: ')
Persona1 = Persona(dni_p1, nombre_p1, apellidos_p1, edad_p1)
print(Persona1)
if Persona1.mayor_edad == True :
    print('Es mayor de edad')
else :
    print('No es mayor de edad')
    
dni_p2 = input('Dime el DNI de la persona1: ')
nombre_p2 = input('Dime el nombre de la persona1: ')
apellidos_p2 = input('Dime el apellidos de la persona1: ')
edad_p2 = input('Dime la edad de la persona1: ')
Persona2 = Persona(dni_p2, nombre_p2, apellidos_p2, edad_p2)
print(Persona2)