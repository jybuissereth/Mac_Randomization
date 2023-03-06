import random
from scapy.all import rdpcap


def random_bytes(num=6):
    return [random.randrange(256) for _ in range(num)]

def generate_mac(uaa=False, multicast=False, oui=None, separator=':', byte_fmt='%02x'):
    mac = random_bytes()
    if oui:
        if type(oui) == str:
            oui = [int(chunk) for chunk in oui.split(separator)]
        mac = oui + random_bytes(num=6-len(oui))
    else:
        if multicast:
            mac[0] |= 1 # set bit 0
        else:
            mac[0] &= ~1 # clear bit 0
        if uaa:
            mac[0] &= ~(1 << 1) # clear bit 1
        else:
            mac[0] |= 1 << 1 # set bit 1
    return separator.join(byte_fmt % b for b in mac)


paquets= rdpcap("test.cap")



addresse_assoc={}

for i in range(20):
    addr = paquets[i]["Dot11"].addr2
    addresse_assoc[addr]=generate_mac()

print(addresse_assoc)