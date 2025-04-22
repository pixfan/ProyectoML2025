from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

#Cargar el modelo
model = joblib.load("model/Adaboost.pkl")

#Lista de variables
class InputData(BaseModel):
    sexo: float
    edad: float
    concentracion_hemoglobina: float
    temperatura_ambiente: float
    valor_acido_urico: float
    valor_albumina: float
    valor_colesterol_hdl: float
    valor_colesterol_ldl: float
    valor_colesterol_total: float
    valor_creatina: float
    resultado_glucosa: float
    valor_insulina: float
    valor_trigliceridos: float
    resultado_glucosa_promedio: float
    valor_hemoglobina_glucosilada: float
    valor_ferritina: float
    valor_folato: float
    valor_homocisteina: float
    valor_proteinac_reactiva: float
    valor_transferrina: float
    valor_vitamina_bdoce: float
    valor_vitamina_d: float
    peso: float
    estatura: float
    medida_cintura: float
    segundamedicion_peso: float
    segundamedicion_estatura: float
    distancia_rodilla_talon: float
    circunferencia_de_la_pantorrilla: float
    segundamedicion_cintura: float
    tension_arterial: float
    sueno_horas: float
    masa_corporal: float
    actividad_total: float

app = FastAPI()

@app.post("/predict/")
def predict(data: InputData):
    features = np.array([[getattr(data, field) for field in data.fields]])
    prediction = model.predict(features)[0]
    return {"riesgo_hipertension": int(prediction)}