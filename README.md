# RedebanTest
RedebanTest

This project was created in Windows11.

To run this test please follow the next instructions.

*  Clone the repository
*  Go inside the folder
*  Run docker compose up --build. It will create two containers. 
*  Test the endpoints with postman or other tool that you want.


Base URL (local): `http://localhost:8000`

GET    `/health`                           
POST   `/v1/parameters`                    
GET    `/v1/parameters`
GET    `/v1/parameters/{name}`
PUT    `/v1/parameters/{name}`
PATCH  `/v1/parameters/{name}`


Objeto JSON

{
  "name": "THEME",
  "value": { "bg": "dark", "accent": "blue" }
}

ARREGLO

{
  "name": "ALLOWED_IPS",
  "value": ["10.0.0.1", "10.0.0.2"]
}

STRING

{
  "name": "WELCOME_MSG",
  "value": "hola mundo"
}

BOOLEAN

{
  "name": "FEATURE_ENABLED",
  "value": true
}

NUMERO

{
  "name": "MAX_RETRIES",
  "value": 5
}

PATCH
{
  "value": 15
}


PUT
{
  "name": "MAX_RETRIES",
  "value": 10,
  "value_type": "number"
}
