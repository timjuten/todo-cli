#!usr/bin/env python3

import json
from pathlib import Path

import questionary
import typer
from Task import Task

app = typer.Typer()

FILE = "task.json"


def load_tasks():
    if not Path(FILE).exists():
        print("The list is empty.")
        return []

    with open(FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)


@app.command(help="")
def add(status: bool = False):
    tasks = load_tasks()
    name = input("Write the name of your task: ")
    task = Task(name, len(tasks), status)

    tasks.append({"name": task.name, "index": task.index, "status": task.status})

    save_tasks(tasks)

    print(f'The task "{task.name}" has been added.')


@app.command(name="list", help="Lists all of the tasks.")
def show():
    tasks = load_tasks()

    for index, t in enumerate(tasks):
        print(f"{t['index'] + 1}: {t['name']}, status: {t['status']}")


@app.command(help="Removes a task from the todo-list.")
def remove():

    tasks = load_tasks()
    choice = questionary.select(
        "Pick a task to remove:", choices=[t["name"] for t in tasks]
    ).ask()

    tasks = [t for t in tasks if t["name"] != choice]
    save_tasks(tasks)

    print(f"{choice} was removed.")


@app.command(help="Changes the task's status to 'finished'.")
def finish():
    tasks = load_tasks()
    choice = questionary.select(
        "Pick a task to finish", choices=[t["name"] for t in tasks]
    ).ask()

    for t in tasks:
        if t["name"] == choice:
            t["status"] = True
            break
    save_tasks(tasks)


if __name__ == "__main__":
    app()
