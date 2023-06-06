FROM python:3.10 as python
LABEL authors="maria"

COPY . /app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r /app/requirements.txt

#EXPOSE 8000

#CMD gunicorn oc_lettings_site.wsgi --bind 0.0.0.0:$PORT

#ENTRYPOINT ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:$PORT"]

#CMD python manage.py runserver 0.0.0.0:$PORT

#ENTRYPOINT ["top", "-b"]