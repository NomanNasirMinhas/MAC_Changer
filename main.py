import subprocess
import optparse
import re
import time

mac_pattern = re.compile(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w")


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

def check_outcome(iface):
    result = subprocess.check_output(["ifconfig", iface], stdin=None, stderr=None, shell=False,
                                     universal_newlines=False)
    mac_search_res = re.search(mac_pattern, result.decode("utf-8"))
    if mac_search_res:
        if iface == mac_search_res.group(0):
            print("[+] Interface MAC Address has been spoofed successfully")
            return True
        else:
            print("[+] Confirming if MAC has been spoofed successfully")
            return False

    else:
        print("[-] MAC address not found for provided interface.")
        return 0

def mac_changer(iface, mac):
    try:
        if mac_pattern.match(mac):
            subprocess.check_output(["ifconfig", iface], stdin=None, stderr=None, shell=False, universal_newlines=False)
            # subprocess.call(["sudo", "ifconfig", iface, "down"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            # condition = True # Condition to See if Interface is down
            # while condition:
            #     result = subprocess.check_output(["ifconfig", iface], stdin=None, stderr=None, shell=False,
            #                                      universal_newlines=False).decode("utf-8")
            #     if "inet" in result:
            #         print("[+] Waiting for " + iface + " status to change to down..")
            #         time.sleep(2)
            #     else:
            #         condition = False
            # print("[+] Changing MAC Address of interface of " + iface + " to " + mac)
            # subprocess.call(["sudo", "ifconfig ", iface, "hw", "ether", mac], stdout=subprocess.DEVNULL,
            #                 stderr=subprocess.STDOUT)
            condition = True # Condition to See if MAC Address Has been spoofed
            count = 1
            while condition:
                if count < 10:
                    if check_outcome(iface):
                        print("[+] MAC Address changed successfully")
                    elif not check_outcome(iface):
                        print("[+] Waiting for " + iface + " MAC Change..")
                        count = count + 1
                        time.sleep(2)
                    elif check_outcome(iface) == 0:
                        return

                else:
                    print("[-] MAC Address Could not be spoofed")
            # subprocess.call(["sudo", "ifconfig ", iface, "up"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        else:
            print("[-] Invalid MAC Address")
            return False
    except:
        print("[-] Something Went Wrong")
        return False


args = get_args()
if args != False:
    res = mac_changer(args.interface, args.new_mac)
    if res != False:
        check_outcome(args.interface)
