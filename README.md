### LAB - Class 31
### Project: Django REST Framework & Docker

### About

This project implements a basic Django API with CRUD methods available for JSON data. The project runs in a Docker 
container.

### Env

.env file required

### Run

docker-compose up

API Site Link:\
http://0.0.0.0:8000/

Admin Page Link:\
http://0.0.0.0:8000/admin

### Test

Test from the command line using httpie (brew install).

To get an access token and a refresh token, run: 

`http POST :8000/api/token/ username=admin password=admin
`

Next, to get entries from the database, use the access token and run: 

`http :8000/ "Authorization: Bearer <access token>"`
