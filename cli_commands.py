import json


def cli_menu(gui):
    run = True
    while run:
        my_input = input("please enter a command")

        match my_input:
            case "hi":
                print("hello")
            case "view_contracts":
                gui.show_contracts()
            case "view_location":
                gui.show_location("X1-QB20-61050B")
            case "view_agent":
                gui.show_agent()
            case "exit":
                run = False

            case _:
                print("unknown command")


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


def cli_print_contracts(data):
    print(data)


def cli_print_waypoint(data):
    return None


def cli_show_agent(data):
    print(data)