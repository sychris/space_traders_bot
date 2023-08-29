import requests
import http.client
import auth_token as auth
import json
import cli_commands as cc

conn = http.client.HTTPSConnection("api.spacetraders.io")
ver = "/v2/"
auth_token = {"Authorization": "Bearer " + auth.token}


def main():
    cc.menu()


def accept_contract(contract_id):
    path = ver + "my/contracts/" + contract_id + "/accept"
    print(post_request(path, auth_token))


def post_request(path, header):
    return send_request("POST", path, header)


def get_request(path, header):
    return send_request("GET", path, header)


def send_request(type, path, header):
    conn.request(type, path, headers=header)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")


def system_from_waypoint(waypoint):
    x = waypoint.split("-")
    system = x[0] + "-" + x[1]
    return system


def view_contracts():
    path = ver + "my/contracts"
    print(get_request(path, auth_token))


# /systems/X1-QB20
# X1-QB20-61050B
def view_location(waypoint):
    sys = system_from_waypoint(waypoint)
    path = ver + "systems/" + sys + "/waypoints/" + waypoint
    phase_waypoint(get_request(path, auth_token))


def view_agent():
    path = ver + "my/agent"
    response = get_request(path, auth_token)
    phase_data(response)


def phase_waypoint(waypoint_data):
    # print(phase_waypoint.Response == 200)
    #print(waypoint_data)
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


def phase_data(data):
    # print(data.content)
    phased = json.loads(data.content)
    print(phased["data"])


def create_token(my_user, my_faction):
    if auth.token != "":
        print("user already generated clear existing token to make anew!")
        exit()
    payload = "{\n  \"faction\": \"" + my_faction + "\",\n  \"symbol\": \"" + my_user + "\"}"
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json"
    }
    conn.request("POST", ver + "register", payload, headers)
    res = conn.getresponse()
    data = res.read()
    phased = json.loads(data)

    if "error" in phased:
        print("error" + str(phased["error"]))
    else:
        print("success")
        token = "token = \"" + phased["data"]["token"] + "\""
        print(phased["data"]["token"])
        file_path = "auth_token.py"
        with open(file_path, "w") as file:
            file.write(token)
        print(f"Token generated in {file_path}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
