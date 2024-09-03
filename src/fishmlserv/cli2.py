import requests
import json 
import typer


headers = {
            'accept': 'application/json',
        }

@app.command()
def main(l:float=typer.Option(...,"--length","-l"), w:float=typer.Option(...,"--weight","-w")):
    if l :
        le=l
        if w:
            we=w
            params = {
                'length': le,
                'weight': we,
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
