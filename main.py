import subprocess
import optparse
import re


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--i", dest="interface", help="Interface of which MAC address is to be changed")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address of the selected interface")
    (options, args) = parser.parse_args()
    if not options.interface:
        print("[-] Please Provide Interface Name to Spoof. Use --help or -h for more info.")
        return False
    elif not options.new_mac:
        print("[-] Please provide the spoofed MAC address. Use --help or -h for more info.")
        return False
    else:
        return options


def mac_changer(iface, mac):
    try:
        subprocess.check_output(["ifconfig", iface], stdin=None, stderr=None, shell=False, universal_newlines=False)
        print("[+] Changing MAC Address of interface of " + iface + " to -> " + mac)
        subprocess.call(["ifconfig", iface, "down"], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        subprocess.call(["ifconfig ", iface, "hw", "ether", mac], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        subprocess.call(["ifconfig ", iface, "up"], shell=True,  stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as err:
        print("[-] Something Went Wrong: " + err)
        return False



def check_outcome(iface):
    result = subprocess.check_output(["ifconfig", iface], stdin=None, stderr=None, shell=False, universal_newlines=False)
    mac_search_res = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w", result.decode("utf-8"))
    if mac_search_res:
        if iface == mac_search_res.group(0):
            print("[+] Interface MAC Address has been spoofed successfully")
        else:
            print("[-] Interface MAC Address could not be spoofed")

    else:
        print("[-] MAC address not found for provided interface.")


args = get_args()
if args != False:
    res = mac_changer(args.interface, args.new_mac)
    if res != False:
        check_outcome(args.interface)
