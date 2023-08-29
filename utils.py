import json


def system_from_waypoint(waypoint):
    x = waypoint.split("-")
    system = x[0] + "-" + x[1]
    return system


def phase_data(data):
    # print(data.content)
    phased = json.loads(data.content)
    print(phased["data"])
