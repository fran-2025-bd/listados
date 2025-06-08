import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import json

# Título
st.title("🍸 Registro de Listas Carmina PA")

# Cargar credenciales desde secrets de Streamlit
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
creds_dict = json.loads(st.secrets["GOOGLE_SHEETS_CREDENTIALS"])
creds = Credentials.from_service_account_info(creds_dict, scopes=scope)

# Autenticación con gspread
client = gspread.authorize(creds)

# Abrimos la hoja de cálculo
sheet = client.open("bdcarmina").sheet1  # Cambiá sheet1 si necesitás otra pestaña

# Inputs del formulario
nombre = st.text_input("Apellido y nombre")
dni = st.text_input("DNI")
fecha_nacimiento = st.date_input("Fecha de nacimiento")

opciones = [
    "Lista Free",
    "Cumpleaños DANIEL MENDOZA - VIERNES 1 JUN",
    "Cumpleaños FRANCO ONTIVERO - SÁBADO 2 JUN"
]
seleccion = st.selectbox("Elegí una Lista:", opciones)

# Botón para guardar
if st.button("Guardar"):
    if nombre and dni:
        sheet.append_row([
            nombre,
            dni,
            fecha_nacimiento.strftime("%d/%m/%Y"),
            seleccion
        ])
        st.success("✅ Datos guardados correctamente.")
    else:
        st.warning("⚠️ Por favor completa todos los campos obligatorios.")
