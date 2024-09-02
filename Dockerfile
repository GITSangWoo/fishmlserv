# FROM python:3.11.9-alpine3.20
FROM python:3.11
# FROM python:3.8

WORKDIR /code

#COPY . /code/
COPY src/fishmlserv/main.py /code/
#COPY requirements.txt /code/

#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r git+https://github.com/GITSangWoo/fishmlserv.git@0.7/MANIFEST


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
