import requests
import json 
import typer


app = typer.Typer()

headers = {
            'accept': 'application/json',
        }

@app.command()
def main(l:int=0, w:int=0):
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


if __name__ == "__main__":
    app()

