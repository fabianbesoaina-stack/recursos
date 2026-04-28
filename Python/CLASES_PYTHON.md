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
```python
mi_personaje.atributos()
```


