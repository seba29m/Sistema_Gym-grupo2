class Gimnasio:
    def __init__(self):
        pass
    
    def saludar(self, dni):
        print("¡Hola! A entrenar!")

    def puede_ingresar_al_gimnasio(self, tiene_certificado):
        if tiene_certificado.lower() == 'sí':
            return "Elegir Actividad."
        elif tiene_certificado.lower() == 'no':
            return "No puede ingresar al gimnasio. Debe traer un certificado médico."
        else:
            return "Respuesta no válida. Por favor, responda 'sí' o 'no'."

    def elegir_actividad(self):
        actividades = ["Yoga", "Musculación", "Zumba", "Boxeo"]
        print("Elija una actividad:")
        for i, actividad in enumerate(actividades, start=1):
            print(f"{i}. {actividad}")
        
        seleccion = input("Ingrese el número de la actividad que desea realizar: ")
        
        try:
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(actividades):
                actividad_elegida = actividades[seleccion - 1]
                return f"Ha elegido {actividad_elegida}. ¡A romperla, no olvides hidratarte!"
            else:
                return "Selección no válida. Debe ingresar un número correspondiente a una actividad."
        except ValueError:
            return "Entrada no válida. Por favor, ingrese un número."

# Uso de la clase Gimnasio
gimnasio = Gimnasio()

dni = input("Ingrese su DNI: ")
gimnasio.saludar(dni)

respuesta = input("¿Tiene certificado médico? (sí/no): ")
mensaje = gimnasio.puede_ingresar_al_gimnasio(respuesta)
print(mensaje)

mensaje_actividad = gimnasio.elegir_actividad()
print(mensaje_actividad)

