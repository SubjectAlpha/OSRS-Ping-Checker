from pythonping import ping
from colorama import Fore, Style
import eel, json

class OSRSPing:
    world = 0
    ping = 0

    def __init__(self, world, ping):
        self.world = world
        self.ping = ping

eel.init("web")

def obj_dict(obj):
    return obj.__dict__

@eel.expose
def CheckPing():
    osrs_pings = list()
    for i in range(1, 236): #236
        response_list = ping(f"oldschool{i}.runescape.com", size=40, count=4)
        current_ping = round(response_list.rtt_avg_ms, 1)
        osrs_pings.append(OSRSPing(i + 300, current_ping))

    sorted_pings = sorted(osrs_pings, key=lambda x: x.ping)

    return json.dumps(sorted_pings, default=obj_dict)

if __name__ == "__main__":
    eel.start("index.html", size=(1024,768))
        