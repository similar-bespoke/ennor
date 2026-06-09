---
vessel: Ennor
title: "CZone Contact 6 PLUS User and Installation Manual v2.1"
category: "Energy Management"
source_pdf: "library_czone/CZone Contact 6 PLUS User and Installation Manual v2.1.pdf"
extraction_method: native
page_count: 19
converted: "2026-02-24"
---

# CZone Contact 6 PLUS User and Installation Manual v2.1

**Vessel:** Ennor | **Category:** Energy Management
**Source PDF:** library_czone/CZone Contact 6 PLUS User and Installation Manual v2.1.pdf | **Pages:** 19 | **Extraction:** native

---

## Page 1

Contact 6 PLUS
User & Installation Manual
V2.1

## Page 2

EN / CZone® Contact 6 PLUS User & Installation Manual
2



Copyright
This document is copyright 2018 under the Creative Commons agreement. Rights are granted to research and
reproduce elements of this document for non-commercial purposes on the condition that BEP Marine is credited as the
source. Electronic re-distribution of the document in any format is restricted, to maintain quality and version control.
Important
BEP Marine strives to ensure all information is correct at the time of printing. However, the company reserves the right
to change without notice any features and specifications of either its products or associated documentation.
Translations: In the event that there is a difference between a translation of this manual and the English version, the
English version should be considered the official version.
It is the owner’s sole responsibility to install and operate the device in a manner that will not cause accidents, personal
injury or property damage.


Use of This Manual
Copyright © 2018 BEP Marine LTD. All rights reserved.
Reproduction, transfer, distribution or storage of part or all of
the contents in this document in any form without the prior written permission of BEP Marine is prohibited.
This manual
serves as a guideline for the safe and effective operation, maintenance and possible correction of minor malfunctions
of the Contact 6 PLUS.

## Page 3

3
EN / CZone® Contact 6 PLUS User & Installation Manual


TABLE OF CONTENTS


1
OVERVIEW
4

Description
4

Parts Included
4

Features
4

Hardware Overview
5
2
DESIGN
7
3
INSTALLATION
7

Things You Need
7

Environment
7

Mounting
8

Connections
9

Inserting Fuses
10

Mechanical Bypass
10

Network Configuration
11
Standalone Installation
11
Networked Installation
11

Fit the Cover
12

Initial Power Up
12
Standalone Installation
12
Networked Installation
12

System Diagram Examples
13

Bilge Sense Example
15
4
ORDERING INFORMATION
16
5
SPECIFICATIONS
16

Technical Specifications
16

Dimensions
17
6
COMPLIANCE
18

## Page 4

EN / CZone® Contact 6 PLUS User & Installation Manual
4


1 OVERVIEW

DESCRIPTION
The Contact 6 PLUS is a 6-channel output module utilizing CZone’s proven solid state switching technology. Designed
to be installed with a NMEA2000 Network or as a standalone system with a CZone Smart Harness and Waterproof
Keypad. When installed with a CZone Waterproof Keypad the Contact 6 PLUS will work out of the box with a pre-
installed factory configuration. To install the Contact 6 PLUS with other CZone modules, or to configure advanced
functionality like timers and single button dimming you will need to use the CZone Configuration Tool which is available
for download at www.downloads.czone.net.

PARTS INCLUDED



1.
Contact 6 PLUS interface
2.
Cable connector
3.
Cable gland
4.
Front cover

FEATURES
•
Entry level digital switching module for Marine and RV applications
•
6 x 15A output channels
•
Plug-and-play out-of-the box functionality
•
PWM circuit dimming and control on all channels
•
Stand-alone or network with other CZone products
•
Compatible with CZone integrated Multi-Function Displays (MFDs)
•
Uses proven CZone technology
•
Full mechanical fuse protection with channel bypass on all circuits
•
Blown fuse detection and system warnings
•
Status LEDs with fault codes for all channels
•
IPx5 ingress protection
•
NMEA2000 compliant
•
Configurable bilge pump running detection on output channel 6 (see 3.11 for details)
1
2
3
4

## Page 5

5
EN / CZone® Contact 6 PLUS User & Installation Manual



HARDWARE OVERVIEW

1.
Channel Status LED Indicators
2.
Network Status LED Indicator
3.
Mounting Holes
4.
Power Supply M6 Stud
5.
Output Connector
6.
ATC Fuse Sockets
7.
Dipswitch
8.
Network / NMEA2000 Micro C Connector
9.
Cable Gland
6
3
4
5
7
8
9
2
1

## Page 6

EN / CZone® Contact 6 PLUS User & Installation Manual
6



Channel Status LED Indicators
Colour
Description
Extinguished
Channel Off
Green Solid On
Channel On
1 Green Flash
Module Not Configured
2 Green Flash
Configuration Conflict
3 Green Flash
DIP Switch Conflict
4 Green Flash
Memory Failure
5 Green Flash
No Modules Detected
7 Green Flash
Fuse Blown
9 Green Flash
Missing Commander

Network Status LED Indicator
Colour
Description
Extinguished
Network Power Disconnected
Green
Network Power Connected
Red Flash
Network Traffic

## Page 7

7
EN / CZone® Contact 6 PLUS User & Installation Manual


2 DESIGN
•
Make a list of all outputs to be wired to the Contact 6 PLUS and assign each of them to one of the 6 channels.
•
Ensure all cables are appropriately rated for each assigned load.
•
Output connector accepts cable gauges 24AWG – 8AWG (0.5 - 6mm).
•
Ensure power supply cable to the Contact 6 PLUS is appropriately rated for the maximum continuous current
of all loads and is fused appropriately to protect the cable.
•
Ensure continuous current draw of each connected load does not exceed maximum channel rating of 15A.
•
Ensure the maximum continuous current of all loads does not exceed the 60A total module current.
•
Install the appropriately rated fuses for each channel.
•
Decide if you will add the Contact 6 PLUS to a NMEA2000 Network or install as a standalone system with the
CZone Smart Harness.
•
Loads exceeding 15A will require paralleling 2 channels together or an external relay.

3 INSTALLATION

THINGS YOU NEED
•
Electrical tools
•
Wiring and fuses
•
Contact 6 PLUS module
•
CZone Waterproof Keypad (if required)
•
CZone Smart Harness or NMEA2000 network cables
•
4 x 8G or 10G (4mm or 5mm) self-tapping screws or bolts for mounting the Contact 6 PLUS

ENVIRONMENT
Obey the following stipulations during installation:
•
Ensure the Contact 6 PLUS is located in an easily accessible location and indicator LED’s are visible.
•
Ensure there is enough clearance above the Contact 6 PLUS to allow the cover to be removed.
•
Ensure there is at least 10mm clearance around the sides and top of the Contact 6 PLUS.
•
Ensure the Contact 6 PLUS is mounted on a vertical flat surface.
•
Ensure there is sufficient space for the wires to exit the product.

## Page 8

EN / CZone® Contact 6 PLUS User & Installation Manual
8



MOUNTING


1. Mount the Contact 6 PLUS on a vertical surface with the cables exiting downwards.
2. Allow enough space below cable grommet for wiring bend radius.
o
Note - Cable radius determined by wiring manufacturer.
3. Fasten the Contact 6 PLUS by using 4 x 8G or 10G (4mm or 5mm) self-tapping screws or bolts (not supplied).



IMPORTANT - The Contact 6 PLUS must be mounted within 30 degrees from the vertical position to ensure
water correctly runs away from the product if mounted in a location where water can contact the product.

## Page 9

9
EN / CZone® Contact 6 PLUS User & Installation Manual



CONNECTIONS
The Contact 6 PLUS has a convenient output connector that requires no crimping tools and accepts cables from 24AWG
to 8AWG (0.5 - 6mm). The unit has no power key and will turn on when power is applied to the network. The module
will continue to draw power even when it is not in operation. It is recommended that a battery isolator switch is installed
for when the system is not in use.

1. Feed output wires through cable grommet
2. Strip and insert each wire into the connector ensuring the correctly rated wire is used for each load and tighten
screws to 4.43 in/lbs (0.5NM).
3. Insert plug firmly into module and tighten 2x retaining screws.
4. Connect CZone Smart Harness to network port. If not using the CZone Smart Harness, connect a NMEA2000
drop cable from the NMEA2000 backbone (do not power up network yet).
5. Connect the appropriate size power supply cable to the M6 positive stud and tighten to 35 in/lbs (4NM), ensuring
washers are installed as per diagram.






IMPORTANT - The positive cable must be sufficient size to carry the maximum current of all loads connected
to the Contact 6 PLUS. It is recommended to have a fuse/circuit breaker rated to protect the cable.
1
4
3
2
5

## Page 10

EN / CZone® Contact 6 PLUS User & Installation Manual
10



INSERTING FUSES
The Contact 6 PLUS provides ignition protected circuit protection for each individual channel via standard ATC fuses
(not supplied). Appropriately rated fuses should be selected and installed for each channel to protect the load and the
wiring for each circuit.


Fuses In Normal Operation
1. Select the appropriate fuse rating for each individual circuit.
2. Insert the correctly rated fuses into the NORMAL (bottom) position of all circuits.
3. The ATC fuse should be rated to protect the connected load and the wiring from the Contact 6 PLUS to the
load and also the ground wire.

MECHANICAL BYPASS
The Contact 6 PLUS includes a mechanical bypass feature for redundancy purposes. Moving any fuse to the BYPASS
(top) position will supply constant battery power to that output. See below diagram showing circuit #3 in the BYPASS
position.


Fuse in Bypass Position



WARNING – Ensure area is free of explosive gasses before removing/replacing fuses or placing fuses in the
bypass position as sparks may occur.

## Page 11

11
EN / CZone® Contact 6 PLUS User & Installation Manual



NETWORK CONFIGURATION
CZone modules communicate with each other over a NMEA2000 CAN BUS network. Each module needs a unique
address, this is achieved by carefully setting the dipswitch on each module with a small screwdriver. The dipswitch on
each module must match the setting in the CZone configuration.
The Contact 6 PLUS comes pre-loaded with a factory configuration to provide plug-and-play functionality when installed
with a CZone Waterproof Keypad. The factory configuration provides basic switching functionality with one-to-one switch
input to channel output mapping.
Standalone Installation
•
Set the dipswitch on the Contact 6 PLUS and Waterproof Keypad to match the below table.
•
Connect the Contact 6 PLUS to the Waterproof Keypad with the CZone Smart Harness or NMEA2000 network.
•
Change any desired circuits to have momentary functionality instead of latching (see Initial Power up section).
Networked Installation
•
To install the Contact 6 PLUS with other networked CZone modules, or to achieve advanced functionality such
as timers, load shedding or one touch Modes of operation, a custom configuration needs to be installed.
•
Set the dipswitch on the Contact 6 PLUS to match the configuration file.
•
All other CZone modules must have the dipswitch set to same as the configuration file.

The example below shows a dipswitch setting of 01101100 where 0 = OFF and 1 = ON

Setting Dipswitch
IMPORTANT - Each CZone device must have a unique dipswitch number and the dipswitch of the device
must match the dipswitch set in the configuration file.
1. Factory configuration table
Module
Dipswitch
Contact 6 PLUS
10000000
Portrait Waterproof Keypad
00000001
Landscape Waterproof Keypad
00000011
Display Interface
11101000

NOTE - If you have a compatible MFD or Display Interface, the factory configuration will work and populate
circuits 1 - 6 on the display for basic on/off control.

## Page 12

EN / CZone® Contact 6 PLUS User & Installation Manual
12



FIT THE COVER

Cover Installed
1. Slide the cable gland up the output wires ensuring it is correctly seated.
2. Firmly push the top cover on to the Contact 6 PLUS until you hear it click into pace on each side.
3. Ensure the cable gland is still correctly in place.
4. Install circuit labels if you have purchased a label sheet.
WARNING!  The Contact 6 PLUS is only ignition protected with the cover correctly installed.

INITIAL POWER UP
Standalone Installation
1. Power up the system.
2. Check that the Network Status LED lights up.
3. Turn the switch/circuit breaker on supplying power to the input stud (if fitted), system will flash all outputs for a
short time while booting.
4. To toggle a circuit to momentary switching, press and hold the power button and the button for that circuit
together on the CZone Waterproof Keypad for 5 seconds.
5. Test all circuits for ON/OFF functionality.
6. Check the circuit status LED’s for each individual circuit. Refer to LED codes to diagnose any faults which
need to be rectified.
Networked Installation
1. Power up the NMEA2000 Network, system will flash all outputs for a short time while booting.
2. Check that the Network Status LED lights up. It may also be flashing if other devices are on the network and
transmitting data.
3. Turn the switch/circuit breaker on supplying power to the input stud (if fitted).
4. Check the software version on the Contact 6 PLUS with the CZone Configuration Tool and update if
necessary.
5. Write the configuration file to the network (Refer to the CZone Configuration Tool Instructions for details on
how to write a CZone configuration file).
6. Test all outputs for correctly configured functionality.
7. Check the circuit status LED’s for each individual circuit. Refer to LED codes to diagnose any faults which
need to be rectified.

## Page 13

13
EN / CZone® Contact 6 PLUS User & Installation Manual


 SYSTEM DIAGRAM EXAMPLES

Basic System Diagram



Basic System Diagram with Extra Display

## Page 14

EN / CZone® Contact 6 PLUS User & Installation Manual
14



Advanced NMEA2000 System Diagram

## Page 15

15
EN / CZone® Contact 6 PLUS User & Installation Manual


 BILGE SENSE EXAMPLE
The Contact 6 PLUS B/S (Part No. 80-911-0161-00, 80-911-0161-01) is equipped with bilge pump running detection,
available only on output channel 6. If bilge detection is required, ensure a separate feed from the bilge pump is wired to
channel 6 and the channel’s ATC fuse is removed (otherwise back-feeding can occur).  Also ensure an appropriate
blocking diode is installed in the manual control circuit, which can be wired to any channel from 1 to 5.
For bilge sensing operation, the module requires an additional negative connection. The negative connection is located
to the right of the main connector on the base of the module and is only necessary where bilge sensing is required. The
negative connection should connect to the vessel’s main negative bus bar, and connection to the module is made with
the appropriately sized 6.4mm insulated female disconnect terminal.


Bilge sensing is configured in the CZone Configuration Tool by enabling ‘External Systems-on Alarm’ on the bilge pump
load (channel 6), CZone will activate a ‘Systems On’ alarm if the channel is off and reverse voltage is detected on the
output i.e., bilge pumps that have a direct feed from the battery through a float switch. The ‘External Systems-On Circuit
Status’ box should be ticked if systems on feedback is also required on any switches configured to control the load
including displays and any CZone connected digital switches.



Main
Fuse
12/24V
BATTERY
NMEA2000
Negative
Bus Bar
Batt Isolator
Bilge Pump
24hr Fuse
Bilge Pump
Float Switch
Bilge Pump
Bilge Sense Negative,
6.4mm Disconnect
Terminal
Manual Control
Sense
Sense
Man Control
Blocking
Diode
Sense Circuit (CH6)
Fuse Removed

## Page 16

EN / CZone® Contact 6 PLUS User & Installation Manual
16


4 ORDERING INFORMATION
Part Numbers and Accessories
Part Number
Description
80-911-0161-00
CZONE CONTACT 6 PLUS BILGE SENSE WITH CONNECTOR AND SEAL
80-911-0161-01
CZONE CONTACT 6 PLUS BILGE SENSE INTERFACE ONLY
80-911-0160-00
CZONE CONTACT 6 PLUS WITH CONNECTOR AND SEAL
80-911-0160-01
CZONE CONTACT 6 PLUS INTERFACE ONLY
80-911-0179-00
CZONE CONTACT 6 PLUS CONNECTOR & SEAL KIT
80-911-0171-00
CZONE 2 MODULE SMART HARNESS
80-911-0172-00
CZONE 3 MODULE SMART HARNESS
80-911-0162-00
CZONE WATERPROOF KEYPAD (LANDSCAPE)
80-911-0163-00
CZONE WATERPROOF KEYPAD (PORTRAIT)


5 SPECIFICATIONS

TECHNICAL SPECIFICATIONS
Circuit protection
ATC Fuse with Blown Fuse Alarms
NMEA2000 connectivity
1 x CAN Micro-C port
Output wire range
0.5 - 6mm (24AWG – 8AWG)
Output channels
6 x 15A 12/24V
Maximum current
60A Total Module Current
Dimming
All channels, PWM @100Hz
Power supply
M6 (1/4") Positive Terminal (9-32V)
Network Supply voltage
9-16V via NMEA2000
Circuit bypass
Mechanical Fuse Bypass on all Channels
Ingress protection
IPx5 (mounted vertical on bulkhead and flat)
Compliance
CE, ABYC, NMEA, ISO8846/SAEJ1171 Ignition Protected
Power consumption max
75mA
Power consumption standby
0.3mA
Warranty period
2 years
Operating temperature range
-15C to +55C (-5F to +131F)
Storage temperature range
-40C to +85C (-40F to +185F)
Dimensions W x H x D
202.5 x 128.5 x 45mm (7.97 x 5.06 x 1.77”)
Weight
600g (1.32lbs)

## Page 17

17
EN / CZone® Contact 6 PLUS User & Installation Manual



DIMENSIONS

## Page 18

EN / CZone® Contact 6 PLUS User & Installation Manual
18


6 COMPLIANCE

## Page 19

19
EN / CZone® Contact 6 PLUS User & Installation Manual
