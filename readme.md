mlflow ui

By default, the MLflow UI will be available at http://localhost:5000

docker build -t mlflow-demo .
docker run -p 5000:5000 mlflow-demo
