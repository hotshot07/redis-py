kubectl apply -f redis-config.yaml
kubectl apply -f redis-combined.yaml
sleep 5;
kubectl apply -f flask-combined.yaml
sleep 5;
minikube service flask-service