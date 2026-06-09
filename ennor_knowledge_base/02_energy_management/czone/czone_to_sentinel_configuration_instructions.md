---
vessel: Ennor
title: "Czone to Sentinel Configuration Instructions"
category: "Energy Management"
source_pdf: "library_czone/Czone to Sentinel Configuration Instructions.pdf"
extraction_method: native
page_count: 5
converted: "2026-02-24"
---

# Czone to Sentinel Configuration Instructions

**Vessel:** Ennor | **Category:** Energy Management
**Source PDF:** library_czone/Czone to Sentinel Configuration Instructions.pdf | **Pages:** 5 | **Extraction:** native

---

Page | 1
CZone Sentinel Configuration Instructions v1.1
CZone Sentinel Configuration Instructions
The following instructions outline the steps required to configure and set up a CZone/Sentinel integrated system.  The Sentinel
boat monitor is a plug & play device providing remote access to a CZone equipped vessel for controlling circuits, displaying
monitoring data and repeating CZone alarms with the Sentinel iOS and Android mobile app.
PREREQUISITES

•
Sentinel Boat Monitor and CZone license (contact support@sentinelmarine.net for confirmation)
•
At least one CZone module supporting Switch Bank PGN (SI, COI, C1, OI, C6 or C6P)
IMPORTANT: firmware must be 6.15.08.0 or newer
•
CZone Configuration Tool R14 (Build 6.15.8.0) or newer
•
USB to CAN Adapter
•
Sentinel iOS or Android Mobile App
BASIC SYSTEM EXAMPLE

Page | 2
CZone Sentinel Configuration Instructions v1.1
1.
CZONE CONFIGURATION
1.
Open the desired CZone configuration in the CZone Configuration Tool and navigate to the ‘Third-Party Devices’ tab.

2.
In the ‘Switch Bank PGN Control’ window select ‘Add’


3.
Enter a name for the Switch Bank PGN or leave blank for the default name.

4.
Select the CZone module (from the supported devices) to enable the Switch Bank PGN.  Each device supports up to
28 remote switches.

5.
Select 0 from the ‘Switch Bank Instance’ drop down.  If more than one Switch Bank PGN is required then each
instance should be unique.

6.
Do NOT enable ‘Advanced CZone remote control’ for Sentinel integration.

7.
Select OK to enable the Switch Bank PGN and create 28 remote switches. Note: repeat these steps to create another
28 switches if required.

8.
Go to the Circuits tab and select the circuit you would like to add a remote switch.

9.
Under ‘Circuit Controls’ select ‘Add’.

10
12
11
13
5
7
3
4
6

Page | 3
CZone Sentinel Configuration Instructions v1.1
10. Select the Module configured in Step 4 from the drop down list.

11. Select one of the 28 remote switches from the drop down list.

12. Select ‘Single Throw Latching’ from the Switch Type drop down list.

13. Select the Switch Output Function from the drop down list.  For a standard circuit select ‘On/Off’. For a mode select
‘On’.

14. Select OK.

15. Repeat steps 8 to 14 for adding remote switches to other circuits.
2.
WRITE CZONE CONFIGURATION TO NETWORK
1.
Connect laptop to powered CZone network with the USB to CAN adapter.

2.
Open CZone Configuration and ensure all CZone modules are showing online.

3.
Ensure modules are updated to software 6.15.08.0 or newer.

4.
Ensure the Sentinel Boat Monitor is also plugged in to the network.

5.
Write the CZone Configuration to the network.
3.
ACTIVATE SENTINEL BOAT MONITOR
1.
Install the ‘Sentinel Marine Solutions’ mobile app (iOS or Android).

2.
Follow registration and activation instructions as outlined in the Sentinel installation manual supplied with the unit.

3.
Once the unit is activated and operating normally the Status LED will blink once every 3 seconds (full list of LED codes
are listed below).  This process may take anwhere from 10 mins to 2 hours depending on cell reception and whether
there are any firmware updates.  Please allow some time for this process.


Status LED Codes
Blinks
State
1
Normal Operation
2
No GPRS Signal, communication not possible
3
Supply Disconnected
Continuous
GPRS Communication active

Status LED

Page | 4
CZone Sentinel Configuration Instructions v1.1
Track LED Codes
Blinks
State
1
Normal Operation
2
No GPS Signal
Continuous
Acquiring new record

Page | 5
CZone Sentinel Configuration Instructions v1.1
4.
SWITCH CONFIGURATION
If everything is configured correctly, switches should automatically appear on the switches page.  It may take up to a minute for
the device to download the configuration and switch names.
Note: If you reconfigure CZone and need Sentinel to update switches and switch names, you can select ‘Refresh CZone
Configuration’ from the menu on the switches page
5.
NMEA SENSOR CONFIGURATION
