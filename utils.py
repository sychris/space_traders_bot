import json
import settings


def system_from_waypoint(waypoint):
    x = waypoint.split("-")
    system = x[0] + "-" + x[1]
    return system


def phase_data(data):
    # print(data.content)
    phased = json.loads(data.content)
    print(phased["data"])


def check_auth_exists():
    if settings.auth_token != "{'Authorization': 'Bearer }":
        return False
    else:
        return True