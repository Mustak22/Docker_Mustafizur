# Docker_Mustafizur

## Docker DevOps Assignment

A full-stack application demonstrating containerization of a Node.js/Express frontend and Flask backend using Docker and Docker Compose.

## Author

**Mustafizur Rahman**

## Project Architecture

    Browser
       |
       | HTTP :3000
       v
    +-----------------------+
    | Node.js + Express     |
    | Frontend              |
    | Port 3000             |
    +-----------+-----------+
                |
                | Docker Network
                | HTTP :5000
                v
    +-----------------------+
    | Flask Backend         |
    | API Server            |
    | Port 5000             |
    +-----------------------+

## Project Structure

    Docker_Mustafizur/
    ├── backend/
    │   ├── .dockerignore
    │   ├── app.py
    │   ├── Dockerfile
    │   └── requirements.txt
    ├── frontend/
    │   ├── .dockerignore
    │   ├── Dockerfile
    │   ├── package.json
    │   ├── public/
    │   │   └── index.html
    │   └── server.js
    ├── .gitignore
    ├── docker-compose.yml
    └── README.md

## Technologies Used

- Ubuntu Server 24.04
- Docker
- Docker Compose
- Node.js
- Express.js
- Python
- Flask
- Flask-CORS
- Git
- GitHub
- Docker Hub

## Backend

The Flask backend runs on port 5000.

### Backend Endpoints

**GET /**

Returns the backend status.

**POST /api/submit**

Accepts JSON data containing name, email and message and returns a JSON response.

## Frontend

The Node.js/Express frontend runs on port 3000.

The frontend provides a web form with:

- Name
- Email
- Message
- Submit button

The frontend forwards form submissions to the Flask backend through the Docker Compose network.

## Docker Images

### Backend

    mustak22/docker-mustafizur-backend:latest

### Frontend

    mustak22/docker-mustafizur-frontend:latest

## Docker Compose

Docker Compose runs both services on the custom bridge network:

    app-network

Services:

    backend
    frontend

The frontend communicates with the backend using:

    http://backend:5000

The frontend is published on:

    3000:3000

## Build and Run

Build the images:

    docker compose build

Start the application:

    docker compose up -d

Check containers:

    docker compose ps

Stop the application:

    docker compose down

## Application Testing

### Frontend Health Check

    curl http://localhost:3000/health

Expected response:

    {"status":"success","message":"Node.js frontend is running"}

### Full-Stack API Test

    curl -X POST http://localhost:3000/api/submit -H "Content-Type: application/json" -d '{"name":"Mustafizur","email":"mustafizur@example.com","message":"Testing Docker Compose"}'

Expected response:

    {"status":"success","message":"Form submitted successfully","data":{"name":"Mustafizur","email":"mustafizur@example.com","message":"Testing Docker Compose"}}

## Docker Hub

Docker Hub username:

    mustak22

Backend repository:

    https://hub.docker.com/r/mustak22/docker-mustafizur-backend

Frontend repository:

    https://hub.docker.com/r/mustak22/docker-mustafizur-frontend

## GitHub

Repository:

    https://github.com/Mustak22/Docker_Mustafizur

Git remote:

    git@github.com:Mustak22/Docker_Mustafizur.git

## Docker Image Commands

Tag backend:

    docker tag docker-mustafizur-backend:latest mustak22/docker-mustafizur-backend:latest

Tag frontend:

    docker tag docker-mustafizur-frontend:latest mustak22/docker-mustafizur-frontend:latest

Push backend:

    docker push mustak22/docker-mustafizur-backend:latest

Push frontend:

    docker push mustak22/docker-mustafizur-frontend:latest

## Git Commands

    git add .
    git commit -m "Update project documentation"
    git push

## .gitignore

The project excludes unnecessary files including:

    node_modules/
    .vscode/
    .env
    __pycache__/
    *.pyc
    .venv/
    *.log

## Docker Network

The frontend and backend communicate through the Docker Compose bridge network.

The frontend uses:

    backend:5000

instead of:

    localhost:5000

Docker's internal DNS resolves the backend service name to the Flask container.

## Verification

The following have been verified:

- Docker installation
- Docker Compose installation
- Backend image build
- Frontend image build
- Docker Compose deployment
- Frontend container
- Backend container
- Frontend health endpoint
- Frontend-to-backend API communication
- Browser form submission
- GitHub push
- Docker Hub login
- Backend Docker image push
- Frontend Docker image push

## Conclusion

This project demonstrates a containerized full-stack application using Node.js/Express, Flask, Docker, and Docker Compose.

The source code is maintained in GitHub and the Docker images are published to Docker Hub.
