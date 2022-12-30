import subprocess
import optparse
import re

mac_pattern = re.compile(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w")


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--i", dest="interface", help="Interface of which MAC address is to be changed")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address of the selected interface")
    parser.add_option("-c", "--cycle", dest="cycle", action='store_true',
                      help="Stop the interface before spoofing MAC address")
    (options, args) = parser.parse_args()
    if not options.interface:
        print("[-] Please Provide Interface Name to Spoof. Use --help or -h for more info.")
        return False
    elif not options.new_mac:
        print("[-] Please provide the spoofed MAC address. Use --help or -h for more info.")
        return False
    else:
        return options


def mac_changer(iface, mac, cycle):
    try:
        if mac_pattern.match(mac):
            subprocess.check_output(["ifconfig", iface], stdin=None, stderr=None, shell=False, universal_newlines=False)
            print("[+] Changing MAC Address of interface of " + iface + " to " + mac)
            if not cycle:
                subprocess.call(["sudo", "ip", "link", "set", "dev", iface, "address", mac])
            else:
                subprocess.call(["sudo", "ip", "link", "set", "dev", iface, "down"])
                wait = True
                count = 0
                while wait:
                    check = check_status(iface, False)
                    if check:
                        print("[+] "+ iface, " has been stopped")
                        wait = False
                    else:
                        if count > 9:
                            return
                        print("[+] Stopping ", iface, " ......")
                        count = count + 1
                subprocess.call(["sudo", "ip", "link", "set", "dev", iface, "address", mac])
                subprocess.call(["sudo", "ip", "link", "set", "dev", iface, "up"])
                wait = True
                count = 0
                while wait:
                    check = check_status(iface, True)
                    if check:
                        print("[+] " + iface, " has started again")
                        wait = False
                    else:
                        if count > 9:
                            return
                        print("[+] Starting ", iface, " ......")
                        count = count + 1
        else:
            print("[-] Invalid MAC Address")
            return False
    except Exception as err:
        print("[-] Something Went Wrong: " + str(err))
        return False


def check_outcome(iface, mac):
    result = subprocess.check_output(["ifconfig", iface], stdin=None, stderr=None, shell=False,
                                     universal_newlines=False)
    mac_search_res = re.search(mac_pattern, result.decode("utf-8"))
    if mac_search_res:
        if mac == mac_search_res.group(0):
            print("[+] Interface MAC Address has been spoofed successfully to " + mac)
        else:
            print("[-] Interface MAC Address could not be spoofed")

    else:
        print("[-] MAC address not found for provided interface.")


def check_status(iface, status):
    result = subprocess.check_output(["ip", "link", "show", iface], stdin=None, stderr=None, shell=False,
                                     universal_newlines=False).decode("utf-8")
    if status:
        if "state UP" in result:
            return True
        else:
            return False
    else:
        if "state DOWN" in result:
            return True
        else:
            return False

args = get_args()
if args != False:
    res = mac_changer(args.interface, args.new_mac, args.cycle)
    if res != False:
        check_outcome(args.interface, args.new_mac)
