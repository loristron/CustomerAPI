To run this application, please execute the following steps:

1. Have Python installed on your computer https://www.python.org/downloads/

1. In your terminal, activate the virtual environment  in this folder by typing:
	1. For Linux and Mac users:
		1. ``` $ source /bin/activate ```
	1. For Windows Users
		1. ``` $ \.Scripts\activate.ps1 ```

1. Navigate to /src/ folder

1. With the virtual environment 'test' activated, install the requirements listed at 'requirements.txt' by typing in your terminal:
	1.  ``` $ pip install -r requirements.txt  ```


1. Migrate the Database setup by typing in your terminal:
	1.  ``` $ python manage.py migrate ```

1. Add the .csv file to the database using the following command
	1. ``` $ python manage.py loadcsv --path customers.csv ```

1. Run the server by typing the following command on the terminal (make sure you're still on /src/ folder)
	1. ``` $ python manage.py runserver ```

1. Open your navigator and type the server address on the URL bar
	- the default URL to access the index page of this project on a local server is http://localhost:8000. 

1. To fill the database rows latitude and longitude:
	1. you can do it by typing in your navigator: http://localhost:8000/fill-geocode
	1. or by typing in your terminal: 
		1.  ```$ python manage.py fillgeocode ```
