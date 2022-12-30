import subprocess

interface = input("Enter Interface Name: ")
new_mac = input("Enter New MAC Address: ")
print("[+] Changing MAC Address of interface of " + interface + " to -> " + new_mac)
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
