#Dockerfile

#pull official python image
FROM python:3.9.4-slim as requirements-stage

#set tmp dir for dependecies
WORKDIR /tmp

#install poetry our package manager
RUN pip install poetry

#copy existing .toml and .lock files to /tmp
COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.9.4-slim

WORKDIR /app
# set env variables
#prevenets python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy project
COPY . .


