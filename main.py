import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--i", dest="interface", help="Interface of which MAC address is to be changed")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address of the selected interface")
(options, args) = parser.parse_args()
interface = options.interface
new_mac = options.new_mac
print("[+] Changing MAC Address of interface of " + interface + " to -> " + new_mac)
# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig ",interface,"hw","ether",new_mac])
subprocess.call(["ifconfig ",interface,"up"])
