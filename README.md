Film Industry - FastAPI Project Structure
===============

`Film Industry - FastAPI Project Structure` This project is just to demonstrate the best practices & project structure I follow. Feel free to add suggestions and best practices.

Prerequisite
----------
It is dockerized project. So you need docker installed in your system.

Installing
----------
Download the `project` file [here](/target/github-download-1.0-SNAPSHOT-jar-with-dependencies.jar). 
It includes all dependencies. You must have the to build and the run the project.

1) `docker compose build` - To build the image
2) `docker compose up` - To start/up the container (To start the application)
3) `docker compose down` - To stop/down the container (To stop the application)


Database to connect to your local machine:

```
When you run a docker container, it behaves a lot like a separate machine. When you try to connect to 127.0.0.1 you're trying to connect to the container itself. 
Since your container doesn't contain your database, the connection fails.
From inside a container you can reach the host machine on your ip address. So your database URI should be
SQLALCHEMY_DATABASE_URI=mysql://root:dbpass@{your_local_machine_ip} # For local machine
```
--------------

Images
----------

<img width="922" alt="FastAPI - Swagger" src="https://user-images.githubusercontent.com/72437756/180607315-35e88d54-d372-48b3-bb52-3e299a6ccea2.png">

<img width="1112" alt="FastAPI - redoc" src="https://user-images.githubusercontent.com/72437756/180607326-b51109ef-e239-4830-963c-b2943946d797.png">



