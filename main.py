import usb.core
import usb.util
import time

# find our device by VID and PID pair
dev = usb.core.find(idVendor=0xcafe, idProduct=0x4014)

# was it found?
if dev is None:
    raise ValueError('Device not found')

#selecting the first configuration
cfg = dev[0]

#selecting the second interface
intf=cfg[(1,0)]

#selecting the IN and OUT endpoints
ep_in = intf[1]
ep_out = intf[0]

#Sending commands to the devcice 
while True:
    ep_out.write("LED_ON", 64)
    time.sleep(1)
    ep_out.write("LED_OFF", 64)
    time.sleep(1)
