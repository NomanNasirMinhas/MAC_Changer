# MAC Spoofer
### This is a very simple Network Interface MAC spoofer for Linux based operating Systems.
## Usage
### In order to use the MAC Spoofer follow below steps
Install "pyfiglet" package if not yet installed
    
    pipe install pyfiglet
then

    git clone https://github.com/NomanNasirMinhas/MAC_Spoofer.git
    cd MAC_Spoofer
If you want to stop the interface before spoofing its MAC

    python3 mac_spoof.py -i INTERFACE_NAME -m NEW_MAC_ADDRESS -c

If you want spoof MAC without stopping the interface

    python3 mac_spoof.py -i INTERFACE_NAME -m NEW_MAC_ADDRESS