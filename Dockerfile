FROM python:3.10.11-slim-bullseye

RUN apt update -y
RUN apt install build-essential -y
RUN apt-get install manpages-dev -y


# set a directory for the app
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code


# tell the port number the container should expose
EXPOSE 5001

# run the command
# CMD ["uvicorn", "app:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "5003"]
CMD [ "python", "app.py" ]

