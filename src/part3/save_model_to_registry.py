# save_model_to_registry.py
import os
from dotenv import load_dotenv
from argparse import ArgumentParser

import mlflow
import pandas as pd
from sqlalchemy import create_engine
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# 0. set mlflow environments
load_dotenv()

# 1. get data
db_connect = create_engine("postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase")
df = pd.read_sql("SELECT * FROM iris_data ORDER BY id DESC LIMIT 100", db_connect)

X = df.drop(["id", "timestamp", "target"], axis="columns")
y = df["target"]
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, random_state=2022)

# 2. model development and train
model_pipeline = Pipeline([("scaler", StandardScaler()), ("svc", SVC())])
model_pipeline.fit(X_train, y_train)

train_pred = model_pipeline.predict(X_train)
valid_pred = model_pipeline.predict(X_valid)

train_acc = accuracy_score(y_true=y_train, y_pred=train_pred)
valid_acc = accuracy_score(y_true=y_valid, y_pred=valid_pred)

print("Train Accuracy :", train_acc)
print("Valid Accuracy :", valid_acc)

# 3. save model
parser = ArgumentParser()
parser.add_argument("--model-name", dest="model_name", type=str, default="sk_model")
args = parser.parse_args()

mlflow.set_experiment("new-exp")

signature = mlflow.models.signature.infer_signature(model_input=X_train, model_output=train_pred)
input_sample = X_train.iloc[:10]

with mlflow.start_run():
    mlflow.log_metrics({"train_acc": train_acc, "valid_acc": valid_acc})
    mlflow.sklearn.log_model(
        sk_model=model_pipeline,
        name=args.model_name,
        signature=signature,
        input_example=input_sample,
    )

# 4. save data
df.to_csv("data.csv", index=False)