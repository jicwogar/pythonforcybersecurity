#Import Platform an os modules
import platform
import os

# assign Ip addess
ip = "127.0.0.1"
#Find the current os
current_os = platform.system().lower()
#craft ping command according to os
if current_os =="windows":
    ping_cmd = "fping -n 1 -w 2 {ip} > null"
else:
    ping_cmd = "fping -c -1 -w {ip} >/dev/null 2>&1"
exit_code = os.system(ping_cmd)
print(exit_code)
    
