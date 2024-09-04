from typing import Union
import pickle
from fastapi import FastAPI
from fishmlserv.model.manager import get_model_path

app = FastAPI()

### 모델 불러오기 
with open(get_model_path(), "rb") as f:
    fish_model = pickle.load(f)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/fish")
def fish(length: float, weight: float):
    """
    물고기의 종류 판별기

    Args:
      
length (float): 물고기 길이(cm)
weight (float): 물고기 무게(g)

    Returns:
      
dict: 물고기 종류를 담은 딕셔너리

"""
    if length > 30.0 :
        prediction = "도미"
    else :
        prediction = "빙어"
    return {
            "prediction": prediction,
            "length": length,
            "weight": weight
           }


@app.get("/fish_ml_predictor")
def fish(length:float, weight:float):
    """
    물고기의 종류 판별기
    
    Args:
        legth (float) : 물고기 길이(cm)\
        weight(float) : 물고기 무기(g)
    
    Returns:
        dict: 물고기 종류를 담은 딕셔너리
        
    """
    
    a=fish_model.predict([[length,weight]])
    
    
    if a == 1:
        prediction = "도미"
    else :
        prediction = "빙어"

    return {
                "prediction" : prediction,
                "length" : length,
                "weight": weight
            }

