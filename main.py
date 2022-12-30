import subprocess
subprocess.call("ifconfig ens160 down", shell=True)
subprocess.call("ifconfig ens160 hw ether 11:22:33:44:55", shell=True)
subprocess.call("ifconfig ens160 up", shell=True)