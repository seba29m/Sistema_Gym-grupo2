import FuncionesGym

dni = input("Ingrese su DNI: ")
gimnasio.saludar(dni)

respuesta = input("¿Tiene certificado médico? (sí/no): ")
mensaje = gimnasio.puede_ingresar_al_gimnasio(respuesta)
print(mensaje)

mensaje_actividad = gimnasio.elegir_actividad()
print(mensaje_actividad)