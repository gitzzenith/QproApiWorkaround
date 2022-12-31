import subprocess
import re

def getApiIPStatic():
    connections = []
    output = subprocess.run(["adb", "shell", "ip", "addr"], stdout=subprocess.PIPE,shell=True)
    lines = output.stdout.decode().splitlines()

    for line in lines:
        line = line.strip()
        pattern = re.compile(r"inet 192.*scope global") # not proven, but the correct IP seems to always follow this pattern on both Q2 and Qpro. There is absolutely a better way to do this.
        string = "inet 10.0.0.1/24 scope global dynamic"
        if(pattern.search(line)):
            data = line.split(" ") # parse out the static part of the IP
            ip = data[1]
            rawip = ip.split("/")[0]
            ipParts = rawip.split(".")[:-1]
            ipStart = ""
            for part in ipParts:
                ipStart += part + "."
            return ipStart
    return None

import time
while(True):
    ip = getApiIPStatic()
    if(ip == None):
        print("Headset not connected via USB or controllers not awake, retrying in 5s...")
        time.sleep(5)
    else:
        ipFile = open('staticIP.txt', 'w')
        ipFile.write(ip)
        ipFile.close()
        print("Ip found:", ip, "Run RUN_ME.bat to join a match")
        input("press enter to exit")
        break
