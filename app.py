import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="CineScore | Cine, música y emociones",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.stApp {background:#0F1015;color:#FFFFFF;}
[data-testid="stSidebar"] {background:#181A22;border-right:1px solid #282C3A;}
h1,h2,h3,h4 {color:#5AD7ED !important;font-family:Montserrat,sans-serif;}
p,label,li {color:#C0C5D0;}
.card-box {background:#181A22;padding:24px;border-radius:12px;border:1px solid #282C3A;margin-bottom:18px;}
.card-box-accent {background:#1F222E;padding:20px;border-radius:10px;border-left:5px solid #705AED;margin-bottom:15px;}
.logo-c {color:#705AED !important;font-weight:700;}
.logo-s {color:#5AD7ED !important;font-weight:700;}
.gold-highlight {color:#EDBA5A;font-weight:bold;}
.stButton>button {background:#705AED;color:white;border-radius:8px;border:none;padding:10px 20px;font-weight:600;}
.stButton>button:hover {background:#EDBA5A;color:#0F1015;}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_database():
    data = [
        {"Película_Serie":"Interstellar","Compositor":"Hans Zimmer","Género_Cinematografico":"Ciencia Ficción / Drama",
         "Historia_del_Soundtrack":"Un viaje espacial para salvar a la humanidad donde el tiempo apremia y la inmensidad del cosmos se apodera de la escena.",
         "Emocion_Principal":"Asombro, Tensión e Inmensidad","Genero_Musical":"Orquestal y Ambiental",
         "Instrumentos_Destacados":"Órgano de tubos, cuerdas, sintetizadores analógicos",
         "Partitura":"Disponible (Análisis melódico completo)","Plataforma_Oficial":"Spotify / Apple Music / YouTube Music",
         "Link_Video":"https://youtu.be/dfe8tCcHnKY","Revision":"Publicado"},
        {"Película_Serie":"El Pianista","Compositor":"Wojciech Kilar (con obras de F. Chopin)","Género_Cinematografico":"Drama Histórico",
         "Historia_del_Soundtrack":"Un pianista judío sobrevive en Varsovia durante la Segunda Guerra Mundial. La música contrasta la belleza frente al horror.",
         "Emocion_Principal":"Nostalgia, Resiliencia y Melancolía","Genero_Musical":"Clásico / Solo Piano",
         "Instrumentos_Destacados":"Piano de cola, violonchelo, orquesta de cámara",
         "Partitura":"Disponible (Fragmento del Nocturno en do menor)","Plataforma_Oficial":"Spotify / Apple Music",
         "Link_Video":"https://youtu.be/RMDWeQHgUrA","Revision":"Publicado"},
        {"Película_Serie":"Psicosis","Compositor":"Bernard Herrmann","Género_Cinematografico":"Terror / Suspenso",
         "Historia_del_Soundtrack":"Una obra maestra del suspense donde el sonido agudo de las cuerdas marca cada sobresalto del espectador.",
         "Emocion_Principal":"Pánico, Terror e Incertidumbre","Genero_Musical":"Atonal / Vanguardia de Cuerdas",
         "Instrumentos_Destacados":"Violines agudos y sección exclusiva de cuerdas",
         "Partitura":"Disponible (Análisis de la escena de la ducha)","Plataforma_Oficial":"Spotify / Apple Music",
         "Link_Video":"https://youtu.be/vCHREyE5GzQ","Revision":"Publicado"}
    ]
    return pd.DataFrame(data)

df_movies=load_database()
if "requests" not in st.session_state:
    st.session_state.requests=[]

st.sidebar.markdown("# <span class='logo-c'>C</span>ine<span class='logo-s'>Score</span>",unsafe_allow_html=True)
st.sidebar.markdown("*Conectando el cine, la música y tus emociones*")
st.sidebar.divider()
menu=st.sidebar.radio("Selecciona una sección:",[
    "🏠 Inicio","🔍 Análisis y Videos","📊 Base de Datos",
    "🎡 Ruleta de Géneros","💬 Comunidad y Solicitudes","⚖️ Avisos Legales"
])
st.sidebar.divider()
st.sidebar.caption("CineScore · Proyecto académico")

if menu=="🏠 Inicio":
    st.title("🎬 CineScore")
    st.subheader("Descubre el propósito emocional de cada soundtrack")
    st.markdown("""<div class='card-box-accent'>
    <h3 style='margin-top:0;'>Nuestra misión principal</h3>
    <p>Ayudamos a los espectadores apasionados por el cine y cinéfilos a comprender la conexión profunda entre lo que se muestra en la pantalla y el soundtrack musical, revelando la intención emocional detrás de cada escena.</p></div>""",unsafe_allow_html=True)
    st.markdown("### ✨ Explora nuestra biblioteca")
    st.write("Analiza cómo la música transforma las escenas, crea atmósferas y conecta con las emociones del espectador.")
    st.subheader("🎥 Video destacado")
    st.video(df_movies.iloc[0]["Link_Video"])
    c1,c2,c3=st.columns(3)
    c1.metric("Obras en catálogo",len(df_movies))
    c2.metric("Géneros explorables",6)
    c3.metric("Enfoque","Emociones")
    st.info("Utiliza el menú lateral para entrar a cada sección de CineScore.")

elif menu=="🔍 Análisis y Videos":
    st.title("🔍 Análisis y reproductor de videos")
    st.write("Selecciona una obra para ver su video y conocer el contexto de su soundtrack.")
    choice=st.selectbox("Elige una obra:",df_movies["Película_Serie"])
    row=df_movies[df_movies["Película_Serie"]==choice].iloc[0]
    left,right=st.columns(2)
    with left:
        st.markdown(f"### 📽️ {row['Película_Serie']}")
        st.video(row["Link_Video"])
        st.caption(f"Plataformas: {row['Plataforma_Oficial']}")
    with right:
        st.markdown("### 🧠 Contexto y emoción")
        st.info(f"**Compositor:** {row['Compositor']}")
        st.write(f"**Género cinematográfico:** {row['Género_Cinematografico']}")
        st.write(f"**Historia:** {row['Historia_del_Soundtrack']}")
        st.markdown(f"<div class='card-box-accent'><b>Emoción principal:</b><br><span class='gold-highlight'>{row['Emocion_Principal']}</span></div>",unsafe_allow_html=True)
        st.write(f"**Instrumentos clave:** {row['Instrumentos_Destacados']}")
        st.write(f"**Partitura:** {row['Partitura']}")

elif menu=="📊 Base de Datos":
    st.title("📊 Base de datos general")
    st.write("Explora, filtra y consulta el catálogo de análisis musical.")
    search=st.text_input("🔎 Buscar película o compositor")
    filtered=df_movies.copy()
    if search:
        mask=filtered["Película_Serie"].str.contains(search,case=False,na=False) | filtered["Compositor"].str.contains(search,case=False,na=False)
        filtered=filtered[mask]
    st.dataframe(filtered,use_container_width=True,hide_index=True)
    st.caption(f"{len(filtered)} resultado(s)")

elif menu=="🎡 Ruleta de Géneros":
    st.title("🎡 Ruleta interactiva de géneros cinematográficos")
    st.write("Elige un género para descubrir su lenguaje musical y su impacto emocional.")
    genres={
      "Terror":{"emocion":"Pánico, sobresalto y tensión","recursos":"Disonancias marcadas, violines agudos estridentes, clusters de cuerdas y silencios repentinos."},
      "Drama / Tristeza":{"emocion":"Melancolía, empatía y duelo","recursos":"Cuerdas lentas en modo menor, tempos pausados y melodías solitarias de piano."},
      "Romance":{"emocion":"Intimidad, conexión y ternura","recursos":"Líneas melódicas ascendentes, arpegios fluidos de piano y cálidos instrumentos de viento madera."},
      "Acción":{"emocion":"Adrenalina y fuerza","recursos":"Percusión intensa, metales imponentes y ostinatos rítmicos acelerados."},
      "Suspenso / Thriller":{"emocion":"Expectativa e incertidumbre","recursos":"Crescendos graduales, texturas minimalistas repetitivas y zumbidos graves ambientales."},
      "Sci-Fi":{"emocion":"Asombro e inmensidad cósmica","recursos":"Sintetizadores analógicos espaciales, timbres electrónicos vanguardistas y efectos envolventes."}
    }
    genre=st.radio("Selecciona un género:",list(genres.keys()),horizontal=True)
    info=genres[genre]
    st.markdown(f"""<div class='card-box'>
    <h2>{genre}</h2><p><b>Respuesta emocional:</b> <span class='gold-highlight'>{info['emocion']}</span></p>
    <p><b>Recursos musicales:</b> {info['recursos']}</p></div>""",unsafe_allow_html=True)

elif menu=="💬 Comunidad y Solicitudes":
    st.title("💬 Comunidad CineScore")
    st.write("¿Qué película o serie te gustaría que analizáramos en una próxima actualización?")
    with st.form("form_comunidad",clear_on_submit=True):
        user=st.text_input("Tu nombre o apodo (opcional)")
        movie=st.text_input("Título de la película o serie *")
        comments=st.text_area("¿Qué te gusta de su soundtrack? (opcional)")
        sent=st.form_submit_button("Enviar solicitud")
        if sent:
            if movie.strip():
                st.session_state.requests.append({"Nombre":user or "Cinéfilo","Película":movie.strip(),"Comentario":comments})
                st.success(f"¡Gracias, {user or 'Cinéfilo'}! Tu solicitud de **{movie.strip()}** se agregó a esta sesión.")
            else:
                st.error("Por favor, escribe el título de una película o serie.")
    if st.session_state.requests:
        st.markdown("### Solicitudes registradas durante esta sesión")
        st.dataframe(pd.DataFrame(st.session_state.requests),use_container_width=True,hide_index=True)
    st.caption("Nota: las solicitudes se muestran durante esta sesión; no se almacenan permanentemente.")

elif menu=="⚖️ Avisos Legales":
    st.title("⚖️ Avisos y marco legal")
    st.markdown("""<div class='card-box'><h3>Propósito académico y educativo</h3>
    <p>CineScore es una plataforma digital desarrollada con fines pedagógicos, culturales y de análisis crítico. Los videos se reproducen mediante los servicios de sus respectivos proveedores.</p></div>
    <div class='card-box'><h3>Derechos de autor</h3>
    <p>Las marcas, nombres de obras, fragmentos musicales, videos y composiciones pertenecen a sus respectivos autores, estudios cinematográficos, productoras discográficas y titulares de derechos. CineScore no reclama propiedad sobre estos materiales.</p></div>
    <div class='card-box'><h3>Enlaces externos</h3>
    <p>Los enlaces y reproductores externos pueden estar sujetos a las condiciones, disponibilidad y políticas de las plataformas correspondientes.</p></div>""",unsafe_allow_html=True)

st.markdown("---")
st.caption("© CineScore · Proyecto académico de análisis de soundtracks")
