# miax_lambda_example


docker build -t echo_lambda -f dockerfiles/echo_lambda/Dockerfile .

Para probar:
docker run -p 9000:8080 echo_lambda

curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}' 

Subimos a ECR:

docker tag echo_lambda:latest 076977333390.dkr.ecr.eu-west-1.amazonaws.com/echo_lambda:latest
docker push 076977333390.dkr.ecr.eu-west-1.amazonaws.com/echo_lambda:latest

---
Para el API:

docker build -t suma_lambda -f dockerfiles/suma_lambda/Dockerfile .
docker tag suma_lambda:latest 076977333390.dkr.ecr.eu-west-1.amazonaws.com/suma_lambda:latest
docker push 076977333390.dkr.ecr.eu-west-1.amazonaws.com/suma_lambda:latest