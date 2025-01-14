import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Start an MLflow run
with mlflow.start_run():
    # Set hyperparameters
    n_estimators = 200
    max_depth = 3

    # Train a model
    clf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
    clf.fit(X_train, y_train)

    # Make predictions
    predictions = clf.predict(X_test)

    # Log model, parameters, and metrics
    mlflow.sklearn.log_model(clf, "model")
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_metric("accuracy", accuracy_score(y_test, predictions))

print("Training complete. Metrics logged to MLflow.")
