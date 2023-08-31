import cli_commands as cc
import server_interface as si
import utils


class GUI:
    def __init__(self, gui_type):
        self.gui_type = gui_type

    def show_main(self):
        if self.is_cli():
            cc.cli_menu(self)

    def show_waypoint(self, waypoint):
        data = si.get_waypoint(waypoint)
        if self.is_cli():
            cc.cli_show_waypoint(data)
    def show_system(self, system):
        data = si.get_system(system)
        if self.is_cli():
            cc.cli_show_system(data)

    def buy_ship(self, waypoint, ship_symbol):
        data = si.buy_ship(waypoint, ship_symbol)
        if self.is_cli():
            cc.show_msg(data)

    def view_ships(self):
        data = si.get_ships()
        if self.is_cli():
            cc.view_ships(data)
    def show_contracts(self):
        data = si.get_contracts()
        if self.is_cli():
            cc.cli_show_contracts(data)

    def show_agent(self):
        data = si.get_agent()
        if self.is_cli():
            cc.cli_show_agent(data)

    def show_check_auth(self):
        if self.is_cli():
            cc.cli_show_check_auth(utils.check_auth_exists())

    def create_token(self, user, faction):
        if self.is_cli():
            si.create_token(user, faction, self)

    def show_error(self, msg):
        if self.is_cli():
            cc.show_error(msg)

    def show_msg(self, msg):
        if self.is_cli():
            cc.show_msg(msg)

    def view_shipyard(self, waypoint):
        data = si.view_shipyard(waypoint)
        if self.is_cli():
            cc.show_shipyard(data)

    def is_cli(self):
        return True if self.gui_type == "cli" else False
