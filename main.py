import requests
import http.client
import json
import auth_token as auth
import json

conn = http.client.HTTPSConnection("api.spacetraders.io")
ver = "/v2/"
auth_token = {"Authorization": "Bearer " + auth.token}


def main():
    system_from_waypoint("X1-QB20-61050B")
    view_location("X1-QB20-61050B")


def system_from_waypoint(waypoint):
    x = waypoint.split("-")
    system = x[0] + "-" + x[1]
    return system

#/systems/X1-QB20
#X1-QB20-61050B
def view_location(waypoint):
    sys = system_from_waypoint(waypoint)
    headers = auth_token
    path = ver + "systems/" + sys + "/waypoints/"+ waypoint
    conn.request("GET", path , headers=headers)
    res = conn.getresponse()
    data = res.read()
    #print(res)
    #print(data)

    #print(data.decode("utf-8"))

    phase_waypoint(data)

def view_agent():
    path = base_url + '/my/agent'
    print(path)
    headers = auth_token
    response = requests.get(path, headers=headers)
    phase_data(response)

def phase_waypoint(waypoint_data):
    #print(phase_waypoint.Response == 200)
    #print(waypoint_data)
    phased = json.loads(waypoint_data)
    #print(phased["data"])
    print("systemSymbol: " + phased["data"]["systemSymbol"])
    print("symbol: " + phased["data"]["symbol"])
    print("type: " + phased["data"]["type"])
    print("x: " + str(phased["data"]["x"]))
    print("y: " + str(phased["data"]["y"]))
    print("orbitals:")
    for orbital in phased["data"]["orbitals"]:
        print("\tsymbol: " + orbital["symbol"])
    if "chart" in phased["data"]:
        print("true")
    print("traits: ")
    for trait in phased["data"]["traits"]:
        print("\tsymbol: " + trait["symbol"])
        print("\tname: " + trait["name"])
        print("\tdescription: " + trait["description"])
    if "chart" in phased["data"]:
        print("chart: ")
        for d in phased["data"]["chart"]:
            print("\t" + d + ": " +phased["data"]["chart"][d])
    if "faction" in phased["data"]:
        print("faction: " + phased["data"]["faction"]["symbol"])

def phase_data(data):
    #print(data.content)
    phased = json.loads(data.content)
    print(phased["data"])


def create_token():
    file_path = "auth_token.txt"
    my_json = { "symbol": "Sychris_test2", "faction": "COSMIC" }
    headers = {"Content-Type": "application/json"}
    response = requests.post("https://api.spacetraders.io/v2/register", headers=headers, json=my_json)
    print(response.content)
    phased = json.loads(response.content)
    t = phased["data"]["token"]
    print(t)
    write_token(t)


def write_token(token):
    file_path = "auth_token.py"
    with open(file_path, "w") as file:
        file.write(token)
    print(f"Token generated in {file_path}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
