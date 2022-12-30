import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--i", dest="interface", help="Interface of which MAC address is to be changed")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address of the selected interface")
(options, args) = parser.parse_args()
interface = options.interface
new_mac = options.new_mac


def mac_changer(iface, mac):
    print("[+] Changing MAC Address of interface of " + iface + " to -> " + new_mac)
    # subprocess.call("ifconfig " + interface + " down", shell=True)
    # subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    # subprocess.call("ifconfig " + interface + " up", shell=True)

    subprocess.call(["ifconfig", iface, "down"])
    subprocess.call(["ifconfig ", iface, "hw", "ether", mac])
    subprocess.call(["ifconfig ", iface, "up"])


mac_changer(interface, new_mac)
