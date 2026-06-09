---
vessel: Ennor
doc_id: "5.4"
title: "Ominsense Ulysses MicroS+ thermal camera"
category: "Topside"
source_pdf: "5.4 Omnisense Ulysses-Micro-Quick-Start-Guide.pdf"
extraction_method: native
page_count: 4
converted: "2026-02-24"
---

# Ominsense Ulysses MicroS+ thermal camera

**Vessel:** Ennor | **Section:** 5.4 | **Category:** Topside
**Source PDF:** 5.4 Omnisense Ulysses-Micro-Quick-Start-Guide.pdf | **Pages:** 4 | **Extraction:** native

---

IMPORTANT:  The Quick Start Guide is part of the complete documentation for your thermal
camera. Please visit Omnisense Systems website to download the complete and latest user
guide for your product.
omnisense-systems.com
Omnisense Systems USA Inc
1881 West State Road 84, Bldg. 1 Unit 102
Fort Lauderdale, Florida, 33315, United States
T: +1 (954) 316-6230
E: enquiries@omnisense-systems.com
Part No: ULS-M384U, ULS-M384S, ULS-M640S
Ver 2.1 Date: Oct 27, 2023
Quick Start Guide

System Layout and Connections
Before you commenced the installation, it is important to produce a schematic
diagram. The diagram will be handy for any future maintenance or upgrades to
the system. The diagram should include the location of all components, cable
types, routing and length.
This is the layout plan of how your Ulysses Micro thermal camera system will be
set-up.
Joystick
Controller
Camera Turret
Junction Box
12V or 24V DC
power supply
NMEA 0183 data
source (if required)
Begin by selecting an appropriate location to install the camera. It should ideally
be installed at a good vantage point with emphasis on forward view.
Using the Mounting Template decal provided, mark and drill all the holes required
for  Camera Turret installation at the selected location.
Prepare the camera for installation by installing the provided 4 x m6 studs into the
base of the camera (Fig.2). Be sure not to over tighten these studs as doing so
may severely damage the camera.
Pass the camera harness cable through the center hole and route it to the
junction box location. Connect the cable harness to mating connector under the
camera base.
Note the orientation of the Camera Turret indicated by the “forward arrow” under
the camera and install the camera with it’s base facing toward the bow of your
vessel. Secure the camera with supplied hardware as indicated in Fig. 2.
Pro Tip: Put a temporary mark of the front side of the base, to indicate the forward
side to aid installation.
Camera can be installed on a riser in the same way.
Mounting the Camera Turret
Ensure depth of screws do not penetrate more than 13mm from the
base. Failure to observe this may severely damage the product
and is not covered under the warranty.
Fig. 1
Fig. 2
Analog monitor
Multifunction Display (MFD)

Mounting the Joystick Controller
Identify the desired location of the Joystick Controller.
Use the supplied mounting template decal and create
the necessary openings as indicated on the template.
The Joystick controller has a ﬂush mounting ﬂange
that will sit on a ﬂat surface and sealed with a gasket.
Secure it from under the panel with supplied
hardware as indicated in Fig. 3. The supplied nut can
be fastened with ﬁngers and then tighten with an
appropriate hand tool.
Note:
Please measure the thickness of your
mounting surface and purchase the
required length of these screws if the
supplied studs are not used.
Fig. 3
Fig. 4
Joystick Controller Functions
Joystick
Menu navigation and
camera control
Enter
Conﬁrm selection
Menu
Display menu options
Zoom
Adjust zoom
Sensor Select
Toggle between
cameras
Function
Programmable key
Color Palette
Select color mode
Radar Track
Activate tracking functions
Power/Standby
Wake, park, or return turret
to home position
All essential functionalities are integrated and accessed via the 8 buttons and
joystick (Fig. 4).
Press any of the button once to activate the menu items on the screen. Use the
joystick to select and cycle-through the options available.
If you are unable to connect to the camera due to the a diﬀerent set of IP
address, follow this step to conﬁgure the camera for Windows user.
1. Go to Settings, then click on Network & Internet.
2. Right-click on your Ethernet Network that is connected to the Junction Box and
click on Properties (Fig. 7).
Change IP Settings
3. On the properties screen, select Internet
Protocol Version 4 (TCP/IPv4) and click on
Properties (Fig. 8).
4. On IPv4 properties screen, select Use the
following IP Address option (Fig. 9).
5. Enter the following IP address: 172.16.6.xxx (any
number). As you can see in above image (Fig. 9),
the ﬁrst 3 number sets (172.16.6) in IP Address
ﬁeld need to be the same as the Junction Box IP
address. You can only change the last number
set with any number from 1 to 254. Click in the
Subnet Mask area, which should auto-complete.
Click OK (Fig. 9).
Fig. 8
Fig. 9
Fig. 7
6. Launch your web browser and enter the following address http://172.16.6.225/
and login with the following:

Username: admin

Password: 12345
Full control of the camera can be accessed through the Web Interface. You can
conﬁgure the IP address to connect to your MFD from the Settings menu.

1. Power cable - Connect the power cable provided to the [Power] port in the
Junction Box and to a DC power source on your vessel. It is recommended that
you use either a 12V or 24V DC power. The power cable consists of Black for (-)
negative, White for (+) wire. Please ensure that the correct polarity is inserted
into the right terminal (Fig. 6).
2. AV Analog cable - Connect the AV Analog cable to the Junction Box [AV] port
and the other end to your analog monitor (if required).
3. Camera harness - Connect the end of the camera harness to the ethernet port
in the Junction Box marked [Camera].
4. Controller cable - Connect the ethernet cable to the Junction Box [Control-
ler/MFD] port (4) and the other end the Joystick Controller.
5. MFD cable - Connect the ethernet cable to the Junction Box [Controller/MFD]
port (5) on and the other end to your MFD.
6. NMEA 0183 socket - For devices that require input from NMEA 0183 devices,
connect the NMEA 0183 data source to the [NMEA] socket in the Junction Box
using 24-20 AWG cables and the output from the NMEA device to the Rx pins
in the Junction Box.
Connecting the Cables
Junction Box
The Junction Box is the primary means to provide power to the Camera and
Joystick Controller. It also serves as a hub for data transmission and interfacing
point to other connected network devices.
Fig. 6
Fig. 5
1.  Power
2. AV
3. Camera
4. Controller/MFD
5. Controller/MFD
6. NMEA
1
2
3
4
6
5
You can choose to display the video output of your Ulysses Micro to a supported
MFD via IP (ethernet), an analog monitor via AV analog cable and/or a laptop
computer (via web browser). Instructions are as follows:
1. Connecting to a MFD:
Connect the ethernet cable from the [Controller/MFD] port in the Junction Box to a
compatible MFD. The camera will work with Garmin MFD with OneHelm. If you are
using a Garmin’s MFD, you should see a Ulysses Micro icon displayed on the
‘OneHelm’ page after powering up both the MFD and camera system. Launch the
Ulysses Micro icon to use the camera.
If you are using a Furuno or Navico’s MFD, you will need to conﬁgure the camera
system to communicate in the correct network environment by using a web
browser or an analog monitor/Joystick Controller. Refer to setup section on the
next page.
2. Connecting to a PC:
Connect an Ethernet cable from your PC to Ethernet port on the Junction Box
marked [Controller/MFD]. On your web browser, enter the default IP address as
indicated at the base of the turret and login with the following:

Username: admin

Password: 12345
Full control of the camera can now be accessed through the Web browser.
3. Connecting to an analog monitor:
Connect the AV analog cable from the [AV] port in the Junction Box to your analog
monitor. The display will appear on the screen. Use the Joystick Controller to
control the camera.
Connecting to your Display via Ethernet (Options)
