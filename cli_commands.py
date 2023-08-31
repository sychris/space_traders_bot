import json
import settings


def cli_menu(gui):
    run = True
    while run:
        my_input = input("please enter a command")

        match my_input:
            case "hi":
                print("hello")
            case "contracts":
                gui.show_contracts()
            case "view_waypoint":
                gui.show_waypoint(get_input("waypoint to view: "))
            case "view_system":
                gui.show_system(get_input("system to view: "))
            case "agent":
                gui.show_agent()
            case "exit":
                run = False
            case "check_auth":
                gui.show_check_auth()
            case "show_auth":
                print(settings.auth_token)
            case "create_token":
                gui.create_token("sychris", "COSMIC")
            case "view_shipyard":
                gui.view_shipyard(get_input("waypoint to view: "))
            case "buy_ship":
                gui.buy_ship(get_input("waypoint: "), get_input("ship symbol: "))
            case "view_ships":
                gui.view_ships()
            case "view_ship":
                gui.view_ship(get_input("ship ID: "))
            case "orbit_ship":
                gui.orbit_ship(get_input("ship ID: "))
            case "navigate_ship":
                gui.navigate_ship(get_input("ship ID: "), get_input("waypoint: "))
            case "dock_ship":
                gui.dock_ship(get_input("ship ID: "))
            case "refuel_ship":
                gui.refuel_ship(get_input("ship ID: "))
            case "extract_here":
                gui.extract(get_input("ship ID: "))
            case "ship_cooldown":
                gui.cooldown(get_input("ship ID: "))

            case _:
                print("unknown command")


def get_input(msg, msg_type ="standard"):
    return input(msg)


def show_waypoint(waypoint_data):
    # print(phase_waypoint.Response == 200)
    # print(waypoint_data)
    phased = json.loads(waypoint_data)
    # print(phased["data"])
    print("systemSymbol: " + phased["data"]["systemSymbol"])
    print("symbol: " + phased["data"]["symbol"])
    print("type: " + phased["data"]["type"])
    print("x: " + str(phased["data"]["x"]))
    print("y: " + str(phased["data"]["y"]))
    print("orbitals:")
    for orbital in phased["data"]["orbitals"]:
        print("\tsymbol: " + orbital["symbol"])
    print("traits: ")
    for trait in phased["data"]["traits"]:
        print("\tsymbol: " + trait["symbol"])
        print("\tname: " + trait["name"])
        print("\tdescription: " + trait["description"])
    if "chart" in phased["data"]:
        print("chart: ")
        for d in phased["data"]["chart"]:
            print("\t" + d + ": " + phased["data"]["chart"][d])
    if "faction" in phased["data"]:
        print("faction: " + phased["data"]["faction"]["symbol"])


def show_contracts(data):
    print(data)


def print_waypoint(data):
    return None


def show_agent(data):
    print(data)


def show_check_auth(exists):
    if exists:
        print("auth token appears to exist")
    else:
        print("auth token not found")


def show_error(msg):
    show_msg(msg, "error")


def show_msg(msg, msg_type = "standard"):
    match msg_type:
        case "error":
            print("Error: ", msg)
        case "ship_yard":
            show_shipyard(msg)
        case "get_ship":
            view_ship(msg)
        case "view_ships":
            view_ships(msg)
        case _:
            print(msg)


def show_shipyard(data):
    print(data)


def show_system(data):
    print(data)


def view_ships(data):
    print(data)
    phased = json.loads(data)
    for ship in phased["data"]:
        view_ship(ship)


def view_ship(data):
    #print(type(data))
    if type(data) == str:
        data = json.loads(data)
        data = data["data"]
    #print(type(data))
    #print(data)
    print("symbol: " + data["symbol"])
    print("name: " + data["registration"]["name"])
    print("role: " + data["registration"]["role"])
    print("frame: " + data["frame"]["symbol"])
    print("")
    print("reactor: ")
    print("\tsymbol: " + data["reactor"]["symbol"])
    print("\tname: " + str(data["reactor"]["name"]))
    print("\tcondition: " + str(data["reactor"]["condition"]))
    print("")
    print("cargo: ")
    print("\tcapacity: " + str(data["cargo"]["capacity"]))
    print("\tused: " + str(data["cargo"]["units"]))
    print("items:")
    for item in data["cargo"]["inventory"]:
        print("symbol: " + item["symbol"])
        print("name: " + item["name"] + ": " + item["description"])
        print("units: " + str(item["units"]))
        print("")
    print("modules: ")
    for module in data["modules"]:
        print("\tsymbol: " + module["symbol"])
    print("")
    print("navigation information: ")
    print("\tstatus: " + data["nav"]["status"])
    print("\tflight mode: " + data["nav"]["flightMode"])
    print("")
    print("fuel:")
    print("\tcurrent: " + str(data["fuel"]["current"]))
    print("\tcapacity: " + str(data["fuel"]["capacity"]))
    print("\n\n\n")