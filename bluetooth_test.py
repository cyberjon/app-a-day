from bluetooth import *





print("Scanning for near by devieces")

nearby_devices = discover_devices(lookup_names = True)



print (f"Found {len(nearby_devices)} devies" )

for  addr, name in nearby_devices:
     print (f'{addr} {name}')
     
     if name == 'Hedwig':
         
         print("Ailin home")
