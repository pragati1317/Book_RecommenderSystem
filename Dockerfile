FROM python:3.11
WORKDIR /Book_RecommenderSystem
COPY  . /Book_RecommenderSystem
RUN pip install -r requirements
EXPOSE $PORT
CMD  gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app

# // Docker First Make a Base Image and then build the Application
# gunicorn Will be required to deploy the Project 
