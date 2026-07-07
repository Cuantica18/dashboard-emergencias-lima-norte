import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("emergencias_bigdata.csv")

st.title("Dashboard de Gestión de Emergencias Urbanas")

st.metric("Total Emergencias", len(df))

st.metric(
    "Tiempo Promedio de Respuesta",
    round(df["TiempoRespuesta"].mean(), 2)
)

st.metric(
    "Costo Operativo Promedio",
    f"S/ {round(df['CostoOperativo'].mean(), 2)}"
)

st.subheader("Emergencias por Distrito")

fig1 = px.bar(
    df["Distrito"].value_counts().reset_index(),
    x="Distrito",
    y="count"
)

st.plotly_chart(fig1)

st.subheader("Tipos de Emergencia")

fig2 = px.pie(
    df,
    names="TipoEmergencia"
)

st.plotly_chart(fig2)

df["FechaRegistro"] = pd.to_datetime(df["FechaRegistro"])
df["Mes"] = df["FechaRegistro"].dt.month
emergencias_mes = df.groupby("Mes").size().reset_index(name="Cantidad")

st.subheader("Emergencias por Mes")

fig3 = px.line(
    emergencias_mes,
    x="Mes",
    y="Cantidad",
    markers=True
)

st.plotly_chart(fig3)
