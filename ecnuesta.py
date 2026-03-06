import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# ------------------------------
# Título
# ------------------------------
st.set_page_config(page_title="Dashboard de Consciencia", layout="wide")
st.title("🧠 Dashboard Clínico de Estados de Consciencia")

st.markdown(
"""
Este dashboard te muestra un análisis quirúrgico de tu nivel de consciencia según el test de 60 preguntas basado en Hawkins. 
Se detecta tu bloque dominante, posibles incoherencias internas y tu punto de palanca evolutivo.
Además, se sugieren **ejercicios semanales** para integrar los bloques y aumentar tu coherencia interna.
"""
)

# ------------------------------
# Datos de ejemplo: medias por bloque
# ------------------------------
bloques = [
    "Defecto/Carencia (B1)",
    "Miedo/Control (B2)",
    "Poder/Logro (B3)",
    "Neutralidad/Aceptación (B4)",
    "Amor/Compasión (B5)",
    "Paz/Trascendencia (B6)"
]

# Medias obtenidas del test (ejemplo proporcionado)
medias = [3.0, 3.4, 3.8, 3.6, 3.9, 3.1]

# ------------------------------
# Radar Chart
# ------------------------------
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
      r=medias,
      theta=bloques,
      fill='toself',
      name='Nivel de Consciencia',
      line=dict(color='royalblue')
))
fig.update_layout(
  polar=dict(
    radialaxis=dict(visible=True, range=[0,5])
  ),
  showlegend=False,
  title="Perfil de Consciencia por Bloques"
)

st.plotly_chart(fig, use_container_width=True)

# ------------------------------
# Tabla Resumen
# ------------------------------
st.subheader("📊 Resumen de Medias por Bloque")
df = pd.DataFrame({
    "Bloque": bloques,
    "Media": medias
})
st.table(df)

# ------------------------------
# Bloque dominante, segundo y sombra
# ------------------------------
dominante = bloques[medias.index(max(medias))]
sombra = bloques[medias.index(min(medias))]
sorted_medias = sorted(zip(medias, bloques), reverse=True)
segundo = sorted_medias[1][1]

st.subheader("🔹 Bloques Clave")
st.markdown(f"**Bloque Dominante:** {dominante}")
st.markdown(f"**Segundo Bloque:** {segundo}")
st.markdown(f"**Bloque Sombra / Vulnerabilidad:** {sombra}")

# ------------------------------
# Incoherencias Clínicas
# ------------------------------
st.subheader("⚠️ Incoherencias detectadas")
incoherencias = []

# Amor + Carencia residual
if medias[4] > 3.5 and medias[0] > 3.0:
    incoherencias.append(
        "Amor alto pero todavía hay autoexigencia y autojuicio (B1 moderado). "
        "Cuidado con sobreentrega y exigencia interna."
    )
# Poder + Amor
if medias[2] > 3.5 and medias[4] > 3.5:
    incoherencias.append(
        "Alto poder y amor: acción y compasión juntos, riesgo de sobrecarga si no se integra la paz interior."
    )
# Paz baja
if medias[5] < 3.5:
    incoherencias.append(
        "Paz interior incipiente (B6 baja): oportunidad de integrar observador y tranquilidad interna."
    )

for i, inco in enumerate(incoherencias, 1):
    st.markdown(f"{i}. {inco}")

# ------------------------------
# Punto de Palanca Evolutivo
# ------------------------------
st.subheader("🎯 Punto de Palanca Evolutivo")
punto = bloques[5]  # B6: Paz / Trascendencia
st.markdown(
    f"Para evolucionar significativamente tu consciencia, enfoca tu trabajo en **{punto}**. "
    "Esto aumentará la coherencia entre tus bloques y reducirá las incoherencias detectadas."
)

# ------------------------------
# Resumen Clínico
# ------------------------------
st.subheader("📝 Resumen Clínico Personalizado")
st.markdown(
"""
Tu perfil indica que tu **bloque de Amor / Compasión (B5)** es tu fuerza, apoyado por un alto nivel de **Poder / Logro (B3)**.
Todavía existe cierta autoexigencia (B1) y tu **Paz / Trascendencia (B6)** puede crecer más.  
**Objetivo:** integrar B6 para que tu acción, amor y aceptación sean sostenibles y coherentes.
"""
)

# ------------------------------
# Ejercicios Semanales Recomendados
# ------------------------------
st.subheader("🏋️ Ejercicios Semanales para Integración y Evolución")
st.markdown(
"""
Se sugieren **3 ejercicios semanales** que fortalecen tu punto de palanca y reducen incoherencias:
"""
)

ejercicios = {
    "Lunes – Observador y Mindfulness": (
        "Dedica 20 minutos a meditar observando tus pensamientos sin juzgarlos. "
        "El objetivo es fortalecer tu B6 (Paz / Trascendencia) y observar B1 sin reaccionar."
    ),
    "Miércoles – Gratitud y Conexión": (
        "Escribe 5 cosas por las que estás agradecido y comparte un gesto amable con alguien. "
        "Esto refuerza B5 (Amor / Compasión) y reduce autoexigencia interna."
    ),
    "Viernes – Acción Consciente": (
        "Escoge una tarea importante y complétala enfocándote en el proceso más que en el resultado. "
        "Esto integra B3 (Poder / Logro) con B6, combinando acción y paz interior."
    )
}

for dia, desc in ejercicios.items():

    st.markdown(f"**{dia}:** {desc}")
