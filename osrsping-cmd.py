from pythonping import ping
from colorama import Fore, Style
import eel

class OSRSPing:
    world = 0
    ping = 0

    def __init__(self, world, ping):
        self.world = world
        self.ping = ping

def CheckPing():
    print("Please wait while I find the server with the best ping.")
    pvp_worlds = [24,43,45,92,117]
    ftp_worlds = [1,8,16,26,35,71,72,79,80,81,82,83,84,85,93,94,97,98,99,113,114,118,119,125,126,127,130,131,132,133,134,135,136,137,138,139,140,151,152,153,154,155,156,157,158,159,168,169,170,171,172,173,174,175,176,183,197,198,199,200,201,202,503,204,230]
    osrs_pings = list()
    for i in range(1, 236): #236
        print(f"Checking world: {i + 300}")
        response_list = ping(f"oldschool{i}.runescape.com", size=40, count=4)
        current_ping = round(response_list.rtt_avg_ms, 1)
        osrs_pings.append(OSRSPing(i + 300, current_ping))

    best_worlds = list()

    sorted_pings = sorted(osrs_pings, key=lambda x: x.ping)

    for o in sorted_pings:
        if (o.world - 300) in ftp_worlds:
            print(f"{Fore.YELLOW}World: {o.world}, Ping: {o.ping}{Style.RESET_ALL}")
        elif (o.world - 300) in pvp_worlds:
            print(f"{Fore.RED}World: {o.world}, Ping: {o.ping}{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}World: {o.world}, Ping: {o.ping}{Style.RESET_ALL}") 

if __name__ == "__main__":
    CheckPing()
        