import pickle
import typer
from fishmlserv.model.manager import get_model_path


def main(l: float = typer.Option(..., "--length", "-l"), w: float = typer.Option(..., "--weight", "-w")):
    # 모델 로드
    with open(get_model_path(), "rb") as f:
        fish_model = pickle.load(f)

    # 예측 수행
    result = fish_model.predict([[l, w]])

    # 예측 결과 출력
    if result == 1:
        typer.echo("도미")
    else:
        typer.echo("빙어")

def run_main():
    typer.run(main)
