from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Input


class TodoApp(App[str]):
    TITLE = "To Do App"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Input(placeholder="Add your task")
        yield Footer()

    def on_button_pressed(self) -> None:
        self.exit()


if __name__ == "__main__":
    app = TodoApp()
    app.run()
