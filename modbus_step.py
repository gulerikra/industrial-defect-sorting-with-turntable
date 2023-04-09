import time
from pyModbusTCP.client import ModbusClient


server_host="192.168.3.250"
server_port=502


plc=ModbusClient()
plc.host(server_host)
plc.port(server_port)


while True:
    if not plc.is_open(): 
        if not plc.open():
            print("unable to connect to"+server_host+":"+str(server_port))
            time.sleep(2)


    if plc.is_open():
        plc.write_multiple_coils(5,[1])
        # plc.write_multiple_coils(6,[1])

