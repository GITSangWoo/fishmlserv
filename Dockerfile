#FROM datamario24/python311scikitlearn-fastapi:1.0.0
FROM dogcenta/fishmlserv:1.0.0


WORKDIR /code

COPY src/fishmlserv/main.py /code/

# 모델 서빙만 하겠다. 의존성은 위 base 이미지에서 모두 설치 했다)
RUN pip install --no-cache-dir --upgrade  git+https://github.com/GITSangWoo/fishmlserv.git@1.0.0/k

#모델 서빙을 위해 API 구동을 위한 FastAPI RUN
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
