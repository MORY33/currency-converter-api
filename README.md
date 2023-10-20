# currency-converter-api

Create and activate your virtualenv

```bash
mkdir myproject && cd myproject

python3 -m venv .venv 
source .venv/bin/activate
```

Install requirements.cfg
```bash
pip install -r requirements.cfg

python manage.py makemigrations converter
python manage.py migrate 
```

Run server with default route containing swagger docs
```bash
python manage.py runserver
```

Check if server is healthy
```bash 
 GET /health_check/
 ```

Fetch current data from yfinance
```bash
python manage.py fetch_currencies
```

Run endpoint tests
```bash 
python manage.py test converter.test_views
```
