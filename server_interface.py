import json

import utils
import settings
import http.client

conn = http.client.HTTPSConnection("api.spacetraders.io")


def get_contracts():
    path = settings.ver + "my/contracts"
    return get_request(path, settings.auth_token)


def get_agent():
    path = settings.ver + "my/agent"
    return get_request(path, settings.auth_token)


def post_request(path: str, header: dict, payload: str = None):
    return send_request("POST", path, header, payload)


def get_request(path, header):
    return send_request("GET", path, header)


def send_request(send_type: str, path: str, header: dict, payload: str = None):
    if payload is None:
        conn.request(send_type, path, headers=header)
    else:
        conn.request(send_type, path, payload, headers=header)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")


def accept_contract(contract_id):
    path = settings.ver + "my/contracts/" + contract_id + "/accept"
    print(post_request(path, settings.auth_token))


def create_token(gui, my_user, my_faction):
    if utils.check_auth_exists():
        gui.show_error("user already generated clear existing token to make anew!")
        exit()
    payload = "{\n  \"faction\": \"" + my_faction + "\",\n  \"symbol\": \"" + my_user + "\"}"
    headers = {'Content-Type': 'application/json'}
    print(type(headers))
    data = post_request(settings.ver + "register", headers, payload)
    phased = json.loads(data)
    if "error" in phased:
        gui.show_error(str(phased["error"]))
    else:
        gui.show_msg("success")
        token = "token = \"" + phased["data"]["token"] + "\""
        gui.show_msg(phased["data"]["token"])
        file_path = "auth_token.py"
        with open(file_path, "w") as file:
            file.write(token)
        gui.show_msg(f"Token generated in {file_path}")


def get_waypoint(waypoint):
    sys = utils.system_from_waypoint(waypoint)
    path = settings.ver + "systems/" + sys + "/waypoints/" + waypoint
    return get_request(path, settings.auth_token)


def view_shipyard(gui, waypoint):
    sys = utils.system_from_waypoint(waypoint)
    path = settings.ver + "systems/" + sys + "/waypoints/" + waypoint + "/shipyard"
    gui.show_msg(get_request(path, settings.auth_token),"view_shipyard")


def get_system(system):
    path = settings.ver + "systems/" + system
    return get_request(path, settings.auth_token)


def buy_ship(waypoint, ship_symbol):
    path = settings.ver + "my/ships"
    payload = '{"shipType": "' + ship_symbol + '", "waypointSymbol": "' + waypoint + '"}'
    headers = {'Content-Type': 'application/json'}
    headers.update(settings.auth_token)
    print(payload)
    return post_request(path, headers,payload)

def get_cooldown(gui,ship_id):
    path = settings.ver + "my/ships/" + ship_id + "/cooldown"
    gui.show_msg(get_request(path, settings.auth_token), "get_cooldown")

def get_ships(gui):
    path = settings.ver + "my/ships"
    gui.show_msg(get_request(path, settings.auth_token), "view_ships")


def get_ship(gui, ship_id):
    path = settings.ver + "my/ships/" + ship_id
    gui.show_msg( get_request(path, settings.auth_token), "get_ship")


def orbit_ship(ship_id):
    path = settings.ver + "my/ships/" + ship_id + "/orbit"
    return post_request(path, settings.auth_token)


def navigate_ship(gui, ship_id, waypoint):
    path = settings.ver + "my/ships/" + ship_id + "/navigate"
    payload = '{"waypointSymbol": "' + waypoint + '"}'
    headers = {'Content-Type': 'application/json'}
    headers.update(settings.auth_token)
    gui.show_msg(post_request(path,headers,payload))
    return  post_request(path,headers,payload)


def dock_ship(gui, ship_id):
    path = settings.ver + "my/ships/" + ship_id + "/dock"
    gui.show_msg(post_request(path, settings.auth_token),"dock_ship")


def refuel_ship(gui, ship_id):
    path = settings.ver + "my/ships/" + ship_id + "/refuel"
    gui.show_msg(post_request(path, settings.auth_token), "refuel_ship")


def extract(gui, ship_id):
    path = settings.ver + "my/ships/" + ship_id + "/extract"
    gui.show_msg(post_request(path, settings.auth_token), "extract")