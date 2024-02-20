FROM python:3.9

WORKDIR /app


COPY requirements.txt .


RUN pip install -r requirements.txt

COPY . .

RUN python arkonproject/manage.py makemigrations

RUN python arkonproject/manage.py migrate

CMD ["python","arkonproject/manage.py","runserver","0.0.0.0:8000"]