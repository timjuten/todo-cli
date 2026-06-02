from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Welcome


class TodoApp(App[str]):
    TITLE = "To Do App"

    def compose(self) -> ComposeResult:
        yield Welcome()
        yield Header()

    def on_button_pressed(self) -> None:
        self.exit()


if __name__ == "__main__":
    app = TodoApp()
    app.run()
