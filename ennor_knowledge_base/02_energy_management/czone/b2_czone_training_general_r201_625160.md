---
vessel: Ennor
title: "B2 CZone Training General R20.1 6.25.16.0"
category: "Energy Management"
source_pdf: "library_czone/B2 CZone Training General R20.1 6.25.16.0.pdf"
extraction_method: native
page_count: 137
converted: "2026-02-24"
---

# B2 CZone Training General R20.1 6.25.16.0

**Vessel:** Ennor | **Category:** Energy Management
**Source PDF:** library_czone/B2 CZone Training General R20.1 6.25.16.0.pdf | **Pages:** 137 | **Extraction:** native

---

## Page 1

©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
B2 Technical Training
2022

## Page 2

| 2
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
©2022 Advanced Systems Group
by Brunswick Co. Confidential and
all rights reserved.
| 2

Configuration Tool

Fault Finding & Diagnostics

Firmware Updates

Favourites

## Page 3

| 3
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
3
Configuration Tool
R20.1 6.25.16.0

## Page 4

| 4
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
New System Configuration
Modules
•
Add all modules to be installed in the system.

## Page 5

| 5
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Modules
When connected live, dipswitch will be detected.  If offline, assign a Dipswitch.
Each module has different settings that can be configured.
Displays should have ‘Switched module/Network Power’ selected.  This will stop an alarm/loads.
shutting down on the system if the display is switched off.
Used if you have already configured
Dipswitches and connected live.

## Page 6

| 6
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Can only be selected after
‘Power Metering’ has been completed
Gives control over DSB switch
Backlighting zones
Modules - COI

## Page 7

| 7
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Modules - ACMI
These will be pre-configured from factory
and do not need to be changed.
Shows loaded CPLD in the
ACMI from factory
Name Load groups to be
Used later in configuration

## Page 8

| 8
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Modules - DI
This changes buttons on displays to single control.
Mostly used for IPAD Configurations.
•
Single button Dim
•
Single button toggle
•
Useful in 5” Touch new UI
De-select this to clean up display if not using
ACMI – This will remove the selection from screen

## Page 9

| 9
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Modules - MasterShunt
Name Shunt to correct battery (visible meter name)
Set correct amp hour capacity
Dipswitch relates to physical dipswitch on shunt, after the initial
CZone enabled dipswitches configured.
Configure correct battery type and nominal voltages

## Page 10

| 10
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Modules - MasterShunt
Changes automatically
Show temperature
Parallel or single unit
Reverse direction of shunt (without physically changing wiring)
Metered DOD showing %
Determines reset current of Meter (2.5% - 4% of total AH)
These determine reset of the CZone SOC meter
•
Peukerts for correct long term battery information
•
Float voltage should be set just LOWER than charger float voltage
•
Absorption voltage should be set the SAME as charger abs voltage

## Page 11

| 11
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Use DOD% Masking to
give the customer
better vision of the state
of the battery capacity
Modules – SOC%
80% DOD = 20% Buffer hidden
User sees 100% - 0%
No Buffer

## Page 12

| 12
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Modules – MasterShunt
Set high and low voltages
Set alarm priority levels
Used for additional switching in CZone if required
Low and Pre-Low alarms should be set to match Battery Type
Set alarm priority levels
Blown fuse detection alarm

## Page 13

| 13
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Modules – Charge Master Plus
Model Type
Battery type and Current limit if required
Dipswitch relates to physical dipswitch on unit, after the initial
CZone enabled dipswitches configured.

## Page 14

| 14
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Modules – Charge Master Plus
14
Charge characteristics
Smart terminal output.  Refer to Mastervolt
user manual of model for descriptions.
Different options will add more items
Label outputs as required
I.E House Battery, Start Battery, Radio Battery
Greyed out items will only be able to be
modified if ‘User Defined’ battery type is
selected in previous window

## Page 15

| 15
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Modules – Charge Master Plus
Reverse polarity alarm for DC installation
High Charger Temp Alarm
AC Input out of range alarm
Configured Shunt (If applicable) not selected correctly
Temperature sensor fault

## Page 16

| 16
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Modules – Combi Master
Model Type
Battery type and Current limit if required
Dipswitch relates to physical dipswitch on unit, after the
initial CZone enabled dipswitches configured.

## Page 17

| 17
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Modules – Combi Master
External contacts on unit.
Alarm:  Fault detected, alarm contacts operate
Power level:
<Power level N/O – Com Connected
>Power level N/C – Com Connected

## Page 18

| 18
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Modules – Combi Master
Set output frequency of the unit
AC Input window large voltage range or narrow
Low power mode (less than 20W for 20 sec)
Uses battery to support external AC MCB tripping
Name AC IN and AC OUT loads
I.E Inverter Circuits

## Page 19

| 19
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Modules – Combi Master
Defines when unit will switch off based
off battery voltage (refer user manual)
Greyed out items will only be able to be
modified if ‘User Defined’ battery type is
selected in previous window

## Page 20

| 20
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Modules – Combi Master
Unit overload alarm
Unit over temp alarm
Unit fault other than the ones listed
I.E Fan Fault
Greyed out items will only be able to be modified if
‘User Defined’ battery type is selected

## Page 21

| 21
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Modules – MLI Ultra
Model Type
Dipswitch relates to physical dipswitch on unit, after the
initial CZone enabled dipswitches configured.
Name to be displayed

## Page 22

| 22
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Modules – MLI Ultra
Determines what configuration is being set for the Safety switch.
ML Switch:  Used for most cases
Daisy chain:  Used when combining batteries for a series system
Advanced:  Used for configuration without BSS Safety switch
Display Battery Temperature

## Page 23

| 23
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Modules – MLI Ultra
Can be used to switch a circuit at 100% SOC
Low voltage and alarm
Set low-capacity alarm level.
Can also be used in circuits as a switch
Set very low-capacity alarm level.
Can also be used in circuits as a switch
Additional SOC switches
I.E To set custom alarm indicators

## Page 24

| 24
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Modules – MLI Ultra
SOC can drift in Liion calculation so batteries
should be charged to 100% periodically.
Can be used to switch a circuit in CZone
I.E Turn on charger
Set temperature levels to use as switches in circuits if
required.
I.E Turn on fans
Indicates Battery safety has occurred
Battery is being discharged with too much current >600A 30s
Battery safety relay is faulty alarm
Hardware fault with battery

## Page 25

| 30
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Summary
30
New configuration; Vessel name, vessel number, revision, date.
Add all modules used in the system, including MFD’s.
Modules must have a dipswitch set to be able to be seen on network.
‘Switched module, network power’ for all Displays, especially MFD’s.
‘All displays = ON/OFF Toggle or Single Button Dim’ if required.
If using standalone Mastervolt/CZone compatible power electronics, ensure to set
dip switches for CZone
Set all parameters required to ensure configuration processes correctly through
configuration tool I.E Metering

## Page 26

| 31
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Meters
Add DC or AC Meters as required to be displayed on Monitoring page on Display/s:

## Page 27

| 32
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Meters - DC
Which Metering device is this configured to.
Changes on its own.  Useful for larger configuration files.
Selects how meter is displayed within CZone/Third Party.
No change to CZone configuration.
What should be displayed on monitoring page.

## Page 28

| 33
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Meters - DC
Set Voltage alarms and severity levels.
Set switches to be used in CZone
configuration.
Enable load shedding if required:
‘Load-Shed on Voltage’
‘Load-Shed on Capacity’

## Page 29

| 34
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Meters - DC
Changes internal calculation settings,
required for long term accuracy.
Required for long term accuracy.
Should be set between 2.5 - 4%
of total battery capacity.  Default 5.0A
Must be set below float voltage of system.
Default 13.5 VDC
Determines when Peukerts Cof should be
used.

## Page 30

| 35
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Meters - DC
Example:
440 A/H, 12VDC Bank
18 Amps reset current (4%)
On Charge
Off Charge/High
Load

## Page 31

| 36
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Meters – DOD%
80% DOD = 20% Buffer hidden
User sees 100% - 0%
No Buffer

## Page 32

| 37
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Meters - AC
Which Metering device is this configured to.
Make instance the same if using Multiple phase
monitoring.  This will allow screens to show multiple
lines in the same text box.
Adjust to suit installation I.E 120VAC 60Hz
This is how the message is displayed on 3rd Party
MFD’s. (PGN’s)
Used for newer PGN standards (Some Raymarine).

## Page 33

| 38
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Meters - AC
Set Voltage Error alarms and severity.
Set Voltage Error switch for use in CZone.
Useful for logic or additional switch requirements.
(Uses voltage Error and Frequency error %)
High Power and low power alarms and/or
switches can also be set and configured for use in
the configuration.
De-select checkbox to create your own cut in /
cut outs.
Invert Alarms/allow on open circuit (rarely used)

## Page 34

| 39
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Meters - AC
If Combi Master has been installed and configured through CZone and modules page:
This will be automatically configured

## Page 35

| 40
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Meters - MasterShunt
If Mastershunt has been installed and configured through CZone and modules page:
This will be automatically configured

## Page 36

| 41
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Meters – MLI Ultra
If Mastervolt Liion Battery has been installed and configured through CZone and modules page:
This will be automatically configured

## Page 37

| 42
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Summary
42
Configure Power Metering to setup the ‘Monitoring’ page on CZone display
Setup Voltage and capacity alarms witch correct severity levels.
Both AC and DC if using.
Configure all battery parameters, Reset volts, Amps, Peukerts and Efficiency!
If using Mastervolt/CZone power electronics, ensure all text is correct on
modules tab.  This is what will be shown as a meter on the display.

## Page 38

| 43
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Inputs
Select input type, (0-1000Ohm, 0-32VDC):
10-180 Ohm (0-1000 Ohm)
240-33 Ohm (0-1000 Ohm)
4-20mA (COI Only)
Positive (0-32VDC)
Negative
Output data type relates to PGN display on MFD
Name of Input – will be shown on CZone display
Location of Input wiring

## Page 39

| 44
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Inputs
Set tank Capacity first

## Page 40

| 45
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Inputs
Use live data when connected to system for
most accurate filling points.
De-selecting checkbox allows manual value
input.
Set Point to move to next calibration value.

## Page 41

| 46
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Inputs
Set alarms to be displayed and switches
to use via CZone configurations.
Alarms are not active until selected!

## Page 42

| 47
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Inputs
Switch to Batt + or – changes Alarm switch
settings.
Add delay directly and configure switching points,
(default shown).
If using a N/C Switch.

## Page 43

| 48
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Inputs
Not used for regular configurations.
This is specific to ‘Airstream’ configurations.

## Page 44

| 49
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Inputs
Ability to add ‘Third party NMEA’ sender directly to inputs.
Sender should be calibrated already and will be displayed through CZone
Instance, Data type and Fluid type should be matched to configured sender

## Page 45

| 50
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Summary
50
Label inputs.
Select Input type and data type.
Calibrate tank level if required.
Configure alarms and switches.

## Page 46

| 51
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Loads
Label what is actually wired to the output.
Select Module and Output load is wired too.
Creates a circuit automatically.
(De-selecting this will disable it for future loads)
Fast, Slow, Motor Start (B, C or D-Curve ratings).
Soft fuse rating should be set to nominal fuse rating
of load / wiring

## Page 47

| 52
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Loads
Load shedding if previously configured:
‘Turn off first LOW’ or ‘Turn off last VERY LOW’ VDC or
SOC
Used for Non-Critical loads to create visual dim up and dim
down effect when turned ON and OFF.
Uses PWM to soft start load.
*First 4 channels of COI do not have PWM/Soft start Control*
CZONE CONFIGURATION - LOADS

## Page 48

| 53
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Loads
Not applicable on the OI, COI only.
Disables alarm.
Not applicable on the OI.  COI first 4 channels only.
Enable to allow alarm, if feedback detected.
Select this for critical circuits.
If load was ON and data lost, load will remain ON.
What state should the load be in if CZone network is
re-powered.  Default OFF.
CZONE CONFIGURATION - LOADS

## Page 49

| 54
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Loads
Only configure if using Systems ON / Low run current
alarms.
Switch or alarm will activate if CZone detects MORE
than 80% of nominal setting.
Switch or alarm will activate if CZone detects LESS
than 80% of nominal setting.
Select channel if parallel wiring a load.
I.E Load requires 50 amps (2x 25A Outputs)
If current calibration required.  Default out of factory.

## Page 50

| 55
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Summary
55
Label loads.
Set soft Fuse rating and install physical Fuse one rating above this.
Enable ‘Smooth start’ to Interior and Exterior non-essential lighting for added effects.
Program advanced settings as required.

## Page 51

| 56
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits
Circuits take all configured Loads, Inputs, Logic etc and create the operation of the system.
Configured Circuits
=
Circuit controls +
Circuit loads
+
Flood Lights

## Page 52

| 57
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits
These can be seen by the user – or just be a background control.
Standard Circuit or Mode.
Blue denotes ‘Mode of operation’
Black denotes ‘Standard circuit’

## Page 53

| 58
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits
Select for additional filtering
Sub categories help with further filtering
Configure your own ‘user defined’
categories I.E ‘Bilge pumps’.
*You will have this option when you configure Loads

## Page 54

| 59
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits
Mode Groups:
Means you can have more than one mode on at a time, up to 4.
Usually, all modes will be under one Group.
I.E
•
DAY CRUISE
•
NIGHT CRUISE
•
DOCK UNATTENDED

## Page 55

| 60
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits
If ‘All display interfaces’ is selected, the ‘Circuit Name’ is written will show
on ‘All displays’
This means that the configured circuit can be operated on all configured
displays
You can select dedicated displays for that circuit only to be shown on

## Page 56

| 61
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits
Software switches can be configured to any type and allow
many different functions within the CZone configuration tool.
*A ‘momentary’ will always over-ride a ‘Latching’*

## Page 57

| 62
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits
Software switches can be configured for any output function.
Software should be matched to physical switch where installed.

## Page 58

| 63
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits
When the Circuit control is operated – what state
should the load change to:
•
ON
•
OFF
•
ON – To a % of the maximum using PWM

## Page 59

| 64
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits - Timers
Select ‘Timer/Advanced Settings’ to add timers

## Page 60

| 65
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits - Timers
“When turned ON:  OFF for a period, then ON for a period, the OFF”

## Page 61

| 66
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits - Timers
Timers:  “When turned ON:  Keep OFF for a period”

## Page 62

| 67
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits - Timers
“When turned OFF:  Keep ON for a period”
Additional:
After being On for at least….

## Page 63

| 68
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits - Timers
Timers:  “When turned OFF:  Keep OFF for a cool down period”
Additional:
After being On for at least….

## Page 64

| 69
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits - Timers
Timers:  “When turned ON:  Keep ON for a minimum / ‘warm-up’ period”

## Page 65

| 70
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits - Limits
On:
Load turns ON.
Off:
Load turns OFF.
On %: Turns on and adjusts the load to a %

## Page 66

| 71
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits - Limits
Disable Output: Load cannot be operated
Remove Limit:
Removes limit that was previously activated in another circuit
Limit %:
Limits the use of this load to a maximum %

## Page 67

| 72
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits - Limits
Disable and Turn Off: Turns load OFF and Load cannot be operated.
Enable and Turn On: Load can be operated and Turns load ON
Set and Limit %:
Turns the load state to a maximum %

## Page 68

| 76
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits - Modes
Modes should always be controlled by an ‘On’
switch. An ‘OFF’ Mode – is turned ‘On’
You never turn OFF a mode, you just switch to
another one!
Add ALL of the loads required to be ‘ON’ or
‘OFF’ in this mode.  You can also add timers
and % on (Dimming) – One Touch

## Page 69

| 77
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits – Modes Guru
Easy adding of loads / timers etc.  Save as PDF and print out for customer / owner.

## Page 70

| 78
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits - Modes

## Page 71

| 79
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits - Modes

## Page 72

| 80
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits – Charge Master Plus
When configured as a module, ON/OFF circuit will automatically be
configured

## Page 73

| 81
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits – Charge Master Plus
Many other Control Input functions can be used for circuits as
previously configured
Example:
When charger in BULK; Turn on Fan

## Page 74

| 82
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits – Combi Master
When configured as a module, ON/OFF circuit will
automatically be configured for Charger and Inverter

## Page 75

| 83
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits – Combi Master
Many other Control Input functions can be used for circuits as previously configured

## Page 76

| 84
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits – MLI Ultra
LI-ION Battery Circuits:
Many other Control Input functions can be used for circuits as previously configured

## Page 77

| 85
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits – MLI Ultra
Stop Charge events must be
configured for all charging sources
to Li-Ion batteries
Create ‘Stop Charge’ circuit
Control is from the Battery
Switch type ‘Single throw Momentary’
Control input is the Stop Charge
Switch function is ‘Momentary On/Off’

## Page 78

| 86
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits – MLI Ultra
Add the Charger Load/s
Select ‘Timer/Advanced Settings’
*This need to be completed for all Charging sources
Set the ‘State’ to OFF

## Page 79

| 87
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Circuits – MLI Ultra
LI-ION Battery Stop Charge Events:
Change control type to ‘Set Limit’
Set limit is chosen because we want to temporarily hold the charging source in an
OFF state.  When the stop charge is released, the limit off will be released also.

## Page 80

| 88
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Summary
88
Circuits = Controls + Loads.
Circuits can be made up of Multiple switch controls from SI’s, SCI’s, VS’s or Logic.
Configure Standard Circuit or Mode (Groups?)
Configure Timers / Advanced settings as required, lockouts, directionality etc.
Add modes and configure ALL loads that need to be controlled including turning
loads OFF.
When using CZone enabled Mastervolt equipment, ensure all circuits are
configured as required.
Stop Charge events for charging sources must be configured for Li-ion batteries.

## Page 81

| 105
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
MasterVolt Bridge
Auto selects based off available locations
Mastervolt / CZone configuration must be done ONLINE
Select the device I.E Charger
Assign AC and DC power meters as previously
configured to populate the page
CZone will automatically create a control circuit
based off requirement I.E Combi, Stand-alone

## Page 82

| 106
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
MasterVolt Bridge
A Circuit will be configured which will have no ‘Circuit Control’.  This is normal.
The created MV ‘Load’ can then be used in other Circuits or Modes as required.
I.E ‘Dock Unattended’ – Turn off ‘Inverter’ and leave ‘Charger’ on.  This will prevent discharge of batteries if Shore
Power is lost

## Page 83

| 107
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
MasterVolt Bridge
Used to select NMEA data to transmit to the
Masterbus network (AC, DC or Fluid Level)
Select the bridge to transmit data
NMEA Index
Name
NMEA Data type (AC, DC or Fluid Level)
Instance number
Line Data

## Page 84

| 108
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Summary
108
Configure all Mastervolt equipment first – before finalising MV in CZone
Select Mastervolt equipment to be controlled / monitored and label correctly
Set Mastervolt Metering in ‘Power Metering’ tab
Reference power meter in Mastervolt item to populate MV Page layout

## Page 85

| 109
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Logic Blocks
Logic is a statement (Control) that is either TRUE or FALSE.
This control, can then be used within CZone to create advanced configuration settings, switching or
alarms.
There are Different levels of logic;
•
‘AND’:  I.E (This) AND (This)
•
‘OR’:
I.E (This) OR (This)
Different controls within CZone, can be used to determine if these statements are TRUE or FALSE

## Page 86

| 110
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Logic Blocks
A ‘Virtual Signal’ is a ‘Software Load’ that is not physically connected to the
Module – but it can be used in the configuration to provide ‘Feedback’ to
The display, used as a control or can be a switch used elsewhere in the
configuration software, I.E Logic Blocks.

## Page 87

| 111
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Logic Blocks
Different modules, have different numbers of available Logic Blocks / Virtual Signals
Output Interface:
6 total Virtual Signals / Logic Blocks
Switch Control Interface:
16 total Virtual Signals / Logic Blocks
Combination Output Interface:
32 total Virtual Signals / Logic Blocks
Control 1:
32 total Virtual Signals / Logic Blocks
Contact 6 Plus:
32 total Virtual Signals / Logic Blocks
Contact 6:
32 total Virtual Signals / Logic Blocks

## Page 88

| 112
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Logic Blocks
Example:  Slide out Alarm
This will be displayed if used as an Alarm
Select the Module that the logic block is
located within.
Select the Logic Type and ‘Alarm Severity’
level (if required).
*Note:  Using a Logic block will remove one, of the
(x) number of available VS’s from that module*

## Page 89

| 113
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Example:  Slide Out Alarm
Logic Blocks
Logic Block and Type have been created
Now select the Input/s required to make the Logic Block TRUE or FALSE.
•
These can be Loads turning ON/OFF
•
Metering switch points, etc
In this example:
•
If the Ignition switch is detected by CZone as ‘ON’
•
‘AND’
•
The ‘Slide Out Extended’ Limit switch (as configured in Signal Inputs tab) is ‘ON’
•
Then the statement (Control) must be ‘TRUE’

## Page 90

| 114
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Logic Blocks
Example:  Virtual Signal used to Control Logic
First: Create the ‘VS Load’

## Page 91

| 115
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Logic Blocks
Example:  Virtual Signal used to Control Logic
Create a circuit that makes sense to the owner / user.  Add the control and the VS as the Load

## Page 92

| 116
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Logic Blocks
Example:  Virtual Signal used to Control Logic
Now add the VS to the logic block
CZONE CONFIGURATION – LOGIC BLOCKS

## Page 93

| 117
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Logic Blocks
Example:  Virtual Signal used to Control Logic
In this example:
•
If the Ignition switch is detected by CZone as ‘ON’
•
‘AND’
•
The ‘Slide Out Extended’ Limit switch (as configured in Signal Inputs tab) is ‘ON’
•
‘AND’
•
The ‘Slide Out Alarm VS’ IS ‘ON’
Then the statement (Control) must be ‘TRUE’
You also have the ability to control a Circuit, using the created logic block!

## Page 94

| 118
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Data Switching
CZone can use standard ‘Time of day’ to achieve further advanced features.
Requires a CZone screen on the system or
COI to store the configuration.
Select the applicable timing
Use the ‘Data switch’ or the ‘Time of day’ switch in the configured ‘Circuit’ as the ‘Circuit Control’

## Page 95

| 119
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Data Switching

## Page 96

| 120
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Third Party Devices
Sea Recovery
Dometic
Simrad / Lowrance Side Bar
Sentinel Switching
NMEA Audio PGN’s
Excludes Fusion
Control X Wiper Configuration

## Page 97

| 121
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
General
Force a Circuit ‘On’ when alarm becomes active
Define own user categories for display

## Page 98

| 122
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
General
Smooth Start up time when checked in Loads
Set minimum dim level for new Dimming functionality
(Single button Dim, Dim up/Dim Down

## Page 99

| 123
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
General
Relates to Keypad, C6P, Control X, SBH.  Will allow ‘sleep’ of these products
using the keypad power button
Changes the units on CZone displays
I.E Pressure BAR to PSI
Can also be change in display settings
Unlocks additional configuration tools – used only for specific configs at this stage
Reset module configuration
Reset NMEA addresses – only used on very large NMEA installations
(service level)

## Page 100

| 124
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
General

## Page 101

| 125
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
125
Fault Finding &
Diagnostics

## Page 102

| 126
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Treat a digital switching installation like any traditional system
Is there a signal at the input?
Is there power feed to an output device?
Is their power out of the output device?
Does the configuration match the inputs?
Incorrect wiring / Faulty connections / Poor joins, still happen with digital switching installations.  As with any technology
the easiest diagnosis is to blame the system.
Fault Finding

## Page 103

| 127
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Alarms
Warning (Blue Bell):
This is the lowest alarm severity and indicates a minor issue.
The alarm will disappear once acknowledged.
Standard (Yellow Bell):
Standard level alarms identify an issue that may soon cause an issue for operation.  Once
acknowledged the alarm will disappear.
Important (Orange Bell):
Something is wrong with a system and you will need to investigate before trying to operate it
again.  This alarm will give you an audible tone and popup dialogue on screen.  The alarm
will remain active in the alarms page.
Critical (Red Bell):
Immediate action is necessary to avoid damage and/or a failure of a system
This alarm will give you a popup dialogue and audible tone no matter the screen or action
you are currently on.  The alarm will return in 10 mins after acknowledgement until the fault is
remedied.

## Page 104

| 128
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Voltage readings on network conductors:
Red to Black
12-15 VDC
Red to Shield
12-15 VDC
Blue (CAN H) to Black (Neg) around 2.2 VDC
White (CAN L) to Black (Neg) around 2.2 VDC
Resistance between CAN H and CAN L, 60 ohms with no devices on network.
Recommend cutting an end off an extension cable to use as a testing tool.
CAN connections can be accessed internally on smaller boxes for voltage testing.
128
NMEA Network Tests

## Page 105

| 129
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
To check a healthy NMEA2000 Network go to the Display Interface (if available) and check the Network page.  All
modules should show as green - Online.
You can also check each CZone module, the Network Status LED will be green with quick red flashing to indicate
normal traffic.
Network Indicators

## Page 106

| 130
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
If a network failure has occurred, you will first notice this by alarms appearing on the Display Interface or MFD.
This will usually be a Blue Bell symbol and/or alarm, stating Device Missing.
These missing devices will usually show no indicator on the Network Status LED.
In some cases, the network LED will remain.
Network Failure

## Page 107

| 131
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
If only one or a few modules are offline, check the NMEA cable and T-Piece at the offline module and make sure it is
connected properly.  If it is, the fault may be with a Tee or cable.
If all or many modules are offline, follow these steps:
Check battery voltage (always check the obvious).
Check network circuit breaker is on.
Check voltage on the network at the point of the power connection.
Check voltage at each end of the network (there should be minimal voltage drop).
Check resistance between data cables (with network breaker off) to ensure resistors are installed.
Check all network connections have been made and are tight.
Orange indicates shorted CAN High or CAN Low cable.  Solid Red indicates loss of power on the network.
Network Failure

## Page 108

| 132
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Check the Network page, the module stating Dipswitch Conflict has the correct setting.
The module that is offline is incorrect, take note of the dipswitch for this device.
Unplug the NMEA2000 connection, set the correct dipswitch and then reconnect the NMEA2000 cable.
Dipswitch Conflict

## Page 109

| 133
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
For the CZone network to function correctly, the firmware on all devices needs to be the same version.
The firmware version for all devices can be checked on the Network Page.
Ensure the latest firmware is used, check the Czone portal: https://downloads.czone.net
Firmware

## Page 110

| 134
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
When a fault occurs on the network the affected module or modules will flash red on the channel status indicator.
To find out the type of fault count the number of flashes.
The fault code can then be referenced on the inside of any module cover.
Fault Codes

## Page 111

| 135
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
When a fault occurs on the network you will also get an alarm on the Display Interface.
You can check active alarms by going into the Alarms page under Monitoring.
Depending on the severity of the alarm there may also be an audible and visual dialog to acknowledge.
Alarms

## Page 112

| 136
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
If a system failure has occurred or you wish to test the output channels manually the channel can be placed into the
manual override position.
Remove the cover from the output module
Locate the channel you want to bypass
Remove the fuse from its Normal position
Place the fuse in the Bypass position
This has now completely bypassed all internal electronics and software control providing complete mechanical bypass.
Note: Bypassing can cause a potential ignition source.
Ensure surrounding area is free of flammable/explosive gasses and
vapors
Bypass

## Page 113

| 137
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Check pin 8 and ensure there is continuity to ground.
Check documentation and test for voltage or ground (depending on switch type) on correct input wire
with switch turned on.
Check network LED is on.
Check dipswitch is correct.
Testing the Input – SI

## Page 114

| 138
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Check for voltage at the input stud.
Negative connected for Analogue inputs?
Check documentation for correct output channel and turn the switch on, does the green status indicator light come on? If
not, then the configuration could be incorrect.
Check the fuse has not blown.
Put the fuse into bypass to test if the load works, if it doesn’t then check wiring to load.
Check network LED and dipswitch is correct.
Testing the Input – COI, CX

## Page 115

| 139
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Troubleshooting a Circuit:
If all these tests are OK, then then check the circuit settings in the configuration.
Most issues are caused by a poorly written configuration – CZone only does what it is programmed to do!
Fault Finding continued

## Page 116

| 140
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
1. Disconnect all wiring connections then remove the faulty module.
2. Ensure the Firmware on the replacement device matches the replaced device.
3. Ensure all the dipswitches on the new module are switched to the off position.
4. If the module is an OI or a MOI remove the fuses from the failed module and fit in the same locations on the new
module (to ensure bypass fuses match load).
5. Fit the new module and connect all wiring except the NMEA cable.
6. Once fitted temporarily connect the NMEA cable until all the indication lights flash once.  Then remove the NMEA
connection.  This has now wiped any program that may have been on the module.
7. Set the dip switches to match the settings of the replaced module. Once the dipswitches are set plug in the NMEA
cable. After a short period of time the new module will receive a copy of the program from the network and begin
functioning normally.
Replacing a module

## Page 117

©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
141
FIRMWARE UPDATES

## Page 118

| 142
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Firmware Updates
GREEN =
Up to date
AMBER =
Needs Updating
RED =
Has not received Firmware correctly

## Page 119

| 143
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Downloads.czone.net for firmware
Firmware Updates

## Page 120

| 144
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Firmware Updates
Select ‘Load Firmware package’ and navigate to installed Firmware
Select start updating and select modules to update
Firmware will begin to install.

## Page 121

| 145
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Firmware Updates
Navigate to folder in your C:\ ‘DI Direct Updaters’
Select the appropriate file
Used for Touch 5
Used for 10” – 8” (Old Style)
Use for Touch 10
Use for 3.5” (Old Style)
Use for Touch 7

## Page 122

| 146
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Firmware Updates – Touch 10”
Insert USB with correct file
‘Settings’ – ‘Update software’ – Select file

## Page 123

| 147
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Firmware Updates – Touch 7
Insert USB with correct file
‘Settings’ – ‘Update software’ – Select file
Version can also be checked

## Page 124

| 148
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Firmware Updates – Touch 5
Insert Micro SD/USB with correct file
‘Settings’ – ‘Update software’ – Select file
Version can also be checked

## Page 125

| 149
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Firmware Updates – COI USB
Can also use the COI USB port for firmware

## Page 126

| 150
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Firmware Updates – COI USB
Locate the Firmware file
Place this file onto an empty USB Drive and insert to COI
Ensure all modules are online
When the USB is inserted, the LED should turn Green

## Page 127

| 151
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Firmware Updates – COI USB
Press and hold the button for 5 seconds or until the LED starts flashing RED

## Page 128

| 152
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Firmware Updates – COI USB
The Output lights on the COI will begin to flash as it checks the network.  These will then transform into a % status
bar to indicate the different module selection.

## Page 129

©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
153
FAVOURITES

## Page 130

| 154
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Favourites Setup
Ensure displays (Touch 10 and Touch 5 only) have the latest 2.0 firmware 6.12.14.0 or above.
This will enable the new 2.0 menu layout

## Page 131

| 155
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Favourites Setup
Open a new project
Give the project a relevant name
(Revision and vessel number)
Select the COMPLETED CZone configuration
Favourites are easiest to configure as a final commissioning – I.E Once CZone configuration is complete.

## Page 132

| 156
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Determine which screen/s you are going to populate

## Page 133

| 157
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Favourites Setup
Configuration file will populate on the right hand side of the page:

## Page 134

| 158
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Favourties Setup
Select the screen you want to populate, ‘drag and drop’ the control or
Monitoring circuit:

## Page 135

| 159
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Favourites Setup
Add or remove a page by selecting the              button at the bottom of the tool
Add an image by selecting ‘Add Image’
Drag and Drop Modes
Drag and mimic icons as required

## Page 136

| 160
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
Favourites Setup
Once favourites completed ‘create .CFP Package
Put the .CFP File on a USB for updates to Touch 10 or Touch 7
Use a Micro SD for Touch 5 or transfer wirelessly:
•
Connect Laptop to Touch 5 screen wireless
•
Select

## Page 137

| 161
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
©2022 Advanced Systems Group by Brunswick Co. Confidential and all rights reserved.
161
