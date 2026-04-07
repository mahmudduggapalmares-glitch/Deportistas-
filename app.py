import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ética Deportiva: Tóxicos vs. No Tóxicos", layout="wide")

# Estilo personalizado (Fondo blanco y señalizaciones azules)
st.markdown("""
    <style>
    .main {
        background-color: #FFFFFF;
    }
    h1, h2, h3 {
        color: #0056b3;
    }
    .stAlert {
        border-left: 5px solid #0056b3;
    }
    .toxic-box {
        padding: 20px;
        border: 2px solid #ff4b4b;
        border-radius: 10px;
        background-color: #fff5f5;
    }
    .pro-box {
        padding: 20px;
        border: 2px solid #0056b3;
        border-radius: 10px;
        background-color: #f0f7ff;
    }
    </style>
    """, unsafe_allow_html=True)

# Título principal
st.title("🏃‍♂️ Comportamiento en el Deporte: Fair Play vs. Toxicidad")
st.write("Explorando la psicología y las acciones de los deportistas en todas las disciplinas.")

# --- SECCIÓN: DEFINICIONES ---
col1, col2 = st.columns(2)

with col1:
    st.header("🚫 El Deportista Tóxico")
    st.markdown("""
    <div class="toxic-box">
    <strong>Definición:</strong> Es aquel que prioriza su ego o el resultado por encima del respeto a los demás. 
    Sus acciones contaminan el ambiente del equipo, degradan al rival y cuestionan la autoridad injustamente.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("¿Qué hace un deportista tóxico?")
    st.write("* **Culpa a otros:** Nunca acepta sus errores en el campo.")
    st.write("* **Falta de respeto:** Insulta a rivales, árbitros o compañeros.")
    st.write("* **Antideportivo:** Busca ganar haciendo trampa o lesionando.")
    
with col2:
    st.header("✅ El Deportista No Tóxico")
    st.markdown("""
    <div class="pro-box">
    <strong>Definición:</strong> También llamado "Líder Positivo", es quien entiende que el deporte es competencia basada en el respeto. 
    Eleva el nivel de su equipo y acepta la derrota con dignidad.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("¿Qué hace un deportista no tóxico?")
    st.write("* **Responsabilidad:** Asume sus fallos y trabaja para mejorar.")
    st.write("* **Empatía:** Ayuda al rival a levantarse y apoya al compañero que falla.")
    st.write("* **Respeto a las reglas:** Acepta las decisiones arbitrales sin violencia.")

st.divider()

# --- SECCIÓN: TIPOS DE JUGADORES ---
st.header("🔍 Tipologías de Jugadores")

tab1, tab2 = st.tabs(["Tipos de Tóxicos", "Tipos de No Tóxicos"])

with tab1:
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image("https://img.freepik.com/vector-gratis/ilustracion-concepto-enojo_114360-3725.jpg", caption="El 'Temperamental'")
        st.write("**El Temperamental:** Pierde el control fácilmente, grita y puede llegar a la agresión física.")
    with c2:
        st.image("https://img.freepik.com/vector-gratis/ilustracion-concepto-mentira_114360-5231.jpg", caption="El 'Tramposo'")
        st.write("**El Tramposo:** Simula faltas, usa sustancias prohibidas o manipula el equipo para ganar ventaja.")
    with c3:
        st.image("https://img.freepik.com/vector-gratis/personaje-dibujos-animados-hombre-orgulloso_23-2148151525.jpg", caption="El 'Egocéntrico'")
        st.write("**El Egocéntrico:** Cree que es mejor que el equipo. No pasa el balón y desprecia el esfuerzo ajeno.")

with tab2:
    c4, c5, c6 = st.columns(3)
    with c4:
        st.image("https://img.freepik.com/vector-gratis/ilustracion-concepto-colaboracion_114360-3914.jpg", caption="El 'Mentor'")
        st.write("**El Mentor:** Enseña a los más jóvenes y mantiene la calma en momentos de alta presión.")
    with c5:
        st.image("https://img.freepik.com/vector-gratis/ilustracion-concepto-honor_114360-6421.jpg", caption="El 'Caballero'")
        st.write("**El Caballero:** Admite si cometió una falta aunque el árbitro no la haya visto.")
    with c6:
        st.image("https://img.freepik.com/vector-gratis/ilustracion-concepto-resiliencia_114360-7067.jpg", caption="El 'Resiliente'")
        st.write("**El Resiliente:** Acepta la derrota, saluda al rival y se enfoca en el próximo entrenamiento.")

# --- SECCIÓN: EJEMPLOS REALES ---
st.divider()
st.header("🏆 Ejemplos en el Deporte Real")

with st.expander("Ejemplos de Conductas Tóxicas"):
    st.write("- **Fútbol:** Insultos racistas hacia rivales o escupitajos.")
    st.write("- **Tenis:** Romper raquetas y discutir agresivamente con el juez de silla.")
    st.write("- **Ciclismo:** Casos históricos de dopaje sistemático para engañar al sistema.")

with st.expander("Ejemplos de Conductas Ejemplares"):
    st.write("- **Atletismo:** Detenerse para ayudar a un corredor lesionado a cruzar la meta.")
    st.write("- **Rugby:** El respeto absoluto al árbitro (solo el capitán habla con él).")
    st.write("- **Baloncesto:** Reconocer el talento del rival tras una final perdida.")

