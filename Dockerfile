# Author: Sakthi Santhosh
# Created on: 13/08/2023
#
# Dockerfile for Flask App
FROM python:3.11-alpine3.17 AS build

COPY ./requirements.txt /

RUN pip3 install -r /requirements.txt

FROM python:3.11-alpine3.17 AS final

WORKDIR /app/

COPY ./ ./
COPY --from=build /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/

EXPOSE 5000/tcp

ENTRYPOINT ["python3", "./runner.py"]
