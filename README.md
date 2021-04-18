# GYM Payment Web App

Web application to have control over gym monthly payments, users and
prices of the different gym plans using Python with Django as the backend
with HTML, CSS and Bootstrap for the frontend with some implementations
using jQuery.

## Installation
* Make sure PostgreSQL is installed, depending on your OS you may need different prerequisites.
(For example libpq-dev in Debian based OS's)
* Create the database.
* Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```
* Remember to configure you database credentials in gym/settings.py

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '*YourDBName*',
        'USER': 'YourUser',
        'PASSWORD': 'YoutPassword',
        'HOST': 'localhost', # If you are running it locally
        'PORT' : ''
    }
}

```
* Run python3 manage.py runserver and check if it runs
* If it did, it's time to migrate
  * Run python3 manage.py makemigrations
  * Then, run python3 manage.py migrate

* You will be prompted to input the price of each payment type, assign the prices you want.
```
Enter Inscription price: 10
Enter Crossfit price: 20
Enter Functional price: 15
Enter Kickboxing price: 15
Enter All access price: 25
```

And that's it! The app should be ready to go.


## Usage
* Create super user with the following command:

```
python3 manage.py createsuperuser
```
Now you will be able to log in and create payments!

Other users can also register and log in but only to see their payments.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)