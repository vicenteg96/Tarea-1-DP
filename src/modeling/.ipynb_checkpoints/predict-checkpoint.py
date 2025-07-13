import joblib
from sklearn.metrics import f1_score

def predict_and_evaluate(df, features, target_col, model_path="random_forest.joblib"):
    #Se carga un modelo entrenado, y se realizan predicciones sobre un conjunto especifico de datos. Por ultimo se calcula la metrica F1 score.
    model = joblib.load(model_path)
    preds = model.predict_proba(df[features])
    preds_labels = [p[1] for p in preds.round()]
    f1 = f1_score(df[target_col], preds_labels)
    return f1, preds_labels