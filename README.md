# Pyusb-RP-PICO
This project will show you how to make a composite USB device with 1 HID keyboard interface and 1 custom interface on raspberry pi pico (RP2040).

## Getting Started
This is an example of how you may give instructions on setting up your project locally.

### Prerequisites
You must have Raspberry pi pico sdk setup and pyusb library installed on your machine.

[Raspberry pi C/C++ SDK](https://www.raspberrypi.com/documentation/microcontrollers/c_sdk.html)
[pyusb](https://github.com/pyusb/pyusb)

### Building the demo
```
git clone https://github.com/shekhuverma/Pyusb-RP-PICO.git
cd Pyusb-RP-PICO/build
cmake ..
make -j4
```

now you will have a Pyusb-RP-PICO.uf2 file in the build folder. You upload this file to your pi pico and run _host.py_

You will be able to see On Board LED blinking on the pico
When 
