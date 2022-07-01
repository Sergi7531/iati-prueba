# Technical test for IATI Seguros:
This test was entirely made by Sergio Domínguez and its main goal is to emulate a small shopping application backend.

## Getting started:

Assuming we are in a Linux environment, we install the dependencies:

    sudo apt install python3-pip
    pip install django
    
Now, we need to make sure we have the right database manager.
<br/>
We can ensure this by running the following command:
    
    sudo apt install mysql-server

Setting up the database will be easy:

    mysql -u root -p

    CREATE DATABASE catalog;

    exit

## Setup local environment:

Migrate the models to the MySQL database:

    python3 manage.py makemigrations
    python3 manage.py migrate

And load the products from the fixture:

    python3 manage.py loaddata products

After this, we can run the server and start the tests:

    python3 manage.py runserver

##  
