# import nessesary python modules
import nmap

# identify target address
target_address = "127.0.0.1"

# identify start and stop ports
port_start = 75
port_end = 100

# create scanner object
scanner = nmap.PortScanner()

print("scanning {0}".format(target_address) )
# loop through each port and scan
for port in range(port_start, port_end +1):
    result = scanner.scan(target_address, str(port))
    port_status = result['scan'][target_address]['tcp'][port]
    print("\tport: {0} is {1}".format(port, port_status))