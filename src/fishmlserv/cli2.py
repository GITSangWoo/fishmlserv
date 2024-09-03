import requests
import json 
import typer


headers = {
            'accept': 'application/json',
        }

def main(l:float=typer.Option(...,"--length","-l"), w:float=typer.Option(...,"--weight","-w")):
    if l :
        if w:
            params = {
                'length': l,
                'weight': w,
                }
            response = requests.get('http://127.0.0.1:8000/fish_ml_predictor', params=params, headers=headers)
            data=json.loads(response.text) 
            typer.echo(f"{data['prediction']}") 
              
        else:
            typer.echo("다시 ㄱ")
    else : 
        typer.echo("다시 ㄱ")


def run_main():
    typer.run(main)
