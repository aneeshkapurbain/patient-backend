
# Patient-backend

A microservice to handle patient crud operations


## Installation

Install patient-backend with 

Prerequites:
- Docker installed on the system
- a stable internet connection as docker will download and install several dependencies.

Get .env file from author/other stakeholder
Get data files(.sql files) which needs to be imported on postgres database

local
```bash
  docker compose up --build
```

Check fastapi app running or not by going to below url:
http://localhost:8000/
or   
0.0.0.0:8000

Go to adminer url and check postgres connection:
http://localhost:8080/adminer

Give following parameters to test connection locally:

- Database: select postgres
- Server:
- user:
- password:
- database name:

from .env file where hostname in .env file will be the Server parameter


Note:

Real time environment like dev and prod will based on specific env file based on the environment type.

Following parameter are expected in that env file
```
POSTGRES_USER=add yours
POSTGRES_PASSWORD=add yours
POSTGRES_DB_NAME=add yours
POSTGRES_PORT=add yours
POSTGRES_HOST=add yours
```

Update these add yours string with exact environment values
