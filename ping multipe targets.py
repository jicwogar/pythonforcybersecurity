import platform
import os


for octet in range(256):
    # Assign ip address
    ip = "127.0.0.{0}".format(octet + 1)
    #find the current os
    current_os = platform.system().lower()
    #craft pind command based on os
    if current_os == "windows":
        ping_cmd = f"ping -n 1 -w 2 {ip} > null"
    else:
        ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
    #run command and capture exit code
    exit_code = os.system(ping_cmd)
    print("{0}: {1}".format(ip,exit_code))


