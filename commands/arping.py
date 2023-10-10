import os
import re

os.system("clear")

def inputHandler(text):
    if text == "e" or text == "E":
        exit(0)
    ip = input(text)
    if not os.path.exists(".history_ip"):
        with open(".history_ip", "w") as f:
            f.write(ip)
    if (not bool(re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip))):
        inputHandler("Invalid IP address, please try again or press e to exit: ")
    return ip

ip = inputHandler("Enter the first IP adress (/24): ").split(".")

for i in range(0,255):
    os.system(f"arping {ip[0]}.{ip[1]}.{ip[2]}.{i} -i eth0")

# 192.168.0.10 is alive
# 192.168.0.13 is alive
# 192.168.0.15 is alive
# 192.168.0.18 is alive
# 192.168.0.35 is alive
# 192.168.0.36 is alive
# 192.168.0.50 is alive