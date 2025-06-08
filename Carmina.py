import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

st.title("🍸 Registro de Listas Carmina PA")

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# ✅ Ya no usamos json.loads
creds_dict = st.secrets["GOOGLE_SHEETS_CREDENTIALS"]
creds = Credentials.from_service_account_info(creds_dict, scopes=scope)

# Cliente gspread
client = gspread.authorize(creds)

# Abrir hoja de cálculo
sheet = client.open("bdcarmina").sheet1

# Inputs
nombre = st.text_input("Apellido y nombre")
dni = st.text_input("DNI")
fecha_nacimiento = st.date_input("Fecha de nacimiento")

opciones = [
    "Lista Free",
    "Cumpleaños DANIEL MENDOZA - VIERNES 1 JUN",
    "Cumpleaños FRANCO ONTIVERO - SÁBADO 2 JUN"
]
seleccion = st.selectbox("Elegí una Lista:", opciones)

if st.button("Guardar"):
    if not nombre or not dni:
        st.warning("⚠️ Por favor completa todos los campos obligatorios.")
    elif not dni.isdigit():
        st.warning("⚠️ El DNI debe contener solo números.")
    else:
        try:
            sheet.append_row([
                nombre,
                dni,
                fecha_nacimiento.strftime("%d/%m/%Y"),
                seleccion
            ])
            st.success("✅ Datos guardados correctamente.")
        except Exception as e:
            st.error(f"❌ Error al guardar los datos: {e}")
