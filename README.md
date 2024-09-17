## Clone the Repository
•	Clone your project repository to your local machine:
1.	Open your terminal or command prompt.
2.	Run the command: git clone https://github.com/yourusername/flask-mongo-crud.git
3.	Navigate to the project directory by running: cd flask-mongo-crud
Install Docker and Docker Compose
•	Ensure that Docker and Docker Compose are installed on your machine. If they are not installed, download and install them from the Docker website.
## Set Up Your Project
•	Ensure your project directory contains all the necessary files:
o	app/__init__.py
o	app/config.py
o	app/models.py
o	app/routes.py
o	Dockerfile
o	docker-compose.yml
o	requirements.txt
o	README.md
## Build and Run the Docker Containers
•	Navigate to the root directory of your project where the docker-compose.yml file is located.
•	Run the following command to build and start your Docker containers:
o	docker-compose up --build
•	This command will:
o	Build the Docker image for your Flask application.
o	Start the Flask application container and the MongoDB container.
## Verify the Containers Are Running
•	You can check if the containers are running by using the following command:
o	docker-compose ps
•	This command should list both the flask-app and mongo containers.
## Access the Flask Application
•	Your Flask application will be accessible at http://localhost:5000.
•	Open this URL in your web browser to verify that the application is running.
## Test the API Endpoints Using Postman
•	You can use Postman to test the CRUD operations by creating a new HTTP request for each operation.
•	API Endpoints to Test:
1.	GET /users
	Method: GET
	URL: http://localhost:5000/users
	Description: Returns a list of all users.
2.	GET /users/{id}
	Method: GET
	URL: http://localhost:5000/users/{id} (replace {id} with an actual user ID)
	Description: Returns the user with the specified ID.

## Directory Structure
• app 
1. __init__.py
2. routes/__init__.py
3. routes/user_routes.py
4. services/__init__.py
5. services/user_service.py
6. config.py
7. models.py

• tests
1. test_user.py

• docker-compose.yml

• Dockerfile


