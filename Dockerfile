FROM python:3.10
LABEL authors="maria"

COPY . /app

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]

ENTRYPOINT ["top", "-b"]