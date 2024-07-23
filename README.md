Crear imagen

```sh
docker build -t fund_manager-back .
```

Cargar imagen a ECR
```sh
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 891377328192.dkr.ecr.us-east-2.amazonaws.com
docker tag fund_manager-back 891377328192.dkr.ecr.us-east-2.amazonaws.com/fund_manager
docker push 891377328192.dkr.ecr.us-east-2.amazonaws.com/fund_manager
```

Descargar imagen de ECR
```sh
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 891377328192.dkr.ecr.us-east-2.amazonaws.com
docker pull 891377328192.dkr.ecr.us-east-2.amazonaws.com/fund_manager
```

Correr imagen
```sh
docker run -d -p 8000:8000 891377328192.dkr.ecr.us-east-2.amazonaws.com/fund_manager
```

