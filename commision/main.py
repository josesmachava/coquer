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
        
        
def create_file(path: str, name: str):
    filepath = os.path.join(path, f'{name}.py')
    if not os.path.exists(path):
        os.makedirs(path)
    f = open(filepath, "w")
    f.close()


@app.command()
def schema(name:str):
    create_file("app/schema" ,name)

@app.command()
def project(name: str):
    directories = ["migrations", "scripts", "tests"]
    create_strcutre(name, directories)
          
    
    subdirectories = ["models", "repos", "schema", "services", "tasks", "lib"]
    create_strcutre(os.path.join(name, "app"),subdirectories)
    typer.echo(f"Creating project {name}")



if __name__ == "__main__":
    app()