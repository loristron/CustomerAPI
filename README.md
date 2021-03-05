To run this application, please execute the following steps:

Have Python installed on your computer https://www.python.org/downloads/

In your terminal, activate the virtual environment  in this folder by typing:
	- For Linux and Mac users:
		- $ source /bin/activate
	- For Windows Users
		- $ \.Scripts\activate.ps1 

Once the environment  'test' is properly activated, install the requirements listed at 'requirements.txt' by typing in your terminal:
	- $ pip install -r requirements.txt

Navigate to /src/ folder

Migrate the Database setup by typing in your terminal:
	- $ python manage.py migrate

Add the .csv file to the database using the following command
	- $ python manage.py loadcsv --path customers.csv

Run the server by typing the following command on the terminal (make sure you're still on /src/ folder)
	- $ python manage.py runserver

Open your navigator and type the server address on the URL bar
	- the default URL to access the index page of this project on a local server is http://localhost:8000. 

To fill the database rows latitude and longitude:
	- you can do it by typing in your navigator: http://localhost:8000/fill-geocode
	- or by typing in your terminal: 
		- $ python manage.py fillgeocode
