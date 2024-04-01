FROM python:3.11 
COPY . /var/www
WORKDIR /var/www
RUN pip install -r requirements.txt
EXPOSE 8000  
CMD python manage.py migrate && python manage.py loaddata default.json && python manage.py runserver 0.0.0.0:8000