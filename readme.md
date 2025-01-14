Test the deployed docker
docker pull ringlearn/mlops_demo:latest
docker run -it -p 5000:5000 ringlearn/mlops_demo:latest
mlflow ui --host 0.0.0.0 --port 5000
By default, the MLflow UI will be available at http://localhost:5000
