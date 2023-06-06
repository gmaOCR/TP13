FROM python:3.10
LABEL authors="maria"

COPY . /app

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8000

CMD gunicorn tp13-gma.wsgi --bind 0.0.0.0:$PORT

ENTRYPOINT ["top", "-b"]