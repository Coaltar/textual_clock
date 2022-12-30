from time import localtime

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Footer, Header, Static

from clock import ClockDisplay


class TextualClock(App):
    """An app that displays an ascii interpretation of an analog clock."""

    CSS_PATH = "stopwatch.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield Container(ClockDisplay())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = TextualClock()
    app.run()
