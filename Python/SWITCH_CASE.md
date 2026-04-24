# Switch Case en Python

Python no tiene switch como otros lenguajes, pero se puede simular.

## Ejemplo

```python
def opcion(numero):
    if numero == 1:
        return "Opción 1"
    elif numero == 2:
        return "Opción 2"
    else:
        return "Otra opción"

print(opcion(1))
