import streamlit as st

# Título de la app
# Muestra el título grande en la página.
st.title("Calculadora del 16%")

# Texto de apoyo
st.write("Ingresa un número y obtén el 16% de ese valor.")

# Entrada del usuario
# Crea una caja donde el usuario mete un número.
numero = st.number_input("Escribe un número:", min_value=0.0, step=1.0)

# Botón para calcular
if st.button("Calcular"):
    resultado = numero * 0.16
    st.success(f"El 16% de {numero} es {resultado}") # Muestra el resultado en una cajita verde.