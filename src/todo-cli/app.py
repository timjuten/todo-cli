from textual.app import App, ComposeResult
from textual.widgets import Button, Footer, Header, Input

from cli import load_tasks, save_tasks
from Task import Task


class TodoApp(App[str]):
    TITLE = "To Do App"
    CSS_PATH = "todo.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Input(placeholder="Write the name of your task", id="task")
        yield Button(label="Add", id="add_button")
        yield Footer()

    def on_button_pressed(self) -> None:
        input_widget = self.query_one("#task", Input)
        name = input_widget.value

        tasks = load_tasks()
        task = Task(name, len(tasks), False)

        tasks.append({"name": task.name, "index": task.index, "status": task.status})

        save_tasks(tasks)


if __name__ == "__main__":
    app = TodoApp()
    app.run()
