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
- Docker
```bash
$ sudo docker build -t fishmlserv:0.4.0 .
$ sudo docker run -d --name fmlserv-040 -p 8877:8765 fishmlserv:0.4.0
$ sudo docker ps
CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS          PORTS                                       NAMES
7244097edb66   fishmlserv:0.7.1   "uvicorn main:app --…"   14 minutes ago   Up 14 minutes   0.0.0.0:7799->8080/tcp, :::7799->8080/tcp   fml071

# docker 컨테이너 안으로...
$ sudo docker exec -it fml071 bash

# 로그 확인
$ sudo docker logs -f <CONTAINER ID|NAMES>

# docker 컨테이너 안에서 ...
root@7244097edb66:/code# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"

# 다시 호스트OS(WSL) 로 exit
root@7244097edb66:/code# exit
```

- Fly.io
```bash
$ fly launch --no-deploy
$ flyctl launch --name mariofish
$ flyctl scale memory 256
$ flyctl deploy
```

- Ref 
* https://curlconverter.com/python
