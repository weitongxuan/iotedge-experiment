docker build -t observcr.azurecr.io/iotedge-test-app -f server/dockerfile server
docker push observcr.azurecr.io/iotedge-test-app


docker run --rm -p 8000:8000 observcr.azurecr.io/iotedge-test-app 