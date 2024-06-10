# Sistema_Gym-grupo2
La propuesta es diseñar un sistema para un gimnasio en el cual se puedan consultar datos de los abonados y de las actividades que efectúan. Además es posible consultar los tipos de abono y si cuentan con certificado médico al día.


Los integrantes del equipo son:


Montes Sebastián DNI 29.965.349; seba29m@gmail.com URL:https://github.com/seba29m


Robledo Tomás DNI 36.235.754; tom.robs.ok@gmail.com URL:https://github.com/tomrobsok


*Modularización de la aplicación*

En la aplicación del GYM, se van a encontrar con dos archivos: el primero (FuncionesGym), será el ingreso; en este se consultará el DNI; luego se consultará si posee el certificado médico y, por último, si esto último es afirmativo, se le dará la opción de seleccionar la actividad para entrenar.

En el segundo archivo (PruebaGym), se verán reflejados los resultados invocando el archivos de funciones modularizadas.

La modularización en este caso se refiere a dividir la funcionalidad en métodos o funciones más pequeñas y específicas, lo que hace que el código sea más legible, mantenible y reutilizable. Aquí está la explicación de las funciones:

__init__(self): Este es el método de inicialización de la clase. Actualmente no realiza ninguna operación específica, solo pasa.

saludar(self, dni): Este método toma un argumento dni (Documento Nacional de Identidad) y simplemente imprime un saludo genérico a los clientes del gimnasio.

puede_ingresar_al_gimnasio(self, tiene_certificado): Este método verifica si un cliente tiene un certificado médico para ingresar al gimnasio. Toma un argumento tiene_certificado, que se espera que sea una cadena que represente "sí" o "no". Dependiendo de la respuesta, devuelve un mensaje correspondiente indicando si el cliente puede o no puede ingresar al gimnasio.

elegir_actividad(self): Este método permite al cliente elegir una actividad del gimnasio. Presenta una lista de actividades disponibles, le pide al usuario que ingrese el número correspondiente a la actividad que desea realizar, y luego devuelve un mensaje indicando la actividad seleccionada.

