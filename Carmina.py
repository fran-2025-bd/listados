import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

st.title("🍸 Registro de Listas Carmina PA")

# Cargar credenciales desde secretos
credentials_info = st.secrets["google_service_account"]
credentials = Credentials.from_service_account_info(credentials_info)

# Autorización con gspread
gc = gspread.authorize(credentials)

# Abrir la hoja y la pestaña especifica
sh = gc.open("bdcarmina")         # Nombre de la hoja
sheet = sh.worksheet("bd")        # Nombre de la pestaña

# Opciones para el selectbox
opciones = [
    "Lista Free", 
    'Cumpleaños "DANIEL MENDOZA - VIERNES 1 JUN"',
    'Cumpleaños "FRANCO ONTIVERO - SABADO 2 JUN"'
]

# Inputs
nombre = st.text_input("Apellido y nombre")
dni = st.text_input("DNI")
fecha_nacimiento = st.date_input("Fecha de nacimiento")
seleccion = st.selectbox("Elegí una Lista:", opciones)

# Botón para guardar
if st.button("Guardar"):
    if nombre.strip() and dni.strip():
        # Agregar fila con los datos a la hoja
        sheet.append_row([
            nombre.strip(),
            dni.strip(),
            fecha_nacimiento.strftime("%d/%m/%Y"),
            seleccion
        ])
        st.success("✅ Datos guardados correctamente.")
    else:
        st.warning("⚠️ Por favor completa todos los campos obligatorios.")
