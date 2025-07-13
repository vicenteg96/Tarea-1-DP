from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(df, features, target_col, output_path="random_forest.joblib"):
    # Se entrena un modelo RandomForest con los datos proporcionados.

    model = RandomForestClassifier(n_estimators=100, max_depth=10)
    model.fit(df[features], df[target_col])

    joblib.dump(model, output_path)
    return model
