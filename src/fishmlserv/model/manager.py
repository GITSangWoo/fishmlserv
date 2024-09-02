import os 

def get_model_path():
    # import os ...
    # 이 함수 파일의 절대 경로를 받아온다
    f= __file__
    # 절대 경로를 이용해 model.pkl의 경로를 조합 
    dir_name=os.path.dirname(f)
    pkl_path=os.path.join(dir_name, "model.pkl")
    # 조합된 경로를 리턴 = 끝
    # 사용 fastapi main.py 에서 아래와 같이 사용 
    # from fishmlserv.model.manager import get_model_path 
    return pkl_path

#테스트 방법 
# (1) pip install . 
# (2) python 
# (3) 모듈 임포트 
# (4) 함수 호출



