---
vessel: Ennor
title: "CZone Signal Interface User & Installation Manual v2.0"
category: "Energy Management"
source_pdf: "library_czone/CZone Signal Interface User & Installation Manual v2.0.pdf"
extraction_method: native
page_count: 13
converted: "2026-02-24"
---

# CZone Signal Interface User & Installation Manual v2.0

**Vessel:** Ennor | **Category:** Energy Management
**Source PDF:** library_czone/CZone Signal Interface User & Installation Manual v2.0.pdf | **Pages:** 13 | **Extraction:** native

---

## Page 1

Signal Interface (SI)
User & Installation Manual
V2.0

## Page 2

EN / CZone® Signal Interface (SI) User & Installation Manual
2


1 Contents
2
GENERAL INFORMATION
3

Use of this manual
3

Guarantee Specifications
3

Quality
3

Validity Of This Manual
3

Liability
3

Changes To The Signal Interface (SI)
3
3
SAFETY AND INSTALLATION PRECAUTIONS
4

Warnings and Symbols
4

Use For Intended Purpose
4

Organizational Measures
4

Maintenance and Repair
4

General Safety and Installation Precautions
4
4
OVERVIEW
5

Description
5

Features
5

Component Overview
5
5
INSTALLATION
6

Guidelines
6

Connections
6

Dipswitch
7

Initial Power Up
7
6
LED FLASH CODES
8
7
LABELLING
9

Connections/LED Flash Code Label
9

Module Identification and Dipswitch label
9
8
SYSTEM WIRING EXAMPLE
10
9
DIMENSIONS
11
10
ORDERING INFORMATION
12

Module
12

Acessories and Spares
12
11
EMC RATINGS
12
12
DECLARATION OF CONFORMITY
13

## Page 3

3
EN / CZone® Signal Interface (SI) User & Installation Manual


2 GENERAL INFORMATION

USE OF THIS MANUAL
Copyright © 2019 BEP Marine. All rights reserved.
Reproduction, transfer, distribution, or storage of part or all of the
contents in this document in any form without the prior written permission of BEP Marine is prohibited.
This manual
serves as a guideline for the safe and effective operation, maintenance and possible correction of minor malfunctions
of the Signal Interface Module (SI).

This manual is valid for the following:
Description
Part number
CZONE SIGNAL INTERFACE c/w SEALS & CONN
80-911-0013-00
CZONE SIGNAL INTERFACE NO SEALS & CONN
80-911-0014-00

It is obligatory that every person who works on or with the Signal Interface is completely familiar with the contents of
this manual, and that he/she carefully follows the instructions contained herein.

Installation of, and work on the Signal Interface, may be carried out only by qualified, authorized, and trained personnel,
consistent with the locally applicable standards and taking into consideration the safety guidelines and measures. Please
keep this manual in a secure place!

GUARANTEE SPECIFICATIONS
BEP Marine guarantees that this unit has been built according to the legally applicable standards and specifications.
Should work take place which is not in accordance with the guidelines, instructions and specifications contained in this
Installation manual, then damage may occur and/or the unit may not fulfil its specifications. All these matters may mean
that the guarantee becomes invalid.

QUALITY
During their production and prior to their delivery, all our units are extensively tested and inspected. The standard
guarantee period is two years.

VALIDITY OF THIS MANUAL
All the specifications, provisions and instructions contained in this manual apply solely to standard versions of the Signal
Interface (SI) delivered by BEP Marine.

LIABILITY
BEP can accept no liability for:
•
Consequential damage due to use of the Signal Interface.  Possible errors in the manuals and the results thereof


CAREFUL! Never remove the identification label


Important technical information required for service and maintenance can be derived from the type number plate.

CHANGES TO THE SIGNAL INTERFACE (SI)
Changes to the Signal Interface may be carried out only after obtaining the written permission of BEP.

## Page 4

EN / CZone® Signal Interface (SI) User & Installation Manual
4


3 SAFETY AND INSTALLATION PRECAUTIONS

WARNINGS AND SYMBOLS
Safety instructions and warnings are marked in this manual by the following pictograms:
CAUTION
Special data, restrictions and rules with regard to preventing damage.

WARNING
A WARNING refers to possible injury to the user or significant material damage to the Signal Interface
if the user does not (carefully) follow the procedures.
A procedure, circumstance, etc, which deserves extra attention.

  USE FOR INTENDED PURPOSE
1. The Signal Interface is constructed as per the applicable safety-technical guidelines.

2. Use the Signal Interface only:

•
In technically correct conditions
•
In a closed space, protected against rain, moisture, dust and condensation
•
Observing the instructions in the installation manual
WARNING Never use the Signal Interface in locations where there is danger of gas or dust explosion
or potentially flammable products!

3. Use of the Signal Interface other than mentioned in point 2 is not considered to be consistent with the
intended purpose. BEP Marine is not liable for any damage resulting from the above.

ORGANIZATIONAL MEASURES
The user must always:
•
Have access to the user's manual and be familiar with the contents of this manual

MAINTENANCE AND REPAIR
•
Switch off supply to the system

•
Be sure that third parties cannot reverse the measures taken

•
If maintenance and repairs are required, only use original spare parts

GENERAL SAFETY AND INSTALLATION PRECAUTIONS
•
Connection and protection must be done in accordance with local standards
•
Do not work on the Signal Interface or system if it is still connected to a power source. Only allow changes
in your electrical system to
be carried out by qualified electricians

•
Check the wiring at least once a year. Defects such as loose connections, burned cables, etc. must be
corrected immediately

## Page 5

5
EN / CZone® Signal Interface (SI) User & Installation Manual


4 OVERVIEW

DESCRIPTION
The Signal Interface (SI) connects the CZone system to your external sensors, alarms and switching devices. The SI
allows intelligent, automated operation of circuits depending on the state of the input.

FEATURES
•
Accepts inputs from traditional switch types being used to control outputs.
•
Accepts inputs from switches to trigger alarm i.e., high water float switch.
•
Accepts inputs from industry standard tank senders (0-5V, 10-180 Ohm, 240-33 Ohm).
•
Accepts inputs from general voltaic or resistive signals can be used for controlling outputs or to display a
physical position i.e., show a hatch is partially open.
•
LED status indicators for each input.
•
Dimensions: WxHxD: 6-3/32"x3-29/32"x1-5/8" 156x100x42 mm     Weight: 281g
•
IPX5 water ingress protection.
•
Resistive input range 0-1000 Ohms.
•
Outputs standard NMEA2000 sentences.

COMPONENT OVERVIEW



















Component
1.
Circuit Status LED’s
2.
Network Status LED
3.
NMEA 2000 Plug
4.
Cable Gland
5.
Cover Retaining Screws
6.
Module Cover
3
4
1
2
6
5
Figure 1. Overview

## Page 6

EN / CZone® Signal Interface (SI) User & Installation Manual
6


5 Installation

GUIDELINES
•
Ensure the modules are installed vertically with the cables exiting downwards, this ensures IPX5 rating is
retained.
•
All seals and cable glands must be fitted including blanking plugs inserted in any unused positions.
•
Ensure all labels are fitted and correct













CONNECTIONS
•
Connect DC Neg to SI input 8, used as reference to ground.
•
Connect each input to SI, inputs 1-6. Input 7 is not connected.
•
Connect an NMEA2000 drop cable from the SI to the NMEA2000 backbone.
•
Ensure NMEA2000 network is properly terminated and connected to 12V power source.


Figure 3. Connections
No connection
DC Negative
Signal input 1
Signal input 2
Signal input 3
Signal input 4
Signal input 5
Signal input 6
Signal inputs:
10-180 Ohm Sender
240-33 Ohm Sender
0-5v Sender
Negative (for switching purposes)
Positive (0-32v, for switching purposes )
NMEA2000 Micro C
Mount Vertically
Cable Exit
Figure 2. Mounting

## Page 7

7
EN / CZone® Signal Interface (SI) User & Installation Manual



DIPSWITCH
•
Using a small screwdriver, carefully set the dipswitch to required setting.
•
The dipswitch number must be unique for all modules on the CZone network and must match the dipswitch
setting in the configuration to function correctly.





The example shows a dipswitch number of 10000000 where 0 = Off and 1 = On.

INITIAL POWER UP
1. Check all plugs are securely seated and connections are tight.
2. Power up the NMEA2000 network.
3. Check that the NMEA2000 Network LED lights up. It may also be flashing if other devices are present and
transmitting data.
4. Check that the Power indicator LED is green.
5. Check the circuit’s status LEDs for each individual circuit. Refer to LED codes to diagnose any faults which
need to be rectified.
6. Check the software version on the Signal Interface with the CZone Configuration Tool and update if
necessary.
7. Refer to the CZone Configuration Tool Instructions for details on how to configure and calibrate the Signal
Interface inputs.
8. Write configuration file to the Signal Interface and the rest of the CZone modules on the system.
9. Test all inputs and outputs for configured functionality.












Figure 4. Dipswitch Setting

## Page 8

EN / CZone® Signal Interface (SI) User & Installation Manual
8


6 LED Flash Codes









1. Circuit Status LED’s
Colour
Description
Green Solid ON
Valid Signal Input
1x Red Flash
Channel Not Configured
2x Red Flash
Configuration Conflict
3x Red Flash
Dip Switch Conflict
4x Red Flash
Memory Comms Failure
5x Red Flash
No Modules Detected
6x Red Flash
Fault On Output
7x Red Flash
Output Not Detected
8x Red Flash
Invalid Signal Input


2. Network Status LED
Colour
Description
Extinguished
Network Power Disconnected
Green
Network Power Connected
Red Flash
Network traffic








1
2
Figure 5. LED Flash Codes

## Page 9

9
EN / CZone® Signal Interface (SI) User & Installation Manual


7 Labelling

CONNECTIONS/LED FLASH CODE LABEL
This label is located on the inside of the front lid of the unit, it shows the LED codes and electrical connections to the
unit:














MODULE IDENTIFICATION AND DIPSWITCH LABEL
These labels allow easy identification of each module whilst recording the dipswitch setting.  These labels are to be
fitted to the cover and to the module (this prevents covers being swapped).  To record the module type and dipswitch
settings use a permanent marker and strike through the applicable boxes (a strike through on a dipswitch box indicates
that switch is on).

Figure 7. Module Identification

8
6
4
2
1
3
5
7
DC V 3 +
DC -
Shunt 1 (B)
Shunt 1 (L)
Shunt 2 (B)
Shunt 2 (L)
DC V 1 +
DC V 2 +
AC I 1 (TXFM)
AC V 1 (TXFM)
AC I 2 (TXFM)
AC V 2 (TXFM)
AC V 3 (TXFM)
TXFM common
I/P 6
I/P 5
I/P 4
I/P 3
I/P 2
I/P 1
DC -
NC
Figure 6. Module Labeling
XX
OI
SI
MI
SCI
MOI
DI
1 2
DIP
3 4 5 6 7 8

## Page 10

EN / CZone® Signal Interface (SI) User & Installation Manual
10


8 System Wiring Example


CIRCUIT
BREAKER
CIRCUIT
BREAKER
BUS BAR
NEGATIVE
FLOAT SWITCH
BILGE PUMP
POSITIVE
BUS BAR
SWITCH PANEL
SWITCH
BATTERY
SEND
NEG.
TANK SENDER
0-5 VOLT
CIRCUIT
BREAKER
No connection
DC Negative
Signal input 1
Signal input 2
Signal input 3
Signal input 4
Signal input 5
Signal input 6
Signal inputs:
10-180 Ohm Sender
240-33 Ohm Sender
0-5v Sender
Negative (for switching purposes)
Positive (0-32v, for switching purposes )
NETWORK
NMEA 2000
SEND POS. NEG.
10-180     or 240-33
TANK SENDER
BATTERY
-
+
Figure 8. Wiring Diagram

## Page 11

11
EN / CZone® Signal Interface (SI) User & Installation Manual


9 Dimensions

































Figure 9. Dimensions

## Page 12

EN / CZone® Signal Interface (SI) User & Installation Manual
12


10 Ordering Information
 MODULE
Description
Part number
CZONE SIGNAL INTERFACE c/w SEALS & CONN
80-911-0013-00
CZONE SIGNAL INTERFACE NO SEALS & CONN
80-911-0014-00

 ACESSORIES AND SPARES
Description
Part number
SEAL CABLE GLAND for ZONE SI BK SILICON
80-911-0036-00
ERM BLOCK MI 8 WAY PLUG 5mm PITCH
80-911-0043-00

11 EMC ratings
•
IEC EN 60945
•
IEC EN 61000
•
FCC Class B
•
ISO 7637 - 1 (12V  Passenger cars and light commercial vehicles with nominal 12 V supply voltage -
Electrical transient conduction along supply lines only)
•
ISO 7637 - 2  (24V Commercial vehicles with nominal 24 V supply voltage - Electrical transient
conduction along supply lines only)
•
IEC Standards for indirect lighting strikes

## Page 13

13
EN / CZone® Signal Interface (SI) User & Installation Manual


12 Declaration Of Conformity
