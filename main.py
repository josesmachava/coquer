import typer
import os 

app = typer.Typer()

def create_directory(name:str):
    try: 
            os.mkdir(name)
    
    except OSError as error: 
            typer.echo(error)
    

def create_strcutre(name: str, directory: list):
    create_directory(name)    
    for directory in directory:

        structure = os.path.join(name, directory)
        
        create_directory(structure)
        
        


@app.command()
def project(name: str):
    directories = ["migrations", "scripts", "tests"]
    create_strcutre(name, directories)
          
    
    subdirectories = ["models", "repos", "schema", "services", "tasts", "lib"]
    create_strcutre(os.path.join(name, "app"),subdirectories)
    typer.echo(f"Creating project {name}")



if __name__ == "__main__":
    app()