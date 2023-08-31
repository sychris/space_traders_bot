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
                gui.buy_ship(get_input("waypoint: "),get_input("ship symbol: "))
            case "view_ships":
                gui.view_ships()
            case _:
                print("unknown command")


def get_input(msg):
    return input(msg)


def cli_show_waypoint(waypoint_data):
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


def cli_show_contracts(data):
    print(data)


def cli_print_waypoint(data):
    return None


def cli_show_agent(data):
    print(data)


def cli_show_check_auth(exists):
    if exists:
        print("auth token appears to exist")
    else:
        print("auth token not found")


def show_error(msg):
    print("Error: " + msg)


def show_msg(msg):
    print("Message: " + msg)


def show_shipyard(data):
    print(data)


def cli_show_system(data):
    print(data)


def view_ships(data):
    print(data)