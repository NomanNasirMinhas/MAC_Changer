import subprocess
import optparse


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--i", dest="interface", help="Interface of which MAC address is to be changed")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address of the selected interface")
    (options, args) = parser.parse_args()
    if not options.interface:
        print("[-] Please Provide Interface Name to Spoof. Use --help or -h for more info.")
    elif not options.new_mac:
        print("[-] Please provide the spoofed MAC address. Use --help or -h for more info.")
    else:
        return options


def mac_changer(iface, mac):
    print("[+] Changing MAC Address of interface of " + iface + " to -> " + new_mac)
    # subprocess.call("ifconfig " + interface + " down", shell=True)
    # subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    # subprocess.call("ifconfig " + interface + " up", shell=True)

    subprocess.call(["ifconfig", iface, "down"])
    subprocess.call(["ifconfig ", iface, "hw", "ether", mac])
    subprocess.call(["ifconfig ", iface, "up"])


args = get_args()
mac_changer(args.interface, args.new_mac)
