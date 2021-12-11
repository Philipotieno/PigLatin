# Pig Latin Transaltor

## Getting Started

#### Python 3.8.2

### Create the virtual environment

```bash

```

- `$ virtualenv -p python3 venv`

```

```

### Activate the virtual environment

```bash

```

- `$ source venv/bin/activate`

```

```

### Install dependencies

```bash

```

- `$ pip install -r requirements.txt`

```

```

### To run the app locally

```bash

```

- `$ python manage.py runserver`

```

```

### To run the app on docker

```bash

```

- Build the image
  - `$ docker-compose up --build -d`
- Test on postman
  - `http://127.0.0.1:8001/api/translate`

```

```

![Docker](http://url/to/img.png)

### To deploy the microservice on a kubernetes cluster

```bash

```

- `$ kubectl apply -f deployment.yaml`
- `minikube service translate-service`

- Test on postman
  - `http://127.0.0.1:8001/api/translate`

```

```

![Docker](http://url/to/img.png)
