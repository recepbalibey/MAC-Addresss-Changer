import subprocess
import optparse
import re

print("------------------------------")
print("MAC changer is started!")
print("------------------------------")

# This is the input from the user in terminal. 
# Example: python macchanger.py -i eth0 -m 11:22:33:44:55:66
# User can provide -i or --interface, same for -m or --mac
def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface",dest="interface",help="Interface to change!")
    parse_object.add_option("-m", "--mac",dest="mac_address",help="Provide the MAC address you wish to change! Example run in terminal: python macchanger.py -i eth0 -m 00:22:33:44:33:66")
    #Parse object is producing a tuple
    return parse_object.parse_args()
    
 
# Normally in Linux terminal
# 1. Check the interface name >> ifconfig
# 2. Deactivete the interface >> ifconfig eth0 down
# 3. Change the mac >> ifconfig eth0 hw ether 00:11:22:33:44:55
# 4. Activete the interface >> ifconfig eth0 up


# This function returns the current MAC address of the running machine.
def current_mac_address(interface):
    current_ifconfig = subprocess.check_output(["ifconfig",interface])
    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(current_ifconfig))
    if current_mac:
        return current_mac.group(0)
    else:
        return None

# This function changes the current MAC address of the running machine.
def change_mac_address(user_interface, user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])
  
# This function controls the changed MAC address of the running machine.  
def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None


(user_input, arguments) = get_user_input()  

print("Your current MAC address:", end='')
print(current_mac_address(user_input.interface))
print("Selected interface:", end='')
print(user_input.interface)
print("------------------------------")

change_mac_address(user_input.interface, user_input.mac_address)    

finalized_mac = control_new_mac(str(user_input.interface))

if finalized_mac == user_input.mac_address:
    print("Your new MAC address:", end='')
    print(finalized_mac)
    print("------------------------------")
    print("MAC address is changed.")
else:
    print("Something went wrong!")
        
