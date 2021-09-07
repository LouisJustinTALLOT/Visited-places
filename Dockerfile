# Python image
FROM python:3.8-slim-buster
# Allow to print directly to the terminal
ENV PYTHONUNBUFFERED 1
# Allow to apt-get by accepting the default prompts
ARG DEBIAN_FRONTEND=noninteractive

RUN mkdir /code
WORKDIR /code

# Python modules
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Debian binaries
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    # GDAL
    gdal-bin \
    # Spatialite
    libsqlite3-mod-spatialite

COPY . /code/