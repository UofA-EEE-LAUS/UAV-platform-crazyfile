# Use Guide
============

author: Zhihan Xu

* This is the user guide for changing the firmware to achieve certain autonomous functions.

## Dependencies

You'll need to use either the [Crazyflie VM](https://wiki.bitcraze.io/projects:virtualmachine:index) or
install some ARM toolchain.

### Install a toolchain

#### OS X
```bash
brew tap PX4/homebrew-px4
brew install gcc-arm-none-eabi
```
#### Windows

The GCC ARM Embedded toolchain for Windows is available at [launchpad.net](https://launchpad.net/gcc-arm-embedded/+download). Download the zip archive rather than the executable installer. There are a few different systems for running UNIX-style shells and build systems on Windows; the instructions below are for [Cygwin](https://www.cygwin.com/).

Install Cygwin with [setup-x86_64.exe](https://www.cygwin.com/setup-x86_64.exe). Use the standard `C:\cygwin64` installation directory and install at least the `make` and `git` packages.

Download the latest `gcc-arm-none-eabi-*-win32.zip` archive from [launchpad.net](https://launchpad.net/gcc-arm-embedded/+download). Create the directory `C:\cygwin64\opt\gcc-arm-none-eabi` and extract the contents of the zip file to it.

Launch a Cygwin terminal and run the following to append to your `~/.bashrc` file:
```bash
echo '[[ $PATH == */opt/gcc-arm-none-eabi/bin* ]] || export PATH=/opt/gcc-arm-none-eabi/bin:$PATH' >>~/.bashrc
source ~/.bashrc
```

Verify the toolchain installation with `arm-none-eabi-gcc --version`

### Cloning

This repository uses git submodules. Clone with the `--recursive` flag

```bash
git clone --recursive https://github.com/bitcraze/crazyflie-firmware.git
```

If you already have cloned the repo without the `--recursive` option, you need to
get the submodules manually

```bash
cd crazyflie-firmware
git submodule init
git submodule update
```

## Compiling

### Crazyflie 2.X

This is the default build so just running ```make``` is enough

### config.mk
To create custom build options create a file called `config.mk` in the `tools/make/`
folder and fill it with options. E.g.
```
PLATFORM=CF2
DEBUG=1
CLOAD=0
```
More information can be found on the
[Bitcraze wiki](http://wiki.bitcraze.io/projects:crazyflie2:index) and later examples

```
# Make targets:
```
all        : Shortcut for build
compile    : Compile cflie.hex. WARNING: Do NOT update version.c
build      : Update version.c and compile cflie.elf/hex
clean_o    : Clean only the Objects files, keep the executables (ie .elf, .hex)
clean      : Clean every compiled files
mrproper   : Clean every compiled files and the classical editors backup files

cload      : If the crazyflie-clients-python is placed on the same directory level and
             the Crazyradio/Crazyradio PA is inserted it will try to flash the firmware
             using the wireless bootloader.
flash      : Flash .elf using OpenOCD
halt       : Halt the target using OpenOCD
reset      : Reset the target using OpenOCD
openocd    : Launch OpenOCD
```

# Unit testing

## Running all unit tests

With the environment set up locally

        make unit
```

# examples

## sequence.c

### Function Describtion
This funciton has the samilar function as the flowsequenceSync.py in python library. The crazyflie will start to fly after 3 seconds the power button is pressed.

### writing the driver
This function is implemented as a deck. 
Deck drivers are in the deck/driver/src folder. Put this file in the deck/driver/src folder

### Adding the driver to the build
Add this to the Makefile, after the line '# Decks':
```
PROJ_OBJ +=

```
### Enabling the driver
Decks can have a memory that contains its name. In our case the sequence driver would be initialised only when a deck identified as “bcSequence” is installed on the Crazyflie. For development purpose it is possible to force enabling a deck driver with a compile flag. To do so create the file tools/make/config.mk with the content:
```
CFLAGS += -DDECK_FORCE=myHello
 
DEBUG=1
```
DEBUG=1 allows to get more information from the Crazyflie console when it starts. Debug should not be enabled if you intend to fly the Crazyflie out of the lab (it disables the watchdog).

### Note
Each time you modify config.mk you should recompile the full firmware by cleaning up the build folder with 'make clean'

### Compile, flash and run

Now the last step is to compile and flash your new firmware. Launch the following commands in a shell:
```
crazyflie-firmware$ make
crazyflie-firmware$ make cload
```



## push.c

Read more information in push folder

## Stop-at-obsticle
The function works during all the running time, which was written in high-level-command. 

In order to achieve the function, you could follow the steps in push folder read.me file. In addition to that, you need to use the push.c in stop-at-obsticle folder instead of the one in push folder. Replace the crtp_commander_high_level.c and crtp_commander_high_level.h files with the original ones in the crazyflie-firmware/src/modules/src and crazyflie-firmware/src/modules/interface.

simple.py is an example to control the crazyflie to move forward for 1 meter, you need crazyflie python library to use this script. You could follow the steps in [formation-control](https://github.com/UofA-EEE-LAUS/UAV-platform-crazyfile/tree/master/formation-control) folder read.me file.
