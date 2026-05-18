## ¿Cuál es la característica principal del tipo de dato CHAR en cuanto a su almacenamiento y qué sucede si el contenido ingresado es menor a la longitud definida?

R: la principal caracteristica de char es que siempre se usara el espacio definido por el usuario, osea, si le indicamos que usaremos 10 espacions, se aplicara esta instruccion incluso si nuestro dato ocupase menos de 10 espacios por lo que seria ineficiente al moento de almacenar caracteres de distinta longitud, ya que muchos quedarian simplemente en blanco y ocuparian el espacio.
Este tipo de dato sirve cunado queremos almacenar datos con longitudes fijas, por ejemplo patentes de autos

## ¿En qué se diferencia principalmente VARCHAR de CHAR y por qué se considera más eficiente para almacenar datos como nombres o direcciones?

la principal diferencia es que varchat si elimina los espacion sobrantes haciendo nuestro proyecto mas eficiente, es mas eficiente con datos en los cuales no hay una cantidad de espacio fija ya que podemos determinar un limite de espacios pero si agragamos un dato de menor longitud este ocupara solo los espacion necesarios sin quitar eficiencia en el proyecto 

## ¿Para qué tipo de escenarios está diseñado el tipo de dato TEXT y cuál es su ventaja respecto a la limitación de caracteres en comparación con los otros tipos vistos? 

el tipo de dato text es para almacenar grandes grupos de textos, por ejemplo en una tienda de supermercado donde necesitan tener una extensa descripcion del producto, la ventaja es que no tiene limitacion de caracteres como los otros datos por lo que se puede almacenar mucha informacion sin problemas y de forma comoda

## Si tuvieras que diseñar una base de datos para almacenar matrículas vehiculares que siempre tienen un formato estándar de 7 caracteres, ¿qué tipo de dato elegirías y por qué?

char ya que este dato limita la cantidad de caracteres al gusto del usuario por lo que si se que cada matricula usara 7 caracteres, se puede definir y no se perdera ningun tipo de eficiencia en el proyecto

## El video menciona que el rendimiento y la optimización son clave. ¿Qué riesgo existe al definir una longitud de caracteres excesivamente grande en un campo VARCHAR si los datos reales son pequeños?

aunque varchat use los datos necesarios, determinar una cantidad exesivamente grande puede afectar al rendimiento si los datos que necesitamos no son realmente tan grandes
