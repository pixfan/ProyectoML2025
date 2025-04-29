from fastapi import FastAPI
from pydantic import BaseModel, Field
import numpy as np
import joblib

# Cargar el modelo
model = joblib.load("model/Adaboost.pkl")

# Lista de variables con validaciones
class InputData(BaseModel):
    sexo: float = Field(..., ge=0, le=1)
    edad: float = Field(..., ge=0, le=120)
    concentracion_hemoglobina: float = Field(..., ge=0)
    temperatura_ambiente: float = Field(..., ge=-10, le=50)
    valor_acido_urico: float = Field(..., ge=0)
    valor_albumina: float = Field(..., ge=0)
    valor_colesterol_hdl: float = Field(..., ge=0)
    valor_colesterol_ldl: float = Field(..., ge=0)
    valor_colesterol_total: float = Field(..., ge=0)
    valor_creatina: float = Field(..., ge=0)
    resultado_glucosa: float = Field(..., ge=0)
    valor_insulina: float = Field(..., ge=0)
    valor_trigliceridos: float = Field(..., ge=0)
    resultado_glucosa_promedio: float = Field(..., ge=0)
    valor_hemoglobina_glucosilada: float = Field(..., ge=0)
    valor_ferritina: float = Field(..., ge=0)
    valor_folato: float = Field(..., ge=0)
    valor_homocisteina: float = Field(..., ge=0)
    valor_proteinac_reactiva: float = Field(..., ge=0)
    valor_transferrina: float = Field(..., ge=0)
    valor_vitamina_bdoce: float = Field(..., ge=0)
    valor_vitamina_d: float = Field(..., ge=0)
    peso: float = Field(..., gt=0)
    estatura: float = Field(..., gt=0)
    medida_cintura: float = Field(..., ge=0)
    segundamedicion_peso: float = Field(..., gt=0)
    segundamedicion_estatura: float = Field(..., gt=0)
    distancia_rodilla_talon: float = Field(..., ge=0)
    circunferencia_de_la_pantorrilla: float = Field(..., ge=0)
    segundamedicion_cintura: float = Field(..., ge=0)
    tension_arterial: float = Field(..., ge=0, le=250)
    sueno_horas: float = Field(..., ge=0, le=24)
    masa_corporal: float = Field(..., gt=0)
    actividad_total: float = Field(..., ge=0)

app = FastAPI()

@app.post("/predict/")
def predict(data: InputData):
    features = np.array([[getattr(data, field) for field in data.model_fields]])
    prediction = model.predict(features)[0]
    return {"riesgo_hipertension": int(prediction)}
