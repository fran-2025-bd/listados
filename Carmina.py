import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

st.title("🍸 Registro de Listas Carmina PA")

# 1. Obtener credenciales desde los secrets
credentials_info = st.secrets["google_service_account"]
scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
credentials = Credentials.from_service_account_info(credentials_info, scopes=scopes)

# 2. Autorización con gspread
gc = gspread.authorize(credentials)

# 3. Abrir hoja de cálculo por nombre
sh = gc.open("bdcarmina")  # ⬅️ Cambia esto por el nombre real
worksheet = sh.worksheet("bd")  # o sh.sheet1 si no especificaste nombre de pestaña



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

