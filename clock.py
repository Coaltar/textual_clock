from time import localtime, monotonic, struct_time

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, Static

from ascii_clock import ASCII_Clock

import time as pytime


class ClockDisplay(Static):
    """An ascii clock widget."""

    # def __init__(self, time_object: struct_time=pytime.localtime()):
        # self.time = reactive(time_object)

    time = reactive(pytime.localtime())
    analog_clock = ASCII_Clock(15)

    def on_mount(self) -> None:
        """Even handler called when widget is added to the app."""
        self.update_timer = self.set_interval(1 / 120, self.update_time)

    def update_time(self) -> None:
        """Method to update the time to the current time."""
        self.time = pytime.localtime()
        

    def watch_time(self, time) -> None:
        """Called when the time attribute changes."""
        clock_image = self.analog_clock.get_clock_ascii(time)
        self.analog_clock.resize(time.tm_sec)
        self.update(clock_image)


