#!/usr/bin/python

from command_widget import CommandWidget
from panel_help import *

colors = ['#dbad72', '#f9d3a5', '#ab9c73']
COLOR_USED = '#f9d3a5'
COLOR_OPEN_EMPTY = '#ab9c73'
COLOR_URGENT = '#fcff60'
COLOR_SEPARATOR = '#e4a972'


class WorkspaceWidget(CommandWidget):
    def __init__(self):
        super(WorkspaceWidget, self).__init__("bspc subscribe")

    def handle_output(self, output):
        output = output.decode("utf8")
        workspaces = str(output).split(":")

        allWorkspaces = []

        for w in workspaces:
            label = w[0]

            title = w[1:]
            title = set_left_click(title, "bspc desktop -f %s" % title)

            dont_draw = False

            # Occupied, not active
            if label == "o":
                title = set_color(title, COLOR_USED)
            # Empty, active
            elif label == "F":
                title = set_color(title, COLOR_OPEN_EMPTY)
                title = set_underline_color(title, COLOR_OPEN_EMPTY)
            # Occupied, active
            elif label == "O":
                title = set_color(title, COLOR_USED)
                title = set_underline_color(title, COLOR_USED)
            # Occupied, active
            elif label == "u":
                title = set_color(title, COLOR_URGENT)
            elif label == "U":
                title = set_color(title, COLOR_URGENT)
                title = set_underline_color(title, COLOR_USED)
            # Display separator
            elif label.lower() == 'm':
                title = "|"
                title = set_color(title, COLOR_SEPARATOR)
            else:
                dont_draw = True

            if not dont_draw:
                allWorkspaces.append(" %s " % title)

        self.text = "".join(allWorkspaces)
        register_update()
