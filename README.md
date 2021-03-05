To run this application, please execute the following steps:

1. Have Python installed on your computer https://www.python.org/downloads/

1. In your terminal, activate the virtual environment  in this folder by typing:
	1. For Linux and Mac users:
		1. <addr> $ source /bin/activate </addr>
	1. For Windows Users
		1. <addr> $ \.Scripts\activate.ps1 </addr>

1. Navigate to /src/ folder

* With the virtual environment 'test' activated, install the requirements listed at 'requirements.txt' by typing in your terminal:
	* <addr> $ pip install -r requirements.txt </addr>


* Migrate the Database setup by typing in your terminal:
	- $ python manage.py migrate

* Add the .csv file to the database using the following command
	- $ python manage.py loadcsv --path customers.csv

6. Run the server by typing the following command on the terminal (make sure you're still on /src/ folder)
	- $ python manage.py runserver

7. Open your navigator and type the server address on the URL bar
	- the default URL to access the index page of this project on a local server is http://localhost:8000. 

8. To fill the database rows latitude and longitude:
	- you can do it by typing in your navigator: http://localhost:8000/fill-geocode
	- or by typing in your terminal: 
		- $ python manage.py fillgeocode
