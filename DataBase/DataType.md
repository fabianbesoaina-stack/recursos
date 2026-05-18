## ¿Cuál es la característica principal del tipo de dato CHAR en cuanto a su almacenamiento y qué sucede si el contenido ingresado es menor a la longitud definida?

R: la principal caracteristica de char es que siempre se usara el espacio definido por el usuario, osea, si le indicamos que usaremos 10 espacions, se aplicara esta instruccion incluso si nuestro dato ocupase menos de 10 espacios por lo que seria ineficiente al moento de almacenar caracteres de distinta longitud, ya que muchos quedarian simplemente en blanco y ocuparian el espacio.
Este tipo de dato sirve cunado queremos almacenar datos con longitudes fijas, por ejemplo patentes de autos

## ¿En qué se diferencia principalmente VARCHAR de CHAR y por qué se considera más eficiente para almacenar datos como nombres o direcciones?


## ¿Para qué tipo de escenarios está diseñado el tipo de dato TEXT y cuál es su ventaja respecto a la limitación de caracteres en comparación con los otros tipos vistos? 


## Si tuvieras que diseñar una base de datos para almacenar matrículas vehiculares que siempre tienen un formato estándar de 7 caracteres, ¿qué tipo de dato elegirías y por qué?


## El video menciona que el rendimiento y la optimización son clave. ¿Qué riesgo existe al definir una longitud de caracteres excesivamente grande en un campo VARCHAR si los datos reales son pequeños?
