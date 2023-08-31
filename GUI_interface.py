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
        if self.is_cli():
            cc.show_waypoint(si.get_waypoint(waypoint))
    def show_system(self, system):
        if self.is_cli():
            cc.show_system(si.get_system(system))

    def buy_ship(self, waypoint, ship_symbol):
        if self.is_cli():
            cc.show_msg(si.buy_ship(waypoint, ship_symbol))

    def view_ships(self):
        si.get_ships(self)

    def refuel_ship(self, ship_id):
        si.refuel_ship(self, ship_id)

    def orbit_ship(self, ship_id):
        if self.is_cli():
            cc.show_msg(si.orbit_ship(ship_id))
    def view_ship(self, ship_id):
        si.get_ship(self, ship_id)
    def show_contracts(self):
        if self.is_cli():
            cc.show_contracts(si.get_contracts())
    def cooldown(self,ship_id):
        si.get_cooldown(self,ship_id)
    def show_agent(self):
        if self.is_cli():
            cc.show_agent(si.get_agent())

    def show_check_auth(self):
        if self.is_cli():
            cc.show_check_auth(utils.check_auth_exists())

    def create_token(self, user, faction):
        si.create_token(self, user, faction)

    def show_error(self, msg):
        if self.is_cli():
            cc.show_error(msg)

    def dock_ship(self, ship_id):
        si.dock_ship(self, ship_id)

    def show_msg(self, msg, msg_type = "standard"):
        if self.is_cli():
            cc.show_msg(msg, msg_type)

    def view_shipyard(self, waypoint):
        if self.is_cli():
            cc.show_shipyard(si.view_shipyard(self, waypoint))

    def navigate_ship(self,ship_id, waypoint):
        si.navigate_ship(self, ship_id,waypoint)

    def extract(self, ship_id):
        si.extract(self, ship_id)

    def is_cli(self):
        return True if self.gui_type == "cli" else False
