import nmap # import nmap.py module
nm = nmap.PortScanner() # instantiate nmap.PortScanner object
scan=nm.scan('127.0.0.1', '22-443') # scan host 127.0.0.1, ports from 22 to 443
nm.command_line() # get command line used for the scan : nmap -oX - -p 22-443 127.0.0.1
nm.scaninfo() # get nmap scan informations {'tcp': {'services': '22-443', 'method': 'connect'}}
nm.all_hosts() # get all hosts that were scanned
nm['127.0.0.1'].hostname() # get one hostname for host 127.0.0.1, usualy the user record
nm['127.0.0.1'].hostnames() # get list of hostnames for host 127.0.0.1 as a list of dict
# [{'name':'hostname1', 'type':'PTR'}, {'name':'hostname2', 'type':'user'}]
host_name =nm['127.0.0.1'].hostname() # get hostname for host 127.0.0.1
for i in scan:
    print(i)

