![alt text](https://www.logolynx.com/images/logolynx/36/36c5ba49dd8ef0a12c11681df3d77548.jpeg)

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Flask_logo.svg/1200px-Flask_logo.svg.png)
![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/1200px-HTML5_logo_and_wordmark.svg.png)
# Data representation Project
***
## Aaron Donnelly-G00299531
***
### This is my submission to the Data representation module of the Data Analytics course in GMIT. This project is a simulation of an electronics shop that deals in secondhand electrical applicances. The table in the database holds product information and the primary key used is SerialNum (Serial number) as this is something that is unique to each item.  
***

## server.py
### This program is the flask server that was adapted from the week 10 tutoral. This will be used to host the database electronicshop. This server imports the ProductDao.py file that is used to connect to the mysql database.

## ProductDao.py
### This program is the database access object. This python program connects to the mysql database using the credientials taking from the hidden dbconfig.py file. This program contains all the functions needed to interact with the Mysql database.

## app.py
### This program is a second flask server that requires user authentications. I created this file by following a youtube tutorial and the link to the video is contained within the comments. To login into the html page the username gmit followed by the password gmit can be used. This server will then redirect the user to the index page where the CRUD operations can be carried out. 

## dbconfig.py
### This python file is hidden and contains the database configuration. This will allow the user to run servers on any machine.

## Instructions
### Begin by cloning the repository. Afer that the user can use the initdb.sql file to initialise a new database containing the products table. The user can then launch the app.py server. The user will be brought to a homepage where they can login using the username gmit and password gmit. The user will then be redirected to the index.html page where they can carry out the CRUD operations on the database.

# Thank you for taking the time to read my README.
