from number_widget import NumberWidget
import os
import re


class BatteryWidget(NumberWidget):
    def __init__(self):
        super().__init__('B')

        self.state = ""
        self.update_time = 60
        self.battery_command = "upower -i $(upower -e | grep 'BAT') |\
      grep -E 'state|time\ to|percentage'"

    def update_number(self):
        battery = self.get_battery_dump()

        try:
            self.state = battery[0][-1]
            self.number = int(battery[-1][-1][:-1])
        except IndexError:
            self.state = ""
            self.number = 0

    def update_char(self):
        if self.state == 'charging':
            self.character = '%{F#00FF00}B'
        elif self.number < 20:
            self.character = '%{F#FF0000}B'
        else:
            self.character = 'B'

    def get_battery_dump(self):
        f = os.popen(self.battery_command)
        return [re.compile("\s+").split(line) for line in f.read().split('\n') if line.strip() != '']
