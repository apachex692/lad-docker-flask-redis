# Author: Sakthi Santhosh
# Created on: 13/08/2023
#
# Dockerfile for Flask App
FROM python:3.11-slim-bookworm

WORKDIR /app/

COPY ./ ./

RUN ["pip3", "install", "-r", "./requirements.txt"]

ENTRYPOINT ["python3", "./runner.py"]
