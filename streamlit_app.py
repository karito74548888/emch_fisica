import streamlit as st
import random

# Función para generar un ejercicio de cinemática
def generar_ejercicio():
    tipo = random.choice(["velocidad", "distancia", "tiempo"])
    
    if tipo == "velocidad":
        distancia = random.randint(50, 500)  # metros
        tiempo = random.randint(5, 60)       # segundos
        correcto = distancia / tiempo
        texto = f"Un objeto recorre {distancia} metros en {tiempo} segundos. ¿Cuál es la velocidad?"
        return texto, correcto
    
    elif tipo == "distancia":
        velocidad = random.randint(5, 50)    # metros por segundo
        tiempo = random.randint(5, 60)       # segundos
        correcto = velocidad * tiempo
        texto = f"Un objeto se mueve a una velocidad de {velocidad} m/s durante {tiempo} segundos. ¿Cuál es la distancia recorrida?"
        return texto, correcto
    
    elif tipo == "tiempo":
        distancia = random.randint(50, 500)  # metros
        velocidad = random.randint(5, 50)    # metros por segundo
        correcto = distancia / velocidad
        texto = f"Un objeto recorre {distancia} metros a una velocidad de {velocidad} m/s. ¿Cuánto tiempo tarda en recorrer la distancia?"
        return texto, correcto

# Título de la aplicación
st.title("Generador de Ejercicios de Cinemática")

# Generar un nuevo ejercicio al cargar la página
texto, respuesta_correcta = generar_ejercicio()
st.write(texto)

# Entrada para la respuesta del usuario
respuesta_usuario = st.number_input("Introduce tu respuesta:", step=0.01)

# Botón para verificar la respuesta
if st.button("Verificar respuesta"):
    if abs(respuesta_usuario - respuesta_correcta) < 0.01:  # Permitir un pequeño margen de error
        st.success("¡Correcto! 😃")
    else:
        st.error(f"Incorrecto. La respuesta correcta es {respuesta_correcta:.2f}.")
