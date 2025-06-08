import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

st.title("📄 Acceso a Google Sheets con Streamlit")

# Obtener credenciales desde secrets
credentials_info = st.secrets["google_service_account"]
credentials = Credentials.from_service_account_info(credentials_info)

# Autorización con gspread
gc = gspread.authorize(credentials)

# Abrir hoja por nombre
sh = gc.open("nombre_de_tu_hoja")  # ⬅️ CAMBIA ESTO por el nombre real de tu hoja
worksheet = sh.sheet1

# Leer valores (primeras 10 filas y 3 columnas)
datos = worksheet.get_all_values()

st.subheader("Contenido de la hoja:")
st.write(datos)

# Formulario para escribir datos
st.subheader("Agregar fila a Google Sheets")
with st.form("formulario"):
    nombre = st.text_input("Nombre")
    email = st.text_input("Email")
    enviado = st.form_submit_button("Guardar")

    if enviado:
        worksheet.append_row([nombre, email])
        st.success("✅ Datos guardados correctamente")
