FROM python:3.8
MAINTAINER Suroj Bera "surojbera@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
