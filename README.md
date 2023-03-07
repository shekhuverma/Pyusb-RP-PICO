# Pyusb-RP-PICO
This project will show you how to make a composite USB device with 1 HID keyboard interface and 1 custom interface on raspberry pi pico (RP2040).

You can read more at my blog [here](https://shekharverma.com/posts/pysusb_and_rp2040/)
## Getting Started

### Prerequisites
You must have Raspberry pi pico C/C++ sdk setup and pyusb library installed on your machine. Follow the instructions in the links given below.

[Raspberry pi C/C++ SDK](https://www.raspberrypi.com/documentation/microcontrollers/c_sdk.html)

[pyusb](https://github.com/pyusb/pyusb)

### Building the demo
```
git clone https://github.com/shekhuverma/Pyusb-RP-PICO.git
cd Pyusb-RP-PICO/build
cmake ..
make -j4
```
## Usage
Now you will have a Pyusb-RP-PICO.uf2 file in the build folder. You upload this file to your pi pico and run _host.py_

You will be able to see On Board LED blinking on the pico and when you will press the button on pico it will act as "a" key being pressed on your keyboard (You can see this by opening any text editor or browser)

## Roadmap
- [ ] Add Micropython example
