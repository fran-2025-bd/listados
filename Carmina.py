import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

st.title("📄 Acceso a Google Sheets con Streamlit")

# 1. Obtener credenciales desde los secrets
credentials_info = st.secrets["google_service_account"]
scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
credentials = Credentials.from_service_account_info(credentials_info, scopes=scopes)

# 2. Autorización con gspread
gc = gspread.authorize(credentials)

# 3. Abrir hoja de cálculo por nombre
sh = gc.open("BD")  # ⬅️ Cambia esto por el nombre real
worksheet = sh.sheet1

# 4. Leer todos los valores
datos = worksheet.get_all_values()

st.subheader("Contenido de la hoja:")
st.write(datos)

# 5. Formulario para escribir nuevos datos
st.subheader("Agregar fila a Google Sheets")
with st.form("formulario"):
    nombre = st.text_input("Nombre")
    email = st.text_input("Email")
    enviado = st.form_submit_button("Guardar")

    if enviado:
        if nombre.strip() == "" or email.strip() == "":
            st.error("❌ Por favor completá todos los campos.")
        else:
            worksheet.append_row([nombre, email])
            st.success("✅ Datos guardados correctamente")
