FROM python:3.10 as python
LABEL authors="maria"

COPY . /app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE $PORT

CMD cd app

CMD python manage.py collectstatic && gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
