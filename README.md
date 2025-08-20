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
