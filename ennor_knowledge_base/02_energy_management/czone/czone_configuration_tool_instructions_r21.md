---
vessel: Ennor
title: "CZone Configuration Tool Instructions R21"
category: "Energy Management"
source_pdf: "library_czone/CZone Configuration Tool Instructions R21.pdf"
extraction_method: native
page_count: 108
converted: "2026-02-24"
---

# CZone Configuration Tool Instructions R21

**Vessel:** Ennor | **Category:** Energy Management
**Source PDF:** library_czone/CZone Configuration Tool Instructions R21.pdf | **Pages:** 108 | **Extraction:** native

---

## Page 1

Configuration Tool Instructions
R21.2

## Page 2

2
EN / CZone Configuration Tool Instructions


TABLE OF CONTENTS
1
GENERAL INFORMATION ....................................................................................................................................... 5
1.1
Description .................................................................................................................................................. 5
1.2
Use Of This Manual ..................................................................................................................................... 5
1.3
Computer Requirements .............................................................................................................................. 5
1.4
Hardware Requirements .............................................................................................................................. 5
2
GETTING STARTED................................................................................................................................................. 6
2.1
Installing The CZone® Configuration Tool..................................................................................................... 6
2.2
USB to CAN Driver Installation ..................................................................................................................... 8
2.2.1
Checking USB to CAN Driver Status ............................................................................................ 8
2.2.2
Forcing the Czone Config Tool to Reinstall the Driver ................................................................... 9
2.2.3
Manual Driver Install Process ....................................................................................................... 9
3
CONFIGURATION TOOL BASICS .......................................................................................................................... 10
3.1
Read From Network ................................................................................................................................... 10
3.2
Write To Network ....................................................................................................................................... 11
3.3
Upgrading Firmware .................................................................................................................................. 12
3.3.1
Firmware Update From Package ................................................................................................ 13
3.4
Commissioning Report ............................................................................................................................... 15
4
CONFIGURING A NEW SYSTEM ........................................................................................................................... 16
4.1
Initial Setup ............................................................................................................................................... 16
4.2
Module Setup ............................................................................................................................................ 17
4.2.1
Initial Settings ............................................................................................................................ 18
4.2.2
Settings Specific to all Output Interfaces ..................................................................................... 19
4.2.3
Backlight Settings Specific to all Digital Switch & Display Interfaces ............................................ 20
4.2.4
Backlight Settings Sepcific to CZone Keypads ............................................................................ 21
4.2.5
Settings Specific to AC Mains Interfaces..................................................................................... 22
4.2.6
MasterBus Bridge Interface Specific Settings .............................................................................. 23
4.2.7
Wireless Interface Specific Settings ............................................................................................ 24
4.3
Power Metering ......................................................................................................................................... 25
4.3.1
DC Meter - Meter Interface/Combination Output Interface/Control 1 ............................................ 26
4.3.2
DC Meter - MasterBus Bridge Interface ...................................................................................... 32
4.3.3
AC Meter - Meter Interface/AC Mains Interface ........................................................................... 33
4.3.4
AC Meter - MasterBus Bridge Interface ...................................................................................... 36
4.4
Loads ........................................................................................................................................................ 37
4.4.1
DC Loads .................................................................................................................................. 38
10.
DC Loads Advanced Settings ..................................................................................................... 39
4.4.2
DC Loads Advanced Settings Specific to Combination Output Interface/Control 1 ........................ 40
4.4.3
AC Loads .................................................................................................................................. 41

## Page 3

EN / CZone Configuration Tool Instructions
3



4.4.4
AC Loads Advanced Settings ..................................................................................................... 42
4.4.5
Virtual Signals ........................................................................................................................... 43
4.4.6
MBI Virtual Signal ...................................................................................................................... 44
4.5
Signal Inputs.............................................................................................................................................. 45
4.5.1
Initial Settings ............................................................................................................................ 46
4.5.2
Switch To Positive Alarm/Switch Settings ................................................................................... 47
4.5.3
Switch To Negative Alarm/Switch Settings .................................................................................. 47
4.5.4
Fluid Level Calibration ............................................................................................................... 48
4.5.5
Temperature Level Calibration ................................................................................................... 52
4.5.6
Pressure Level Calibration ......................................................................................................... 53
4.5.7
Trim Level Calibration ................................................................................................................ 54
4.6
Circuits ...................................................................................................................................................... 56
4.6.1
New Circuit Configuration........................................................................................................... 57
4.6.2
Switch Configuration .................................................................................................................. 59
4.6.3
Load Configuration .................................................................................................................... 63
4.6.4
Modes Guru .............................................................................................................................. 65
4.6.5
Circuit Test ................................................................................................................................ 65
4.7
AC Mains .................................................................................................................................................. 66
4.8
Generator Control ...................................................................................................................................... 69
4.8.1
Hardware Requirements ............................................................................................................ 69
4.8.2
Configuring Generator Control: Dual Alternating/Split-Bus Example............................................. 69
4.9
Mastervolt.................................................................................................................................................. 81
4.9.1
Mastervolt Device Configuration ................................................................................................. 82
4.10
Logic Blocks .............................................................................................................................................. 84
4.10.1
Logic Block Inital Setup .............................................................................................................. 84
4.10.2
Logic Block Input Configuration .................................................................................................. 85
4.11
Data Switching........................................................................................................................................... 87
4.11.1
PGN Switching .......................................................................................................................... 87
4.11.2
Time Of Day Switching............................................................................................................... 89
4.12
Third Party Devices.................................................................................................................................... 90
4.12.1
Sea Recovery® Water Makers ................................................................................................... 90
4.12.2
Dometic® HVAC ........................................................................................................................ 91
4.12.3
Switch Bank PGN Control .......................................................................................................... 92
4.13
Settings ..................................................................................................................................................... 93
4.13.1
Sleep Mode Settings .................................................................................................................. 94
4.13.2
Configuration Password Protection ............................................................................................. 96
5
APPENDIX ............................................................................................................................................................. 98
5.1
Alarms ....................................................................................................................................................... 98
5.2
Logic Types ............................................................................................................................................... 99
5.2.1
AND .......................................................................................................................................... 99

## Page 4

4
EN / CZone Configuration Tool Instructions


5.2.2
OR ...........................................................................................................................................100
5.2.3
XOR .........................................................................................................................................100
5.2.4
NAND.......................................................................................................................................101
5.2.5
NOR .........................................................................................................................................101
5.2.6
XNOR ......................................................................................................................................102
5.3
Supported Mastervolt (Masterbus) Devices ................................................................................................103
5.4
Supported Mastervolt (CZone Compatible) Devices ...................................................................................105
5.5
NMEA 2000 PGNs Supported for Data Switching.......................................................................................106
5.6
NMEA 2000 PGN’s Transmitted From CZone Modules ..............................................................................106
5.6.1
Meter Interface .........................................................................................................................106
5.6.2
Signal Interface ........................................................................................................................107
5.6.3
AC Mains Interface ...................................................................................................................107
5.6.4
Combination Output Interface/Control 1 .....................................................................................107
5.6.5
Masterbus Bridge Interface .......................................................................................................108
5.6.6
RV1..........................................................................................................................................108
5.6.7
Control X ..................................................................................................................................108

TABLE OF FIGURES
Figure 1
Module Tab Example ................................................................................................................................... 17
Figure 2
Power Metering Tab Example ...................................................................................................................... 25
Figure 3
Loads Tab Example ..................................................................................................................................... 37
Figure 4
Signal Inputs Tab Example........................................................................................................................... 45
Figure 5
Circuits Tab Example ................................................................................................................................... 56
Figure 6
AC Mains Page Example ............................................................................................................................. 66
Figure 7
Auto Changeover Enable Load ..................................................................................................................... 68
Figure 8            AC Mains Tab .............................................................................................................................................. 68
Figure 9
ChargeMaster Example ............................................................................................................................... 81
Figure 10
Mass Combi Example .................................................................................................................................. 81
Figure 11
PGN Switch ................................................................................................................................................. 88
Figure 12
Alarm Severities .......................................................................................................................................... 98
Figure 13
Alarm Severities on Touch Screen................................................................................................................ 98
Figure 14
AND Logic Example ..................................................................................................................................... 99
Figure 15
OR Logic Example ..................................................................................................................................... 100
Figure 16
XOR Logic Example................................................................................................................................... 100
Figure 17
NAND Logic Example ................................................................................................................................ 101
Figure 18
NOR Logic Example .................................................................................................................................. 101
Figure 19
XNOR Logic Example ................................................................................................................................ 102

## Page 5

EN / CZone Configuration Tool Instructions
5




1 GENERAL INFORMATION
1.1
DESCRIPTION
The CZone® Configuration Tool allows you to create or modify the parameters and settings of a CZone® system. The
parameters and settings are saved as a configuration. For a CZone® system to operate correctly, each device must have a
copy of this configuration.
The Configuration Tool can:
•
read and write configurations from a network
•
check and upgrade firmware on all CZone® modules.
1.2
USE OF THIS MANUAL
Copyright © 2019 BEP Marine. All rights reserved. Reproduction, transfer, distribution or storage of part or all of the contents in
this document in any form without the prior written permission of BEP Marine is prohibited.
1.3
COMPUTER REQUIREMENTS
The following minimum computer specifications are required:
•
Operating System: Windows XP, Vista, Windows 7, Windows 8, Windows 10
•
.NET Framework: 3.5 Service Pack 1 (for Windows XP)
•
Processor: INTEL/AMD single core or higher
•
RAM: 1GB
•
Hard Drive: 10GB
•
USB: 2.0/3.0
1.4
HARDWARE REQUIREMENTS
Additional hardware requirements:
A USB to CAN adapter is required to connect a PC to the CZone system.  The following are compatible USB to CAN Adapters:
•
USB to CAN Adapter (CZone Part # 80-911-0044-01)
•
MasterBus USB Interface (Mastervolt Part # 77030100)
•
KVaser USB to CAN Adapter

## Page 6

6
EN / CZone Configuration Tool Instructions


2 GETTING STARTED
2.1
INSTALLING THE CZONE® CONFIGURATION TOOL
1.
Double-click on the ‘CZone Config Tool Installer.msi’ file and click ‘Run’.

2.
Click ‘Next’.

3.
Select a location for the program to be installed, or click ‘Next’ for the default location.

## Page 7

EN / CZone Configuration Tool Instructions
7




4.
Click ‘Install’.

5.
The above screen will appear, showing that the Configuration Tool has been installed. Click ‘Finish’.
To finish the installation, open the Configuration Tool. A shortcut will be placed on your desktop for quick access. This will
install the required USB-to-CAN drivers.

## Page 8

8
EN / CZone Configuration Tool Instructions


2.2
USB TO CAN DRIVER INSTALLATION
The first time the CZone Configuration tool is opened the necessary drivers for the USB to CAN Interface are installed. On
some computers where the user has no admin rights the auto-installation process can not run.  In this case a manual driver
install is required.
2.2.1
Checking USB to CAN Driver Status
To check the drivers have been installed correctly follow the below steps
1.
Disconnect & reconnect the USB to CAN adaptor to a USB port on your PC.

2.
Go to Control Panel > Device Manager. Check under Universal Serial Bus Controllers. If there is a device named
‘Navico USB IO Computer’ the drivers have been installed correctly and you do not need to continue


3.
If the Navico USB IO Computer device is not listed go to ‘Other Devices’ and check for device named ‘Client
Application Interface’.  This indicates the drivers have not installed correctly

## Page 9

EN / CZone Configuration Tool Instructions
9



2.2.2
Forcing the Czone Config Tool to Reinstall the Driver
The tool will not reinstall the drivers if it detects that you have already installed it earlier.
To force it to re-install again:
1)
Go to Documents>Czone>User Data
2)
Delete the file PegasusInstalled.txt
3)
Restart the Czone Config Tool, this will reinstall all driver during startup.
4)
Disconnect & reconnect the USB to CAN adaptor to a USB port on your PC.
5)
Lastly, restart the Czone Config Tool. It should now be able to detect Czone modules connected to the network.

2.2.3
Manual Driver Install Process
If forcing the tool to auto re-install all the drivers doesn’t work. Follow the below steps to install USB to CAN drivers manually
via the installed auto-run application
1.
Navigate to the folder C:\Program Files (x86)\BEP\CZone Configuration Tool

2.
Right click on the file ‘DriverInstaller.exe’ and select ‘Run as Administrator’. You will see the following window whilst
the appropriate drivers are installed.  When Complete Press any key.



3.
Go back to Control Panel > Device Manager and ensure the device ‘Navico USB IO Computer’ device is listed.  You
may need to disconnect and reconnect the USB to CAN and restart the configuration tool before it is recognized.

4.
The driver installation process is now complete.

## Page 10

10
EN / CZone Configuration Tool Instructions


3 CONFIGURATION TOOL BASICS
Basic procedures performed with CZone® configuration files are outlined in this section.
3.1
READ FROM NETWORK
Follow the below steps to read a CZone® configuration from an existing CZone® system. When working on a CZone® system,
it is always recommended to read the configuration and save a copy before making any changes. The configuration can be
modified on-line or off-line; the changes will not take effect until the modified configuration is written back to the network. It is
also important, when modifying a CZone system containing devices with older firmware, that they must be updated to match
the version of the Configuration Tool. Refer to section 3.3 for this process.

Plug your USB-to-CAN adapter into the powered network and open the CZone® Configuration Tool, then:
1.
Check that the ‘Network Status’ field indicates a connection to the network. The field should show the number of on-
line modules.
2.
Select ‘Read Config From Network’. As the system’s configuration is uploaded from the network, the ‘Network Status’
field will show how the upload is progressing. The upload may take a few seconds, or longer on large systems.
3.
Once the configuration has been read successfully you will see a list of all the configured modules. A module shown in
green is on-line. A module shown in black is off-line: its dipswitches may not be set, or it may lack a working
connection to the network.
4.
Select ‘Save Config to File’ to save the configuration file to your hard drive. The default location is
My Documents > CZone® > Config Files.
Note: If Network Status is showing ‘No Modules On-line’, ensure the network is powered and by a 12V source only (for USB to
CAN part number 80-911-0044-01) and each device has its network traffic indicator illuminated green. Also ensure the USB-to-
CAN drivers have been installed properly


1
2
3
4

## Page 11

EN / CZone Configuration Tool Instructions
11



3.2
WRITE TO NETWORK
Follow the steps below to write a new or modified CZone® configuration to the network.


Plug your USB-to-CAN adapter into the powered network and open the CZone® Configuration Tool, then:
1.
Select ‘Load Config From File’, locate the desired configuration file and press ‘Open’
2.
Before writing to the network, ensure all interfaces are showing green (on-line)
3.
Select ‘Write Config to Network’. The ‘Network Status’ field will change to ‘Transmitting Configuration Data’.
Once transmission is complete, the system will reboot and the devices will show off-line for a few seconds. The system is ready
to use with the new configuration when devices have rebooted and are showing on-line.


3
2
1

## Page 12

12
EN / CZone Configuration Tool Instructions


3.3
UPGRADING FIRMWARE
The CZone® Configuration Tool allows firmware upgrades to be performed on most CZone® modules over the CAN network.
Although CAN is the only method to update the majority of CZone modules, the CZone Displays have an additional Direct
Updater file for updating firmware via the displays local USB or SD Card port.  Because of the large file size it is recommended
to use the direct updater which is a much faster method.  The Wireless Interface cannot be updated over CAN.
A breakdown of the module types and their update methods are listed below:

CAN
USB
SD
ETHERNET
OI/MOI
✓
COI
✓
✓
Contact 6
✓



Contact 6 Plus
✓



Control 1
✓
✓


Control X
✓



DDS
✓



RV1
✓
✓


Keypad
✓



Switchpad
✓



SCI
✓
SI
✓
MI
✓
ACOI
✓
ACMI
✓
MBI
✓
DI 3.5”
✓*
✓**
DI TOUCH 8” & 10”
✓
✓
TOUCH 10
✓
TOUCH 7




TOUCH 5
✓
✓
WIRELESS INTERFACE
✓

*CAN update only possible on devices with firmware 6.00.01.02 or newer.  Older devices must be updated via Ethernet
**CZone DI ethernet programming cable required : Part number:80-911-0058-00

## Page 13

EN / CZone Configuration Tool Instructions
13



3.3.1
Firmware Update From Package
Follow the below steps to update a module or modules with a specific firmware package saved to your PC.

Ensure the CZone® network is powered and the USB-to-CAN adaptor is plugged into the network, then:
1.
Click on the ‘Firmware’ tab
2.
Ensure all interfaces appear on this list.
3.
Click on ‘Load Firmware Package’.
4.
Select the firmware package (.czswup file) to be used and click ‘Open’.
5.
The interface/s will appear in a different colour once the package is loaded. A breakdown of what each colour means
is below.
Green
Latest firmware installed, no need to upgrade
Orange
Out-of-date firmware, new firmware must be installed
Red
No firmware installed, new firmware must be installed
Grey
No firmware update available

6.
To update the firmware click the ‘Start Updating’ button.  The module types to be updated will be ticked in the next
window.  If your system is large, it is recommended that you upgrade one module type at a time. Select OK to
continue.


3
1
6
2

## Page 14

14
EN / CZone Configuration Tool Instructions



7.
It is recommended that you save a copy of the configuration file before upgrading firmware. If you have not yet done
so, check the ‘Read/Save/Update Configuration During Update’ box.

8.
The firmware upgrade will now begin. The progress bar will be repeated for each module type that is upgraded. Note,
some modules may require a bootloader update, in this case the progress bar will run twice for that particular module
type.


9.
Click ‘OK’ to finish the firmware update.
The upgraded interfaces should now appear in green to indicate that the latest firmware is installed.

## Page 15

EN / CZone Configuration Tool Instructions
15



3.4
COMMISSIONING REPORT
The commissioning report provides a checklist of recommended installation requirements and tests to help installers through
the commissioning process.  It also generates a PDF report with all the detailed information about the system and a copy of the
configuration file.  This report should be saved for your own records and also sent to report@czone.net for better support from
CZone technical support teams.
1.
To start the commissioning process, ensure the configuration tool is plugged into a live system.  Go to the firmware
tab and press the ‘Commissioning Report’ button.

2.
Enter general system details for the vessel/vehicle and complete checklist. Notes and attachments (such as
installation diagrams and photos) can be attached if required.

3.
Once all fields has been completed, press the ‘Generate Report’ button. All details and selections made in the
checklist along with a snapshot of all networked devices, serial numbers and firmware versions will be populated in a
PDF document. All reports will be saved in the My Documents/CZone/Commissioning Reports folder.

## Page 16

16
EN / CZone Configuration Tool Instructions


4 CONFIGURING A NEW SYSTEM
A CZone® configuration can be completed off-line, then written to the network at a later date. This chapter will explain how to
write a new CZone® Configuration. It will also give definitions for all settings within the CZone® Configuration Tool.
4.1
INITIAL SETUP

1.
To begin a new configuration, select ‘New System Configuration’.

2.
Enter a name for the configuration and select ‘OK’. This will also be the default filename when the configuration is
saved for the first time.


1
2

## Page 17

EN / CZone Configuration Tool Instructions
17



4.2
MODULE SETUP
The first step in building a CZone® configuration is to add the CZone® modules that will make up the system, including:
•
new modules that you intend to install
•
modules already present on the network, if you are working on an existing system.
See Figure 1 for an example of a configured Modules tab.

Figure 1
Module Tab Example
1.
The ‘Configured Modules’ section shows a list of module types. Under each module type are one or more such
modules, with their dipswitch settings and configured names. The total number of modules is listed at the top.
2.
There are buttons for adding, editing, and removing modules from the configuration.
3.
To identify a module on a live network without physically checking its dipswitch setting, tick the ‘Identify Modules’ box.
Then select the module to be identified, from the ‘Configured Modules’ list. The status LEDs on that device will flash
between red and green for a short time.
4.
To quickly view a module’s configured settings, select the + symbol next to that module in the ‘Module Configuration
Details’ panel. A drop-down list of the inputs or outputs configured for that device will be displayed, together with all its
settings. (No editing is available from this panel.)
1
2
3
4

## Page 18

18
EN / CZone Configuration Tool Instructions


4.2.1
Initial Settings
To begin adding modules to the configuration, from the Modules tab select the ‘Add’ button.

1.
Select the type of module you wish to add to the system.
2.
Enter a name for the module that you are adding, or enter nothing to accept a default name (In the example shown,
MI01 would be assigned.)
3.
For each module a dipswitch must be assigned.
a.
These numbers can be assigned manually on the units, before the configuration is generated in the
configuration tool. In this case select the dipswitch number from the drop-down list, or use the ‘Edit Dipswitch
Graphically’ box beneath it.

b.
The dipswitch setting can also be assigned automatically by the configuration tool. Sequential numbers will
be assigned as the modules are entered. These numbers must then be copied and assigned to the physical
dipswitches on the CZone® modules.

c.
Dipswitch settings can also be detected automatically:
i. Ensure the PC that is running the Configuration Tool is plugged into the network
3
2
1
3.c.ii
4
5

## Page 19

EN / CZone Configuration Tool Instructions
19



ii. Ensure the ‘Auto-Select First Detected Module’ box is ticked
iii. Choose a module type.
iv. The network will be scanned, for the first module of that type whose dipswitch is set. In the
configuration tool, that module’s dipswitch configuration will be made automatically.
4.
If required, the ‘Switched Module/Network Power’ option can be selected. By selecting this option the ‘Missing Module’
alarm will not occur when a module loses power or communication. In standard systems this should remain unticked,
but use this option in systems where a display or touch-screen is fed from a switched supply.
5.
After the module name has been entered and the dipswitch number assigned, click ‘OK’. The module modification
window will close and the program will return to the ‘Modules’ tab.

You will see the module that has just been entered will now show in the ‘Configured Modules’ list, the settings are now
complete for this unit. It is recommended that all modules are entered before continuing the configuration process. Follow the
same process for all modules. Some processes are unique to each module; these are explained in the subsections below.
4.2.2
Settings Specific to all Output Interfaces

1.
For the load shedding functionality to work correctly, the Output Interface must be assigned to a battery bank (power
supply). This is done by selecting the battery bank under the ‘DC Power Source’ drop-down list. The factory setting list
comprises ‘Unmetered 12V’ and ‘Unmetered 24V’. The purpose of these values is to give the user an indication, on
the Display Interface, of the supply voltage that the circuits are connected to. (This list will auto-populate as inputs are
configured. The above example shows an Output Interface that has been configured with a House Bank). To add to
this list, the Metering Interfaces must be configured in the ‘Power Metering’ Tab. It is recommended that all modules
are entered before any of the individual modules are configured. The ‘DC Power Source’ selection can be made at a
later time, after all modules have been entered and the Metering interfaces have been configured.
Note: Load shedding and battery monitoring functionality is only available if a Meter Interface is connected to the system.
1

## Page 20

20
EN / CZone Configuration Tool Instructions


4.2.3
Backlight Settings Specific to all Digital Switch & Display Interfaces
The backlighting for digital switches are controlled via a Display Interface or a dedicated switch. There may be many locations
for both the switches and Display Interfaces, with different lighting intensity requirements. The CZone® system allows each unit
to be allocated a backlighting zone, so adjustment to the backlighting can be specific to an area on the vessel without affecting
another module.

1.
Select the Display or Digital Switch module from the module type drop down.
2.
Click on the drop-down box under the ‘Backlighting Zone’ section and select the desired backlighting zone for the
module.
Note: CZone® touch screens and supported MFDs are each classified as a Display Interface and must be configured
accordingly.
3.
Alternatively click on ‘New’ under the ‘Backlighting Zone’ section, enter a name for the new backlighting zone and click
OK.
4.
If the CZone® system has an AC Mains Interface control module, and you would like the ability to select AC sources
from a Display Interface, you must select the ‘Show AC Mains Control’ option. This allows only dedicated screens to
have control of the AC Mains.






1
2
3
4

## Page 21

EN / CZone Configuration Tool Instructions
21



4.2.4
Backlight Settings Sepcific to CZone Keypads
Default backlight colour selection is available for all CZone Keypads. Introdcued in R20 firmware, you can now select a default
colour for CZone Keypads. Configured backlight colour will only persist until user changes the colour manually via the Keypad
or if config is written back to network.


1.
When adding a new Keypad to a CZone configuration, a backlighting zone can be edited to have a default colour.

2.
Select colour from presets.
3.
Or, make a custom colour selection.
4.
Select OK to add default colour.










1
4
2
3

## Page 22

22
EN / CZone Configuration Tool Instructions


4.2.5
Settings Specific to AC Mains Interfaces
To configure an AC Mains Interface you must be connected to the network with the interface powered and with its dipswitch
assigned correctly. If the PC is not connected to the network these specific settings can be made later.

1.
Click on the ‘View/Edit Contactor Wiring Configuration’ option.

2.
Click on ‘Read Config From Device’. This will read the hard-coded settings from the ACMI and display them.
Note: The hard coded software on the ACMI is set at the time of manufacture in accordance with your specifications. If
the requirements have changed please contact your Mastervolt representative.
3.
Enter the names of the Load Groups (if required) as you would like them to be displayed.
4.
Select ‘OK’. The final settings of the AC Mains Control will be done in the AC Mains tab in section 4.7.
1
4
2
3

## Page 23

EN / CZone Configuration Tool Instructions
23



4.2.6
MasterBus Bridge Interface Specific Settings

1.
By default the MBI is configured to interface to the Masterbus network.  The MBI can also be configured to interface to
other 3rd party CAN networks as they are added by BEP Marine, select the required interface from the drop down box.
2.
Tick this box if you would like all alarms present on the MasterBus network to be repeated on CZone® Displays and
CZone integrated MFD’s.
3.
There is no physical dipswitch on the MasterBus Bridge Inteface. Instead it has a virtual dipswitch set in the software
to identify it on the network. The default dipswitch is 11111111. If this dipswitch is already used in your system you
can change it, either graphically or by selecting a new dipswitch in the drop-down box, then press the ‘Force Dipswitch
for Address’ button.


2
3
1

## Page 24

24
EN / CZone Configuration Tool Instructions


4.2.7
Wireless Interface Specific Settings
The Wireless Interface acts as the server for iPads to connect to and control/monitor the CZone® system with the CZone®
App. There are several settings that can be changed to make the app more user-friendly. The first few relate to how switches
are displayed on the home page of the CZone® App.

1.
Tick this box to change iPad controls for All Displays On/Off switch type to Toggle. This cleans up the controls by
having a single button instead of separate On and Off buttons.
2.
Tick this box to change iPad controls for All Display Dim Up/Down to Single-Button Dim. This cleans up the controls by
having a single button instead of separate On and Off buttons.
3.
There is no physical dipswitch on the Wireless Inteface. Instead it has a virtual dipswitch set in the software to identify
it on the network. The dipswitch for the WI is set up manually in the WI Configuration Tool. If this dipswitch is already
used in your system you can change it, either graphically or by selecting a new dipswitch in the drop-down box, then
press the ‘Force Dipswitch for Address’ button.


2
3
1

## Page 25

EN / CZone Configuration Tool Instructions
25



4.3
POWER METERING
The ‘Power Metering’ tab is where both AC and DC monitoring is configured. This includes adding meters, adjusting alarms and
load shedding while also carrying out final calibration. AC and DC meters can be monitored from the Meter Interface or from
MasterBus devices through the MasterBus Bidge. AC meters can also be monitored from the AC Mains Interface. See Figure 2
for an example of a configured Modules tab with all monitoring devices and their associated DC and AC Meters.

Figure 2
Power Metering Tab Example
1.
ACMI (AC Mains Interface) with AC meters for Generator, Shore Power 1 and Shore Power 2.
2.
MBI (MasterBus Bridge Interface) with DC meters repeated from Mastervolt devices (MasterShunt and Li-ion Battery).
3.
MI (Meter Interface) with a DC meter for House Battery.
4.
The Display Ordering of the configured meters can be changed from this drop-down list. This ordering will be shown
on the Power Metering tab of the Configuration Tool and, after the config has been written to the network, on the
Monitoring page of any Display Interface. The options are explained below:
•
By Module - Default View, shows meters in a tree view starting with Module/Dipswitch then input numbers
•
Alphabetical - Shows meters in alphabetical order split, into AC and DC
•
By Instance/Line – Shows meters in order of NMEA instance number and then line for multi-phase AC
meters.
The following sections explain how to configure each type of AC and DC meter.


4
2
3
1

## Page 26

26
EN / CZone Configuration Tool Instructions


4.3.1
DC Meter - Meter Interface/Combination Output Interface/Control 1
4.3.1.1
Initial Settings
To configure a DC Meter connected to a Meter Interface or one of the analogue inputs on the COI or Control 1, from the Power
Metering Tab select ‘Add DC Meter’.

1.
Select the ‘Metering Device’ from the available module which has the input to be configured
2.
Enter a name that relates to the physical input to the module. This name will be used on the Display Interface to
represent that input.
3.
From the ‘Input/Channel’ drop-down list, select the channel which matches the physical input connections to the
Module.  Note: the COI/Control 1 has internal voltage sensing on the Main Power Stud and the NMEA2000 bus
(COI only) which can be configured to show on CZone Displays.
4.
NMEA 2000 Instances are used to differentiate between multiple monitoring sources. These are assigned
automatically by the configuration tool, to ensure the instances are unique for each source being monitored.
5.
Select the Nominal Voltage of supply from the drop-down list.
6.
Select the DC Supply Type that represents the supply type for this input.
7.
Tick the appropriate Display Options boxes for the input being configured. This allows you to select what DC
monitoring parameters are shown on the Display Interface. In this example the House Bank also has a shunt
wired to the Meter Interface, therefore we want to display the current and state of charge as well as the voltage.
The COI analogue inputs are voltage sensing only.
8.
For Meter Interface inputs with current sensing, click the ‘Battery Configuration’ button to launch the Battery
Settings dialogue.
Note: Calibration settings will need to be done once the entire system is configured and downloaded to the network.
1
2
5
6
7
8
3
4

## Page 27

EN / CZone Configuration Tool Instructions
27



4.3.1.2
Battery Configuration
The Battery Configuration options are used in the battery capacity calculations. It is important that these values are entered
correctly. Failure to do so will cause the battery monitoring to be inaccurate. If you are unsure of any of these values you can
get them from the battery manufacturer.

1.
Select the ‘Battery Type’ that represents the battery to be monitored.
2.
Select the ‘Battery Chemistry’ that represents the battery to be monitored.
3.
Enter the ‘Battery Capacity’ of the battery bank in Ah. This will be shown on the Display Interface and used to
calculate the State of Charge.
4.
Enter the Minimum Discharge Current (A). Any discharge current above this value is when Peukert’s calculation is
applied.
5.
To reset the State Of Charge of the battery to 100%, select the ‘Set Battery Fully Charged’ button. This should
only be done if the battery is full and the PC is connected to the CZone® Network.
6.
Enter the Charging Efficiency of the battery to be monitored. Under charging conditions, the measured charge
current is multiplied by the charging efficiency and the result added to the State Of Charge. The efficiency can be
obtained from the battery manufacturer.
7.
Enter the Peukert’s Coefficient of the battery to be monitored. This affects the State Of Charge calculation at
higher discharge currents. The Peukert’s value can be obtained from the battery manufacturer.
8.
Enter the Battery Full Current (A). This should be between 2.5% and 4% of Battery Capacity (Ah). Under charging
conditions, if the current is below the ‘Battery Full Current’ setting and voltage is above the ‘Battery Full Voltage’
setting for five minutes, State of Charge will reset to 100%.
9.
Enter the Battery Full Voltage (V). This should be set just lower than the charging sources ‘float’ voltage. Under
charging conditions, if the current is below the ‘Battery Full Current’ setting and voltage is above the ‘Battery Full
Voltage’ setting for five minutes, State of Charge will reset to 100%.
10. Click OK to save the battery configuration settings.


1
2
3
4
5
6
7
8
9
10

## Page 28

28
EN / CZone Configuration Tool Instructions


4.3.1.3
DC Voltage Calibration
To calibrate DC Voltage the PC must be connected to the CZone® Network. It is recommended to do this process during
commissioning of the system.


1.
To calibrate the voltage for this input, select ‘Calibrate Voltage’.

2.
With an accurate voltmeter, check the voltage at the battery against the value in the ‘Calibrated Measurement’
window.
3.
If the values are different, enter the measured value in the ‘Enter Non-Zero voltage’ box.
4.
Click on the ‘Set Non-Zero Voltage’ tab. The voltage in the ‘Calibrated Measurement’ will now match the value of the
entered voltage.
5.
Click OK to return to the DC Advanced Configuration page, then write the config to the network for the new settings to
take effect.


2
3
4
5
1

## Page 29

EN / CZone Configuration Tool Instructions
29



4.3.1.4
DC Current Calibration
To calibrate DC current the PC must be connected to the CZone® Network. It is recommended to do this process during
commissioning of the system.

1.
To calibrate the current for this input, click Calibrate Current to launch the DC Current Calibration dialogue.

2.
This is the calibrated current for the input that was selected. It is recommended to do a current calibration on a new
system. There are two ways to do this calibration:
a.
If you have easy access to the shunt, you can set the zero point first.
i. Connect both sense wires together under the battery side of the shunt terminal; this means no
current can be sensed across the shunt. Click the ‘Set Zero Amps’ tab. Return the load-side sense
wire to the load side of the shunt.
1
2.b
2.a.ii
2.a.i
2
3

## Page 30

30
EN / CZone Configuration Tool Instructions


ii. Now that we have a zero-point calibration, we need to set a non-zero point. Turn on a circuit to put a
load on the system. (The higher the current, the more accurate the current readings will be. Select
loads that do not vary in current draw). With an accurate current meter, check the current draw on
the shunt to the battery against the value in the ‘Calibrated Measurement’ window. If the values are
different, enter the measured value in the ‘Non-Zero Current” box and click on the ‘Set Non-Zero
Amps’ button. The current in the ‘Calibrated Measurement’ will now match the value of the entered
current.
b.
If you don’t have easy acess to the shunt to create a zero point, instead you can use two calibration points
(non-zero and secondary non-zero).
Start with the non-zero point in step ‘a.ii’. The wider the current range between the two points, the more
accurate it will be. It is a good idea to use charge current for the non-zero point and discharge current for the
secondary non-zero point. Enter this secondary current into the ‘Secondary Non-Zero Current’ box and then
press the ‘Set Secondary Non-Zero Amps’ button. The current in the ‘Calibrated Measurement’ will now
match the value of the entered curent.
3.
Click OK to return back to the DC Advanced Configuration page, then write the config to network for the new settings
to take effect.
4.3.1.5
DC Alarm and Switch Settings

1.
To configure any alarms or switches for the selected DC meter, press ‘Alarm/Switch Settings’. (Alarms and Switches
can be used as inputs to Logic Blocks (see section 4.10) but not directly as Circuit controllers.)
Note: Preset and non-adjustable delays to the alarms/switches are listed below:
Alarm/Switch Point
Delay
High Voltage
5 seconds
Low Voltage
5 minutes
Very Low Voltage
5 minutes
High Battery Capacity
3 minutes
Low Battery Capacity
3 minutes
Very Low Battery Capacity
3 minutes
1

## Page 31

EN / CZone Configuration Tool Instructions
31




2.
For every DC Meter there are six levels of alarms/switches that can be enabled for Battery Capacity and Battery
Voltage readings. The alarms (visual and audible depending on severity) will be triggered on any Display Interface.
The switches can be assigned to control any circuit configured in the Circuits tab (e.g. a low battery capacity switch
can be used to start a generator).
3.
Tick the box next to the required alarm or switch to enable it.
4.
Enter the On value, in volts or % capacity, at which you require the alarm/switch to be activated.
5.
The Off value for the alarm/switch is greyed out by default. If you require a different level for this alarm/switch to be
deactivated, un-tick the ‘Use Default Hysteresis’ box at the bottom.
6.
If enabling an alarm, select its severity from the drop-down list. (Refer to for section 5.1 for detail on alarm severities.)
7.
To enable load shedding of DC loads, first tick the ‘Enable Load Shedding Alarms’ box. Then use the drop-down list to
select the load shedding mode you wish to use. The two options for load shedding are voltage or battery capacity
controlled. The switch points at which load shedding occurs are based on the settings adjusted in the above steps.
Once load shedding is enabled, each load when added to the configuration will have the option to load-shed at one of
these preset levels. This is described in section 4.4.
8.
Depending on the supply that is connected to this meter input, you may require an alarm or switch to activate at a zero
value (volts or capacity). In that case, click on the ‘Allow Alarms/Switches on Open Circuit’ box. This functionality is
provided because all other low voltage alarms and switches will not operate at zero voltage. (If they did, an alarm
could trigger when a master switch or circuit breaker was turned off: it would cause zero volts to appear at the meter
interface voltage input.)
Note: Low or Very Low Alarms/Switches must be active for Alarm or Switch on Open Circuit to work.
9.
Click OK to save settings and return to the ‘DC Meter Configuration’ box.
Select OK again to return to the ‘Power Metering’ page.
7
9
8
6
5
4
3
2

## Page 32

32
EN / CZone Configuration Tool Instructions


4.3.2
DC Meter - MasterBus Bridge Interface
4.3.2.1
Initial Settings
To configure a DC Meter connected to an MBI (MasterBus Bridge Interface), from the Power Metering Tab select ‘Add DC
Meter’.

1.
Enter a name for the input that relates to the Mastervolt device or battery the MBI is monitoring. This name will be
used on the Display Interface to represent this input.
2.
From the ‘Metering Device’ drop-down list, select the MBI’s which has the meter to be configured
3.
Select an available MBI Meter Input, from the ‘Input/Channel’ drop-down list. The MBI has 16 metering channels
available.
4.
Select the MasterBus Device to be used for DC monitoring from the drop-down list. If the Mastervolt device is powered
and on-line it will be shown in this list and configured automatically, If the device is to be configured through
MasterAdjust, select the ‘Configured in MasterAdjust’ option.
5.
Select the ‘Monitoring Data Item’ from the drop-down list for the chosen device. If you would like to edit these values
manually, select ‘Manually Configured’.
6.
NMEA 2000 Instances are used to differentiate between multiple monitoring sources. These are assigned
automatically by the configuration tool, to ensure the instances are unique for each source that is monitored.
7.
Select the DC Supply Type that represents the supply type for this input.
8.
Select the Nominal Voltage of the supply from the drop-down list.
9.
Enter the Battery Capacity in Amp-Hours.
10. Tick the appropriate Display Options boxes for the input to be configured. This allows you to select what DC
monitoring parameters are shown on the Display Interface. In this example the House Bank is being monitored
through a MasterShunt, which has montitoring parameters available for Volts, Amps and State of Charge.
11. When configuring a supported Mastervolt device, the MasterBus index numbers are assigned automatically. If these
index numbers need to be edited, select the ‘Edit MasterBus Values’ box.
1
2
3
4
6
5
7
9
11
12
13
10
8

## Page 33

EN / CZone Configuration Tool Instructions
33



12. DC Alarm and Switch settings can also be configured when metering with a MasterBus Bridge Interface. The method
is the same as for a Meter Interface: follow the instructions in section 4.3.1.5.
13. Click OK to complete the DC Meter configuration and return to the ‘Power Metering’ page.
4.3.3
AC Meter - Meter Interface/AC Mains Interface
This section describes how to configure an AC Meter. AC metering requires either a Meter Interface or an AC Mains Interface.
4.3.3.1
Initial Settings
To configure an AC Meter connected to a Meter Interface, from the Power Metering Tab select ‘Add AC Meter’.

1.
Enter a name for the input that relates to the physical connection into the Meter Interface. This name will be used on
the Display Interface to describe this input.
2.
Select the Meter Input, from the ‘Meter Interface Input’ drop-down list, that matches the physical input connections to
the Meter Interface. If you are configuring an AC Mains Interface you can use one of the six metering inputs of the
ACMI.
3.
NMEA 2000 Instances are used to differentiate between multiple monitoring sources. These are assigned
automatically by the configuration tool, to ensure the instances are unique for each source being monitored.
4.
AC Line is used if you are monitoring two- or three-phase AC sources. If a multiphase source is to be monitored,
assign the same NMEA 2000 AC Instance to each phase from that source and then select the the appropriate AC Line
for each phase.
5.
Enter the nominal voltage of this input.
6.
Enter the nominal frequency of this input.
7.
Tick the required boxes of the data you would like shown on the Display Interface for this input.
8.
Select the Message Type that best represents the type of AC being configured: AC Input or AC Output.
9.
Click on the ‘Calibrate Voltage’ or ‘Calibrate Current’ tabs to enter calibration pages. Follow the same calibration
process as for the DC Settings in section 4.3.1.4. This must be done when the PC is connected to the CZone®
network.
10. To configure any alarms or switches for the selected AC Meter, click ‘Alarm/Switch Settings’
4
10
9
8
2
3
5
6
7
1

## Page 34

34
EN / CZone Configuration Tool Instructions


4.3.3.2
AC Alarm/Switch Settings
Like DC Alarms and Switches, AC Alarms and Switches can be used as inputs to Logic Blocks (see section 4.10) but not
directly as Circuit controllers.

1.
For every AC Meter there is a Voltage Error or Frequency Error Alarm/Switch that can be enabled. If the voltage or
frequency is outside the configured percentage, the alarm/switch will be triggered. The nominal voltage and nominal
frequency values configured in the AC Meter Settings (section 4.3.3.1) are used as a reference for these
alarms/switches.
2.
There are also three levels of Power Alarms/Switches that can be enabled. The alarms (visual and audible depending
on severity) will be triggered on any Display Interface. The switch can be assigned to control any circuit configured in
the circuits tab.
3.
Tick the box next to the required alarm or switch to enable it.
4.
Enter the On value, in kW or Amps, at which you require the alarm/switch to be activated. (The appropriate unit can be
changed from kW to Amps near the bottom of the window.) The configuration tool will calculate the secondary value
once one of the boxes is filled in e.g. a kW value will auto-enter when an Amps value is entered. The values are given
in power and in current for situations where only one or the other is known, e.g. typically a dock-side power plinth
rating is given in current not power.
5.
The Off value for the alarm/switch is greyed out by default. If you require this alarm/switch to be deactivated at a
different level, un-tick the ‘Use Default Hysteresis’ box at the bottom of the window.
6.
If enabling an alarm, select its severity from the drop-down list. (Refer to section 5.1 for detail on alarm severities).
7.
Tick the ‘Allow Alarms/Switches on Open Circuit’ check-box to allow alarms and switches to activate at a zero value
(volts, frequency, power) for the supply that is connected to this meter input. This functionality is provided because all
other low voltage alarms and switches will not operate at zero voltage. (If they did, an alarm could trigger when a
3
4
5
1
8
2
7
6
9

## Page 35

EN / CZone Configuration Tool Instructions
35



power source was unavailable or a circuit breaker was turned off: it would cause zero volts to appear at the meter
interface voltage input.)
Note: Low or Very Low Alarms/Switches must be active for Alarm/Switch on Open Circuit to work.
8.
Most switches are activated on error conditions. Conversely if you want a switch to be activated when configured
voltage and frequency conditions are met, tick the ‘AC OK Switch’ check-box.
9.
Select OK to save settings and return to the ‘AC Meter Configuration’ box.
10. Select OK again to complete AC Meter configuration and return to the ‘Power Metering’ page.
Note: There are preset and non-adjustable delays to the following alarms/switches:
Alarm/Switch Point
Delay
Voltage Error
10 seconds
Frequency Error
10 seconds
High Power
10 seconds
Very High Power
10 seconds
Low Power
10 seconds

## Page 36

36
EN / CZone Configuration Tool Instructions


4.3.4
AC Meter - MasterBus Bridge Interface
4.3.4.1
Initial Settings
To configure an AC Meter connected to an MBI (MasterBus Bridge Interface), from the Power Metering tab select ‘Add AC
Meter’.
1.
Enter a name for the input that relates to the Mastervolt device or AC Meter to be monitored through the MBI. This
name will be used on the Display Interface to represent this input.
2.
Select an available MBI Meter Input, from the ‘Metering Input’ drop-down list. The MBI has 16 Metering channels
available.
3.
Select the MasterBus Device to be used for AC Monitoring from the drop-down list. If the Mastervolt device is powered
and on-line it will be shown in this list, If the device is to be configured through MasterAdjust, select the ‘Configured in
MasterAdjust’ option.
4.
Select the ‘Monitoring Data Item’ from the drop-down list for the chosen device. If you would like to edit these values
manually, select ‘Manually Configured’.
5.
Select the ‘Edit MasterBus Values’ box to edit the index numbers referenced from the Mastervolt device. These will be
configured automatically for the chosen device.
6.
NMEA 2000 Instances are used to differentiate between multiple monitoring sources. These are assigned
automatically by the configuration tool, to ensure the instances are unique for each source being monitored.
7.
AC Line is used if you are monitoring two- or three-phase AC sources. If a multiphase source is to be monitored, first
assign the same NMEA 2000 AC Instance to each phase from that source. Then select the the appropriate AC Line
for each phase.
8.
Enter the Nominal Voltage of the supply.
9.
Enter the Nominal Frequency of the supply.
10. AC Alarm and Switch settings can also be configured when metering with a MasterBus Bridge Interface. The method
is the same as for a Meter Interface: follow the instructions in section 4.3.3.2.
11. Check the required boxes of the data you would like shown on the Display Interface for this input.
12. Select the Message Type that best represents the type of AC being configured: either AC Input or AC Output.
13. Click OK to complete the AC Meter configuration and return to the ‘Power Metering’ page.
1
2
6
7
8
9
11
3
4
5
10
13
12

## Page 37

EN / CZone Configuration Tool Instructions
37



4.4
LOADS
The Loads tab is where the systems loads are created and their parameters set. This includes setting the circuit trip current, trip
characteristic and load shedding functionality. See Figure 3 for an example of a configured Loads tab.

Figure 3
Loads Tab Example
1.
By default, configured Loads are listed here by module, dipswitch number and then channel number.
2.
There are buttons for adding, editing, and removing modules from the configuration.
3.
The Display Ordering of the configured loads can be changed from this drop-down list. The options are explained
below:
•
By Module – Default View, shows loads in a tree view starting with module, dipswitch then channel number.
•
Alphabetical – Shows all loads in alphabetical order by their configured name.
•
By Power Supply – Shows loads in a tree view starting with their assigned battery supply then module,
dipswitch and channel number.
The following sections will explain how to configure each type of AC and DC load.
1
2
3

## Page 38

38
EN / CZone Configuration Tool Instructions


4.4.1
DC Loads
To configure a DC Load connected to any Output Module, from the Loads Tab select ‘Add DC Meter’:

1.
Enter the name of the load in this box. Labels will auto-predict as text is entered. This name will only be shown if a
fault (e.g. short circuit, low run current etc.) occurs for that channel. The name that will be shown on any CZone®
display is entered in the Circuits tab.
2.
From the ‘Module’ drop-down list, select the module that the load is to be configured on.
3.
From the ‘Channel’ drop-down list, select the channel that the load is to be configured on. (This list is dynamic: it will
only offer outputs that have not already been configured.) Virtual-Signal is an advanced option for controlling circuits
based on the state of a load. For more details refer to section 4.4.5.
4.
Select the fuse type for the circuit (Fast, Slow Blow or Motor Start). Motor Start should only be used if high in-rush
currents are causing the circuit to enter over-current or short-circuit status with the recommended current setting.
Note, software fusing is not available on the C6, C6+ or Control 1, all outputs are protected by the modules internal or
external fuses
5.
Select the software fuse rating for the circuit (either manually or from the drop-down list). This will be in accordance
with the equipment manufacturer’s specifications. Note that the software fuse should be set lower than the physical
fuse in the device, to ensure the software fuse trips first.
Note, software fusing is not available on the C6, C6+ or Control 1, all outputs are protected by the modules internal or
external fuses
6.
If load shedding is required for this load, select the load shedding value from the ‘Low Voltage Load-Shedding Priority’
drop-down list. (Options are: Never Turn Off (default); Turn Off Last (Very Low Voltage/Capacity); and Turn Off First
(Low Voltage/Capacity.) For this function to work, the tick-box in the appropriate DC metering advanced options page
must also be selected. Switching points for load shedding are based on those assigned in the DC metering set-up.
7.
Check ‘Smooth Start (Visual Effect)’ box to allow the circuit to come on gradually. This functionality is designed to give
a gradual visual effect during the turning on and off of lighting circuits. The rate at which the lights turn on/off can be
adjusted in the global settings tab. Note, feature not supported on all modules
8.
Check ‘Soft/Motor Start’ box to allow soft starting of halogen lights. This functionality prolongs the life of halogen bulbs
by inhibiting the shock from inrush current at start up. There is no need to select this box if you have selected the
smooth start option above. This function can also be applied to motors for soft starting. If using this function on motors,
1
2
4
6
7
8
9
3
5

## Page 39

EN / CZone Configuration Tool Instructions
39



check the manufacturer’s recommendations for the correct settings. If the motor-start fuse type has been selected, the
slowest/lowest setting allowed is 0.10 second. Note, feature not supported on all modules.
9.
The ‘Create All Displays Circuit’ option is visible when configuring a load for the first time.  It is recommended to
enable this option.  When the OK button is pressed, a complete circuit will be created including the configured load
and an All Displays switch, this drastically reduces configuration time.
10. DC Loads Advanced Settings

1.
Nominal Run Current is used to enter the average run current for the load being configured. This value is used for
calculating the Low Run Current or System On alarms and switches. The units can be changed between Amps and
Watts if one value is unknown. Note, feature not supported on all modules.
2.
Check the ‘Systems On Switch’ box to allow a switch function if the current exceeds 80% of the nominal run current.
The switch can be assigned to control any circuit configured in the Circuits tab.  Note, feature not supported on all
modules.
3.
If the current exceeds 80% of the nominal run current and a ‘Systems On’ alarm is needed, select the required Alarm
Severity from the drop-down list. Note, feature not supported on all modules.
4.
Tick the ‘Low Run Current Switch’ box to allow a switch function if the current falls below 80% of the nominal run
current. The switch can be assigned to control any circuit configured in the Circuits tab. Note, feature not supported on
all modules.
5.
If the current falls below 80% of the nominal run current and a ‘Low Run Current’ alarm is needed, select the required
Alarm Severity from the drop-down list. Note, feature not supported on all modules.
6.
‘Max On/Forward Level’ allows the user to set an absolute maximum PWM (Pulse Width Modulation) level that this
output will ever reach. For example it may be used to limit a 24V-supplied output module to 50% to supply a 12V
halogen light bulb. (Powering 12V electronics from a 24V supply is not recommended.)  Note, feature not supported
on all modules.
1
4
2
3
5
6
7
9
10
8
12
11

## Page 40

40
EN / CZone Configuration Tool Instructions


7.
‘Paralleled Outputs’ should be ticked when the current of a circuit exceeds the channels limit and it is required to
connect a load to two or more output channels. Once each paralleled channel is selected, you will be able to enter a
software fuse rating to the total max current of all channels
8.
‘Stay On when Configuring OR if Comms Fail’ should be ticked for critical items that should remain on:
•
if there is a communications failure on the network; or
•
when a configuration is being written to the network. (All other loads will turn off during this process.)
Note: This will not keep a load on if the module losses network power.
9.
Select which state the load must be in when the device or network is powered up. The default is Off.
10. ‘Calibrate Current’ This is a factory setting and should not be modified unless instructed by a CZone® application
engineer.
11. Check this box to disable the fuse in bypass alarm (COI only).  This can be useful for high capacitive loads where
voltage is present on the output 15 seconds or more after turning off the load.
12. Select OK to save the advanced settings and return to the ‘Load Configuration’ page.
13. Select OK on the ‘Load Configuration’ page to save the Load settings and return to the ‘Loads’ page.
The load is now configured and ready to be used in the Circuits tab. Repeat the above steps until all DC loads are configured.
4.4.2
DC Loads Advanced Settings Specific to Combination Output Interface/Control 1

1.
‘External Systems-on Alarm’ is an option available on all 4 High Current Channels of the COI/Control 1.  By enabling
this option, CZone will activate a ‘Systems On’ alarm if the channel is off and reverse voltage is detected on the
output. i.e. usefull for Bilge Pumps that have a direct feed from the battery through a float switch.  The ‘External
Systems-On Circuit Status’ box should be ticked if systems on feedback is also required on any switches configured to
control the load including displays and any CZone connected digital switches.
2.
The 4 High Current Channels can be paralleled up to a maximum fuse rating of 100A and the 12 Low Current
Channels can be paralleled up to a maximum fuse rating of 120A (Ensure the total load on the does not exceed 150A
continuous).
1
2

## Page 41

EN / CZone Configuration Tool Instructions
41



4.4.3
AC Loads
To configure an AC Load connected to an AC Output Interface, from the Loads tab select ‘Add’ to launch the Load
Configuration dialogue:

1.
Enter the name of the load in this box. Labels will auto-predict as text is entered. This name will only be shown if a
fault occurs for that channel. The name that will be shown on any CZone® display is entered in the Circuits tab.
2.
From the ‘Module’ drop-down list, select the module that the load is to be configured on.
3.
From the ‘Channel’ drop-down list, select the channel that the load is to be configured on. (This list is dynamic: it will
only offer outputs that have not already been configured.)
4.
Select the ‘AC Supply’ from the drop-down list. This list is based on metering and load groups that have been
assigned in the AC Metering and AC Mains setup (section 4.3.3). By selecting the source, the CZone® displays will
show if a source is available when the user is trying to turn on an AC circuit. If there is no AC Supply monitoring then
select ‘Unmetered AC’.
5.
Some circuit breakers are fitted with feedback which can raise an alarm if the breaker is tripped (i.e. goes open-
circuit). If the circuit breaker for this channel has that feature, you can select it here with the 'AC Circuit Breaker
Feedback’ drop-down list. (All CZone® systems are supplied standard without the feedback option fitted.)
6.
It is recommended to check the ’Create All Displays Circuit’ box. When the OK button is pressed, a complete circuit
will be created for this load with an All Displays control switch in the Circuits tab. This drastically reduces configuration
time.
7.
For modifying other load settings click on the ‘Advanced Settings’


1
2
7
3
6
4
5

## Page 42

42
EN / CZone Configuration Tool Instructions


4.4.4
AC Loads Advanced Settings

1.
Nominal Run Current is used to enter the average run current for the load being configured. This value is used for
calculating the Low Run Current or System On alarms and switches. The units can be changed between Amps and
Watts if one value is unknown.
2.
Check the ‘Systems On Switch’ box to allow a switch function if the current exceeds 80% of the nominal run current.
The switch can be assigned to control any circuit configured in the Circuits tab.
3.
If the current exceeds 80% of the nominal run current and a ‘Systems On’ alarm is needed, select the required Alarm
Severity from the drop-down list.
4.
Tick the ‘Low Run Current Switch’ box to allow a switch function if the current falls below 80% of the nominal run
current. The switch can be assigned to control any circuit configured in the Circuits tab.
5.
If the current falls below 80% of the nominal run current and a ‘Low Run Current’ alarm is needed, select the required
Alarm Severity from the drop-down list.
6.
Select the state that the load must be in when the device or network is powered up. The default is Off.
7.
‘Stay On when Configuring OR if Comms Fail’ should be checked for critical items that must remain on:
•
if there is a communications failure on the network; or
•
when a a configuration is being written to the network. (All other loads will turn off during this process.)
Note: This will not keep a load on if the module loses network power.
8.
‘Calibrate Current’ is a factory setting and should not be modified unless instructed by a CZone® application engineer.
9.
Click OK to save the advanced settings and return to the ‘Load Configuration’ page.
Click OK on the Load Configuration page to save the Load settings and return to the ‘Loads’ page.
The load is now configured and ready to be used in the Circuits tab. Repeat the above steps until all AC loads are configured.
1
3
5
6
8
2
4
7
9

## Page 43

EN / CZone Configuration Tool Instructions
43



4.4.5
Virtual Signals
The virtual signal function allows a circuit to be controlled based on the state of a load. For example, you may want a
secondary bilge pump to turn on after a primary bilge pump has been running for 30 seconds.
To create a virtual signal function go to the Loads tab and select ‘Add’

1.
Enter a name for the Virtual Signal.
2.
Select an Output Interface (OI), Combination Output Interface (COI) or Switch Control Interface (SCI) from the drop-
down list. To create a virtual signal, one of these module types must be on the network.
3.
Select the Virtual Signal number from the drop-down list. An OI can store up to six Virtual Signals/Logic Blocks; a COI
can store up to 32 and an SCI can store up to 16.
4.
To create a complete circuit in the Circuits tab, with the configured load and an All Displays On/Off control switch, tick
the ‘Create All Displays Circuit’ box.
5.
If an alarm is required when the Virtual Signal is turned on, select its severity from the drop-down list.
6.
Press the ‘Advanced Settings’ button for further load settings. Refer to section 10 for more information on these.
7.
Select OK to save the Virtual Signal and return to the Loads tab.
The Virtual Signal is now configured and ready to be used in the Circuits tab. Repeat the above steps to configure more virtual
signals.



4
1
2
5
6
3
7

## Page 44

44
EN / CZone Configuration Tool Instructions


4.4.6
MBI Virtual Signal
The control mechanism between CZone® and MasterBus functions by configuring virtual signals (MasterBus Event Sources)
within CZone® which subsequently function as virtual switches (Control to MB) within MasterBus. To control one of these
virtual switches, a load must first be configured within CZone® and programmed to turn on/off within a CZone® circuit. The
corresponding switch within MasterBus will then follow the state (on = closed, off = open) of this virtual signal (MasterBus Event
Source). When configuring a supported Mastervolt device (see section 4.9), these MBI loads are configured automatically.
The MasterBus Bridge Interface (MBI) has 16 Event Sources. To configure one of these event sources, go to the Loads tab and
select ‘Add DC Meter’.

1.
Enter a name for the MasterBus Event Source.
2.
Select the MBI module from the ‘Module’ drop-down list.
3.
Select one of the 16 available Event Sources from the ‘Channel’ drop-down list.
4.
It is recommended to tick this box, to enable CZone® On and Off commands to control MasterBus devices.
5.
It is recommended to tick this box, to allow Systems On feedback from MasterBus to be repeated on CZone®.
6.
To create a complete circuit in the Circuits tab, with the configured load and an All Displays On/Off control switch, tick
the ‘Create All Displays Circuit’ box.
7.
Press the ‘Advanced Settings’ button for further load settings. Refer to section 10 for more information on these.
8.
Click OK to save the load configuration and return to the Loads tab.
The load is now configured and ready to be used in the Circuits tab. Repeat the above steps until all MBI loads are configured.


1
2
4
5
7
3
8
6

## Page 45

EN / CZone Configuration Tool Instructions
45



4.5
SIGNAL INPUTS
The Signal Inputs tab is where inputs from devices such as tank senders, light switches, float switches and external switches
and tank senders are configured. See Figure 4 for an example of a configured Signal Inputs tab.

Figure 4
Signal Inputs Tab Example
1.
By default, configured Signal Inputs are listed here by module, dipswitch number and then channel number.
2.
There are buttons for adding, editing, and removing modules from the configuration.
3.
The Display Ordering of the configured loads can be changed using this drop-down list. The options are explained
below:
•
By Module – Default View, shows loads in a tree view starting with module, dipswitch then channel number.
•
Alphabetical – Shows inputs in a tree view, starting with their data type then in alphabetical order.
•
By Type Then Instance - Shows inputs in order of data type then NMEA instance number.
•
By Instance Then Type - Shows inputs in order of NMEA instance number then data type.
The following sections will explain how to configure each type of Signal Input.
1
2
3

## Page 46

46
EN / CZone Configuration Tool Instructions


4.5.1
Initial Settings
To begin adding inputs to the configuration, from the Signal Inputs tab select the ‘Add’ button.

1.
Enter the name of the signal device in the ‘Signal Input Channel Name’ box e.g. Fuel Tank. This name will be used for
this input on the Display Interface.
2.
From the ‘Signal Input Module’ drop-down list, select the Signal Interface, Combination Output Interface or Masterbus
Bridge Interface that the device is connected to.
3.
From the ‘Input Number’ drop-down list, select the physical input position to which the device is connected.
4.
Select the type of input for this position from the ‘Input Type’ drop-down list:
•
10-180 Ohm Sender - For inputs to devices that output 10-180 ohm signals.
•
240-33 Ohm Sender - For inputs to devices that output 240-33 ohm signals.
•
0-5V Sender - For inputs to devices that output 0-5 volt signals.
•
4-20mA Sender – For inputs to devices that output 4-20mA signals (COI Only)
•
Switch to Battery + - For utilising a standard mechanical switch which connects positive to the Signal interface
input when the switch is closed. This input type can be used to raise an alarm, or it can be configured on the
Circuits page to control a circuit output.
•
Switch to Battery -/Open circuit - For utilising a standard mechanical switch which connects negative or open
circuit to the Signal interface input when the switch is closed. This input type can be used to raise an alarm, or it
can be configured on the Circuits page to control a circuit output.
Note: Although we state the above industry-standard inputs, CZone® can accept inputs from 0-1000 ohm, 1000-0 ohm and
0-30 V DC.
5.
Select the output type of the device from the ‘Output Data Type’ drop-down list (Fluid level, Pressure, Temperature or
Trim).
6.
To calibrate a signal input for a Fluid Level, Pressure, Temperature or Trim input, click the ‘Edit Calibration’ button.
7.
To configure any alarms/switches for this input click ‘Alarm/Switch Settings.
1
2
3
5
7
6
4

## Page 47

EN / CZone Configuration Tool Instructions
47



4.5.2
Switch To Positive Alarm/Switch Settings
For every switch to positive input you can enable an alarm and a switch. The alarms (visual and audible depending on severity)
will be triggered on any Display Interface. The switches can be assigned to control any circuit configured on the Circuits tab.
For example, a bilge pump float switch could trigger an alarm for high water level and turn on the bilge pump.

1.
Tick the box next to the required alarm and/or switch to enable it.
2.
If a custom switching/alarm threshold is needed for the signal enter it here. The default is On at 8V and Off at 7V.
3.
If a delay is needed before the alarm/switch is triggered, enter the time in seconds in this box.
4.
If enabling an alarm, select the severity of the alarm from the drop-down list. (Refer to section 5.1 for more detail on
alarm severities.)
5.
Tick this box to invert the alarm. The alarm will then trigger when the switch is in the open position.
4.5.3
Switch To Negative Alarm/Switch Settings
For every switch to negative input you can enable an alarm and a switch. The alarms (visual and audible depending on
severity) will be triggered on any Display Interface. The switches can be assigned to control any circuit configured on the
Circuits tab. For example, a bilge pump float switch could trigger an alarm for high water level and turn on the bilge pump.

1.
Tick the box next to the required alarm and/or switch to enable it.
2.
If a custom switching/alarm threshold is needed for the signal, enter it here. The default is On at 1.5V and Off at 2V.
5
4
1
3
2
5
4
1
3
2

## Page 48

48
EN / CZone Configuration Tool Instructions


3.
If a delay is needed before the alarm/switch is triggered, enter the time in seconds in this box.
4.
If enabling an alarm, select the severity of the alarm from the drop-down list. (Refer to section 5.1 for detail on alarm
severities.)
5.
Tick this box to invert the alarm. The alarm will then trigger when the switch is in the open position.
4.5.4
Fluid Level Calibration

1.
Select the type of fluid for the input from the ‘Fluid Type’ drop-down list.
2.
Enter the tank capacity in the ‘Tank Capacity’ field.
3.
Check the box for the units that are to be used for calibrating. The units shown on a display can be changed through
the screen by the customer at any stage.
4.
NMEA 2000 Instances are used to differentiate between multiple fluid level sources. Ensure all NMEA 2000 Instances
are unique for each source being monitored. If Instances are assigned with the same value, the data may not be
displayed or may displayed inaccurately. If monitoring a fluid level from a non-CZone® NMEA sender on the network,
ensure the instance number matches the instance number on the sender.
5.
There are two ways to calibrate a tank: the Auto Table method, which prompts the user to input a number of tank
steps to calibrate to; or the Manual input method, which is more suited to a custom-shape tank where the user has
more flexibility on the number of level inputs. Both methods can be used with live data. The PC must be connected for
this functionality. To calibrate a signal using the manual table method, click on the ‘Add Point’ tab.
1
2
3
4
5

## Page 49

EN / CZone Configuration Tool Instructions
49



4.5.4.1
Manual Calibration Method

1.
Tick the ‘Use Live Data’ box if the PC is plugged into the CZone® network and the tank is being filled at the time of the
calibration.
2.
If using live data, the ‘Sender Output’ field auto-populate. (Check that this value changes as the level increases.) If live
data are not being used, and the output value of the sender for each level is known, manually enter those output
values in this field.
3.
If live data are being used then the ‘% of Capacity’ and ‘Fluid Level’ fields will auto-populate. If live data are not being
used, enter these values manually from the sender outputs at each level.
4.
Click OK to save calibration and to return to the ‘Fluid Level Calibration’ window. Click the ‘Add Point’ button on the
‘Fluid Level Calibration’ window to add another level point; repeat the process until full level is reached. (The ‘Table of
Calibrated Points’ will show the set levels as the calibration advances.)
5.
Click OK on ‘Fluid Level Calibration’ page to return to the ‘Signal Inputs’ window. This input is now configured and will
be shown in the ‘Configured SI Channels’ list.
Repeat the above process for further fluid level inputs.
To calibrate a signal using the Auto Table Method click on ‘New Auto Table’.
4.5.4.2
Auto Table Calibration Method

1.
Enter the number of calibration points that has been chosen for the tank (minimum 2, maximum 33). Click OK to save
the number, the ‘Fluid Level Calibration Auto Table’ window will open.
1
2
3
4
1

## Page 50

50
EN / CZone Configuration Tool Instructions



2.
 Tick the ‘Use Live Data’ box if the PC is plugged into the CZone® network and the tank is being filled at the time of
the calibration.
3.
Tick ‘Auto-Increment Level’ if the tank is symmetrical and the levels are all equal.
4.
If using live data, the ‘Sender Output’ field will auto -populate. (Check that this value changes as the level increases.)
If live data are not being used, and the output value of the sender for each level is known, manually enter those output
values in this field.
5.
If live data are being used and ‘Auto-Increment Level’ is ticked, the ‘% of Capacity’ and ‘Fluid Level’ fields will auto-
populate. If live data are not being used, enter these levels manually from the sender outputs.
6.
Use the “Set Point” tab when the output ‘% Capacity’ or ‘Fluid Level’ reaches a set point. Follow this process until all of
the values reach their highest points.
7.
Use the ‘Go back One Point’ button to remove a level set-point.
8.
The “Table of Calibrated Points’ will show the set levels as the calibration advances.
9.
Click OK to save calibration and return to the ‘Fluid Level Calibration’ window.
10. Click OK to return to the ‘Signal Inputs Channel Modification’ window. This input is now configured and will be shown
in the ‘Configured SI Channels’ list.
11. Click on the ‘Alarm/Switch Settings’ box.


5
8
3
2
4
6
7

## Page 51

EN / CZone Configuration Tool Instructions
51



4.5.4.3
Alarm/Switch Settings
For every Fluid Level input there are four levels of alarms/switches that can be enabled. The alarms (visual and audible
depending on severity) will be triggered on any Display Interface. The switches can be assigned to control any circuit
configured on the Circuits tab. For example, a low level fresh water tank switch can turn off the fresh water pump.

1.
Tick the box next to the required alarm or switch to enable it.
2.
Enter the On level, in % capacity or litres/gallons, at which you require the alarm/switch to be activated. (The unused
field will auto-calculate.)
3.
The Off value for the alarm/switch is greyed out by default. If you require this alarm/switch to be deactivated at a
different level, un-tick the ‘Use Default Hysteresis’ box at the bottom and enter a custom value.
4.
If a delay is needed before the alarm/switch is triggered, enter the time in seconds.
5.
If enabling an alarm, select its severity from the drop-down list. (Refer to section 5.1 for more detail on alarm
severities.)
6.
Select OK to save settings and return to the ‘SI Channel Modification’ window.
Select OK again to return to the ‘Signal Inputs’ page.
1
2
3
4
5
6

## Page 52

52
EN / CZone Configuration Tool Instructions


4.5.5
Temperature Level Calibration

1.
Select the type of temperature for the input from the ‘Temperature Type’ drop-down list.
2.
NMEA 2000 Instances are used to differentiate between multiple temperature level sources. Ensure that all NMEA
2000 Instances are unique for each source being monitored. If Instances are assigned with the same value, the data
may not be displayed or may displayed inaccurately.
3.
Choose the units that are to be used for calibrating. The units shown on a display can be changed through the screen
by the customer at any stage.
4.
Tick this box to enable high-temperature messages to be transmitted as a standard NMEA 2000 PGN for other NMEA
2000 displays to read.
5.
To calibrate a signal using the manual table method, click the ‘Add Point’ button.

1.
Tick ‘Use Live Data’ if the PC is plugged into the CZone® network and the temperature is able to be monitored at the
the time of the calibration.
1
2
5
4
3
4
1
3
2

## Page 53

EN / CZone Configuration Tool Instructions
53



2.
If using live data, the ‘Sender Output’ field, will auto-populate. (Check that this value changes as the level increases.)
If live data are not being used, and the outputs are known for the sender at each level, manually enter them in this
field.
3.
Enter the Temperature value for the given input value based on actual readings or the sensor’s output vs. temperature
chart.
4.
Click OK to save calibration and to return back to the ‘Temperature Level Calibration’ window, Click ‘Add Point’ to add
another level point, repeat this process until desired amount of calibration points is entered. It is recommended to
enter at least 5 calibration points for a linear output sender and as many as required for a non linear output sender.
5.
Click OK on ‘Temperature Calibration’ page to return back to the ‘Signal Inputs’ window, this input is now configured
and will be shown in the ‘Configured SI Channels’ list.
For Temperature Alarm/Switch Settings refer to the Fluid Level Alarm/Switch Settings section 0.
4.5.6
Pressure Level Calibration

1.
Select the type of pressure for the input from the ‘Pressure Type’ drop-down list.
2.
NMEA 2000 Instances are used to differentiate between multiple pressure level sources. Ensure that all NMEA 2000
Instances are unique for each source being monitored. If Instances are assigned with the same value, the data may
not be displayed or may be displayed inaccurately.
3.
Tick the box for the units that are to be used for calibrating. The units shown on a display can be changed through the
screen by the customer at any stage.
4.
To calibrate a signal using the manual table method, click on the ‘Add Point’ button.
3
1
2
4

## Page 54

54
EN / CZone Configuration Tool Instructions



1.
Tick ‘Use Live Data’ if the PC is plugged into the CZone® network and the pressure can be monitored at the the time
of the calibration.
2.
If using live data, the ‘Sender Output’ field will auto-populate. (Check that this value changes as the level increases.) If
live data are not being used, and the output is known for the sensor at each level, manually enter the outputs in this
field.
3.
Enter the Pressure value for the given input, based on actual readings or the pressure sensor’s output vs. pressure
chart.
4.
Click OK to save the calibration and return to the ‘Pressure Level Calibration’ window. Click ‘Add Point’ to add another
level point; repeat the process until the desired number of calibration points is entered. It is recommended to enter at
least five calibration points for a linear output sender, or as many as are required for a nonlinear output sender.
5.
Click OK on the ‘Pressure Calibration’ page to return to the ‘Signal Inputs’ window. This input is now configured and
will be shown in the ‘Configured SI Channels’ list.
For Pressure Alarm/Switch Settings, refer to the Fluid Level Alarm/Switch Settings section.
4.5.7
Trim Level Calibration

1.
Select the type of Trim Tab for the input from the ‘Trim Tab’ drop-down list.
2.
To calibrate a signal using the manual table method, click on the ‘Add Point’ tab.
4
1
3
2
1
2

## Page 55

EN / CZone Configuration Tool Instructions
55




1.
Tick ‘Use Live Data’ if the PC is plugged into the CZone® network and the trim is able to be monitored at the the time
of the calibration.
2.
If using live data, the ‘Sender Output’ field will auto-populate. (Check that this value changes as the level increases.) If
live data are not being used, and the output is known for the sensor at each level, manually enter the outputs in this
field.
3.
Enter the Trim % value for the given input, based on actual readings or on the sensor’s output vs. trim chart.
4.
Click OK to save the calibration and to return to the ‘Trim Level Calibration’ window. Click ‘Add Point’ to add another
level point; repeat the process until the desired number of calibration points is entered.
5.
Click OK on the ‘Trim Calibration’ page to return to the ‘Signal Inputs’ window. This input is now configured and will be
shown in the ‘Configured SI Channels’ list.
6.
For Trim Alarm/Switch Settings, refer to the Fluid Level Alarm/Switch Settings section 0.


1
2
3
4

## Page 56

56
EN / CZone Configuration Tool Instructions


4.6
CIRCUITS
The Circuits page is where a circuit is created by adding a circuit switch and a load. A Circuit must be created in order for the
load to be controlled by a switch or through a display. The Modes function is also configured on the Circuits page.
See Figure 5 for an example of the Circuits page on a completed system. If the ‘Create All Displays Circuit’ option was enabled
when adding loads to the configuration, his circuits list will be populated.
Figure 5
Circuits Tab Example
1.
Click on the ‘Circuits’ tab
2.
The configured circuit names in black are ‘Standard Circuits’. These names will be shown on the Control page of the
Display Interface.
3.
The configured circuit names in blue are ‘Modes of Operation’. These names will be shown on the Modes page of the
Display Interface.
4.
By default, the circuits are listed on the Display Interface alphabetically. To change the ordering, select ‘Custom’ from
the drop-down list and use the ‘Move Up’ and ‘Move Down’ buttons to achieve the desired ordering.
5.
The ‘Circuit Controls’ area is where all the switching devices are configured for the selected circuit. Multiple switches
can be added for each circuit e.g. a Cabin Light may have a switch from a Display Interface and also a mechanical
switch connected to a Signal Interface.
6.
The Modes Guru button opens a window which allows fast creation and editing of modes with the ability to export the
configuration to various file formats.
7.
The ‘Circuit Load’ area is where a load is configured for the selected circuit. Multiple loads can be added for each
circuit also. e.g. a Navigation Light circuit may turn on the Navigation Light and Anchor Light.
8.
The Test Circuit button allows a circuit to be tested on a live system
9.
To create a new Circuit, click the ‘Add’ button.
1
2
3
4
6
8
9
5
7

## Page 57

EN / CZone Configuration Tool Instructions
57



4.6.1
New Circuit Configuration

1.
Enter the circuit or mode name. This name will be shown on any configured Display Interface.
2.
Select the Circuit Type from the drop-down list. The options are:
•
Standard Circuit - All circuits that have at least one load or control switch. These standard circuits will
appear in the ‘Control’ menu on any display configured for that circuit.
•
Mode of Operation - Controls multiple loads, for example ‘Cruise’ mode may be configured to activate all
loads required to operate the vessel. Modes will appear in the ‘Modes’ menu on any display configured for
that circuit.
Modes are also grouped into four categories: Group 1, Group 2, Group 3 and Exclusive. If more than one mode is to
be used at a time, they need to be distributed among these groups. If only one mode is going to be used at a time, all
modes should be put in the same group. When switching between modes, the previously selected mode will be
deselected.
3.
Select a ‘Master Category’ to assign the circuit to a top-level category, in which it will appear on any controlling
display. This is the first level of control category when going to the Control page in the Display Interface. AC and DC
circuits are automatically assigned. Use the ‘Favorites’ category for any circuits that need to be accessed quickly.
4.
Select a ‘Sub Category’ to assign the circuit to a secondary category, in which it will appear on any controlling display.
This is the second level of control category when going to the Control page in the Display Interface. Selecting
appropriate categories for the circuit will make it easier to find a particular circuit, especially if many circuits are
configured e.g. a Bilge Pump could be categorised under ‘Pumps’.
5.
Select a ‘User Defined Sub-Category’ if there are no appropriate sub-categories that aptly describe the circuit. These
categories are configured on the Global Settings tab.
6.
Click this button to deselect all categories. Note: circuits that don’t have any categories selected can still be accessed
on the Control page of a Display Interface through the ‘All’ category.
7.
Click OK to save the Circuit Configuration Settings and return to the Circuits tab.
1
6
5
4
3
2
7

## Page 58

58
EN / CZone Configuration Tool Instructions



8.
The circuit name will be added to the Configured Circuits.
9.
Under ‘Circuit Controls’ click the Add button.
8
9

## Page 59

EN / CZone Configuration Tool Instructions
59



4.6.2
Switch Configuration

1.
Select the Module that the Controlling Device is connected to.
Note: To allow all displays to control a circuit, select ‘All Display Interfaces’. (It may not be desirable to allow critical
circuits to be controlled from all displays. For each such circuit, enter only the display that is required.)
2.
From the drop-down list, select the type of switch that is being used. This should match the physical switch that is
connected to the SCI, SI or COI. A Display Interface switch is a Double Throw Momentary. Note: If the physical switch
is a latching switch and a momentary switch type is selected, this switch will override all other switches controlling the
loads in this particular circuit.
3.
From the ‘Input/Throws’ drop-down list, select the Input channel and switching position of the controlling device. This
box will either appear as Switch Input (for SCI and SI inputs) or as Control Input (for Display Interfaces).
•
For SCI or SI Inputs, select the physical switch input for that circuit.
•
For Display Interfaces, select where you would like the circuit to be listed in the menu.
Control Menu – The Circuit will only appear in the Control Page of the selected Display Interface.
Control Menu & Fuel Tank – Allows the circuit to be listed in the Control menu and assigned to a tank monitoring
page. This is useful for pumps. For example a freshwater pump could be controlled from the freshwater tank
monitoring page, or a fuel transfer pump from the fuel tank monitoring page. If a tank has been configured, you can
select it here as an additional control menu.
4.
From the ‘Switch (Output) Function’ drop-down list, select the operation of the load that this circuit is controlling. Refer
to the explanation in section 4.6.2.1 for all available ‘Switch (Output) Functions’.
Note: The image of the controlling device, on the right-hand side of the page, will change to represent the different
settings of the above three selection boxes.
5.
If a double-throw switch has been selected you can reverse the throw functions by checking this box.
1
2
3
4
5
6
7

## Page 60

60
EN / CZone Configuration Tool Instructions


6.
Optionally enter the location of the controlling device in the ‘Switch Location’ box.
7.
Click ’Advanced Options’ for further settings.
4.6.2.1
Switch Output Functions
Single-Throw Latching
On/Off
The load is turned on when the switch is on and the load is turned off when the switch is off.
Toggle
Every time the switch is turned to the on position the state of the load is changed.
On
The loads will only be turned on when the switch is on and will not turn off when the switch is off.
Off
The loads will only be turned off when the switch is on and will not turn on when the switch is off.
Forward/Off
Will turn a motor channel on in the forward direction whilst the switch is on.
Reverse/Off
Will turn a motor channel on in the reverse direction whilst the switch is on.
Single-Throw Momentary
Toggle On/Off
Every time the switch is pressed the state of the load is changed.
Momentary On/Off
The load will be turned on only whilst the switch is pressed.
Single Button Dim
The output to the load will be increased or decreased when holding the switch down. Short press will
turn the load on or off.
Dim Up
The output to the load will be increased when holding the switch down. Short press will turn load on
full.
Dim Down
The output to the load will be decreased when holding the switch down. Short press will turn load off.
On(Reverse)/Off
Will turn a motor channel on in the reverse direction whilst switch is pressed.
On/Restore
Will turn a load on and then revert load to its previous state when switch is depressed.
Off/Restore
Will turn a load off and then revert load to its previous state when switch is depressed.
Step Up
Each press of the switch will increase the output to the load by 20%.
Step Down
Each press of the switch will decrease the output to the load by 20%.
On (Off
Configured
Elsewhere)
The loads will only be turned on when the switch is turned on.
Off (On
Configured
Elsewhere)
The loads will only be turned off when the switch is turned on.
Sequential
Allows a single switch to be used to scroll through up to five different circuits with each button press.
Double-Throw Latching
On/Off
Will turn the load on when the switch is in the on position and off when in the off position.
Double-Throw Momentary
On/Off
The load will be turned on when the switch is in one direction and then off when pressed in the
opposite direction
Dim Up/Dim Down
The output to the load will be increased when holding the switch down in one direction and a short
press will turn load on full. The output to the load will be decreased when holding the switch down in
the opposite direction and a short press will turn the load off.

## Page 61

EN / CZone Configuration Tool Instructions
61



Forward/Reverse
Will turn a motor channel on in the forward direction when pressed in one direction and in reverse
when pressed in the opposite direction.
Out/In
Same function as Forward/Reverse but labelled to suit the application.
Up/Down
Same function as Forward/Reverse but labelled to suit the application.
Open/Close
Same function as Forward/Reverse but labelled to suit the application.
Start/Stop
Same function as Forward/Reverse but labelled to suit the application.
On(Fwd)/Off(Rev)
Same function as Forward/Reverse but labelled to suit the application.
Step Up/Step
Down
Each press of the switch in one direction will increase the output to the load by 20%. Each press of
the switch in the opposite direction will decrease the output to the load by 20%.
Toggle Forward/
Toggle Reverse
Same function as Forward/Reverse but each switch direction is pressed once to turn motor on and
once to turn motor off.
Toggle Out/Toggle
In
Same function as Toggle Forward/Toggle Reverse but labelled to suit the application.
Toggle Up/Toggle
Down
Same function as Toggle Forward/Toggle Reverse but labelled to suit the application.
Toggle Open/
Toggle Close
Same function as Toggle Forward/Toggle Reverse but labelled to suit the application.
Toggle Start/
Toggle Stop
Same function as Toggle Forward/Toggle Reverse but labelled to suit the application.
Toggle On(Fwd)/
Toggle Off(Rev)
Same function as Toggle Forward/Toggle Reverse but labelled to suit the application

4.6.2.2
Switch Modification Advanced Settings

1.
Switch Priority allows a hierarchy of controlling devices to be set up, i.e. if a lower priority controlling device is being
held on and a higher priority controlling device is switched off then the circuit load will follow the command of the
higher priority off command and turn off.
2.
Tick the ‘Normally Closed’ box to allow normally closed operation of a controlling device.
7
2
3
5
6
1
4

## Page 62

62
EN / CZone Configuration Tool Instructions


3.
A switch can control a number of circuits. The ‘Systems On’ indicator shows the on/off state of these outputs. The
‘Systems On’ indicator can be configured as follows:
•
Systems On OR – Systems On indication when ANY of the loads in the circuit are on. (This is the default.)
•
Systems On AND – Systems On indication when ALL loads in the circuit are on.
4.
Tick this box to allow the controlling device to override any Timer delay functionality.
5.
When using a dimming switch output, tick this box to enable ‘Exponential Dimming’. This speeds up the dimming
process the longer a button is held down.
6.
If the switch is on a Display Interface, you can enable a User Confirmation Dialog box. If enabled, when turning the
switch ON or OFF a confirmation box will pop up on the screen; the switch state will not be adopted unless
confirmation is granted.
7.
Click OK to save advanced settings and return to the ‘Switch Configuration ‘ window.
8.
Click OK again to return to the Circuits tab.

1.
The switch just configured will now be shown under the ‘Circuit Controls’ window.
2.
Multiple switches can be configured for every circuit: to configure more switches, click ‘Add’ and repeat the above
process.
3.
When finished adding switches, click ‘Add’ under ‘Circuit Loads’ to begin configuring loads.
1
2
3

## Page 63

EN / CZone Configuration Tool Instructions
63



4.6.3
Load Configuration

1.
From the ‘Load’ drop-down list, select a load that the circuit will control. The Load list is auto-populated, in alphabetical
order, from the loads that are configured on the Loads tab.
2.
Select the state that the load is to be in when the circuit is switched on. The choices are On, Off, and % for a standard
load. Turning a load off may be necessary in speciality circuits or modes e.g. a Systems Off mode. % allows the load
to be turned on at a percentage of the full supply voltage; this can be used for lighting effects etc. For a motor output
the states available are Forward, Reverse, Off, Forward % and Reverse %.
3.
Tick ‘Follow Last New State’ if there are multiple loads that will be configured with the same load state. The next time a
load is added to the same circuit the state will default to the most-recently used state.
4.
Click the ‘Timer/Advanced Settings’ button to launch the ‘Circuit Load Timer/Cycling Settings’ dialogue:

1.
To enable a timer for the load, select the appropriate timer from the drop-down list. The function of each timer is
explained on the next page with a practical example.
2.
The timer resolution can be changed from seconds to minutes by clicking the required option-button.
•
When turned ON: OFF for a period, then ON for a period, then OFF
(Example: Keeping the cockpit lights on for a period of time after selecting ‘Dock’ mode)
Note if the first OFF period is not required then set it to 0.
1
2
3
4
1
3
4
5
2
6

## Page 64

64
EN / CZone Configuration Tool Instructions


•
When turned ON: keep OFF for a period
(Example: Delaying a bilge pump from turning on after the float rises)
•
When turned OFF: keep ON for a period
(Example: Running engine blowers after ignition is turned off)
•
When turned OFF: keep OFF for a cool-down period
(Example: Used for a load that must not be restarted for a period after it is shut down)
•
When turned ON: keep ON for a minimum warm-up period
(Example: Used for a load that must not be shut down during a start-up process)
3.
Tick this box to enable load cycling. When the circuit is turned on, this load will cycle on and off until the circuit is
turned off. The Cycle On and Cycle Off intervals can be adjusted to suit the application.
4.
The Control Type for the load can be changed to add limits (or lockouts). For example a hatch can be limited to 0%
when in cruise mode and then the limit can be raised to 100% when in dock mode. This would lock the hatch out in
cruise mode, so no switch could operate it until dock mode was activated.
•
Set State - allows the load to be turned On, Off or at a percentage of the full supply voltage. (This is the default.)
•
Set Limit – allows the load to be locked On, Off or at a percentage of the full supply voltage
•
Set State and Limit - allows the load to be turned On, Off or at a percentage of the full supply voltage, as well as
being locked at the chosen state.
•
Bidirectional Limit – allows reversing motor-output loads to be locked On or Off in both directions.
Important: When locking a load to OFF in a circuit, it is important to have another circuit to release that lock. Otherwise
the load will be locked in the OFF state until the network is reset.
5.
When two or more loads are added to a circuit, Control Directionality allows the load to be assigned to one direction of
a double-throw switch. This can be useful for a motor circuit that is controlling two solenoids instead of a reversing
MOI channel e.g. winches. The Up Solenoid Load would use the Forward Control Directionality and the Down
Solenoid Load would use the Reverse Control Directionality.
6.
Click OK to save settings and return to the ‘Circuit Load Configuration’.
7.
Repeat the Load Configuration process if any more loads are required for this circuit.
8.
When all loads are configured, press OK again to return to the Circuits tab.
The circuit is now complete. Repeat the New Circuit Configuration process to add more circuits.

## Page 65

EN / CZone Configuration Tool Instructions
65



4.6.4
Modes Guru
The Modes Guru is a user friendly and fast way to view, edit and create Modes of Operation.  Loads are presented in logical
colours to easily identify the state changes between Modes and can be edited directly by toggling the space bar or using the
copy and paste functions.  When Modes are finalized the configuration can be exported as a CSV or PDF file which can be
used in the vessels documentation or printed for the end user to reference.

4.6.5
Circuit Test
The ‘Test’ button on the Circuits tab allows any Circuit (Standard Circuit or Mode of Operation) to be turned On, Off or set to a
specific PWM level directly from the Configuration Tool.  This can be usefull when testing a circuit on a live system without
having to activate the circuit from a display or physical switch.
To control a circuit, ensure the laptop is connected to the network and all modules are online within the config tool.  Select the
desired circuit on the Circuits tab and then press the ‘Test Circuit’ button.  The following window will be shown.  Press the ‘On’
or ‘Set PWM%’ buttons to turn the circuit on. Press the ‘Off’ button to turn the circuit off.

## Page 66

66
EN / CZone Configuration Tool Instructions


4.7
AC MAINS
This area of the configuration will allow you to configure how the AC Mains control page is displayed on CZone® screens,
including source names, icons, monitoring parameters and layout. Auto-changeover of contactors can also be configured, by
setting priorites for each source. This section only needs to be completed if an ACMI is on the system. It can be completed off-
line. See Figure 6 for an example of the AC Mains page on the CZone® Touch Screen.
Important: Before setting up the AC Mains configuration, it is necessary to know how the contactors are wired and which source
each one is controlling. This schematic will be supplied with the ACMI. Please contact BEP Marine if you do not have a copy.
Figure 6
AC Mains Page Example


1.
Click on the ‘AC Mains’ tab.
2.
Click the ‘Add’ button.
2
1

## Page 67

EN / CZone Configuration Tool Instructions
67




1.
From the drop-down list, select the AC Mains Interface to be configured.
2.
From the drop-down list, select the Contactor to be configured. In this example it is labelled ‘AC Supply 1 for Load
Group 1’. If the contactors are not labelled then the custom ACMI code has not been read from the device. (Refer to
section 4.2.4 for this process.)
3.
Enter the ‘AC Supply Name’. This name will be shown on the Display Interface. The name should match the physical
input that supplies the chosen contactor. Please refer to documentation supplied with the ACMI to ensure the name is
correct.
4.
Select the Contactor Display Type associated with the input; this will be displayed on the AC Mains page. (See Figure
6 for examples of these icons.)
5.
From the drop-down list, select the Display Order in which this input will be displayed on the AC Mains page.
6.
Select the AC Meter associated with the input. If the AC Meter has not been configured, select ‘Add New’ and follow
the settings from section 4.3.3. If voltage and amps are configured they will be shown next to the contactor on the AC
Mains page. If Volts/Amps/Power/Frequency are configured they will be shown for the selected input on the left pane
of the AC Mains page (see Figure 6).
7.
If auto-changeover of contactors is required, from the drop-down list select the priority (1 - 6) for the chosen input. The
contactor with the highest priority on that load group will turn on when power is available, and any other contactors on
5
8
10
12
3
1
2
4
6
7
9
11
13

## Page 68

68
EN / CZone Configuration Tool Instructions


that load group will turn off. If the parallel option is selected, the parallel contactor will also be turned on and this input
will supply the second load group when power is available.
Important: An ‘Auto-Changeover Enable’ load is created for any inputs where a priority is set. For safety
reasons, these loads must be turned on in a circuit before any automation will take effect. Refer to Figure 7 for
an example of an ‘Auto-Changeover Enable’ load for Ships Power.

Figure 7
Auto Changeover Enable Load
The state of ACMI auto-changeover is shown on the Auto-Changeover field of the AC Mains page. See Figure 8 for an
example of the AC Mains page with auto-changeover active. Auto-changeover can be disabled by turning off the Auto-
Changeover Enable loads or by manually controlling one of the contactors. To resume auto-changeover the Auto-
Changeover Enable Loads must be turned on again.
8.
If a delay is needed between the system detecting that power is available and turning the contactor On, enter an Auto-
Changeover Delay in seconds. This could be useful for letting generators come up to speed before loads are
connected.
9.
If an alarm is needed when AC Supply is lost, select the alarm severity from the drop-down list.
10. The acceptance range is the percentage of the nominal voltage of the AC Meter (set in section 4.3.3). This value is
used to determine when power is available. The default value is 5%.
11. A pre-configured circuit can be used to turn on with the contactor. If required, select the circuit from the drop-down list.
12. To ensure a contactor remains open briefly before it is closed, configure a Break Before Make Delay (s).
13. Select OK to save the settings. Repeat the process for any further contactors.

The finished AC Mains tab is shown below:


Figure 8 AC Mains Tab

## Page 69

EN / CZone Configuration Tool Instructions
69



4.8
GENERATOR CONTROL
This section describes a method for controlling ship-board generators automatically. Each AC Mains Interface can control one
or two generators, in three possible modes:
1.
The Single configuration is for a vessel with one generator.
2.
The Dual Independent configuration is for a vessel with two generators to be operated independenly of each other.
3.
The Dual Alternating/Split-Bus configuration is for a vessel with two generators to be run one-at-a-time in an
alternating fashion, or together over a split AC bus when demand on a single generator exceeds a certain threshold.
All three modes support features such as safety interlocks and warm-up/cool-down intervals. (Safety interlocks are not
illustrated here but typically might prevent the generators from running without a coolant supply.)
Generator control was possible in previous CZone releases, but required a complex arrangement of logic blocks and other
configured elements. The approach here is both more powerful and less error-prone.
No additional hardware is required for Generator Control, on top of an existing AC Mains (ACMI) installation.
4.8.1
Hardware Requirements
Generator control applies to AC supplies and loads; this presupposes a minimum set of CZone modules. It is only relevant to
CZone systems equipped with at least one of each of the following:
•
an AC Mains Interface
The ACMI, with its high-voltage contactors, is a key module for selecting AC supplies and allocating their loads.
•
an Output Interface
Start and Stop generator control circuits require DC signals. These must be available via an OI at critical times.
•
a Display Interface
4.8.2
Configuring Generator Control: Dual Alternating/Split-Bus Example
The following example is representative of best-practice CZone configuration. It shows how to configure dual alternating/split-
bus generator control, for a vessel with port and starboard generators and one of each of the following modules:
•
an AC Mains Interface
•
a Display Interface
•
a Meter Interface
•
an Output Interface.
Other approaches are possible and sometimes necessary, but this will cover a majority of installations.
This is a lengthy and detailed example, deliberately so. Generator control is complicated - it links numerous CZone modules
with powerful machines and heavy loads - and must be configured carefully.
The sequence followed in the example here is:
1.
Configure the individual CZone modules.
2.
Configure metering.
3.
Define and configure start and stop circuits for each generator.
4.
Create a logic block, at this stage as a placeholder with no inputs. This logic block will specify the conditions for
requesting generator control; its inputs will be configured at step 6.
5.
Populate the generator control configuration dialogue, including the start and stop circuits from step 3 and the logic
block from step 4.
6.
Fill in the logic block from step 4, by creating circuits and signals required for its input conditions.

## Page 70

70
EN / CZone Configuration Tool Instructions


4.8.2.1
Configuring CZone Modules
AC Mains Interface
It is assumed that the ACMI has been configured by following section 4.2.4, and its contactors configured in accordance with
section 4.7. This example assumes AC supplies from only a port and a starboard generator, but generator control is still
possible where shore power or other sources are available too.
For the example given here, the ACMI Contactor Wiring Configuration, and the upper portion of the corresponding Configured
AC Mains Interfaces panel for the ACMI, are shown below:

Display Interface
Follow the instructions in section 4.2.3 to configure the vessel’s Display Interfaces. (The example here assumes only one.)
It is generally useful to provide manual overrides, for switching a vessel’s AC mains contactors from one or more DIs. When
configuring a DI that will have access to this feature, tick the Show AC Mains Control box in the Module Modification dialogue.
Meter Interface
Follow the instructions in section 4.2.1 to add and name the vessel’s Meter Interface/s. (The example here assumes only one.)
The supply to any MI that meters a critical DC source – such as a starter battery – should be hardwired not switched, so leave
its Switched Module/Network Power box unticked.

## Page 71

EN / CZone Configuration Tool Instructions
71



4.8.2.2
Configuring AC/DC Metering
Generator control logic will be dependent on AC monitoring in order to determine when a Generator has successfully started or
stopped. DC usually plays a part on Generator control logic as well, typically with the detection of a low voltge on the primary
House battery being used to trigger the generator on.
AC Supplies
To review the AC supplies, either:
•
on the Modules tab select the ACMI. The Module Configuration Details pane on the right will include the Contactor
Wiring Configuration. Expand this and note the AC supplies for all load groups.
OR
•
select the AC Mains tab. The Configured AC Mains Interfaces pane will show the same information as the Contactor
Wiring Configuration referred to above.

Follow section 4.3.3.1 to ensure an AC meter is defined for each generator that is to be placed under generator control. The
ACMI has AC metering channels of its own, or a Meter Interface can be used instead.
DC Supplies
A useful feature of generator control is to run a generator automatically when a battery needs charging; this requires metering
the battery. Some generators depend on DC supplies for pre-heat and other functions; to allow automatic generator control, the
state of these ancillary supplies must be known.
After identifying the DC sources required for generator control, follow section 0 to ensure a DC meter is configured for each
one. In the example here, the 12V house battery will be charged under generator control when necessary (including stopping
the generators when they are no longer needed). This battery is metered on channel 1 of the MI as shown below:

## Page 72

72
EN / CZone Configuration Tool Instructions


To activate battery charging under generator control, a switch is required at a low battery voltage; this switch is provided by the
MI that monitors the battery. Battery charging logic can be quite sophisticated but the example here is kept simple: the house
battery needs charging if its voltage falls to 12.2V; once charging commences it continues for a two-hour fixed cycle.
In section 4.3.1.5, configure a Low Voltage Switch to come on at 12.2V to signal that the house battery needs charging:

4.8.2.3
Configuring Generator Start/Stop DC Signals and Circuits
The example here assumes each generator is started or stopped via DC signals from an OI:
1.
On the Loads tab, click Add to launch the Load Configuration dialogue.
2.
Follow section 4.4.1 to make one of the four generator-start or -stop channels on the OI available as a named load.
Give the load a descriptive name (in the example below, Gen PT Start for the channel that is wired to the port
generator’s startup actuator). For simplicity the example here assumes a single OI, but a real vessel would probably

## Page 73

EN / CZone Configuration Tool Instructions
73



have more; use the Module and Channel drop-downs to ensure the correct OI and channel are selected. A 10A slow-
blow fuse would be typical. Other settings can be left at their defaults.

Repeat steps 1 and 2 above until all four loads have been configured - a start and a stop channel for both the port and
starboard generators. The upper portion of the Configured Loads pane on the Loads tab should then resemble the following:

Configuring Start/Stop Circuits., With Additional DI Control:
Follow section 4.6.1 to add a standard circuit for each of the generator start/stop functions. Assign descriptive names: for
example, Gen STBD Start or Gen PT Stop. (Long names should be avoided. For example, Port Generator Start will not fit on
the switch-description summary in the Switch Configuration dialogue.)
These circuits will typically be activated automatically by the generator control function being configured, but it can be useful to
provide a manual override for each one. The simplest way is to ensure the Add ‘All Displays’ Circuit Control box is ticked. (DI
switches are double-throw momentary; their switch function should be set to ‘On’, as the signals will be configured to turn off
automatilcally after a time.

## Page 74

74
EN / CZone Configuration Tool Instructions


On the Circuits tab, the upper portion of the Configured Circuits pane will now include the following entries:


Configure DC Loads for Generator Start and Stop Circuits
A load must be assigned to the start and stop circuit for each generator, so activating it will pulse the appropriate actuator
electrics.
1.
On the Circuits tab, select one of the generator-start or -stop circuits. In this example they are:
•
Gen PT Start
•
Gen PT Stop
•
Gen STBD Start
•
Gen STBD Stop
2.
Below the Circuit Loads pane, click Add to launch the Circuit Load Configuration dialogue. Having earlier configured
the Output Interface, its channels will be available as named loads; use the Load drop-down to assign the correct
channel (in this example, Gen STBD Start (DC) for the Gen STBD Start circuit):

## Page 75

EN / CZone Configuration Tool Instructions
75



Leave other settings at their defaults, but click Timer/Advanced Settings to launch the Circuit Load Timer/Cycling
Settings dialogue:

To tailor a pulse for the vessel’s start or stop electrics, consult its generator specifications. In this example, each pulse
needs no ‘front porch’ delay – it is sent immediately – and must last for 20s. Accordingly:
•
the Timer Function drop-down is changed to ‘When turned ON: OFF for a period, then ON for a period, then
Off.’
•
the ‘OFF for: (s)’ value is left at its default of 0
•
the ‘Then ON for: (s)’ value is set to 20.0.
Leave other settings at their defaults and click OK to close the Circuit Load Timer/Cycling Settings dialogue.
Click OK on the Circuit Load Configuration dialogue to close it and return to the Circuits tab.
3.
Repeat steps 1 and 2 above, until each of the four generator-start and -stop circuits has been assigned the
appropriate DC load. As an example, for the Gen STBD Start circuit the upper-left portion of the Circuits tab will then
resemble the following:

## Page 76

76
EN / CZone Configuration Tool Instructions


4.8.2.4
Create a Placeholder Logic Block for Requesting Generator Control
Follow the instructions in section 4.10.1 to create a logic block with the function OR. The inputs to this logic block will each
represent a condition underwhich the generator should be started. These condition will vary per installation and will often
represent the most complex part of the Generator Control configuration. We will leave them empty for now in order to move on
to the main Generator Configuration block which can now be completed.
A common example of the configuration of these logic inputs is given below in section 4.8.3.6.
4.8.2.5
Configuring Generator Control:
With AC Mains Contactors and their associated AC metering, Generator Start and Stop signals and their associated circuits,
and a place-holder Generator Run Condition Logic Block created, the generator configuration item  can now be populated. On
the AC Mains tab, below the Configured Generators pane click Add to launch the below Generator Control dialog:

1.
From the AC Mains Interface drop-down, ensure the correct ACMI is selected. (This example is for a vessel with only
one.)
2.
From the Generator Configuration drop-down, ensure the appropriate mode is selected. Use the Name field to give
the configuration a descriptive name. (In this example, the name is chosen simply to echo the generator-configuration
mode.)
3.
Each of the supplies available to an ACMI is presented on its designated contactor, which was given a descriptive
name when the ACMI was configured in section 4.8.2.1. (Supplies from the generators in this example appear on
ACMI contactors 1 and 2, labelled Gen PT and Gen STBD respectively.)
However, generator control only ‘knows’ the generators that it manages as Generator 1 and Generator 2. Those
internal names must therefore be tied to the physical contactors that will be managed under generator control.
Using the Generator 1 AC Mains Contactor drop-down, assign Generator 1 to the correct ACMI contactor: Gen PT in
this example. Do the same with the Generator 2 AC Mains Contactor drop-down: in this example, assign the
starboard generator. These assignments must match the contactor designations for which the ACMI was customised,
and in turn the vessel’s wiring.
4.
Assign the Gens RunUnderGenCtrl logic block using the Generator Run Logic drop-down.
1
6
3
4
2
7
8
9
10
11
5

## Page 77

EN / CZone Configuration Tool Instructions
77



5.
Using the appropriate drop-downs, assign the correct generator-start and -stop circuits to Generator 1 and
Generator 2.
Generator specific circuit controls will be automatically added to the selected circuits and visible on returning to the
Circuits listing once this configuration task is complete.
6.
The Overload/Split-Bus Threshold (kW) and Overload Time deterine the conditions under which both generators will
be run when the ‘Dual Alternating/Split-Bus’ configuration is selected.
Set the On threshold to the kilowatts of load at which both generators should be brought on-line and the supply bus
split between them.This should represent a significant percentage of the generator’s nomila power rating, e.g. 20kW
for a 25kW rated generator.
Set the Overload Time to the duration for which a single generator should carry the overload. When one generator
has been overloaded for longer than this it will be relieved, by bringing the second generator on-line and splitting the
AC bus. This delay intended to allow for short in-rush currents as larger AC loads are started, in order to not trigger
both generators ON when such a load is only temporary.
The Off threshold takes into account the demand on both generators once they are both running, such that when the
demand on both falls below a threshold, somewhere below the On threshold, the system will return to single generator
operation.
7.
Generators do not always start first-time, so set the Startup Tries to the maximum number of attempts. (If a generator
is needed but fails to start after this number of attempts, generator control will forgo splitting the bus.)
A startup attempt is considered to have failed if the generator is not on-line within the Startup/Failure Time. (This
interval is the total time allowed, from when the generator is commanded to start until its metered output should have
settled. It must therefore exceed the total of various other intervals: for example, generator pre-heat delay; the
duration of the longest timer used to pulse a start circuit; and the no-load settling time of the AC output.)
8.
Once a generator has started successfully, before being loaded it can be allowed to run open-circuit for a Warm-Up
Period with the intention of achieving a better service life.
Similarly, a generator can be configured to run open-circuit for a Cool-Down Period before being stopped.
9.
Generators can be started by different methods: automatically under generator control; with panel switches; from a
Display Interface; and so on. Regardless of how a generator was started, once started successfully it will be run for at
least the Minimum Run Time whether it is still needed or not.
Similarly, once a generator has been stopped it will not be available to be restarted for at least the Minimum Off
Time.
These two settings prevent rapid cycling of the generators in the case of inappropriately configured or erroneous
start/stop signals.
10. A generator that was started under generator control will be run for at most the Max. Auto Run Time; it will then be
stopped. This is a safety factor which can reduce wear and the risk of running fuel tanks dry, typically if a generator is
run unattended with the ‘Generator Run Condition’ rmaing true indefinitely.
In Dual Alternating/Split-Bus mode, before one generator is swapped for the other it will be run for at least the Min.
Run Time for Changeover. This prevents frequent alternating between the generators to ensure similar run-times for
each.
11. Click OK to accept the generator-control configuration. This configuration will now appear in the Configured
Generators pane on the AC Mains tab.
4.8.2.6
Configure ‘Run Generators Under Generator Control’ Logic
Preview: Conditions Which Make Generator Control Active
The system now ‘knows’ how generators are to be managed under generator control. It remains to be told when generator
control should be active.
1.
Once the generator configuration dialog has been completed, automatically created ‘Gen (Auto-Start/Stop Enable)’
signals, prefixed with the user-configured Generator Configuration name are made available to be added to Modes
and Circuits. These signals must be set to ON throught some means after reconfiguring or powering on a system, and
are typically added to all modes. They do not trigger the generators to come on or off directly, they simply indicate that

## Page 78

78
EN / CZone Configuration Tool Instructions


auto-generator control is enabled, thereafter relying on the user-configured run conditions being true for a generator to
actually run,
If the master enable signal is active, any of the user-configured conditions can activate generator control; conversely,
if it is inactive then generator control is unavailable regardless of any request for it.
2.
The inputs to the Generator Run Condition place holder logic block must then be filled in.The below example will
provide three conditions to this logic block:
•
The house battery was measured below 12.2V some time in the past two hours
That is: when the battery voltage goes low, generator control is invoked and remains on for a fixed, two-hour
charge cycle.
•
The time of day is between 0700 and 0800
That is: the generators are run daily for an hour regardless of any other requirement for them.
•
A manual user-controlled ‘Generator Run’ signal has been issued from a DI.
In this example we will user a circuit called ‘Generator Manual Control’. When turned On the generator
control will be requested to turn onactive regardless of the time of day or the state of the house battery.
o
turning it On will request that generator control becomes active
o
turning it Off will, in the absence of either of the other two conditions (low battery or time-of-day) will
result in the generator turning off once it has run for its minimum period..
If any of the three conditons is true then generator control will be requested; if none of them is true, it is not needed.
From section 5.2 this is recognizable as OR logic.
Create Loads, Logic and Circuits
Time-of-Day Switch State:
Follow the instructions in section 4.11.2 to create a Time-of-Day switch, on any available channel of the DI.
The example here uses On Time and Off Time of 0700 and 0800 respectively; accordingly it is named 0700to0800. The
Enabled on Power-Up box, on the Time of Day Switch Configuration dialogue, should be ticked.
Low House Battery Virtual Signal:
Follow the instructions in section 4.4.5 to create a virtual signal which will be activated to charge the house battery under
generator control.
The signal is created on a spare Virtual Signal channel of the OI. In the example here it is named Batt House Charge. (This
follows a convention of listing the type of controlling device first, then a qualifying identifier for the actual device, then the
function that is being controlled.)
Other settings, including those in the Load Configuration Advanced Settings dialogue, can be left at their defaults: there is no
associated alarm; and the signal should be Off at power-up.
Now f ollow the instructions in section 4.6 to create a new circuit named Low House Battery Signal.
Do not create an All Displays circuit control. Instead, as the sole circuit control, add the MI Control named
House Battery - Low Voltage; this will have been provided automatically by the MI when the low-voltage switch was configured.
Other settings can be left at their defaults: the Switch Type should be Single Throw Momentary and the
Switch (Output) Function should be On.
As the sole circuit load, add the Batt House Charge virtual signal which was created above. When this load is activated it
should remain on for the two-hour duration of the battery-charge cycle, so a timer must be configured for it. In section 4.6.3, in
the Circuit Load Timer/Cycling Settings dialogue, set the Timer Function to
When turned ON: OFF for a period, then ON for a period, then OFF. Set the Timer Resolution to Minutes and the value for
‘Then ON for’ to 120.0 (i.e. two hours).
Other settings can remain at their defaults.

## Page 79

EN / CZone Configuration Tool Instructions
79



Manual-Control Virtual Signal:
Follow the instructions in section 4.4.5 again, to create a virtual signal which will be activated when generator control is
requested via the DI.
The signal is created on a spare Virtual Signal channel of the OI. In the example here it is named Generator Manual Control.
Other settings, including those in the Load Configuration Advanced Settings dialogue, can be left at their defaults: there is no
associated alarm; and the signal should be Off at power-up.
Follow the instructions in section 4.6 to create a new circuit named Generator Manual Control.
Create an All Displays circuit control; this will be the only one for the circuit.
Most settings can be left at their defaults: DI switches are double-throw momentary; the switch function should be set to On/Off;
and this circuit would usually be managed from the Control menu. However, in section 4.6.2.2, in the Switch Configuration
Advanced Settings dialogue, change the User Confirmation Dialog drop-down to Confirm On and Off. This will raise a
confirmation dialogue when the user toggles the manual override switch.
Logic Block: Link Conditions to Request Generator Control
Now add the above created conditions/signals to the place-holder logic block:
•
Follow the instructions in section 4.10.2 to add, as the first input to the logic block, the load on the Time of Day switch.
From the Logic Input Type drop-down choose Data Switch; then, from the Data Switch drop-down, choose
DI - 0700to0800. The state of the input is On.
•
Follow the instructions in section 4.10.2 to add, as the second input to the logic block, the Batt House Charge load.
From the Logic Input Type drop-down choose Circuit Load/Virtual Signal; then, from the Circuit Load drop-down,
choose Batt House Charge. The state of the input is On.
•
Follow the instructions in section 4.10.2 to add, as the final input to the logic block, the Gens RunUnderGenCtrl (Mnul)
load. From the Logic Input Type drop-down choose Circuit Load/Virtual Signal; then, from the Data Switch drop-
down, choose Gens RunUnderGenCtrl (Mnul). The state of the input is On.
With the logic block configured, the upper-left portion of the Logic Blocks tab should resemble the following:

Enabling Auto Generator Start/Stop
Follow the instructions in section 4.6 to create a new circuit named Gens Auto-start/-stop Enable.
Create an All Displays circuit control; the DI will be the only place from where the master enable can be issued.
(Note: although a standard circuit is used here for illustration, typically the master enable would be more sophisticated. A vessel
would be configured for various operating modes, and any suitable mode would activate the master enable as a side-effect.
Modes where the generators might have no coolant supply would be excluded.)
Other settings can be left at their defaults: DI switches are double-throw momentary; the switch function should be set to
On/Off; and this circuit would usually be managed from the Control menu. However, in section 4.6.2.2, in the Switch
Configuration Advanced Settings dialogue, change the User Confirmation Dialog drop-down to Confirm On and Off. This will
raise a confirmation dialogue when the user toggles the manual override switch.

## Page 80

80
EN / CZone Configuration Tool Instructions


In section 4.6.3, as Circuit Loads add the low-level activation loads Dual Alternating/Split-Bus Gen 1 (Auto-Start/Stop Enable)
and Dual Alternating/Split-Bus Gen 2 (Auto-Start/Stop Enable). The settings for each of these circuit loads can be left at their
defaults: the State should be On; and there is no associated timer.
With all of the circuits now configured, the upper-left of the Circuits tab should resemble the following:

This completes the configuration. Save and then write this configuration to your systems and you will be ready to test it all out.
Turning On the ‘Gens Auto-Start/stop Enable’ Circuit, then waiting for either of the time of day or low battery conditions, or
turning on the ‘Generator Manual Control’ circuit, will now cause the generator to be run.
This example of generator control configuration is now complete

## Page 81

EN / CZone Configuration Tool Instructions
81



4.9
MASTERVOLT
The Mastervolt configuration page is where Mastervolt Inverters, Chargers and Combis are configured (using Masterbus
communication). Once configuration is complete these devices can be accessed from the Control > Inverters/Chargers page
from the Display Interface.
Note – DC-DC chargers are not currently displayed on Inverters/Chargers Page on a Display Interface.
In order to setup Mastervolt (Masterbus) devices:
•
a MasterBus Bridge Interface (MBI) must be installed and configured on the network; and
•
the Mastervolt devices must be powered and showing on-line in the Network Status field of the configuration tool.

Below are example screenshots of what you can expect on a CZone® Touch Screen, for a couple of common Mastervolt
devices (ChargeMaster and Mass Combi Inverter/Charger).

Figure 9
ChargeMaster Example

Figure 10
Mass Combi Example
Charger AC
Input
Charger
Control
Batterys
Charger
Status
Charger
Status
Charger
Control
AC
Input
Inverter
Control
Inverter
Status
AC
Output
Batterys

## Page 82

82
EN / CZone Configuration Tool Instructions


4.9.1
Mastervolt Device Configuration
To begin configuration of a Mastervolt device, from the Mastervolt tab select ‘Add’ in the Configured Mastervolt Chargers and
Inverters section.

1.
Enter the Device Name. This name will be shown on the Inverter/Charger control page on all Display Interfaces
connected to the system.
2.
Select an available metering channel for the Charger/Inverter Status from the MBI (MasterBus Bridge Interface). This
monitoring field will repeat from MasterBus the state of the Inverter and/or Charger e.g.Float/Absorption/Bulk. (See
Figure 9 and Figure 10 for examples.) The MBI has a total of 16 metering channels.
3.
Select the Mastervolt Device from the drop-down list. If the Mastervolt device is powered and on-line it will be shown in
this list. If the device is to be configured through MasterAdjust, select the ‘Configured in MasterAdjust’ option. Refer to
section 5.3 for a list of supported devices.
4.
Select the device type from the drop-down list. If a Mastervolt Device has already been selected, this field will be
configured automatically.
5.
The MasterBus Values will automatically populate from the MasterBus Index numbers referenced from the device
database. To edit these values press the ‘Edit MasterBus Values’ button.
6.
NMEA 2000 Instances are used to differentiate between multiple monitoring sources. Ensure all NMEA 2000
Instances are unique for each source being monitored. If Instances are assigned with the same value, the data may
not be displayed or may be displayed inaccurately.
7.
If configuring a Charger or Combi, select the AC Meter that will be used to represent the Charger Input. If the Charger
has the ability to monitor AC, select the ‘Add New’ option and follow section 4.3.4 for configuration steps; otherwise a
1
2
3
6
7
9
10
12
4
5
8
11

## Page 83

EN / CZone Configuration Tool Instructions
83



pre-configured AC Meter from a Meter Interface or AC Mains Interface can be used. Selecting ‘None’ will leave the
Charger Input field on the Display Interface unpopulated.
8.
If configuring an Inverter or Combi, select the AC Meter that will be used to represent the Inverter Output. If the
Inverter or Combi has the ability to monitor AC Output, select the ‘Add New’ option and follow section 4.3.4 for
configuration steps; otherwise a pre-configured AC Meter from a Meter Interface or AC Mains Interface can be used.
Selecting ‘None’ will leave the AC Output field on the Display Interface unpopulated.
9.
Select the DC Meter that will be used to represent battery for the Charger or Inverter. If the Charger or Inverter has the
ability to monitor DC, select the ‘Add New’ option and folllow section 4.3.2 for configuration steps; otherwise a pre-
configured DC Meter from a Meter Interface can be used. Selecting ‘None’ will leave the Battery field on the Display
Interface unpopulated. Repeat the process for second and third batteries if required.
10. If configuring a Charger or Combi, select the circuit that will be used for control of the charger. Selecting ‘Automatically
Assigned’ will automatically configure necessary MBI loads and circuits within CZone®, along with events on
MasterBus.
11. If configuring an Inverter or Combi, select the circuit that will be used for control of the inverter. Selecting
‘Automatically Assigned’ will automatically configure necessary MBI loads and circuits within CZone®, along with
events on MasterBus.
12. Select OK to complete the Mastervolt device configuration and return to the Mastervolt tab.

## Page 84

84
EN / CZone Configuration Tool Instructions


4.10 LOGIC BLOCKS
A logic block takes a user‐defined set of input/output states, drawn from the complete set of loads and switches already
configured within the system, and performs a logic operation (AND, OR, NAND, NOR, XOR, XNOR) on these states. This
generates a switch which can be used to control circuits and/or alarm when the condition has occurred.
4.10.1 Logic Block Inital Setup
For the below example we are going to set up a logic block that will activate an alarm when a hatch is open and the engine
ignition is on.

1.
Click on the ‘Logic Blocks’ tab.
2.
Click the ‘Add’ button.

3.
Enter a name for the Logic Block. In this example we are using ‘Fwd Hatch Open!!’. If an alarm is required when the
logic block is true, this is the name that will appear on any Display Interface.
4.
Select a module (OI, COI or SCI) from the drop-down list. To create a logic block, one of these three module types
must be on the network.
2
1
3
4
6
7
5
8

## Page 85

EN / CZone Configuration Tool Instructions
85



5.
Select the Logic Block Number from the drop-down list. An Output Interface (OI) can store up to six Logic
Blocks/Virtual Signals; a Combination Output Interface (COI) can store up to 32 and a Switch Control Interface (SCI)
can store up to 16.
6.
Select the Logic Type from the drop-down list. For a definition of each, refer to section 5.2. In this example we shall
use AND logic.
7.
To enable an alarm when the logic block is true, select the severity from the drop-down list. Refer to section 5.1 for a
definition of alarm severities.
8.
Click OK to save the Logic Block and close the Logic Block Modification window.

9.
The Logic Block that was just configured will be listed in the Logic Blocks section.
10. The next step is to add the inputs and configure their state. Click the Add button in the Inputs section.








4.10.2 Logic Block Input Configuration
Now that the logic block has been configured we need to add at least one Logic Input, which will form the conditions for making
the block’s output true or false.


9
10

## Page 86

86
EN / CZone Configuration Tool Instructions


1.
Select the Logic Input Type from the drop-down list. The available inputs that can be used for logic are:
•
Circuit Load/Virtual Signal
•
SI Switch
•
SCI Switch
•
Metering Switch
•
Data Switch
•
MasterBus Event Target
Note: To use a Data Switch (Time Of Day or PGN) as a logic input, the switch must be configured on the Circuits tab first.
The circuit does not need to be switching a load for it to be enabled.
2.
A full list of configured inputs will be displayed for the chosen input type. Select the required switch or load from the
drop-down list.
3.
Select the state of this switch or load: ON or OFF. This will form part of the logic check based on the logic type
selected earlier.
4.
Select OK to save the Logic Input Configuration.
5.
Repeat this process to configure further inputs.

The logic block is now complete. In this example we have created a logic block that will activate an important alarm when the
engine ignition is On AND the FWD Hatch sensor is Off (i.e. the hatch is open). Once the logic block is created it can also be
used as a switch on the Circuits tab. Refer to section 4.6.2 on adding switches to circuits. To find the configured logic block
switch, select the module (OI or SCI) that was used to store the logic block.
1
2
3
4

## Page 87

EN / CZone Configuration Tool Instructions
87



4.11 DATA SWITCHING
There are two types of data switch available within CZone®: PGN switch and Time of Day switch. To use either of these
switches a CZone® Display, Wireless Interface, COI or C1 must be on the network.
4.11.1 PGN Switching
All data transmitted on the NMEA 2000 network are organized into groups. These groups are identified by a Parameter Group
Number (PGN) which describes the type of data contained in that group. If the CZone® network is connected to other NMEA
2000 devices that transmit a standard NMEA 2000 PGN, it is possible to use the data from these PGNs to switch loads within
the CZone® network. See section 5.5 for a list of supported PGNs.
To configure a PGN switch, from the Advance>Data Switching>PGN Switching tab select ‘Add’ in the PGN switching section.

1.
Enter a name for the PGN switch. This is the name that will be displayed under the switching section when adding it to
a circuit.
2.
Select the Device to use for the PGN switch from the drop-down list. Important: the only devices that can be used for
data switching are the CZone® Displays, Wireless Interface, COI/Control 1, Control X and RV1.
3.
Select one of 15 available data switching channels per device.
4.
From the drop-down list, select the PGN Number that corresponds with the NMEA 2000 device that will be used for
switching.
5.
Select the Field from the drop-down list for the type of data that will be used for the PGN switch. This list will populate
according to the PGN Number selected previously.
6.
Select the NMEA 2000 Instance for the device that will be used for the PGN switch. Each NMEA 2000 device will have
a unique NMEA 2000 instance, set on the hardware itself or through software, to differentiate it from other NMEA 2000
devices on the network.
7.
Enter the required value of the data that will serve as the threshold for the PGN switch. The type of data will change
depending on the PGN and field that were selected previously.
8.
Select the Switch Type from the drop-down list. The options are Above Threshold, Below Threshold, Within Range or
Outside Range.
1
9
7
5
6
4
2
10
3
8

## Page 88

88
EN / CZone Configuration Tool Instructions


9.
The ‘Enable on Power‐Up’ check-box is ticked by default: the PGN switch is enabled. A PGN switch has an associated
load which is created automatically. Optionally, this load can be added to a circuit to enable and disable the switch
manually.
10. Click OK to complete the PGN switch configuration and return to the Data Switching tab.
Once the PGN switch is complete it can be used as a switch on the Circuits tab. When adding the switch, select the Display
Interface that it was configured on and the PGN name from the Control Input drop-down list . See Figure 11 for an example of a
PGN switch labelled Battery Temperature configured on DI - Touch Screen.

Figure 11
PGN Switch

## Page 89

EN / CZone Configuration Tool Instructions
89



4.11.2 Time Of Day Switching
A Time Of Day switch allows a circuit or multiple circuits to be turned ON and/or OFF at a particular time of day. In order to use
this feature, a CZone module with an internal clock or GPS must be on the network (CZone Displays or Wireless Interface).
When using one of these devices, ensure the date/time settings are correct. On the Display Interface, go to
Settings > System > Date Time, ensure all fields are correct and then click Save. This will synchronize settings to any other
displays on the network.
To configure a Time Of Day switch, from the Data Switching tab select ‘Add’ in the Time Of Day switching section.

1.
Enter a name for the Time Of Day switch. This is the name that will be displayed under the switching section when
adding it to a circuit.
2.
Select the Device to use for the switch from the drop-down list. Important: the only devices that can be used for time of
day switching are CZone® Displays and the Wireless Interface.
3.
Select one of 15 available data switching channels per device.
4.
Select the Time Format from the drop-down list. The options are 12-Hour or 24-Hour.
5.
Enter the On Time for the switch. This can be typed into the box, or adjusted using the up and down arrows.
6.
Enter the Off Time for the switch. This can be typed into the box, or adjusted using the up and down arrows.
7.
The ‘Enable on Power‐Up’ box is checked by default: the Time Of Day switch is enabled. A Time Of Day switch has an
associated load which is created automatically. Optionally, this load can be added to a circuit to enable and disable
the switch manually.
8.
Click OK to complete the Time Of Day switch configuration and return to the Data Switching tab.
Once the switch is completed it can be used as a switch on the Circuits tab. When adding the switch, select the Display
Interface that it was configured on and the Time Of Day name from the Control Input drop-down list.



1
2
5
6
7
3
4
8

## Page 90

90
EN / CZone Configuration Tool Instructions


4.12 THIRD PARTY DEVICES
The Third Party Devices tab allows supported devices to communicate with CZone over the NMEA2000 network. The
functionality varies dependent on device type, but control of these systems (such as Airconditioning and Watermakers) from
CZone displays is the primary function. The devices may require additional hardware if they are not NMEA2000 compatible.
4.12.1 Sea Recovery® Water Makers
NMEA2000 Sea Recovery Water Makers can be integrated on the CZone network and commands such as Start Production,
Start Flush, Start Rinse, Stop and Emergency break can be set using virtual signals built-in on the COI, OI or SCI. No additional
hardware is required as they are NMEA 2000 compatible.
Models Supported:
•
A14C Aqua matic Compact 450-1800 GPD
•
A15M Aqua matic modular 450-1800 GPD
•
A300C Aqua matic XL compact 2200-3400 GPD
•
A310M Aqua matic XL Modular 2200-3400 GPD
•
A93C Aqua whisper DX Compact 450-1800 GPD
•
A94M modular Aqua whisper DX  450-1800 GPD

4.12.1.1 Water Maker Set Up
To set up a Sea Recovery Water Maker, from the Third-Party Devics tab select Add


1.
Enter a name for the Watermaker or leave it blank for default name.

2.
Select the CZone device to use for virtual signal control (COI, OI, SCI) from the drop down list.

3.
Select an available Virtual Signal channel from the drop down list.

4.
Select or enter the instance of the Water Maker. Default should be 0 for a single Water Maker, if there is more than
one than the instance should match what is configured on the Water Maker.

5.
Tick this box if you would like Water Maker control to remain on during configuring or comms failure.

6.
Press OK to save the configured Water Maker.

The Watermaker is now set up and ready for virtual signals to be controlled from the Circuits tab.



3
1
2
4
5
6

## Page 91

EN / CZone Configuration Tool Instructions
91



4.12.1.2 Water Maker Control Configuration
To set up Water Maker control, go to the Circuits Tab and add a Load to an existing or new Circuit or Mode of Operation.



1.
Select the Water Maker configured in 4.12.1.1 from the drop down box.

2.
Select the desired Water Maker command from the drop down box. Options are Stop, Start Production, Start Flush,
Start Rinse and Emergency Break.

3.
Select ‘Timer/Advanced Settings’ to configure any timer options if required.

4.
Select OK to save the Load settings.

The Water Maker control is now configured. To add additional circuits to for other Water Maker commands repeat this process.

4.12.2 Dometic® HVAC
Dometic HVAC (Heating, Ventilation & Air Conditioning) units can be added to the CZone configuration and controlled using the
dedicated climate controls on CZone 2.0 Displays.  CZone supports marine and RV networked HVAC’s, both require an MBI
(Masterbus Bridge Interface) which acts as a gateway between the two networks.
Refer to CZone Dometic Instructions for complete integration instructions



1
2
4
3

## Page 92

92
EN / CZone Configuration Tool Instructions


4.12.3 Switch Bank PGN Control
Switch Bank PGN control allows CZone circuits to be controlled from a 3rd party device such as the Sentinel remote control
app.
To enable remote control functionality one of the following devices must be used: COI, Control 1, OI, SI, Contact 6 or Contact 6
Plus.  Each module allows up to 28 remote switches.

4.12.3.1 Switch Bank Setup

To enable remote switching, from the Third-Party Devices tab select Add from the ‘Switch Bank PGN Control’


1.
Enter a name to describe the first block of 28 remote switches or leave blank for the default name.

2.
Select the desired module to enable the block.

3.
Select a unique instance for each block from the drop down list (starting with 0).

4.
The ‘Advanced CZone remote control’ box should only be checked if the 3rd party device supports it.  By default, the
Switch Bank PGN only supports an On/Off switch function.  The advanced controls will allow all CZone switch
functions (mom, latching, dim up/down etc) to be used.

5.
Select OK to enable the first remote control block.

6.
Repeat steps above for adding more blocks (if 28 switches is unsufficient).

The Remote Control is now enabled.  The next step is to assign remote switches to the desired CZone circuits, go to the
Circuits tab, select a circuit and add a remote switch in the ‘circuit controls’ window.  Ensure the module configured above is
selected from the drop down.


3
5
1
2
4

## Page 93

EN / CZone Configuration Tool Instructions
93



4.13 SETTINGS
General Settings are used to configure the alarm circuits, and to define custom circuit display categories and various global
settings. Select the General Settings tab to access these functions.



1.
The ‘Alarm Circuits’ section allows a preconfigured circuit to be selected, to switch on when any alarm in any of the
alarm levels groups is triggered. This functionality allows for external lights and buzzers, to complement the visual and
audible alarms on the Display Interface/s.
2.
These are advanced options and should not be used without instructions from BEP Marine.
3.
‘Smooth Start’ is a visual effect option available for DC loads: it controls the rate at which these loads are turned on or
off. Adjust the ‘Smooth Start Startup Time’ to modify this rate. The default is two seconds.
4.
‘Minimum Dim Level’, sets the minimum dimming level allowable for diming circuits.
5.
The ‘User Defined Circuit Display Categories’ allow up to five custom circuit categories to be created. Once a new
category is created it will become available for selection from the circuits display catogories option.
6.
‘Long Press Delay’, set the delay time for all configured long button presses.
7.
‘Power User Login’, only accessible for ASG Power Users.
8.
The ‘Reset Network Config’ option requests all modules active on the network to erase their configurations. This
requires all modules to be repowered for the operation to complete.
9.
The ‘Reset NMEA 2000 Addresses’ option resets the NMEA 2000 source address for all modules active on the
network and forces them to claim new addresses.



1
3
4
6
7
9
4.13.1
4.13.2
5
8
2

## Page 94

94
EN / CZone Configuration Tool Instructions


4.13.1 Sleep Mode Settings
The Contact 6 PLUS, Control X, RV1 and Waterproof Keypad range include an ultra low current draw Sleep function.
Introduced in RTM20, CZone now supports Sleep Mode on all legacy CZone modues. Legacy modules have reduced current
draw in sleep but do not support the Ultra Low Current draw like C6Plus, CX, RV1. Displays are not yet supported.
By default, CZone Sleep is enabled. You can turn this off by unticking ‘Enable CZone Sleep’ on the ‘General Settings’ tab.
When sleep is disabled, the power button will still function as a back-light controller for the keypad and any other devices on the
same backlight group.

When enabled, a long press of the power button on a CZone Waterproof Keypad you can place all compatable modules on the
network to sleep. When asleep, all outputs turn off and the modules enter a low current draw state for conserving battery
power. You can wake up the devices via the power button or any button press on a Waterproof Keypad. The Control X and
RV1 have dedicated sleep switch inputs to wake the


4.13.1.1 Sleep Mode Circuits/Modes
Alternatively, you can configure the Sleep function to be activated by a Circuit or Mode.

1.
Add a new Mode of Operation, for this example we have created a ‘Systems Off’ mode.

2.
Add desired Circuit Loads to the mode.
1
3
2

## Page 95

EN / CZone Configuration Tool Instructions
95




3.
Set the desired state of each load.

4.
Select the Mode or Circuit you want to be triggered in the ‘CZone Sleep Circuit’ drop down on the ‘General Settings’ tab,
for our example we will select the ‘Systems Off’ mode we created.

5.
Enter a Sleep Delay if you want the system to wait for a defined period before going to sleep after triggering the Sleep
Circuit.























4
5

## Page 96

96
EN / CZone Configuration Tool Instructions


4.13.2 Configuration Password Protection
The Config Tool now has an option to password protect individual configuration files.  OEM’s can enable password protection to
prevent end users from editing configs which may negatively affect the operation or performance of the system.

To add a password:


1.
Password protection can be added to the configuration in the ‘General’ tab of the Config Tool.
2.
Select ‘Add Config File Password’.




3.
Follow prompts to add new passworld, select OK when finished.


1
2
3

## Page 97

EN / CZone Configuration Tool Instructions
97



Edit/Remove Password:

4.
To edit/remove password, select ‘Edit Config File Password’












5.
Enter existing password and follow prompts to either change or remove password, select OK when finished.







4
5

## Page 98

98
EN / CZone Configuration Tool Instructions


5 APPENDIX
5.1
ALARMS
Alarms are integral to the CZone® system. They are used to alert the user/owner to problems with the system and/or with
equipment on board. Alarms must be set up in order to function correctly.
Alarms can be visual, audible or both, depending on severity. Severities range from the basic ‘Systems On’ indication
that a circuit is functioning correctly, to ‘Critical’ where immediate action must be performed to avoid damage and/or a
catastrophic failure. Severity can be selected for each alarm. An overview of the alarm severities is shown in Figure
12, and an example of the Alarms page on a Display Interface is shown in Figure 13.
Alarm
Level
Bell
Colour
Action on Trigger
Additional Note
Critical
Red
Full-Screen Dialog
Audible Tone
Acknowledgement times out after 10 minutes then
re-alarms
Important
Orange
Full-Screen Dialog
Audible Tone
Acknowledgement times out after 10 minutes
Standard
Yellow
Full-Screen Dialog
Full-screen dialogue disappears once alarm is
acknowledged
Warning
Blue
Bell Appears
Bell disappears once alarm is acknowledged
Systems
On
N/A
Item Appears in
Systems Operation
List
Item disappears from list once the load is turned
off
Figure 12
Alarm Severities

Figure 13
Alarm Severities on Touch Screen

## Page 99

EN / CZone Configuration Tool Instructions
99



5.2
LOGIC TYPES
This section describes various logical connections that can be made between two inputs, A and B, and an output. Each
connection is described in four equivalent ways:
1.
in writing.
2.
using an electrical circuit in the form of ‘ladder logic’, comprising:
•
two inputs which together control the output. Each input is represented by a switch (or, in more-complex
circuits, two switches). A switch may be in one of two states:
o
closed (or ON):
. In this example the label shows that the switch affects input A.
o
open (or OFF):
. In this example the label shows that the switch affects input B.
•
the output, represented by a light-bulb:
. The bulb is lit i.e. the inputs as shown cause the output to be
ON.
3.
with a schematic symbol. Here the type of logic (e.g. AND or OR) is represented by the symbol’s shape. More-
complex functions may be represented by a unique symbol or a combination of simpler ones. In all cases the output is
on the right and the two inputs are on the left.
4.
in a truth table, again with the output on the right and the inputs on the left. The two inputs A and B may be combined
in four different ways. One combination is shown in each row of the truth table, together with the resulting output. Truth
tables use digits: 0 represents OFF, 1 represents ON.
5.2.1
AND
The output of the AND function is active only when input A AND input B are ON. That is, if any input is OFF then the output also
is OFF. The circuit representation, truth table and symbol for the AND function are shown in Figure 14.

Figure 14
AND Logic Example

## Page 100

100
EN / CZone Configuration Tool Instructions


5.2.2
OR
The output of the OR function is active whenever input A OR input B is ON. That is, to turn the output OFF all inputs must be
OFF. The circuit representation, truth table and symbol for the OR function are shown in Figure 15.

Figure 15
OR Logic Example
5.2.3
XOR
The output of the XOR function is only active when the inputs are different: one input must be OFF and the other ON. That is, if
the inputs are the same then the output will be OFF. (The ‘X’ in XOR is short for ‘mutually exclusive’.) The circuit
representation, truth table and symbol for the XOR function are shown in Figure 16.

Figure 16
XOR Logic Example

## Page 101

EN / CZone Configuration Tool Instructions 101



5.2.4
NAND
The NAND function is derived from a Not AND state; it is opposite in logic to the AND function. Its output is active when any
input is OFF. That is, to turn the output OFF, both inputs must be ON. The circuit representation, truth table and symbol for the
NAND function are shown in Figure 17.

Figure 17
NAND Logic Example
5.2.5
NOR
The NOR function is derived from a Not OR state; it is opposite in logic to the OR function. Its output is only active when both
inputs are OFF. That is, if any input is ON then the output will be OFF. The circuit representation, truth table and symbol for the
NOR function are shown in Figure 18.

Figure 18
NOR Logic Example

## Page 102

102
EN / CZone Configuration Tool Instructions


5.2.6
XNOR
The XNOR function is derived from a Not XOR state; it is opposite in logic to the XOR function. Its output is only active when
both inputs are the same. That is, if the inputs are different then the output will be OFF. The circuit representation, truth table
and symbol for the XNOR function are shown in Figure 19.

Figure 19
XNOR Logic Example

## Page 103

EN / CZone Configuration Tool Instructions 103



5.3
SUPPORTED MASTERVOLT (MASTERBUS) DEVICES
See below for a list of all Mastervolt (Masterbus) devices that can be configured automatically through the CZone®
Configuration Tool:

Device Name
Article #
Release
MasterShunt
77020100

MasterShunt
77020110
R16
MasterShunt
77020115
R16
Alpha Pro MB
45512000

Alpha Pro MB
45513000
R16
System Switch 6kW
55008005

System Switch 10kW
55008105

System Switch 16kW
55008205

Li-ion Battery
66020160

Li-ion 12/2500
66012500

Li-ion 12/5000
66015000

Li-ion 24/5000
66025000

MLI  Ultra 12/1250
66011250
R20
MLI  Ultra 24/1250
66021250
R20
MLI Ultra 12/2750
66012750
R16
MLI Ultra 12/3000
66013000
R20
MLI Ultra 12/5500
66015500
R16
MLI Ultra 12/6000
66016000
R20
MLI Ultra 24/5500
66025500
R16
MLI Ultra 24/6000
66026000
R20
Mass GI 3.5
88000350

ISO Mass GI 3.5
88000355

Mass GI 7.0
88000355

Mass Combi (via Serial Interface)
77030450

Mac/Magic DC-DC Converter (via
Serial Interface)
77030450

Mass Combi 12/1600-60 / 230V
36011600

Mass Combi 12/2200-100 / 230V
36012200

Mass Combi 24/1800-35 / 230V
36021800

Device Name
Article #
Release
Mass Combi 24/2600-60 / 230V
36022600

CombiMaster 12/3000-100 (230 V)
35013000
R16
CombiMaster 24/3000-60 (230 V)
35023000
R16
CombiMaster 12/2000-60 (230 V)
35012000
R16
CombiMaster 24/2000-40 (230 V)
35022000
R16
CombiMaster 12/800-40 (230 V)
35010800
R16
CombiMaster 24/800-300 (230 V)
35020800
R16
CombiMaster 12/500-30 (230 V)
35010500
R16
CombiMaster 12/800-40 (120 V)
35510800
R16
CombiMaster 12/1000-40 (120 V)
35511000
R16
CombiMaster 12/1500-60 (120 V)
35511500
R16
CombiMaster 12/2000-100 (120 V)
35512000
R16
CombiMaster 12/3000-160 (120 V)
35513000
R16
CombiMaster 24/2000-60 (120 V)
35522000
R16
CombiMaster 12/3500-200 (120 V)
35513500
R20
CombiMaster 24/3500-100 (120 V)
35523500
R20
CombiMaster 24/4500-120 (120 V)
35524500
R20
CombiMaster 48/5000-200 (120 V)
35545000
R20
CombiMaster 24/3000-70 (120V)
35523000

ChargeMaster 12/25-3
44010250

ChargeMaster 12/35-3
44010350

ChargeMaster 12/50-3
44010500

ChargeMaster 12/70-3
44010700

ChargeMaster 12/100-3
44011000

ChargeMaster 24/12-3
44020120

ChargeMaster 24/20-3
44020200

ChargeMaster 24/30-3
44020300

ChargeMaster 24/40-3
44020400

## Page 104

104
EN / CZone Configuration Tool Instructions


Device Name
Article #
Release
ChargeMaster 24/60-3
44020600

MAC Plus 12/12
81205100

MAC Plus 24/12
81205200

MAC Plus 12/24
81205300

MAC Plus 24/24
81205400

Mass Charger 24/15-2
40020156

Mass Charger 24/25-2
40020256

Mass Charger 24/25-2 DNV
40020266

Mass Charger 24/50-2
40020506

Mass Charger 24/75
40020756

Mass Charger 24/100
40021006

Mass Charger 24/100 3Ph
40031006

Mass Charger 48/25
40040256

Mass Charger 48/50
40040506

Mass Charger 12/60-2
40010606

Mass Charger 12/80-2
40010806

DDC Generator
77031600

Mass Sine Inverter
77030700

Mass Sine Ultra 24/4000
26024000

AC Power Analyser
77031200

Solar ChargeMaster 60
131906000

Mass Combi Ultra 48/3500-100
38343500

Mass Combi Ultra 24/3500-100
38023500

Mass Combi Ultra 12/3000-100
38013000

Mass Combi Pro 12/3000-150
38513000

Mass Combi Pro 24/3500-100
38523500

Alpha Pro
45513000

Mastershunt MKIII
77020110

Device Name
Article #
Release
ChargeMaster 24/80-3
44020800

ChargeMaster 24/100-3
44021000

ChargeMaster Plus 12/15-3
44310150
R16
ChargeMaster Plus 12/15-3
44310250
R16
ChargeMaster Plus 12/15-3
44310350
R16
ChargeMaster Plus 12/15-3
44320120
R16
ChargeMaster Plus 12/15-3
44310500
R16
ChargeMaster Plus 12/15-3
44310750
R16
ChargeMaster Plus 12/15-3
44311000
R16
ChargeMaster Plus 12/15-3
44311500
R16
ChargeMaster Plus 12/35
44310355
R20
ChargeMaster Plus 12/50
44310505
R20
ChargeMaster Plus 12/75-3
44310750

ChargeMaster Plus 12/100-3
44311000

ChargeMaster Plus 12/150-3
44311500

ChargeMaster Plus 24/12-3
44320120

ChargeMaster Plus 24/20-3
44320200

ChargeMaster Plus 24/40-3
44320400

ChargeMaster Plus 24/60-3
44320600

ChargeMaster Plus 24/80-3
44320800

ChargeMaster Plus 24/110-3
44321100

ChargeMaster Plus 24/40
44320205
R20
ChargeMaster Plus 24/30
44320305
R20
ChargeMaster Plus 12/15-3
44310150

ChargeMaster Plus 12/25-3
44310250

ChargeMaster Plus 12/35-3
44310350

ChargeMaster Plus 12/50-3
44310500

## Page 105

EN / CZone Configuration Tool Instructions 105



5.4
SUPPORTED MASTERVOLT (CZONE COMPATIBLE) DEVICES
See below for a list of all Mastervolt (CZone Compatible) devices that can be configured from the Modules tab in the CZone®
Configuration Tool:























Device Name
Article #
Release
Added
Mastershunt 500
77020115

ChargeMaster Plus 12/35
44310355
R18
ChargeMaster Plus 12/50
44310505
R18
ChargeMaster Plus 12/75
44310755

ChargeMaster Plus 12/100
44311005

ChargeMaster Plus 24/20
44320205
R18
ChargeMaster Plus 24/30
44320305
R18
ChargeMaster Plus 24/40
44320405

ChargeMaster Plus 24/60
44320605

ChargeMaster Plus 24/110
44321105

ChargeMaster Plus 24/80
44320805

CombiMaster 12V/2000 60A
35012000

CombiMaster 12V/3000 100A
35013000

CombiMaster 12V/800 40A
35510800

CombiMaster 12V/1000 40A
35511000

CombiMaster 12V/1500 60A
35511500

CombiMaster 12V/2000 100A
35512000

CombiMaster 12V/3000 160A
35513000

CombiMaster 24V/2000 40A
35022000

CombiMaster 24V/3000 60A
35023000

CombiMaster 24V/2000 60A
35522000

CombiMaster 24V/3000 70A
35523000

CombiMaster 24V/4500 120A
35524500
R20
CombiMaster 48V/5000 70A
35545000
R20
MLI Ultra Battery 12/2750
66012750
R16
MLI Ultra Battery 12/5500
66015500
R16
MLI Ultra Battery 24/5500
66025500
R16
MLI Ultra Battery 12/1250
66011250
R18
MLI Ultra Battery 24/1250
66021250
R18
Device Name
Article #
Release
Added
MLI Ultra Battery 12/3000
66013000
R20
MLI Ultra Battery 12/6000
66016000
R20
MLI Ultra Battery 24/6000
66026000
R20
Mac Plus 12/12-50
81205105
R21
Mac Plus 12/24-30
81205305
R21
Mac Plus 24/12-50
81205205
R21
Mac Plus 24/24-30
81205405
R21
Mac Plus 24/24-50
81205505
R21
Mac Plus 48/12-50
81203105
R21.1
Mac Plus 12/48-15
81203205
R21.1
Mac Plus 48/24-30
81203305
R21.1
Mac Plus 24/48-15
81203405
R21.1

## Page 106

106
EN / CZone Configuration Tool Instructions


5.5
NMEA 2000 PGNS SUPPORTED FOR DATA SWITCHING
PGN Number
Description
Fields
127503
AC Input Status
Voltage, Current, Frequency, Real Power
127504
AC Output Status
Voltage, Current, Frequency, Real Power
127505
Fluid Level
Fluid Level
127506
DC Detailed Status
State of Charge, State of Health, Time Remaining
127507
Charger Status
Operating State, Charger Mode, Charger Enable/Disable
127508
Battery Status
Battery Voltage, Battery Current, Battery Case Temperature
127509
Inverter Status
Operating State, Inverter Enable/Disable
127488
Engine Parameters
Engine Speed, Boost Pressure, Tilt/Trim
127489
Engine Parameters
Oil Pressure, Oil Temp, Engine Temp, Alternator Potential, Fuel
Rate, Total Engine Hours, Coolant Pressure, Fuel Pressure, Engine
Load, Engine Torque
129026
SOG
SOG
130312
Temperature
Actual Temperature
130314
Pressure
Pressure
128267
Water Depth
Depth

5.6
NMEA 2000 PGN’S TRANSMITTED FROM CZONE MODULES
5.6.1
Meter Interface
PGN Number
Description
Fields
127503
AC Input Status
Voltage, Current, Frequency, Real Power
127504
AC Output Status
Voltage, Current, Frequency, Real Power
127506
DC Detailed Status
State of Charge
127508
Battery Status
Battery Voltage, Battery Current
127744
AC P&C Phase A
AC Power and Current
127745
AC P&C Phase B
AC Power and Current
127746
AC P&C Phase C
AC Power and Current
127747
AC V&F Phase A
AC Voltage and Frequency
127748
AC V&F Phase B
AC Voltage and Frequency
127749
AC V&F Phase C
AC Voltage and Frequency

## Page 107

EN / CZone Configuration Tool Instructions 107



5.6.2
Signal Interface
PGN Number
Description
Fields
127505
Fluid Level
Fluid Level
130312
Temperature
Actual Temperature
130314
Pressure
Pressure
130316
Temperature, Extended Range


Actual Temperature

5.6.3
AC Mains Interface
PGN Number
Description
Fields
127503
AC Input Status
Voltage, Current, Frequency, Real Power
127504
AC Output Status
Voltage, Current, Frequency, Real Power
127744
AC P&C Phase A
AC Power and Current
127745
AC P&C Phase B
AC Power and Current
127746
AC P&C Phase C
AC Power and Current
127747
AC V&F Phase A
AC Voltage and Frequency
127748
AC V&F Phase B
AC Voltage and Frequency
127749
AC V&F Phase C
AC Voltage and Frequency

5.6.4
Combination Output Interface/Control 1
PGN Number
Description
Fields
127505
Fluid Level
Fluid Level
127508
Battery Status
Battery Voltage
130312
Temperature
Actual Temperature
130314
Pressure
Pressure
130316
Temperature, Extended Range
Actual Temperature

## Page 108

108
EN / CZone Configuration Tool Instructions


5.6.5
Masterbus Bridge Interface
PGN Number
Description
Fields
127503
AC Input Status
Voltage, Current, Frequency, Real Power
127504
AC Output Status
Voltage, Current, Frequency, Real Power
127505
Fluid Level
Fluid Level
127506
DC Detailed Status
State of Charge, State of Health, Time Remaining
127507
Charger Status
Operating State, Charger Mode, Charger Enable/Disable
127508
Battery Status
Battery Voltage, Battery Current, Battery Case Temperature
127509
Inverter Status
Operating State, Inverter Enable/Disable
130312
Temperature
Actual Temperature
130314
Pressure
Pressure
5.6.6
RV1
PGN Number
Description
Fields
127508
Battery Status
Battery Voltage, Battery Current
127506
DC Detailed Status
State of Charge, Time Remaining, DC Type
127505
Fluid Level
Fluid Level
130312
Temperature
Actual Temperature
130314
Pressure
Pressure
130316
Temperature, Extended Range
Actual Temperature
5.6.7
Control X
PGN Number
Description
Fields
127508
Battery Status
Battery Voltage, Battery Current
127506
DC Detailed Status
State of Charge, Time Remaining, DC Type
127505
Fluid Level
Fluid Level
130312
Temperature
Actual Temperature
130314
Pressure
Pressure
130316
Temperature, Extended Range
Actual Temperature
