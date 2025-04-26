import pandas as pd
from sklearn.pipeline import Pipeline

import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report

#PIPELINE Y PRE PROCESAMIENTO


df = pd.read_csv(r"data\Hipertension_Arterial_Mexico.csv")
df = df[df.masa_corporal != 1 ]
X = df.drop(columns=['FOLIO_I',"riesgo_hipertension"])
y = df["riesgo_hipertension"]


numeric_features = X.columns

# Crear un transformador para escalar las columnas numéricas
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features)
    ]
)

# Construir el pipeline con preprocesamiento y AdaBoost
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', AdaBoostClassifier(
        estimator=DecisionTreeClassifier(max_depth=2),
        random_state=333  # Fijamos la semilla para reproducibilidad
    ))
])

# Definir grid  de parámetros para GridSearchCV
parameters = {
    'classifier__n_estimators': [2, 3, 7, 8, 11, 12, 20],
    'classifier__learning_rate': [(0.97 + x / 100) for x in range(0, 5)]
}

# Dividir  en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=333
)

#  GridSearchCV con validación cruzada de 5 folds
grid_search = GridSearchCV(pipeline, param_grid=parameters, cv=5, scoring='accuracy')


#ENTRAMIENTO Y ELECCION DE MODELO


# Entrenar el modelo
grid_search.fit(X_train, y_train)

# Imprimir los mejores parámetros y la mejor puntuación

# Evaluar el mejor modelo en el conjunto de prueba
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)


with open("metrics.txt", 'w') as outfile:
    outfile.write("Training accuracy: %2.1f%%\n" % accuracy_score(y_test, y_pred)+ '\n')
    outfile.write("Mejores parámetros: " + str(grid_search.best_params_)+ '\n' )
    outfile.write("Mejor Accuracy en CV:"+ str(grid_search.best_score_)+ '\n')
    outfile.write(str(classification_report(y_test, y_pred)))




model_filename = r'.\model\Adaboost.pkl'
joblib.dump(best_model, model_filename)