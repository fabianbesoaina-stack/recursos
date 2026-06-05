# Modelo de Base de Datos ppara tienda de perfumes


<img width="1322" height="1600" alt="image" src="https://github.com/user-attachments/assets/3f8de035-ec3c-4127-addc-c4c630b555f7" />

Preguntas

## ¿Qué formas normales uso y por qué?

en este proyecto se uso la primera, segunda y tercera forma normal.

-la primera forma normal se cumple por que ningun dato esta repetido, cada celda tiene un solo dato, por ejemplo, en la tabla CLIENTES, cada celda tiene un solo dato como por ejemplo nombre telefono o correo.

-la segunda forma normal se cumple por que cada tabla tiene una llave primaria y cada atributo depende de ella por ejemplo, en la tabla PEDIDOS, los datos como fecha y total dependen únicamente del id_pedido.

-la tercera forma normal se cumple por que no existen dependencias transitivas entre datos por ejemplo las marcas de los perfumes estan en una tabla a parte y no en perfumes, por ejemplo

## ¿Cuál fue la parte más compleja de resolver y por qué?

¿Cuál fue la parte más compleja de resolver y por qué?

-Esta situación genera una relación muchos a muchos (N), la cual no se recomienda manejar directamente en bases de datos relacionales. Para solucionar esto fue necesario crear una tabla intermedia llamada DETALLE_PEDIDO.

## ¿Qué tablas aún le faltarían al sistema para producción y por qué?

- se podrian agregar los datos de envion, metodos de pago, fechas de pedido etc
