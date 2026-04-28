## creacion del constructor

la creacion del constructor es el principio de nuestro personaje y la base para crear el mismo y es a lo que se agregara los atributos de nuestro personaje 

```python
class personaje:
  pass

mi_personaje = personaje()
print(mi_personaje)
```     
## ¿Que es self?

es un argumento que se refiere a "el mismo" como lo significa el ingles, este nos permite por medio del punto (.) acceder a los atributos y metodos de nuestro personaje 

        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

## ¿Que es def?

"def" se utiliza para definir o crear una funcion, permite crear bloques de codigo para luego poder ser reutilizados
```python
 def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
```
## ¿como acceder a los atributos de un personaje?

para acceder a los atributos del personaje se debera colocar la variable asociada a nuestro personaje con el comando "." y luego nuestra variable de atributos
```
mi_personaje.atributos()
```



# Encapsulacion

## ¿cómo se encapsula código en python?
para encapsular en python debemos colocar dos guiones bajos (__) antes de nuestro atributo, esto nos permitira que no se pueda modificar nuestro atrivito de forma externa 


## ¿para que se usan los métodos get y set en el código?

estos metodos son para modificar o acceder los atributos individualmente de una forma controlada

## ¿se puede acceder a los método o atributos una vez encapsulados?

si se puede modificar los atributos una vez encapsulados, se encapsula para protegerlos de una accesibilidad muy directa pero podemos acceder a ellos mediante los metodos getters y setters, esto nos permite mantener seguros los atributos de modificaciones accidentales fuera de la clase.




