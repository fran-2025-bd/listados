import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Definimos el scope de permisos
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Ruta al archivo JSON de credenciales (asegurate que esté en la misma carpeta o pon la ruta completa)
creds = Credentials.from_service_account_file("carminalistados.json", scopes=scope)

# Autenticación y conexión con gspread
client = gspread.authorize(creds)

# Abrimos la hoja llamada 'bdcarmina'
sheet = client.open("bdcarmina").sheet1  # sheet1 abre la primera pestaña. Si tenés varias, cambiá el método.

st.title("🍸 Registro de Listas Carmina PA")

# Inputs
nombre = st.text_input("Apellido y nombre")
dni = st.text_input("DNI")
fecha_nacimiento = st.date_input("Fecha de nacimiento")
opciones = ["Lista Free", "Cumpleaños ""DANIEL MENDOZA - VIERNES 1 JUN """, "Cumpleaños ""FRANCO ONTIVERO - SABADO 2 JUN"""]
seleccion = st.selectbox("Elegí una Lista:", opciones)


if st.button("Guardar"):
    if nombre and dni:
        # Agregamos la fila con los datos
        sheet.append_row([nombre, dni, fecha_nacimiento.strftime("%d/%m/%Y"),seleccion])
        st.success("✅ Datos guardados correctamente.")
    else:
        st.warning("⚠️ Por favor completa todos los campos obligatorios.")
