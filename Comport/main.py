import serial,time
import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
for portString in ports:
    com = str(portString)
    comPort = com[0:4]

print(comPort)
serialPort = serial.Serial(port=comPort, baudrate=9600, timeout=2)
while True:
    inp = input("a:")
    if inp == 'A':
        serialPort.write(b'A')
    elif inp == 'B':
        serialPort.write(b'B')
