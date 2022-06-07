import platform
import os


def ping_address(ip_address):
    #find current os
    current_os = platform.system().lower()
    #craft ping command based on os
    if current_os == "windows":
        ping_cmd = f"ping -n 1 -w 2 {ip_address} > nul"
    else:
        ping_cmd = f"ping -c 1 -w 2 {ip_address} > /dev/null 2>&1"
    exit_code = os.system(ping_cmd)
    return exit_code

for octet in range(256):
    # Assign ip address
    ip = "127.0.0.{0}".format(octet + 1)
    # call function
    exit_code = ping_address(ip)
    #print eit code to screen
    print("{0}: {1}".format(ip,exit_code))
