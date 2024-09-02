FROM python:3.8

WORKDIR /code

#COPY . /code/
COPY  src/fishmlserv/main.py /code/


#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install git+https://github.com/GITSangWoo/fishmlserv.git@0.7/MANIFEST


CMD ["uvicorn", "src.fishmlserv.main:app", "--host", "0.0.0.0", "--port", "8080"]
