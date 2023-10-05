import os
import re

os.system("clear")

def inputHandler(text):
    if text == e or text == E:
        exit(0)
    ip = input(text)
    if not os.path.exists(".history_ip"):
        with open(".history_ip", "w") as f:
            f.write(ip)
    if (not bool(re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip))):
        inputHandler("Invalid IP address, please try again or press e to exit: ")
    return ip

ip = inputHandler("Enter the IP address: ")



os.system("nmap -sV -sC -Pn -oN nmap_scan.txt " + ip)

