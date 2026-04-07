import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Liderazgo y Ética Deportiva", layout="wide")

# Estilo personalizado: Fondo blanco y señalizaciones azules
st.markdown("""
    <style>
    .main {
        background-color: #FFFFFF;
    }
    h1, h2, h3 {
        color: #004A99; /* Azul fuerte */
        font-family: 'Helvetica', sans-serif;
    }
    .stAlert {
        border-left: 5px solid #004A99;
    }
    .blue-line {
        height: 4px;
        background-color: #004A99;
        margin-bottom: 20px;
        border-radius: 2px;
    }
    .card-pro {
        padding: 20px;
        border: 2px solid #004A99;
        border-radius: 15px;
        background-color: #F0F8FF;
    }
    .card-toxic {
        padding: 20px;
        border: 2px solid #E63946;
        border-radius: 15px;
        background-color: #FFF5F5;
    }
    </style>
    """, unsafe_allow_html=True)

# Título Principal
st.title("🏆 Ética en el Deporte: Líderes vs. Disciplina")
st.markdown('<div class="blue-line"></div>', unsafe_allow_html=True)

# --- SECCIÓN: DEFINICIONES GENERALES ---
st.header("📌 Definiciones y Señalizaciones")
col_def1, col_def2 = st.columns(2)

with col_def1:
    st.subheader("🔵 ¿Qué es un Jugador con Buen Fairplay?")
    st.write("""
    Es aquel que cumple las reglas de forma íntegra, respeta al rival y mantiene una disciplina 
    constante tanto dentro como fuera de la cancha. 
    
    **Señales de un Líder:**
    * **Puntualidad y Esfuerzo:** Es el primero en llegar y el último en irse.
    * **Resiliencia:** No se rinde ante la adversidad.
    * **Inspiración:** Motiva a sus compañeros a ser mejores.
    """)

with col_def2:
    st.subheader("🔴 ¿Qué es la Falta de Fairplay (Toxicidad/Indisciplina)?")
    st.write("""
    Ocurre cuando el deportista, a pesar de su talento, rompe las normas de convivencia o 
    profesionalismo, priorizando distracciones o placeres inmediatos sobre su carrera.
    
    **Señales de Advertencia:**
    * **Indisciplina:** Faltar a entrenamientos o descuidar el físico.
    * **Egoísmo:** Poner los deseos personales por encima del bienestar del equipo.
    * **Ruptura de Reglas:** Involucrarse en problemas legales o conductas inapropiadas fuera del juego.
    """)

st.divider()

# --- SECCIÓN: CASOS DE ESTUDIO (CRISTIANO VS RONALDINHO) ---
st.header("⚽ Ejemplos de Vida en el Deporte")

col_cr7, col_r10 = st.columns(2)

with col_cr7:
    st.image("https://images.unsplash.com/photo-1599407630303-3f1917f892fe?q=80&w=500&auto=format&fit=crop", caption="Liderazgo y Disciplina")
    st.markdown("""
    <div class="card-pro">
    <h3>Cristiano Ronaldo: El Líder Inalcanzable</h3>
    <strong>¿Por qué es un ejemplo de Fairplay y Liderazgo?</strong><br>
    Ronaldo representa la ética de trabajo pura. Su liderazgo se basa en el ejemplo:
    <ul>
        <li><strong>Demostraciones:</strong> Ha mantenido un nivel de élite por más de 20 años gracias a una dieta estricta, descanso y entrenamiento mental.</li>
        <li><strong>Mentalidad:</strong> En momentos críticos, toma la responsabilidad del equipo y empuja a sus compañeros a no rendirse.</li>
        <li><strong>Respeto al Deporte:</strong> Trata su cuerpo como un templo y el campo de juego como un lugar sagrado.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col_r10:
    st.image("https://images.unsplash.com/photo-1574629810360-7efbbe195018?q=80&w=500&auto=format&fit=crop", caption="Talento vs. Tentación")
    st.markdown("""
    <div class="card-toxic">
    <h3>Ronaldinho: El Talento que la Noche Apagó</h3>
    <strong>¿Por qué es un ejemplo de falta de disciplina profesional?</strong><br>
    Aunque es uno de los jugadores más queridos de la historia por su magia, su carrera es un recordatorio de los riesgos:
    <ul>
        <li><strong>Actitudes fuera de la cancha:</strong> Su preferencia por las fiestas y la vida nocturna afectó su rendimiento físico a una edad temprana.</li>
        <li><strong>Ruptura de reglas:</strong> Tuvo problemas graves de disciplina en sus clubes y situaciones legales fuera del fútbol (como su detención en Paraguay).</li>
        <li><strong>Consecuencia:</strong> A pesar de ser respetado por su juego, muchos consideran que "arruinó" su potencial de ser el mejor de todos los tiempos por ceder ante las tentaciones.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- SECCIÓN: DIFERENTES TIPOS EN OTROS DEPORTES ---
st.header("🏃‍♂️ Tipos de Jugadores en el Mundo")

tab1, tab2 = st.tabs(["Líderes Positivos", "Figuras Polémicas"])

with tab1:
    st.write("**El Estratega Calmo (Tenis):** Jugadores como Rafael Nadal, que nunca rompen una raqueta y respetan cada punto del rival.")
    st.write("**El Mentor (Baloncesto):** Veteranos que enseñan a los novatos a manejar la fama y el dinero con humildad.")

with tab2:
    st.write("**El Temperamental:** Deportistas que insultan a los jueces o se pelean con la grada.")
    st.write("**El Talentoso Indisciplinado:** Aquellos que faltan a las prácticas porque confían solo en su talento natural.")

# Pie de página
st.markdown('<br><hr><center>Página creada para el análisis del comportamiento deportivo - 2026</center>', unsafe_allow_html=True)
