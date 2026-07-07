import streamlit as st
import pandas as pd
import plotly.express as px

# Leer datos
df = pd.read_csv("emergencias_bigdata.csv")

# Título
st.title("Dashboard de Gestión de Emergencias Urbanas")

# Indicadores
st.metric("Total Emergencias", len(df))

st.metric(
    "Tiempo Promedio de Respuesta (min)",
    round(df["TiempoRespuesta_Min"].mean(), 2)
)

st.metric(
    "Costo Operativo Promedio",
    f"S/ {round(df['CostoOperativo_PEN'].mean(), 2)}"
)

# Emergencias por distrito
st.subheader("Emergencias por Distrito")

distritos = (
    df["Distrito"]
    .value_counts()
    .reset_index()
)

distritos.columns = ["Distrito", "Cantidad"]

fig1 = px.bar(
    distritos,
    x="Distrito",
    y="Cantidad",
    color="Cantidad",
    title="Cantidad de Emergencias por Distrito"
)

st.plotly_chart(fig1, use_container_width=True)

# Tipos de emergencia
st.subheader("Distribución por Tipo de Emergencia")

fig2 = px.pie(
    df,
    names="TipoEmergencia",
    title="Tipos de Emergencia"
)

st.plotly_chart(fig2, use_container_width=True)

# Emergencias por mes
df["FechaRegistro"] = pd.to_datetime(df["FechaRegistro"])
df["Mes"] = df["FechaRegistro"].dt.month_name()

emergencias_mes = (
    df.groupby("Mes")
      .size()
      .reset_index(name="Cantidad")
)

st.subheader("Emergencias por Mes")

fig3 = px.line(
    emergencias_mes,
    x="Mes",
    y="Cantidad",
    markers=True,
    title="Cantidad de Emergencias Registradas por Mes"
)

st.plotly_chart(fig3, use_container_width=True)
