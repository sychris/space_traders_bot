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


def post_request(path, header):
    return send_request("POST", path, header)


def get_request(path, header):
    return send_request("GET", path, header)


def send_request(send_type, path, header):
    conn.request(send_type, path, headers=header)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")


def accept_contract(contract_id):
    path = settings.ver + "my/contracts/" + contract_id + "/accept"
    print(post_request(path, settings.auth_token))


def create_token(my_user, my_faction):
    if auth.token != "":
        print("user already generated clear existing token to make anew!")
        exit()
    payload = "{\n  \"faction\": \"" + my_faction + "\",\n  \"symbol\": \"" + my_user + "\"}"
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json"
    }
    conn.request("POST", settings.ver + "register", payload, headers)
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


def get_waypoint(waypoint):
    sys = utils.system_from_waypoint(waypoint)
    path = settings.ver + "systems/" + sys + "/waypoints/" + waypoint
    return get_request(path, settings.auth_token)
