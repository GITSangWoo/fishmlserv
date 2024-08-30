# fishmlserv

### Deploy
![image](https://github.com/user-attachments/assets/aa0556f8-1873-4adc-af03-69b0a1a69eb4)


### Run
- dev
- http://localhost:8000/docs
```bash
# uvicorn --help
$ uvicorn src.fishmlserv.main:app --reload # 변경된 코드가 적용되는 개발용 옵션
```

- prd
```bash
$ uvicorn srci.fishmlserv.main:app --host 0.0.0.0 --port 8949 # [port default 8000]
```


