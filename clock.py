from time import localtime, monotonic, struct_time

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, Static

from print_clock import get_clock, display_matrix

import time as pytime


class ClockDisplay(Static):
    """An ascii clock widget."""

    # def __init__(self, time_object: struct_time=pytime.localtime()):
        # self.time = reactive(time_object)

    time = reactive(pytime.localtime())

    def on_mount(self) -> None:
        """Even handler called when widdget is added to the app."""
        self.update_timer = self.set_interval(1 / 120, self.update_time)

    def update_time(self) -> None:
        """Method to update the time to the current time."""
        self.time = pytime.localtime()
        

    def watch_time(self, time) -> None:
        """Called when the time attribute changes."""
        now = time
        hour = now.tm_hour
        min = now.tm_min
        sec = now.tm_sec
        clock_matrix = get_clock(hour,min,sec)
        clock_image = display_matrix(clock_matrix)
        self.update(clock_image )


