from pythonping import ping
from colorama import Fore, Style

class OSRSPing:
    world = 0
    ping = 0

    def __init__(self, world, ping):
        self.world = world
        self.ping = ping

if __name__ == "__main__":
    print("Please wait while I find the server with the best ping.")
    #Bad worlds are F2P and PVP Worlds
    bad_worlds = [1,8,16,24,26,35,43,45,71,72,79,80,81,82,83,84,85,92,93,94,97,98,99,113,114,117,118,119,125,126,127,130,131,132,133,134,135,136,137,138,139,140,151,152,153,154,155,156,157,158,159,168,169,170,171,172,173,174,175,176,183,197,198,199,200,201,202,503,204,230]
    osrs_pings = list()
    for i in range(1, 15): #236
        print(f"Checking world: {i + 300}")
        response_list = ping(f"oldschool{i}.runescape.com", size=40, count=4)
        current_ping = round(response_list.rtt_avg_ms, 1)
        osrs_pings.append(OSRSPing(i + 300, current_ping))

    best_ping = 10000
    best_world = 0

    best_worlds = list()

    for o in osrs_pings:
        if o.ping < best_ping:
            for bw in bad_worlds:
                if o.world != bw:
                    best_ping = o.ping
                    best_world = o.world

    sorted_pings = sorted(osrs_pings, key=lambda x: x.ping)

    for o in sorted_pings:
        if o.world in bad_worlds:
            print(f"{Fore.RED}World: {o.world}, Ping: {o.ping}")
        else:
            print(f"{Fore.GREEN}World: {o.world}, Ping: {o.ping}")
    
    print(f"Best world: {best_world}, ping: {best_ping}")
    
        