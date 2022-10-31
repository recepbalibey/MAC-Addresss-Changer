# MAC-Addresss-Changer
This is the python file to change the MAC address of the running machine on Linux terminal

# What is MAC Address?
Just like each house has it's own postal address, every device connected on a network has a Media Access Control (MAC) address, that uniquely identifies it. <br />
The MAC address is a 12 digit hexadecimal number that is most often displayed with a colon or hypen separating every two digits (an octet), making it easier to read. <br />
Example: A MAC address of `2c549188c9e3` is typically displayed as `2C:54:91:88:C9:E3` or `2c-54-91-88-c9-e3`.

 [More about](https://slts.osu.edu/articles/whats-a-mac-address-and-how-do-i-find-it/)

# Usage
Run in terminal: <br />
`python macchanger.py -i interfacename -m MAC_ADDRESS` <br />
Example:`python macchanger.py -i eth0 -m 00:22:33:44:33:66` <br />

Note: Start your MAC address with 00. 
