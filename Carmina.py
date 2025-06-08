import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

st.title("🍸 Registro de Listas Carmina PA")

# Autenticación con Google
credentials_info = st.secrets["google_service_account"]
scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
credentials = Credentials.from_service_account_info(credentials_info, scopes=scopes)
gc = gspread.authorize(credentials)

# Abrir hoja de cálculo
sh = gc.open("bdcarmina")
worksheet = sh.worksheet("BD")  # Aquí se define correctamente

# Inputs
nombre = st.text_input("Apellido y nombre")
dni = st.text_input("DNI")
fecha_nacimiento = st.text_input("Fecha de nacimiento")

opciones = [
    "Lista Free",
    "Cumpleaños DANIEL MENDOZA - VIERNES 1 JUN",
    "Cumpleaños FRANCO ONTIVERO - SABADO 2 JUN"
]
seleccion = st.selectbox("Elegí una Lista:", opciones)

if st.button("Guardar"):
    if nombre.strip() and dni.strip():
        worksheet.append_row([nombre, dni, fecha_nacimiento.strftime("%d/%m/%Y"), seleccion])
        st.success("✅ Datos guardados correctamente.")
    else:
        st.warning("⚠️ Por favor completá todos los campos obligatorios.")
