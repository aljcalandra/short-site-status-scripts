import requests


def find_ffxiv_server_status(server):
    r = requests.get("https://na.finalfantasyxiv.com/lodestone/worldstatus/").text
    server_location = r.find(server)
    server_status_location = r.rfind('data-tooltip="', 0, server_location)
    return r[server_status_location:server_location].split()[1]
