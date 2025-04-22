import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Cargar el modelo entrenado
model = joblib.load("model/Adaboost.pkl")

st.title("🫀 Predicción de Riesgo de Hipertensión Arterial")

def user_input():
    sexo = st.selectbox("Sexo", ["Femenino", "Masculino"])
    edad = st.number_input("Edad", 0.0, 120.0)
    concentracion_hemoglobina = st.number_input("Concentración de Hemoglobina")
    temperatura_ambiente = st.number_input("Temperatura Ambiente")
    valor_acido_urico = st.number_input("Ácido Úrico")
    valor_albumina = st.number_input("Albúmina")
    valor_colesterol_hdl = st.number_input("Colesterol HDL")
    valor_colesterol_ldl = st.number_input("Colesterol LDL")
    valor_colesterol_total = st.number_input("Colesterol Total")
    valor_creatina = st.number_input("Creatinina")
    resultado_glucosa = st.number_input("Resultado Glucosa")
    valor_insulina = st.number_input("Insulina")
    valor_trigliceridos = st.number_input("Triglicéridos")
    resultado_glucosa_promedio = st.number_input("Glucosa Promedio")
    valor_hemoglobina_glucosilada = st.number_input("Hemoglobina Glucosilada")
    valor_ferritina = st.number_input("Ferritina")
    valor_folato = st.number_input("Folato")
    valor_homocisteina = st.number_input("Homocisteína")
    valor_proteinac_reactiva = st.number_input("Proteína C Reactiva")
    valor_transferrina = st.number_input("Transferrina")
    valor_vitamina_bdoce = st.number_input("Vitamina B12")
    valor_vitamina_d = st.number_input("Vitamina D")
    peso = st.number_input("Peso (kg)")
    estatura = st.number_input("Estatura (cm)")
    medida_cintura = st.number_input("Medida Cintura (cm)")
    segundamedicion_peso = st.number_input("2da Medición Peso")
    segundamedicion_estatura = st.number_input("2da Medición Estatura")
    distancia_rodilla_talon = st.number_input("Distancia Rodilla-Talón")
    circunferencia_de_la_pantorrilla = st.number_input("Circunferencia Pantorrilla")
    segundamedicion_cintura = st.number_input("2da Medición Cintura")
    tension_arterial = st.number_input("Tensión Arterial")
    sueno_horas = st.number_input("Horas de Sueño")
    masa_corporal = st.number_input("Masa Corporal")
    actividad_total = st.number_input("Actividad Total")

    return [[1 if sexo == "Masculino" else 0, edad, concentracion_hemoglobina,
             temperatura_ambiente, valor_acido_urico, valor_albumina, valor_colesterol_hdl,
             valor_colesterol_ldl, valor_colesterol_total, valor_creatina, resultado_glucosa,
             valor_insulina, valor_trigliceridos, resultado_glucosa_promedio,
             valor_hemoglobina_glucosilada, valor_ferritina, valor_folato, valor_homocisteina,
             valor_proteinac_reactiva, valor_transferrina, valor_vitamina_bdoce,
             valor_vitamina_d, peso, estatura, medida_cintura, segundamedicion_peso,
             segundamedicion_estatura, distancia_rodilla_talon,
             circunferencia_de_la_pantorrilla, segundamedicion_cintura,
             tension_arterial, sueno_horas, masa_corporal, actividad_total]]

# Obtener valores del usuario
valores = user_input()

# Crear DataFrame con los nombres correctos de las columnas
columnas = ['sexo', 'edad', 'concentracion_hemoglobina', 'temperatura_ambiente',
            'valor_acido_urico', 'valor_albumina', 'valor_colesterol_hdl',
            'valor_colesterol_ldl', 'valor_colesterol_total', 'valor_creatina',
            'resultado_glucosa', 'valor_insulina', 'valor_trigliceridos',
            'resultado_glucosa_promedio', 'valor_hemoglobina_glucosilada',
            'valor_ferritina', 'valor_folato', 'valor_homocisteina',
            'valor_proteinac_reactiva', 'valor_transferrina', 'valor_vitamina_bdoce',
            'valor_vitamina_d', 'peso', 'estatura', 'medida_cintura',
            'segundamedicion_peso', 'segundamedicion_estatura',
            'distancia_rodilla_talon', 'circunferencia_de_la_pantorrilla',
            'segundamedicion_cintura', 'tension_arterial', 'sueno_horas',
            'masa_corporal', 'actividad_total']

df_input = pd.DataFrame(valores, columns=columnas)

# Botón para hacer predicción
if st.button("Predecir"):
    pred = model.predict(df_input)[0]
    if pred == 1:
        st.error("⚠️ Riesgo alto de hipertensión arterial.")
    else:
        st.success("✅ No hay riesgo de hipertensión detectado.")