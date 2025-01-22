'''Ejercicio 1 - Punto
    Crea un programa con una clase llamada Punto que representará un punto de dos dimensiones en un plano.
    Solo contendrá dos atributos enteros llamados x e y (coordenadas). 
    En la función principal instancia 3 objetos Punto con las coordenadas (5,0), (10,10) y (-3, 7).
    Muestra por pantalla sus coordenadas (utiliza un print para cada punto). Modifica todas las coordenadas y vuelve a imprimirlas'''
    
class Punto :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
        
    def __str__(self) :
        return f'({self.x}, {self.y})'
    
punto1 = Punto(5, 0)
print(punto1)
punto1.x = 7
punto1.y = 3
print(f'Modificado{punto1}')

punto2 = Punto(10, 10)
print(punto2)
punto2.x = 2
punto2.y = 3
print(f'Modificado{punto2}')

punto3 = Punto(-3, 7)
print(punto3)
punto3.x = 1
punto3.y = 0
print(f'Modificado{punto3}')

''' Crea un programa con una clase llamada Persona que representará los datos principales de una persona:
    dni, nombre, apellidos y edad.
    En la función principal instancia dos objetos de la clase Persona.
    Luego, pide por teclado los datos  de ambas personas (guárdalos en los objetos).
    Por último, imprime dos mensajes por pantalla (uno por objeto) con un mensaje del estilo
        “Azucena Luján García con DNI … es / no es mayor de edad”.'''

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


