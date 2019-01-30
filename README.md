# DjangoREST
This is a demo project Django RESTfull api with custom user

This is a demo project that you can can extend to any project you want to build.
# 1) Cloning the Project:
run this command on your command prompt to clone this project.
https://github.com/kmerakeb/DjangoREST.git

# 2) Create Virtual Environment
After cloning the project, create a virtual enviroment and activate it.

# 3) Installing Dependencies
Navigate to the folder and run: pip install -r requirement.txt

# 4) Run Migrations
Run migrations using : python manage.py makemigrations
                 Then: python manage.py migrate
                 
# 5) Create Suer user
create super user so you can loging as an admin later to add and work with some data:
on the command prompt enter: python manage.py createsuperuser
  Enter a username
  Enter an email
  enter a password
 
# 6) Running the project
Enther the following command in the prompt: python manage.py runserver

# 7) browse the api:
Head to your favorit browser enter: localhost:8000/ap1/v1/users

