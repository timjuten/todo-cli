import typer
from Task import Task

app = typer.Typer()

todo_list = []


@app.command()
def add(name: str, status: bool = False):
    task = Task(name, status)
    print(f"")


if __name__ == "__main__":
    pass
