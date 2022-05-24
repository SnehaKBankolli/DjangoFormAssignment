## Steps for running the project through docker
Clone the repository
``docker-compose up -d``
http://127.0.0.1:port/ 

## Steps to run the project through python 

Clone the repositiry
install requirements.txt
change directory to MyProject

run `python manage.py makemigrations`

run `python manage.py migrate`

After migrations are done 
run `python manage.py runserver` to start the server

got to
http://127.0.0.1:port/
http://127.0.0.1:port/polls/
here port is 8000

## About the project
This a registration form designed using html, CSS, JavaScript and Django framework.
The user enters username and email address. The username and email are validated. After successful validation the user is registered.

SQlite database is used for development purposes.
To make the project scaleable 
1.We can migrate the database to a scalable database like PostgreSQL.
2.Since we have dockerized the application we can deploy it on K8s pods with autoscaling.

