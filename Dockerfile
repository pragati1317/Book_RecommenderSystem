FROM python:3.11
COPY ./app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD  gunicorn --workers=4 --bind 0.0.0.0:$PORT app:main

# // Docker First Make a Base Image and then build the Application
# gunicorn Will be required to deploy the Project 