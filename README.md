# Zone-Occurrence-Counter
Zone Occurrence Counter

## Running application
Clone or download repo and go to source directory.

Install virtualenv for Python 2.7:
```
pip install virtualenv
```

Create your virtual environment:
```
virtualenv venv
```

Activate your virtual environment:
```
source venv/bin/activate
```

Install requirements:
```
pip install -r requirements.txt
```
Export optional flags:
``` 
export FLASK_APP=app
export FLASK_ENV=development
```

Run application (development server):
``` 
flask run --reload --port 5000
```

Head to http://127.0.0.1:5000/
