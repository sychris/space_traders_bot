import cli_commands as cc
import server_interface as si


class GUI:
    def __init__(self, gui_type):
        self.gui_type = gui_type

    def show_main(self):
        if self.is_cli():
            cc.cli_menu(self)

    def show_location(self, waypoint):
        data = si.get_waypoint(waypoint)
        if self.is_cli():
            cc.cli_show_waypoint(data)

    def show_contracts(self):
        data = si.get_contracts()
        if self.is_cli():
            cc.cli_show_contracts(data)

    def show_agent(self):
        data = si.get_agent()
        if self.is_cli():
            cc.cli_show_agent(data)



    def is_cli(self):
        return True if self.gui_type == "cli" else False