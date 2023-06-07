FROM python:3.10 as python
LABEL authors="maria"

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE $PORT

CMD if [ "$DEPLOYMENT_ENV" = "local" ]; then \
        python manage.py collectstatic --noinput && gunicorn oc_lettings_site.wsgi:application --bind :$PORT; \
    else \
        python manage.py collectstatic --noinput && gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT; \
    fi
