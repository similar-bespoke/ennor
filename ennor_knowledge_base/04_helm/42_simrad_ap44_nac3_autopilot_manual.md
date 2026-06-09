---
vessel: Ennor
doc_id: "4.2"
title: "Simrad Autopilot"
category: "Helm"
source_pdf: "4.2 Simrad AP44 & NAC3 Autopilot manual.pdf"
extraction_method: native
page_count: 85
converted: "2026-02-24"
---

# Simrad Autopilot

**Vessel:** Ennor | **Section:** 4.2 | **Category:** Helm
**Source PDF:** 4.2 Simrad AP44 & NAC3 Autopilot manual.pdf | **Pages:** 85 | **Extraction:** native

---

## Page 1

ENGLISH
AP™ 44
Operator Manual
www.simrad-yachting.com

## Page 2

Contents
9
Introduction
10
Front panel and keys
11
The autopilot page
12
Basic operation
12
Safe operation with the autopilot
12
Turning the unit on and off
13
Operating the menu system
14
Display setup
15
Autopilot modes
15
Selecting an autopilot mode
15
Standby mode
15
Follow-up (FU) mode
15
AUTO mode (Heading hold)
17
Wind mode
18
NoDrift mode
19
Heading capture
19
NAV mode
21
Turn pattern steering
25
Using the autopilot in an EVC system
25
SteadySteer
26
Trip log
27
Alarms
27
Alarm indication
27
Acknowledging the alarms
28
Enabling the alarm system and the alarm siren
29
Alarm history
30
Software setup
30
Calibration
35
Damping
36
Autopilot settings
36
System settings
Contents | AP™ 44 Operator Manual
7

## Page 3

41
Maintenance
41
Preventive maintenance
41
Cleaning the display unit
41
Checking the connectors
42
Software update
44
Menu tree
46
Technical specifications
47
Dimensional drawing
48
Terms and abbreviations
50
Supported data
50
NMEA 2000 PGN (transmit)
50
NMEA 2000 PGN (receive)
8
Contents | AP™ 44 Operator Manual

## Page 4

Introduction
The AP44 is a networked autopilot display and control unit.
The unit is compatible with a range of Navico autopilot computers.
The AP44 systems include several modules that need to be
mounted in different locations on the vessel and that need to
interface with at least three different systems on the boat:
•
The boat’s steering system
•
The boat’s electrical system (input power)
•
Other equipment onboard
All parts of the autopilot system must be installed and configured
according to supplied documentation prior to using the autopilot.
The following steps are required:
•
Mechanical installation and wiring of all units. Refer to separate
documentation for the units
•
Software setup of the system. Refer to "Software setup" on page 30
•
Commissioning and setup of the autopilot computer. Refer to
the installation and commissioning documentation for your
autopilot computer
1
Introduction | AP™ 44 Operator Manual
9

## Page 5

Front panel and keys
1
2
3
4
5
STBY
MODE
AUTO
MENU
X
1
STBY key
Press to turn the autopilot to Standby mode.
2
MENU/X key
With no menu active:
•
Press to display the Settings menu
•
Press and hold to display the Display setup dialog
Menu and dialog operation:
•
Press to return to previous menu level or to exit a dialog
3
Rotary knob
Menu and dialog operation:
•
Turn to move up and down in menus and dialogs
•
Turn to adjust a value
•
Press to select a menu option and to enter the next menu
level
In STBY mode:
•
Press to select FU mode
In FU mode:
•
Turn to set rudder angle
In AUTO, NoDrift and Wind mode:
•
Turn to change set heading/set course/set wind angle
10
Introduction | AP™ 44 Operator Manual

## Page 6

4
MODE key
Press to display the Mode list
5
AUTO key
Press to turn the autopilot to AUTO mode
The autopilot page
The content of the autopilot page varies with active mode. All
modes include:
•
Response/ Profile mode (depending on connected autopilot
computer) (A)
•
Heading indicator, analog and digital (B)
•
Autopilot mode indication (C)
•
Rudder indicator, analog and digital (D)
For more information, refer to the separate mode descriptions and
to the "Terms and abbreviations" on page 48.
Introduction | AP™ 44 Operator Manual
11

## Page 7

Basic operation
Safe operation with the autopilot
 Warning: An autopilot is a useful navigational aid,
but DOES NOT replace a human navigator.
 Warning: Ensure the autopilot has been installed
correctly, commissioned and calibrated before use.
Do not use automatic steering when:
•
In heavy traffic areas or in narrow waters
•
In poor visibility or extreme sea conditions
•
When in areas where use of an autopilot is prohibited by law
When using an autopilot:
•
Do not leave the helm unattended
•
Do not place any magnetic material or equipment near the
heading sensor used by the autopilot system
•
Verify at regular intervals the course and position of the vessel
•
Always switch to Standby mode and reduce speed in due time to
avoid hazardous situations
Turning the unit on and off
The unit has no power key, and it will be running as long as power is
connected to the NMEA 2000 network backbone.
First time startup
When the unit is started for the first time and after a factory reset,
the unit displays a setup wizard. Respond to the setup wizard
prompts to select some fundamental setup options. These settings
can later be changed and further configuration made as described
in "Software setup" on page 30.
2
12
Basic operation | AP™ 44 Operator Manual

## Page 8

Sleep mode
In Sleep mode, the backlight for screen and keys are turned off to
save power. The system continues to run in the background.
You select Sleep mode from the Display setup dialog, activated by
pressing and holding the MENU key. Switch from Sleep mode to
normal operation by a short press on the MENU key.
Operating the menu system
All settings and configuration in the unit are available from the
Settings menu, activated by pressing the MENU key.
•
Turn the Rotary knob to move up and down in the menus and in
the dialogs
•
Confirm a selection by pressing the Rotary knob
•
Return to previous menu level by pressing the MENU key
Edit a numeric value
1. Turn the Rotary knob to select the entry field
2. Press Rotary knob to turn the field into edit mode
- The left digit starts flashing
3. Turn the Rotary knob to set the value for the flashing digit
4. Press the Rotary knob to move focus to the next digit
5. Repeat step 3 and 4 until all digits are set
6. Press the Rotary knob to leave edit mode for the selected field
7. Turn the Rotary knob to select the Cancel or Save buttons, then
press the Rotary knob to confirm your selection and to close the
dialog
Selected field
Field in edit mode
Ú Note: You can at any time press the MENU key to leave a
dialog without saving the entries.
Basic operation | AP™ 44 Operator Manual
13

## Page 9

Display setup
The display setup can be adjusted at any time from the Display
setup dialog, activated by pressing and holding the MENU key.
The following options are available:
•
Backlight level: Adjusts the backlight level from Min (10%) to Max
(100%) in 10% increments
-
When the Backlight level field is active, subsequent presses on
the MENU key adjusts backlight level in decrements of 30%
•
Display group: Defines which network group the unit belongs to
•
Night mode: Activates/deactivates the night mode color palette
•
Night mode color: Sets the night mode color palette
•
Invert day color: Changes the background color for the pages
from default black to white
•
Sleep: Turns the backlight for screen and keys off to save power
Ú Note: All changes made to the display setup will apply to all
units belonging to the same display group. For more
information about network groups, refer to "Network groups" on
page 39.
14
Basic operation | AP™ 44 Operator Manual

## Page 10

Autopilot modes
The autopilot has several steering modes. The number of modes
and features within the mode depend on the autopilot computer,
the boat type and available inputs, as explained in the description of
the following steering modes.
Selecting an autopilot mode
You select Standby mode and AUTO mode by pressing the
dedicated STBY and AUTO keys.
You select other modes and automatic features by selecting the
relevant option from the Mode list, activated by pressing the MODE
key.
Standby mode
Standby mode is used when you steer the boat at the helm.
•
Switch to Standby mode by pressing the STBY key.
Ú Note: If sensor data vital for autopilot operation (e.g. rudder
response) is lost when the autopilot is running in an automatic
mode, the system will automatically switch to Standby mode.
Follow-up (FU) mode
In FU mode you turn the rotary knob to adjust the set rudder angle.
The rudder will move to the commanded angle and then stop.
•
Switch to FU mode from any mode by selecting the Follow-up
option in the Mode list, or switch directly from Standby mode to
FU mode by pressing the rotary knob.
AUTO mode (Heading hold)
In AUTO mode the autopilot issues rudder commands required to
steer the vessel automatically on a set heading. In this mode the
autopilot does not compensate for any drifting caused by current
and/or wind (A).
3
Autopilot modes | AP™ 44 Operator Manual
15

## Page 11

A
•
Switch to AUTO mode by pressing the AUTO key. When the
mode is activated, the autopilot selects the current boat heading
as the set heading.
Changing set heading in AUTO mode
You adjust the set heading by turning the rotary knob.
An immediate heading change takes place. The new heading is
maintained until a new heading is set.
Tacking and Gybing in AUTO mode
Ú Note: Only available when the boat type is set to SAIL.
Tacking and Gybing in AUTO mode uses the heading as reference.
The tacking/gybing operation changes the set heading to port or
starboard with a fixed angle.
The tacking parameters are set in the Setup/Sailing parameters: The
Tack angle defines the tacking angle, while the Tack time defines
the rate of turn during the tack/gybe. Refer to "Autopilot settings" on
page 36.
•
Initiate the Tack or Gybe function by selecting the Tack/Gybe
option in the Mode list.
-
The turn is started when the direction is selected in the dialog.
16
Autopilot modes | AP™ 44 Operator Manual

## Page 12

Wind mode
Ú Note: Wind mode is only available when the boat type is set to
SAIL. It is not possible to activate wind mode if wind
information is missing.
When wind mode is engaged, the autopilot captures the current
wind angle as steering reference, and adjusts the heading of the
boat to maintain this wind angle.
Prior to entering wind mode the autopilot system must be
operating in AUTO mode and with valid input from the wind
transducer.
•
Switch to Wind mode by selecting the Wind option in the Mode
list
 Warning: In wind mode the autopilot steers to the
apparent or true wind angle and not to a compass
heading. Any wind shift could result in the vessel
steering on an undesired course.
Tacking and Gybing in Wind mode
Tacking and Gybing in Wind mode can be performed when sailing
with apparent or true wind as the reference. In either case the true
wind angle must be less than 90 degrees (tacking) and more than
120° (gybing).
The tacking/gybing operation will mirror the set wind angle on the
opposite tack.
The rate of turn during the tack/gybe is set by the Tack time in the
Setup/Sailing menu. Refer to "Autopilot settings" on page 36.
•
Initiate the Tack or Gybe function by selecting the Tack/Gybe
option in the Mode list.
•
Confirm the tack/gybe in the dialog.
Autopilot modes | AP™ 44 Operator Manual
17

## Page 13

Ú Note: The autopilot will temporarily add a 5 degree bear-away
on the new tack to allow the boat to pick up speed. After a
short period the wind angle will return to the set angle.
Ú Note: If the Tack/Gybe is not confirmed the dialog will close
after 10 seconds, and the requested tack/gybe will not be
initiated.
NoDrift mode
Ú Note: It is not possible to select NoDrift mode if GPS position
and heading information is missing.
In NoDrift mode the vessel is steered along a calculated track line,
from present position and in a direction set by the user. If the vessel
is drifting away from the track line due to current and/or wind (A),
the vessel will follow the line with a crab angle.
Prior to entering NoDrift mode the autopilot system must be
operating in AUTO mode and with valid input from GPS and
heading sensor.
•
Switch to NoDrift mode by selecting the NoDrift option in the
Mode list
-
The autopilot will draw an invisible track line based on current
heading from the vessel’s position
The autopilot will now use the position information to calculate the
cross track distance, and automatically steer along the calculated
track.
Changing set course in NoDrift mode
You adjust the set course by turning the rotary knob.
An immediate course change takes place. The new course is
maintained until a new course is set.
18
Autopilot modes | AP™ 44 Operator Manual

## Page 14

Dodging
Ú Note: Only available for AC12N/AC42N autopilot computers.
If you need to avoid an obstacle when using NoDrift mode, you can
set the autopilot to Standby mode and power steer or use the helm
until the obstacle is passed.
If you return to NoDrift mode within 60 seconds you can select to
continue on previous set bearing line.
If you do not respond, the dialog disappears and the autopilot goes
to NoDrift mode with current heading as set bearing line.
Heading capture
When the vessel is turning in AUTO mode, an instant re-press on the
AUTO key activates the heading capture function. This will
automatically cancel the turn, and the vessel will continue on the
heading read from the compass the very moment you pressed the
AUTO key.
NAV mode
Ú Note: NAV mode requires a compatible chartplotter connected
to the network.
It is not possible to select NAV mode if heading information is
missing, or if steering information is not received from the
external chartplotter.
 Warning: NAV mode should only be used in open
waters. Navigation mode must not be used while
sailing, as course changes may result in unexpected
tacks or gybes!
In NAV mode the autopilot uses steering information from an
external chartplotter to direct the vessel to one specific waypoint
location, or through a series of waypoints.
In NAV mode, the autopilot's heading sensor is used as heading
source for course keeping. Speed information is taken from SOG or
from selected speed sensor. The steering information received from
the external chartplotter alters the set course to direct the vessel to
the destination waypoint.
Autopilot modes | AP™ 44 Operator Manual
19

## Page 15

To obtain satisfactory navigation steering, the autopilot system
must have valid input from the chartplotter. Autosteering must be
tested and determined satisfactory prior to entering NAV mode.
Ú Note: If the chartplotter does not transmit a message with
bearing to next waypoint, the autopilot will steer using Cross
Track Error (XTE) only. In that case you must revert to AUTO
mode at each waypoint and manually change set course to
equal bearing to next waypoint and then select NAV mode
again.
Prior to entering NAV mode the chartplotter must be navigating a
route or towards a waypoint.
•
Initiate NAV mode by selecting the NAV option in the Mode list
•
Confirm to switch to NAV mode in the dialog.
Turning in NAV mode
When your vessel reaches a waypoint, the autopilot will give an
audible warning and display a dialog with the new course
information.
There is a user defined limit for the allowed automatic course
change to next waypoint in a route. If the course change is more
than this set limit, you are prompted to verify that the upcoming
course change is acceptable.
•
If the required course change to the next waypoint is less than
the course change limit, the autopilot will automatically change
the course. The dialog will disappear after 8 seconds unless
cleared by the Pages key.
•
If the required course change to next waypoint is more than the
set limit, you are prompted to verify that the upcoming course
change is acceptable. If the turn is not accepted, the vessel will
continue with the current set heading.
20
Autopilot modes | AP™ 44 Operator Manual

## Page 16

Course change less than set limit
Course change larger than set limit
The limit for automatic course change is set during commisioning
of the autopilot computer. For more information refer to "Autopilot
settings" on page 36.
Turn pattern steering
The system includes a number of automatic turn steering features
when the autopilot is in AUTO mode.
Ú Note: Turn pattern steering is not available if the boat type is
set to Sail. Instead the tack/gybe feature is implemented.
Turn variables
All turn patters, except the U-turn, have settings that you adjust
before you start a turn or at any time when the boat is in a turn.
The turn settings are available from the Autopilot settings dialog.
The variables are described for each turn pattern option in the
following pages.
Starting and stopping a turn
Ú Note: For starting a DCT turn, see "Depth contour tracking (DCT)" on
page 23.
You start the turn by selecting the turn option in the Mode list,
followed by selecting the port or starboard options in the turn
dialog to select the turn direction.
Autopilot modes | AP™ 44 Operator Manual
21

## Page 17

You can at any time stop the turn by pressing the STBY key to
return to Standby mode and manual steering.
C-turn (Continuous turn)
Steers the vessel in a circle.
•
Turn variable:
-
Rate of turn. Increasing the value makes the vessel turn a
smaller circle.
U-turn
Changes the current set heading to be 180° in the opposite
direction.
The turn rate is set during commisioning of the autopilot computer.
For more information refer to "Autopilot settings" on page 36.
Spiral turn
Makes the vessel turn in a spiral with a decreasing or increasing
radius.
•
Turn variables:
-
Initial radius
-
Change/turn. If this value is set to zero, the boat will turn in a
circle. Negative values indicate decreasing radius while positive
values indicate increasing radius.
Zigzag turn
Steers the vessel in a zigzag pattern.
•
Turn variables:
-
Course change (A)
-
Leg distance (B)
22
Autopilot modes | AP™ 44 Operator Manual

## Page 18

B
A
Square turn
Makes the vessel automatically turn 90° after having travelled a
defined leg distance.
•
Turn variable:
-
Leg distance
S-turn
Makes the vessel yaw around the main heading.
•
Turn variables:
-
Course change (C)
-
Turn radius (D)
D
C
Depth contour tracking (DCT)
Makes the autopilot follow a depth contour.
Ú Note: DCT turn pattern is only available if the system has a valid
depth input.
 Warning: Do not use the DCT turn pattern unless the
seabed is suitable. Do not use it in rocky waters where
the depth is varying significantly over a small area.
Autopilot modes | AP™ 44 Operator Manual
23

## Page 19

To initiate a DCT turn:
•
Ensure that you have depth reading on the panel or on a
separate depth instrument
•
Steer the boat to the depth you want to track, and in the
direction of the depth contour
•
Activate AUTO mode, then select depth contour tracking while
monitoring the depth reading
•
Select the port or starboard option in the turn dialog to initiate
the depth contour steering to follow the bottom sloping to
starboard or to port
Port option
(depth decreases to port)
Starboard option
(depth decreases to starboard)
•
Turn variables:
-
Depth gain. This parameter determines the ratio between
commanded rudder and the deviation from the selected depth
contour. The higher depth gain value the more rudder is
applied. If the value is too small it will take a long time to
compensate for drifting off the set depth contour, and the
autopilot will fail to keep the boat on the selected depth. If the
value is set too high the overshoot will increase and the
steering will be unstable.
-
CCA. The CCA is an angle that is added to or subtracted from
the set course. With this parameter you can make the boat yaw
around the reference depth with s movements. The larger the
CCA the bigger yawing will be allowed. If the CCA is set to zero
there is no S-ing.
-
Ref. depth. This is the reference depth for the DCT function.
When DCT is initiated the autopilot reads the current depth
and set this as the reference depth. The reference depth can be
changed when the function is running.
24
Autopilot modes | AP™ 44 Operator Manual

## Page 20

Ú Note: If depth data is lost during DCT the autopilot will
automatically switch to AUTO mode.
It is recommended to turn ON the AP Depth Data Missing alarm
when using DCT. When this alarm is activated an alarm will be
raised if the depth data is lost during DCT.
Using the autopilot in an EVC system
When the autopilot is connected to an EVC system, you can take
manual control of the steering regardless of the autopilot mode.
The mode indicator is replaced by a dash to indicate EVC override.
The autopilot goes into standby mode if no rudder command is
given from the EVC system within a predefined period.
SteadySteer
The SteadySteer feature allows you to control how the autopilot
system reacts to manual steering.
When enabled:
•
Manual steering overrides theactive mode.
•
If Auto mode or NoDrift mode was active before going into
manual steering, they will automatically re-engage when the
vessel has stabilized on a new course.
•
If NAV mode was active before going into manual steering a
dialog will be shown.
-
Confirm course change to reactivate NAV mode.
-
Cancel the course change to activate Auto mode on the new
heading.
-
If no action is taken the autopilot will go into Standby mode.
For any other modes, the autopilot goes into Standby mode.
When disabled:
•
Manual steering overrides the active mode.
•
Independent of modes, the autopilot goes into Standby mode.
Refer to the documentation for your autopilot computer for more
information.
Autopilot modes | AP™ 44 Operator Manual
25

## Page 21

Trip log
The Trip log is available from the Settings menu.
There are three log options available:
•
Trip 1: records distance traveled through the water (Log input)
•
Trip 2: records distance traveled via GPS input
•
Log: shows total distance run from system installation or from a
system restore
Ú Note: Trip 1 requires correctly calibrated boat speed for
accurate trip records.
Trip 2 requires a compatible GPS connected to the network.
You start, stop and reset the active Trip log from the menu,
activated by pressing the rotary knob.
4
26
Trip log| AP™ 44 Operator Manual

## Page 22

Alarms
The system continuously checks for dangerous situations and
system faults while the system is running. The alarm system can be
activated if any alarm settings are exceeded.
Ú Note: If sensor data vital for autopilot operation (e.g. rudder
response) is lost when the autopilot is running in an automatic
mode, the system will automatically switch to Standby mode.
Alarm indication
An alarm situation is indicated with an alarm pop-up. If you have
enabled the siren, the alarm message is followed by an audible
alarm.
A single alarm is displayed with the name of the alarm as the title,
and with details for the alarm.
If more than one alarm is activated simultaneously, the alarm pop-
up can display 2 alarms. The alarms are listed in the order they occur
with the alarm activated first at the top. The remaining alarms are
available in the Alarms dialog.
Type of messages
The messages are classified according to how the reported situation
affects your vessel. The following color codes are used:
Color
Importance
Red
Critical alarm
Orange
Important alarm
Yellow
Standard alarm
Blue
Warning
Green
Lite warning
Acknowledging the alarms
The most recent alarm is acknowledged by pressing the rotary
knob.
5
Alarms| AP™ 44 Operator Manual
27

## Page 23

This removes the alarm notification, and silences the alarm from all
units that belong to the same alarm group. A reminder reappears at
given intervals for as long as the alarm condition exists.
Ú Note: An alarm received from non Navico units on the network
must be acknowledged on the unit generating the alarm.
Enabling the alarm system and the alarm
siren
You enable the alarm system and the alarm siren from the Alarms
menu.
It is recommended that you enable all autopilot alarms when using
an autopilot.
Individual alarm settings
You enable/disable the single alarm and set the alarm limits from
the Alarms settings dialog.
•
Press the rotary knob to display the menu from where you can
enable/disable the alarm and set the alarm limit
28
Alarms| AP™ 44 Operator Manual

## Page 24

Alarm history
The Alarm history dialog stores alarm messages until they are
manually cleared.
You show alarm details for a selected alarm and clear all alarms in
the alarm history by pressing the rotary knob when the Alarm
history dialog is active.
Menu options
Alarm details
Alarms| AP™ 44 Operator Manual
29

## Page 25

Software setup
Prior to use, the AP44 requires a number of settings be configured
in order for the system to perform as expected. Access to the
required options are found in the Settings menu, accessed by
pressing the MENU key.
Ú Note: The following settings are described in other sections of
this manual:
"Trip log" on page 26
"Alarms" on page 27
Calibration
Ú Note: Once the unit is setup and before you proceed with
calibration ensure all network sources are selected and
configured. Refer to "System settings" on page 36.
Boat speed
Speed calibration is necessary to compensate for hull shape and
paddlewheel location on your boat. For accurate speed and log
readings, it is essential that the paddlewheel is calibrated.
SOG reference
This is an auto calibration option that uses speed over ground (SOG)
from your GPS, and compares the average of SOG against the
average boat speed from the speed sensor for the duration of the
calibration run.
Ú Note: This calibration should be made in calm sea with no
effect from wind or tidal current.
6
30
Software setup| AP™ 44 Operator Manual

## Page 26

•
Bring the boat up to cruising speed (above 5 knots), then
•
Select the SOG reference option
When the calibration is completed the Boat speed calibration scale
will show the adjusted percentage value of the boat speed.
Distance reference
Allows you to calibrate the log via a distance reference. You will
need to complete consecutive runs, under power at a constant
speed made along a given course and distance.
Ú Note: The distance should be greater than 0.5 NM, ideally 1 NM.
To eliminate the effect of tidal conditions it is advisable to
perform at least two runs, preferably three, along the measured
course.
Referring to the diagram, A and B are the markers for each run. X is
the actual distance for each run.
•
Enter the desired distance in nautical miles that you would like to
calculate the distance reference over
•
When the boat gets to the predetermined starting position of the
distance reference calculation, start the calibration timer
•
As the boat passes marks A and B on each run, instruct the
system to start and stop and finally OK to end calibration.
x
B
A
Use SOG as boat speed
If boat speed is not available from a paddle wheel sensor, it is
possible to use speed over ground from a GPS. SOG will be
displayed as boat speed and used in the true wind calculations and
the speed log.
Software setup| AP™ 44 Operator Manual
31

## Page 27

Wind
MHU (Masthead unit) alignment
This provides an off set calibration in degrees to compensate for any
mechanical misalignment between the masthead unit and the
center line of the vessel.
To check the masthead unit alignment error we recommend you
use the following method which involves a sailing trial:
•
Sail on a starboard tack on a close hauled course and record the
wind angle, then repeat the process on a port tack
•
Divide the difference between the two recorded numbers and
enter this as the wind angle off set
If the starboard apparent wind angle is greater than the port angle,
then divide the difference by 2 and enter this as a negative offset.
If the port angle is greater than the starboard then divide the
difference by 2 and enter this as a positive offset.
Enter the offset it into the MHU Align calibration field.
Depth
Depth offset
All transducers measure water depth from the transducer to the
bottom. As a result, water depth readings do not account for the
distance from the transducer to the lowest point of the boat (for
example; bottom of the keel, rudder, or propeller) in the water or
from the transducer to the water surface.
•
For depth below keel (A): Set the distance from transducer to the
bottom of the keel as a negative value. For example, -2.0.
•
For depth below transducer (B): no offset required.
•
For depth below surface (waterline) (C): Set the distance from
transducer to the surface as a positive value. For example,+0.5.
32
Software setup| AP™ 44 Operator Manual

## Page 28

A
B
C
+0.5
+0.0
-2.0
Aft depth offset
This option allows the system to display two depth readings.
The Aft depth is calibrated in the same manner as the Depth offset.
Ú Note: Aft Depth is only available when a valid signal is received
from a second and compatible NMEA 2000 or NMEA 0183
device.
Heading
Ú Note: All magnetic compasses must be calibrated to ensure
correct heading reference.
The calibration must be made on the active compass.
The calibration should be done in calm sea conditions and with
minimal wind and current to obtain good results.
Offset
The Offset option is used for compensating for any difference
between the boat’s center line (A) and the compass lubber line (B).
1. Find the bearing from the boat position to a visible object. Use a
chart or a chart plotter
2. Steer the boat so that the center line of the boat is aligned with
the bearing line pointing towards the object.
3. Change the offset parameter so that the bearing to the object
and the compass readout becomes equal.
Ú Note: Make sure that both the compass heading and the
bearing to the object have the same unit (°M or °T).
B
A
x
Software setup| AP™ 44 Operator Manual
33

## Page 29

User triggered calibration
Ú Note: Before the calibration is started, make sure that there is
enough open water around the vessel to make a full turn.
The Calibrate option is used for manually starting the heading
calibration procedure.
During this calibration, the compass measures the magnitude and
direction of the local magnetic field.
The illustration shows magnitude of local field in percentage of
earth's magnetic field (A), direction of local field (B) with respect to
the boat's centerline (C).
Follow the on-screen instruction, and use about 60-90 seconds to
make a full circle. Keep turning until the system reports a pass.
•
If the local magnetic field is stronger than the earth’s magnetic
field (the local field is reading more than 100%), the compass
calibration will fail.
•
If the local field is reading more than 30%, you should look for
any interfering magnetic objects and remove them, or you
should move the compass to a different location. The (local) field
angle guides you to the local interfering magnetic object.
Ú Note: In certain areas and at high latitudes the local magnetic
interference becomes more significant, and heading errors
exceeding ±3° may have to be accepted.
Automatic calibration
An auto calibration option is available for compasses that offers a
fully automatic calibration procedure.
See more instructions in the documentation delivered with your
compass.
Magnetic variation
Defines how magnetic variation is handled by the system.
•
Auto: Receives variation data from a network source
•
Manual: Used for manually entering a value for the magnetic
variation
20%
030˚
030˚
B
C
A
34
Software setup| AP™ 44 Operator Manual

## Page 30

Use COG as heading
If heading data is not available from a compass sensor, it is possible
to use COG from a GPS. COG will be used in the true wind
calculations.
Ú Note: The autopilot cannot be operated using COG as the
heading source. COG cannot be calculated when stationary.
Pitch and roll
If a suitable sensor is fitted, the system will monitor the inclination of
the vessel. The offset value should be entered to adjust the readings
so that while the vessel is stationary at the dock, the pitch and roll
value reads 0.
Environment
If a suitable sensor is fitted, the system will monitor the current
sea/air temperature and barometric pressure.
The offset value to be entered should adjust the reading from the
sensor to match a calibrated source.
Rudder
Starts the automatic calibration of the rudder feedback. This
procedure sets the correct relationship between the physical rudder
movement and the rudder angle readout.
Follow the instructions on the display to perform the rudder
feedback calibration procedure.
Advanced
This option is used for manually applying an offset to the displayed
data for third party sensors which cannot be calibrated through the
AP44.
Damping
If data appears erratic or too sensitive, damping may be applied to
make the information appear more stable. With damping set to off,
the data is presented in raw form with no damping applied.
Software setup| AP™ 44 Operator Manual
35

## Page 31

Autopilot settings
The autopilot settings can be split between settings done by the
user, and settings done during installation and commissioning of
the autopilot system.
•
User settings can be changed for various operational conditions
or user preferences
•
Installation settings are defined during commissioning of the
autopilot system. No changes should later be done to these
settings
For setup and commissioning, refer to the documentation for your
autopilot computer.
Ú Note: For Turn pattern settings, refer to "Turn pattern steering" on
page 21.
System settings
Network
Sources
Data sources provide live data to the system.
The data may originate from modules internal to the unit (for
example internal GPS or sonar), or external modules connected to
the NMEA 2000 or via NMEA 0183 if available on the unit.
When a device is connected to more than one source providing the
same data, the user can choose the preferred source. Before
commencing with source selection make sure all external devices
and the NMEA 2000 backbone are connected and are turned on.
•
Auto select: Looks for all sources connected to the device. If more
than one source is available for each data type, selection is made
from an internal priority list. This option is suitable for the
majority of installations.
•
Manual source selection: Manual selection is generally only
required where there is more than one source for the same data,
and the automatically selected source is not the one desired.
Device list
36
Software setup| AP™ 44 Operator Manual

## Page 32

The Device list shows the devices that provide data. This may
include a module inside the unit, or any external NMEA 2000 device.
Selecting a device in this list will bring up additional details and
actions:
All devices allow allocation of an instance number in the configure
option. Set unique instance numbers on any identical devices on
the network to allow for the unit to distinguish between them. The
data option shows all data being output by the device. Some
devices will show additional options specific to the device.
Ú Note: Setting the instance number on a 3rd party product is
typically not possible.
Diagnostics
The NMEA 2000 tab on the diagnostics page can provide
information useful for identifying an issue with the network.
Ú Note: The following information may not always indicate an
issue that can be simply resolved with minor adjustment to
network layout or connected devices and their activity on the
network. However, Rx and Tx errors are most likely indicating
issues with the physical network, which may be resolved by
Software setup| AP™ 44 Operator Manual
37

## Page 33

correcting termination, reducing backbone or drop lengths, or
reducing the number of network nodes (devices).
Bus state
Indicates whether the bus is powered, but not necessarily
connected to any data sources. However, if bus shows as off, but
power is present along with an increasing error count, it is possible
that termination or cable topology is incorrect.
Rx Overflows
The unit received too many messages for its buffer before the
application could read them.
Rx Overruns
The unit contained too many messages for its buffer before the
driver could read them.
Rx/Tx Errors
These two numbers increase when there are error messages, and
decrease when messages are received successfully. These (unlike
the other values) are not a cumulative count. Under normal
operation these should be at 0. Values around 96 upwards indicate
a heavily error prone network. If these numbers go too high for a
given device, it will automatically drop off the bus.
Rx/Tx Messages
Shows actual traffic in and out of device.
Bus Load
A high value here indicates network is near full capacity. Some
devices automatically adjust rate of transmission, if network traffic is
heavy.
Fast Packet Errors
Cumulative counter of any fast packet error. This could be a missed
frame, or a frame out of sequence etc. NMEA 2000 PGNs are made
of up to 32 frames. The entire message will be discarded when a
frame is missed.
Ú Note: Rx and Tx Errors often indicate an issue with the physical
network, which may be resolved by correcting termination,
38
Software setup| AP™ 44 Operator Manual

## Page 34

reducing backbone or drop lengths, or reducing the number of
network nodes (devices).
Network groups
The Network Group function is used to control parameter settings,
either globally or in groups of units. The function is used on larger
vessels where several units are connected to the network. By
assigning several units to the same group, a parameter update on
one unit will have the same effect on the rest of the group
members.
Units
Provides setup of units of measure used on various data types.
Decimal places
Defines number of decimals used for speed and sea temperature.
Key beeps
Controls the loudness of the beep sound when a key is pressed.
Language
Controls the language used on this unit.
Time
Controls the local time zone offset, and the format of the time and
date.
Display setup
Displays the Display setup dialog.
The following options are available:
•
Backlight level: Adjusts the backlight level from Min (10%) to Max
(100%) in 10% increments
-
When the Backlight level field is active, subsequent presses on
the backlight key adjusts backlight level in decrements of 30%
•
Display group: Defines which network group the unit belongs to
•
Night mode: Activates/deactivates the night mode color palette
•
Night mode color: Sets the night mode color palette
Software setup| AP™ 44 Operator Manual
39

## Page 35

•
Invert day color: Changes the background color for the pages
from default black to white
•
Sleep: Turns the backlight for screen and keys off to save power
Files
File management system. Used to browse the contents of the unit's
internal memory and the content of a device plugged into the unit's
USB port.
Simulate
Runs the display with simulated data. Use the simulator to become
familiar with your unit before using it on the water.
When activated, the simulator mode is indicated on the display.
Restore defaults
Allows you to select which settings are to be restored to their
original factory settings.
Global reset
Resets the source selection on all displays connected to the
network.
About
Displays copyright information, software version, and technical
information for this unit.
40
Software setup| AP™ 44 Operator Manual

## Page 36

Maintenance
Preventive maintenance
The unit does not contain any field serviceable components.
Therefore, the operator is required to perform only a very limited
amount of preventative maintenance.
It is recommended that you always fit the supplied protective sun
cover when the unit is not in use.
Cleaning the display unit
To clean the screen:
•
A micro-fiber or a soft cotton cloth should be used to clean the
screen. Use plenty of water to dissolve and take away salt
remains. Crystallized salt, sand, dirt, etc. can scratch the protective
coating if using a damp cloth. Use a light fresh water spray then
wipe the unit dry with a micro-fiber or a soft cotton cloth. Do not
apply pressure with the cloth.
To clean the housing:
•
Use warm water with a dash of liquid dish soap or detergent.
Avoid using abrasive cleaning products or products containing
solvents (acetone, mineral turpentine, etc.), acid, ammonia, or
alcohol as they can damage the display and plastic housing.
Do not use a jet or high pressure wash. Do not run your unit
through a car wash.
Checking the connectors
The connectors should be checked by visual inspection only.
Push the connector plugs into the connector. If the connector plugs
are equipped with a lock, ensure that it is in the correct position.
7
Maintenance| AP™ 44 Operator Manual
41

## Page 37

Software update
The AP44 includes a USB port of the back of the units. You use this
port for software updates.
You can update the software for the AP44 unit itself and for NMEA
2000 sensors connected to the network from the AP44.
You can check the units software version from the About dialog.
The software version for connected NMEA 2000 sensors is available
in the Device list.
The latest software is available for download from our website:
www.simrad-yachting.com.
Software update for the unit
1. Download the latest software from our website: www.simrad-
yachting.com, and save it to a USB device
2. Insert the USB device to the AP44 unit, and restart the AP44 unit
- The upgrade will now start automatically the upgrade
procedure for all units
42
Maintenance| AP™ 44 Operator Manual

## Page 38

3. Remove the USB device when the update is completed.
 Warning: Do not remove the USB device until the
update is completed. Removing the USB device before
the update is completed may damage the unit.
Software update for remote devices
1. Download the latest software from our website: www.simrad-
yachting.com, and save it to a USB device
2. Insert the USB device to the AP44 unit
3. Start the File explorer, and select the update file on the USB
device
4. Start the update from the file details dialog
5. Remove the USB device when the update is completed.
Maintenance| AP™ 44 Operator Manual
43

## Page 39

Menu tree
The system includes a Settings menu, accessed by pressing the
MENU key. The Settings menu gives access to settings for the
sensors, the vessel, the autopilot computer and for the system.
Level 1
Level 2
Calibration
Boat speed...
Wind...
Depth...
Heading...
Roll/Pitch...
Environment...
Rudder...
Advanced...
Damping
Heading
Apparent wind
True wind
Boat speed
SOG
COG
Attitude Roll
Attitude Pitch
Tide
Trip log
Trip 1...
Trip 2...
Log...
Alarms
Alarm history...
Alarm settings...
Alarms enabled
Siren Enabled
8
44
Menu tree| AP™ 44 Operator Manual

## Page 40

Level 1
Level 2
Autopilot
Available options depend on
connected autopilot computer.
Steering
Sailing
Turn patterns
Installation
System
Network
Units
Decimal places
Key beeps
Language
Time
Display Setup...
Digital gauges
Files
Simulate
Restore defaults...
Global reset...
About
Menu tree| AP™ 44 Operator Manual
45

## Page 41

Technical specifications
Dimensions
Refer to "Dimensional drawing" on
page 47
Weight
0.32 kg (0.7 lbs)
Power consumption(@ 13.5
V)
Backlight OFF 1.35 W (100 mA)
Backlight MAX 2.16 W (160 mA)
Network load
4 LEN
Color
Black
Display
Size 4.1" (diagonal). 4:3 Aspect ratio
Type Transmissive TFT-LCD. White
LED backlight
Resolution 320 x 240 pixels
Illumination White for day mode. Red, green,
blue or white for night mode
Environmental protection
Waterproof rating IPx7
Humidity 100% RH
Temperature
Operating -25° to +65ºC (-13°F to +149 ºF)
Storage -40° to +85ºC (-40°F to +185 ºF)
9
46
Technical specifications| AP™ 44 Operator Manual

## Page 42

Dimensional drawing
118 mm (4.64")
115 mm (4.52")
8 mm
(0.31")
36.5 mm
(1.43")
28.5 mm
(1.12")
97.5 mm (3.83")
48.5 mm (1.91")
STBY
MODE
AUTO
MENU
X
10
Dimensional drawing| AP™ 44 Operator Manual
47

## Page 43

Terms and abbreviations
This list shows terms and abbreviations used in the pages and in
dialogs in the AP44 system.
AIR TEMP
Air temperature
AIS
Automatic Identification System
AVG SPD
Average speed
AWA
Apparent wind angle
AWS
Apparent wind speed
BSPD
Boat speed
BTW
Bearing to waypoint
BWW
Bearing Waypoint To Waypoint
COG
Course Over Ground
CTS
Course To Steer
DGPS
Differential Gps
DTW
Distance to next waypoint
DSC
Digital Selective Calling
EPFS
Electronic Position Fixing System
EPIRB
Emergency Position Indicating Radio Beacon
ETA
Estimated Time Of Arrival
ETW
Estimated time of arrival to next waypoint
GLONASS
Global Orbiting Navigation Satellite System
GMDSS
Global Maritime Distress And Safety System
GNSS
Global Navigation Satellite System
GPS
Global Positioning System
HDG
Heading
Km
Kilometer
KN
Knots
LL DIST
Layline distance
LL TIME
Layline time
m
Meters
11
48
Terms and abbreviations| AP™ 44 Operator Manual

## Page 44

MAX SPD
Maximum speed
MIN
Minimum
MOB
Man Over Board
NM
Nautical Mile
OPP HDG
Heading on opposite tack
POS
Position
RM
Relative Motion
RNG
Range
ROT
Rate Of Turn
RTE
Route
SAR
Search And Rescue
SOG
Speed Over Ground
SPD
Speed
STBD
Starboard
STW
Speed Through Water
TCPA
Time To Closest Point Of Approach
TGT
Target
TIME LOC
Local time
TM
True Motion
TRK
Track
TRK CRS
Track course to next waypoint
TWA
True wind angle
TWD
True wind direction
TWS
True wind speed
WOL
Wheel Over Line
WOP
Wheel Over Point
WPT
Waypoint name
WPT BRG
Bearing to waypoint
WPT DIST
Distance to waypoint
XTE
Cross track error
Terms and abbreviations| AP™ 44 Operator Manual
49

## Page 45

Supported data
Ú Note: NMEA 0183 and NMEA 2000 data output requires the
connection of relevant sensors.
NMEA 2000 PGN (transmit)
59904
ISO Request
60928
ISO Address Claim
126208
ISO Command Group Function
126996
Product Info
127258
Magnetic Variation
NMEA 2000 PGN (receive)
59392
ISO Acknowledgement
59904
ISO Request
60928
ISO Address Claim
126208
ISO Command Group Function
126992
System Time
126996
Product Info
127237
Heading/Track Control
127245
Rudder
127250
Vessel Heading
127251
Rate of Turn
127257
Attitude
127258
Magnetic Variation
128259
Speed, Water referenced
128267
Water Depth
128275
Distance Log
129025
Position, Rapid Update
12
50
Supported data| AP™ 44 Operator Manual

## Page 46

129026
COG & SOG, Rapid Update
129029
GNSS Position Data
129033
Time & Date
129283
Cross Track Error
129284
Navigation Data
129539
GNSS DOPs
129283
Cross Track Error
129284
Navigation Data
130074
Route and WP Service - WP List - WP Name & Position
130306
Wind Data
130576
Small Craft Status
130577
Direction Data
Supported data| AP™ 44 Operator Manual
51

## Page 47

ENGLISH
NAC™ -2/NAC™ -3
Commissioning Manual
www.lowrance.com | www.simrad-yachting.com | www.bandg.com

## Page 48

Contents
9
Introduction
9
NAC-2 and NAC-3 autopilot computers
9
The user interface
10
Autopilot controllers
10
Autopilot computer setup
13
Dockside setup
13
Data source selection
13
Input function
14
Auto/Standby
14
Disengage
14
SteadySteer
15
Disable input
15
Boat characteristics
15
Drive configuration
18
Rudder setup
21
Sea trial
21
Compass setup
22
Transition speed
23
Set rudder zero position
23
Set turn rate
24
Tuning the autopilot
28
User settings
28
Steering profile settings
29
Sailing parameters
30
Turn pattern settings
34
Installation verification
34
Checklist
34
Boat specific settings
37
Maintenance
37
Preventive maintenance
37
Checking the connectors
37
Software update
Contents | NAC-2/NAC-3 Commissioning Manual
7

## Page 49

37
Resetting the autopilot computer
39
Technical specifications
39
NAC-2
40
NAC-3
8
Contents | NAC-2/NAC-3 Commissioning Manual

## Page 50

Introduction
NAC-2 and NAC-3 autopilot computers
The NAC-2 and NAC-3 autopilot computers contain the electronics
needed to operate a hydraulic steering pump or mechanical drive
unit, while also interfacing with rudder feedback units and NMEA
2000 devices.
The NAC-2 is designed for boats up to 10 metres (33 feet) in length
and is suitable for low-current pumps, mechanical drive units, or
solenoid valves (8 A continuous/16 A peak).
The NAC-3 is designed for boats 10 metres (33 feet) or greater in
length and is rated to operate high-current pumps, mechanical
drive units, and solenoid valves (30 A continuous/50 A peak).
The user interface
Autopilot functions are presented a bit differently depending on the
device being used, for example multi-function displays (MFD) and
autopilot controllers (AP44 or AP48).
This manual shows screen examples from both an MFD running
NOS software and the AP48.
MFDs running NOS software and autopilot controller
displays
The instructions in this manual are for MFDs running NOS software
and autopilot controller displays like the AP48.
The screenshots in this manual are from an MFD running NOS
software and the AP48.
MFDs running NEON software
If the home page on your MFD looks similar to the following
illustration, then you have a NEON software based MFD.
To commission the autopilot connected to your NEON software
based system, select the Set up guide button on the home screen
and follow the prompts in the setup app. Alternatively, select the
settings button on the home page and navigate to the device set
up screen. Setting up connected devices is described in the
documentation available for the MFD running NEON software.
1
Introduction | NAC-2/NAC-3 Commissioning Manual
9

## Page 51

Autopilot controllers
The NAC can be controlled by various Navico control units. This can
be dedicated autopilot controllers, Multifunction displays (MFDs)
and autopilot remote controllers used in combination with
instrument systems, or any combination of the above.
Autopilot functions
NAC-2 and NAC-3 include a large range of functions, but not all
autopilot controllers have access to all options. E.g. autopilot
systems including only an autopilot remote controller (without
display unit) do not have access to turn patterns.
Autopilot computer setup
When the autopilot installation is completed, the setup of the
autopilot computer must be performed. Failure in setting up the
autopilot correctly may prohibit the autopilot from functioning
properly.
The setup of the autopilot computer is divided in two main steps:
•
Installation settings
-
Including dockside and seatrial commissioning. See "Dockside
setup" on page 13 and "Sea trial" on page 21
•
User adjustment of autopilot settings
10
Introduction | NAC-2/NAC-3 Commissioning Manual

## Page 52

-
Manual fine-tuning for various operational conditions and user
preferences. See "User settings" on page 28
Ú Note: Dockside settings can only be accessed when the
autopilot is in Standby mode.
Ú Note: Some systems require a dedicated physical standby key
to perform installation procedures. This key can be a key on the
autopilot controller, on an autopilot remote controller, or it can
be a separate standby key.
 Warning: When the autopilot is delivered from
factory and any time after an autopilot reset has been
performed, the installation settings are all reset to
factory preset (default) values. A notification will be
displayed, and a complete setup has to be made.
Failure to do so correctly may prohibit the autopilot
from functioning properly!
Introduction | NAC-2/NAC-3 Commissioning Manual
11

## Page 53

Installation setup workflow
12
Introduction | NAC-2/NAC-3 Commissioning Manual

## Page 54

Dockside setup
Data source selection
Before commencing with autopilot computer setup the data
sources must be available and configured.
Data sources selection is required on initial start-up of the system, if
any part of the network has been changed or replaced, or if an
alternative source is made available for a given data type and this
source has not been selected automatically.
You can let the system automatically select your sources, or set up
each source manually. Refer to documentation for the autopilot
controller or for the display unit for details about how to perform
the data source selection.
Input function
Determines how the autopilot computer/system reacts to an
external input. External input can be connected to blue/yellow wire
on NAC-2 and mode/function selector on NAC-3. For wiring details
and options, refer to the installation documentation.
Autopilot installation dialog, MFDs
2
Dockside setup | NAC-2/NAC-3 Commissioning Manual
13

## Page 55

Autopilot installation dialog, AP48
Auto/Standby
Select this mode if you have a toggle button connected to your
NAC-2 autopilot computer. Press the button to toggle between
Auto and Standby mode.
Disengage
Select this mode if you have a disengage switch connected to your
NAC-3 autopilot computer.
•
OPEN – Normal operation, can be controlled by controller.
•
CLOSED to OPEN – Activates Auto mode regardless of previous
state.
•
CLOSED – Disengaged. Cannot be controlled by controller.
SteadySteer
Select this mode if you have a SteadySteer connected to your
NAC-2/NAC-3.
•
Manual steering overrides the active mode.
•
If Auto mode or NoDrift mode was active before going into
manual steering, they will automatically re-engage when the
vessel has stabilized on a new course.
•
For any other modes, the autopilot goes into Standby mode.
•
If NAV mode was active before going into manual steering a
dialog will be shown.
-
Confirm course change to reactivate NAV mode.
-
Cancel the course change to activate Auto mode on the new
heading.
•
If no action is taken the autopilot will go into Standby mode.
14
Dockside setup | NAC-2/NAC-3 Commissioning Manual

## Page 56

Disable input
Select if no external input is connected, or to disable connected
input (default).
Boat characteristics
Boat type
Affects steering parameters as well as available autopilot features.
The following options are available:
•
Sail
•
Displacement
•
Planing
Ú Note: If the boat type is set to Sail, Virtual Rudder Feedback is
not available.
Boat length
Used by the autopilot system to calculate steering parameters.
Cruising speed
Used if no speed info is available. It is used by the autopilot system
to calculate steering parameters.
Drive configuration
The drive configuration controls how the autopilot computer
operates the steering system.
Refer to your drive unit documentation for relevant specifications.
Control method
Used for setting the appropriate control ouput for your drive.
The following options are available:
•
Solenoid
For on/off steering of hydraulic valves. Gives fixed rudder speed.
•
Reversible motor
For variable speed pumps/drives.
Dockside setup | NAC-2/NAC-3 Commissioning Manual
15

## Page 57

Drive voltage
Nominal drive voltage specified for your drive unit.
•
Options: 12 V and 24 V.
Ú Note: 24 V output is only available with 24 V supply.
The setting must match the spec of the solenoids/pump/motor.
 Warning: Selection of improper voltage level for your
drive unit may damage both the drive unit and the
autopilot computer even if the protection circuits are
activated.
Drive engage
Defines how the Engage output is used.
The following options are available:
•
Clutch
If your drive unit/motor/pump needs clutch to engage the
actuator, it shall be connected to the "engage" output. Configure
the "Drive engage" as clutch. The clutch will be activated when
autopilot computer is controlling the rudder. In standby, the
clutch is released to allow manual steering. Check specification of
your drive unit to determine whether clutch is required.
•
Auto
Output activated when autopilot computer is in Auto, NoDrift or
Navigation modes. For manual rudder control (Standby, NFU and
FU) the output is not activated. Typically used to switch between
two rudder speeds on a continuous running pump, used when
different rudder speeds are required for automatic and Follow-
up/Non-Follow-up steering.
Minimum rudder
Some boats may have a tendency to not respond to small rudder
commands around the “course keeping” position because of a small
rudder, whirls/disturbance of the water-stream passing the rudder,
or it is a single nozzle water jet boat. By increasing the Minimum
rudder parameter you may improve the course keeping
16
Dockside setup | NAC-2/NAC-3 Commissioning Manual

## Page 58

performance on some boats. However, this will increase the rudder
activity.
Ú Note: Only set a value for minimum rudder if it proves to give a
better course keeping performance in calm sea. It should be set
after the autopilot steering parameters have been optimised/
tuned.
Rudder deadband
Prevents the rudder from hunting induced by mechanical play in
the steering gear or rudder.
The following options are available
•
Auto
(Recommended).
The rudder deadband is adaptive and is continuously operative. It
will also optimize the deadband to the pressure on the rudder
•
Manual
If the Auto setting doesn’t perform properly due to extreme
rudder speed and/or overshoot, it can be adjusted manually. Can
also be used to reduce the rudder activity. Rudder commands
smaller than the size of the dead band will be ignored
Find the lowest possible value that will prevent the rudder from
continuous hunting. A wide deadband will cause inaccurate
steering. It is recommended to check rudder stability in AUTO mode
at cruising speed to get pressure on the rudder. (Slight hunting
observed dockside may disappear at cruising speed.)
Dockside setup | NAC-2/NAC-3 Commissioning Manual
17

## Page 59

Rudder setup
 Warning: During the rudder calibration and test the
autopilot computer issues a series of rudder
commands. Stand clear of the helm and do not
attempt to take manual control of the rudder during
this test!
Rudder source
The correct rudder source has to be selected before the rudder
feedback calibration can be performed.
Rudder source selection, MFDs
18
Dockside setup | NAC-2/NAC-3 Commissioning Manual

## Page 60

Rudder source selection, AP48
Rudder feedback calibration
Ú Note: Only available if you have a rudder feedback unit installed
and selected as rudder source.
The rudder feedback calibration determines the rudder feedback's
direction.
•
Follow the on-screen guided steps until the rudder calibration is
completed.
Rudder test
This rudder test verifies the drive direction. It detects minimum
power to drive the rudder and reduces the rudder speed if it
exceeds the maximum preferred speed for autopilot operation.
Ú Note: If the boat uses power assisted steering, it is important
that the engine or electric motor used to enable the power
assist steering is turned on prior to this test.
•
Run the rudder test as described in the on-screen instructions
-
Rudder should make a small movement within 10 seconds,
then follow up with travelling both directions
Failure to complete test will result in an alarm.
VRF calibration
Ú Note: Only available if the rudder source is set to a virtual
rudder feedback.
Dockside setup | NAC-2/NAC-3 Commissioning Manual
19

## Page 61

VRF calibration determines the direction of rudder movement, the
minimum output required to move the rudder and the voltage to
rudder speed ratio.
To perform the VRF calibration you must be able to view the
movement of the rudder.
•
Follow the on-screen guided steps until the VRF calibration is
completed.
Ú Note: When you get asked if the rudder moved you may have
to select no several times to ensure the pump provides enough
power to turn the motor at high vessel speed.
20
Dockside setup | NAC-2/NAC-3 Commissioning Manual

## Page 62

Sea trial
 Warning: An autopilot is intended only as a
supplemental aid to navigation. It IS NOT a
replacement for a human navigator or prudent
seamanship. Never leave the helm unattended.
A seatrial can only be performed after the dockside settings are
completed.
Ú Note: The seatrial must always be performed in calm
conditions, in open waters and at a safe distance from other
traffic.
Compass setup
To achieve the best possible performance, the compass should be
calibrated, and any offsets should be compensated for.
The setup needs to be done from an appropriate display unit.
Depending on the unit, access to the compass setup is available
from the compass’s device dialog, or from a dedicated Calibration
option in the unit’s Settings menu.
Device dialog, MFDs
3
Sea trial | NAC-2/NAC-3 Commissioning Manual
21

## Page 63

Calibration option, AP48
Ú Note: The setup of the compass should be done in calm sea
conditions and with minimal wind and current to obtain good
results. Ensure that there is enough open water around the
vessel to make a full turn.
Refer to your heading sensor's documentation for further details for
your unit.
Transition speed
Ú Note: Only available if the boat type is set to Planing.
The transition speed is the speed at which the system automatically
changes between Low speed and High speed profiles.
The profiles are used to accommodate the boats' tendency to
exhibit different steering characteristics at different speeds. You may
also have different preferences about the steering performance of
your boat required at low and high speeds.
It is recommended that you set a value that represents the speed
where the boat's steering characteristics change. For instance the
planing threshold (recommended), or at the speed you want the
autopilot to change behavior.
There is a 2 knots hysteresis to prevent oscillation of high/low
settings when the vessel is travelling at or near the transition speed.
Example
The transition speed is set to 9 knots.
•
The system changes from Low profile to High profile when the
speed increases to 10 knots (= Transition speed plus 1 knot)
22
Sea trial | NAC-2/NAC-3 Commissioning Manual

## Page 64

•
The system changes from High profile to Low profile when the
speed decreases to 8 knots (= Transition speed minus 1 knot)
The active profile ('Low' or 'High') is shown in the autopilot page
(e.g. AP44) and in the autopilot pop-up (MFDs):
AP48 page
MFD Autopilot control bar
Set rudder zero position
Used to correct the rudder zero position found during dockside
commissioning if the boat needs a small rudder offset in order to
steer straight.
Ú Note: Setting rudder zero position should always be done in
calm conditions, where steering is not affected by wind and/or
current.
Bring the rudder to the position where the boat steers straight, then
activate the Set rudder zero option to save the rudder zero
parameter.
Ú Note: On dual engine boats, verify that the engine RPM is equal
on both engines so that the thrust from both propellers is
equal. Otherwise, the zero rudder position might be set wrong.
Set turn rate
Used for setting the preferred turn rate of the boat.
Bring the boat into a turn with the preferred safe and comfortable
turn rate, then activate the Set turn rate option to save the turn
rate parameters.
Ú Note: The captured turn rate will be stored in the active
steering profile. This setting must therefore be repeated for
each steering profile.
Sea trial | NAC-2/NAC-3 Commissioning Manual
23

## Page 65

Tuning the autopilot
Ú Note: Tuning of the autopilot must be done separately for low
and high speed profiles.
Both Autotune and manual tuning should be performed in
calm or moderate sea conditions.
Providing you have entered correct vessel type, length and cruising
speed, you may not have to perform further manual or automatic
tuning.
Proceed as follows to verify satisfactorily steering:
1. Stabilize the vessel on a heading, and then select AUTO mode
2. Observe course keeping and rudder commands
- The autopilot should keep the vessel on the set heading
within an average of +/-1 degree, providing calm sea and
wind
3. Make some small and bigger heading changes to port and
starboard and observe how the vessel settles on the new
heading
- The vessel should have a minimum of overshoot. See "Rudder
gain" on page 26 and "Counter rudder" on page 26.
If the autopilot is not keeping the heading satisfactorily or not
making the turns satisfactorily, you may now either try the Autotune
function or go directly to manual tuning.
Ú Note: If the vessel is more than approximately 30 m/100 ft or
has a very high cruising speed it may be unpractical to perform
Autotune. It is then suggested to proceed with manual tuning.
Autotuning
When performing an autotune, the vessel will automatically be
taken through a number of S-turns. Based on the vessel behavior,
the autopilot will automatically set the most important steering
parameters (Rudder gain and Counter rudder).
•
Stabilize the vessel on a heading and set the speed between 5-10
kn, then select Autotune.
-
The autopilot will now switch to AUTO mode and take control
of the vessel.
Ú Note: Autotuning can be stopped at any time by pressing the
STBY key on the autopilot controller.
24
Sea trial | NAC-2/NAC-3 Commissioning Manual

## Page 66

The autotuning takes approximately 3 minutes to complete. When
completed the autopilot automatically switches to Standby mode,
and the rudder must be controlled manually.
Ú Note: All parameters that are set during autotuning can be
manually adjusted. For optimal steering performance it is
recommended to manually adjust the steering parameters after
running the autotune.
Manual tuning
Rudder gain and Counter rudder can be manually adjusted.
•
Stabilize the vessel on a heading and set the speed in the middle
of the profile range (well clear of the transition speed) to avoid
profile switching during tuning. Then activate the Rudder gain
option. Adjust the value according to the descriptions below.
•
If required, adjust slightly the Counter rudder option.
Tuning parameters, MFDs
Sea trial | NAC-2/NAC-3 Commissioning Manual
25

## Page 67

Tuning parameters, AP48
Rudder gain
This parameter determines the ratio between commanded rudder
and the heading error. The higher rudder gain value the more
rudder is applied. If the value is too small it will take a long time to
compensate for a heading error, and the autopilot will fail to keep a
steady course. If the value is set too high the overshoot will increase
and the steering will be unstable.
A
B
A
The value is set too high. Steering becomes unstable and
often the overshoot will increase
B
The value is set too low. It will take a long time to
compensate for a heading error, and the autopilot will fail to
keep a steady course
Counter rudder
Counter rudder is the amount of counteracting (opposite) rudder
applied to stop the turn at the end of a major course change. The
settings depend on vessel’s characteristics, inertia, hull shape and
rudder efficiency.
26
Sea trial | NAC-2/NAC-3 Commissioning Manual

## Page 68

•
If the vessel has good dynamic stability, a relatively small value
will be sufficient
•
An unstable vessel will require high value
•
The greater the vessel’s inertia, the greater value will be required
Increasing counter rudder value may result in some higher rudder
activity also when steering a straight course, particularly in high
waves.
The best way of checking the value of the Counter rudder setting is
when making turns. The figures illustrate the effects of various
Counter Rudder settings.
A
B
C
A
Counter rudder value too low; overshoot response
B
Counter rudder value is too high; sluggish and creeping
response
C
Correct setting of Counter rudder; ideal response
Perform various course changes and observe how the boat settles
on the new heading. Start with small changes, 10-20 degrees, and
proceed with bigger changes, 60-90 degrees. Adjust Counter rudder
value to obtain best possible response as in illustration C.
Ú Note: As many boats turns differently to port versus starboard
(due to propeller rotation direction), do the course changes in
both directions. You may end up with a compromise setting of
Counter rudder that gives a little overshoot to one side and a
bit creeping response to the other.
Sea trial | NAC-2/NAC-3 Commissioning Manual
27

## Page 69

User settings
The user settings can be configured differently between the
different profiles, depending on boat steering characteristics and
user preferences.
Steering profile settings
The NAC include two steering profiles (High and Low), used for high
and low boat speed.
The initial parameters are automatically assigned when you select
your vessel type. During the seatrial the parameters will be tuned for
optimized steering performance. See "Tuning the autopilot" on page 24.
The options listed in the next pages are available for both High and
Low speed profiles.
For Rudder gain and Counter rudder, see "Rudder gain" on page 26 and
"Counter rudder" on page 26.
Turn rate
Used for manually setting the turn rate used when the heading
change is larger than 5°.
Autotrim
Controls how fast the autopilot will apply rudder to compensate for
a constant heading offset, e.g. when external forces such as wind or
current affects the heading. Lower autotrim will give faster
elimination of a constant heading offset
Init rudder
Defines how the system moves the rudder when switching from
hand steering (Standby, FU and NFU) to an automatic mode.
The following options are available:
•
Center
Moves the rudder to zero position
•
Actual
Maintains the rudder angle, and assumes that the current rudder
angle is the trim required to maintain a steady heading.
4
28
User settings | NAC-2/NAC-3 Commissioning Manual

## Page 70

Rudder limit
Determines the dynamic range of the rudder before its movement
is restricted and alarm is triggered. Typical usage is to limit the
amount of rudder action caused by yawing in following sea.
Ú Note: Rudder limit is not a hard limitation of the rudder range,
only around the current setpoint.
This Rudder limit does not affect Non-Follow-up or Follow Up
steering.
Off heading limit angle
Sets the limit for the off heading alarm.
When the alarm option is activated an alarm occurs when the actual
heading deviates from the set heading more than the selected limit.
Track response
Defines how aggressively the autopilot should steer towards the
active route's leg.
Track approach angle
This setting is a limit to prevent approaching the track too steeply.
Approaching the track at shallower angles is permitted depending
on the cross track distance (XTD) and track response setting.
This setting is used both when you start navigating and whenever
the autopilot is working the boat towards the route.
Course change confirm angle
Defines the limit for automatic course change to next waypoint in a
route when the autopilot is following a route (NAV mode).
If the course change is greater than this set limit, you are prompted
to verify that the upcoming course change is acceptable.
Sailing parameters
Ú Note: Only available if the boat type is set to SAIL.
Wind mode
Select what wind angle the autopilot will steer towards.
User settings | NAC-2/NAC-3 Commissioning Manual
29

## Page 71

The following options are available:
•
Auto
If True Wind Angle (TWA) is <70º: Wind mode will steer towards
Apparant Wind Angle (AWA)
If TWA is !70º: Wind mode will steer towards TWA
•
Apparent
Steers towards AWA
•
True
Steers towards TWA
Tack time
Controls how fast the autopilot tacks in wind mode.
Tack angle
Controls the angle that the boat will tack to in AUTO mode.
Manual speed
If neither boat speed nor SOG data are available and/or deemed
unreliable, a manual value for speed can be entered and used by
the autopilot to aid steering calculations.
Turn pattern settings
The autopilot computer supports a number of automatic turn
steering features when the autopilot is in AUTO mode.
Ú Note: Turn pattern steering is not available if the boat type is
set to Sail.
All turn patters, except the U-turn, have associated turn pattern
settings. Depending on the autopilot controller these turn pattern
settings can be adjusted before you start the turn or during the turn.
30
User settings | NAC-2/NAC-3 Commissioning Manual

## Page 72

Turn pattern settings, MFD
Turn pattern settings, AP48
Ú Note: Not all autopilot controllers include turn pattern steering.
Refer to your autopilot controller for more information.
C-turn (Continuous turn)
Steers the vessel in a circle.
•
Turn variable:
-
Rate of turn. Increasing the value makes the vessel turn a
smaller circle.
User settings | NAC-2/NAC-3 Commissioning Manual
31

## Page 73

U-turn
Changes the current set heading to be 180° in the opposite
direction.
Spiral turn
Makes the vessel turn in a spiral with a decreasing or increasing
radius.
•
Turn variables:
-
Initial radius
-
Change/turn. If this value is set to zero, the boat will turn in a
circle. Negative values indicate decreasing radius while positive
values indicate increasing radius.
Ú Note: This turn pattern is not available for HDS Live multi-
function displays.
Zigzag turn
Steers the vessel in a zigzag pattern.
•
Turn variables:
-
Course change (A)
-
Leg distance (B)
B
A
Square turn
Makes the vessel automatically turn 90° after having travelled a
defined leg distance.
•
Turn variable:
-
Leg distance
S-turn
Makes the vessel yaw around the main heading.
•
Turn variables:
-
Course change (C)
-
Turn radius (D)
32
User settings | NAC-2/NAC-3 Commissioning Manual

## Page 74

D
C
Depth contour tracking (DCT)
Makes the autopilot follow a depth contour.
Ú Note: DCT turn pattern is only available if the system has a valid
depth input.
 Warning: Do not use the DCT turn pattern unless the
seabed is suitable. Do not use it in rocky waters where
the depth is varying significantly over a small area.
•
Turn variables:
-
Depth gain. This parameter determines the ratio between
commanded rudder and the deviation from the selected depth
contour. The higher depth gain value the more rudder is
applied. If the value is too small it will take a long time to
compensate for drifting off the set depth contour, and the
autopilot will fail to keep the boat on the selected depth. If the
value is set too high the overshoot will increase and the
steering will be unstable.
-
CCA. The CCA is an angle that is added to or subtracted from
the set course. With this parameter you can make the boat yaw
around the reference depth with s movements. The larger the
CCA the bigger yawing will be allowed. If the CCA is set to zero
there is no S-ing.
-
Ref. depth. This is the reference depth for the DCT function.
When DCT is initiated the autopilot reads the current depth
and set this as the reference depth. The reference depth can be
changed when the function is running.
Ú Note: If depth data is lost during DCT the autopilot will
automatically switch to AUTO mode.
It is recommended to turn ON the AP Depth Data Missing alarm
when using DCT. When this alarm is activated an alarm will be
raised if the depth data is lost during DCT.
User settings | NAC-2/NAC-3 Commissioning Manual
33

## Page 75

Installation verification
When all units in the autopilot system are installed, external
equipment connected and the software configured according to
the previous chapters, the installation should be verified according
to the checklist. The boat specific settings should be noted down in
the relevant tables included this chapter.
Checklist
Description
Reference
Units mounted and secured
according to instructions
Installation instructions for the
units
Network powered and
terminated according to
instructions
Wiring instructions for the units
Sources selected
Autopilot control unit
documentation
Vessel configured
"Boat characteristics" on page 15
Drive units configured and
calibrated
"Drive configuration" on page 15
Compass calibrated
"Compass setup" on page 21
Seatrial completed (manual or
autotune)
"Sea trial" on page 21
Boat specific settings
Boat
Settings
Boat type
Boat length
Cruising speed
Transition sped
5
34
Installation verification | NAC-2/NAC-3 Commissioning
Manual

## Page 76

Drives
Settings
Drive type
Drive control method
Nominal drive voltage
Drive engage
Minimum rudder
Rudder deadband
Manual deadband
Minimum output
Maximum output
Sailing parameters
Settings
Wind mode

Tack time

Tack angle

Manual speed

Steering profiles
Settings
Low Speed
High Speed
Turn Rate


Rudder gain


Counter rudder


Autotrim


Init rudder


Rudder limit


Installation verification | NAC-2/NAC-3 Commissioning Manual
35

## Page 77

Settings
Low Speed
High Speed
Off heading limit


Track response


Track approach
angle


Course change
confirm angle


Turn Pattern settings
Settings
Continuous
Rate of turn
Spiral
Initial radius
Change/turn
Zigzag
Course change
Leg distance
Square
Leg distance
Lazy-S
Course change
Turn radius
Depth contour
Depth gain
CCA
36
Installation verification | NAC-2/NAC-3 Commissioning
Manual

## Page 78

Maintenance
Preventive maintenance
The unit does not contain any field serviceable components.
Therefore, the operator is required to perform only a very limited
amount of preventative maintenance.
Checking the connectors
The connectors should be checked by visual inspection only.
Push the connector plugs into the connector. If the connector plugs
are equipped with a lock, ensure that it is in the correct position.
Software update
You can update the software for the autopilot computer from a
display unit connected to the network.
You can check the autopilot computer's software version from the
display unit's Device list.
The latest software is available for download from the product
webpage at: www.lowrance.com, www.simrad-yachting.com and
www.bandg.com.
Resetting the autopilot computer
You can reset the autopilot to factory default settings.
Reset autopilot computer, MFDs
6
Maintenance | NAC-2/NAC-3 Commissioning Manual
37

## Page 79

Reset autopilot computer, AP48
The first time the autopilot computer is started after reset, it will run
through the automatic setup-procedure.
Ú Note: Unless you need to clear all values set during the
installation set-up procedure, you should not perform a reset of
the autopilot computer.
38
Maintenance | NAC-2/NAC-3 Commissioning Manual

## Page 80

Technical specifications
Ú Note: The most up-to-date specifications list is available at:
www.lowrance.com, www.simrad-yachting.com and
www.bandg.com.
NAC-2
Approvals
Compliance EMC directive 2014/30/EU
Electrical
Supply voltage 9-31.2 V DC
Power consumption - Max 500 W
Power consumption - Typical As required to drive rudder
actuator. See pump/motor
power ratings
Recommended fuse rating 20 A
Environmental
Operating temperature -25°C to +55°C (-13°F to 131°F)
Storage temperature -30°C to +70°C (-22°F to 158°F)
Waterproof rating IPx5
Humidity 100%
Shock and vibration Acc to EN60945
Connectivity
NMEA 2000 1 Micro-C port, 1 LEN
Drive 12/24 V DC, min 10 mA, max 3 A
Rudder Feedback Variable voltage/resistive 0‐5 V
Physical
Weight 0.6 kg (1.3 lbs)
Compass Safe Distance 500 mm (20 inches)
Warranty
2 years
7
Technical specifications | NAC-2/NAC-3 Commissioning Manual
39

## Page 81

NAC-3
Approvals
Compliance EMC directive 2014/30/EU
Electrical
Supply voltage 12/24 V DC +/- 10-30%
Power consumption - Max 750 W
Power consumption - Typical As required to drive rudder
actuator. See pump/motor
power ratings
Recommended fuse rating 30 A
Environmental
Operating temperature -25°C - +55°C (-13°F - 131°F)
Storage temperature -30° - +70°C (-22°F - 158°F)
Waterproof rating IPx5
Humidity 100%
Shock and vibration Acc to EN60945
Connectivity
NMEA 2000 1 Micro-C port, 1 LEN
NMEA 0183 1 port IN/OUT. 4.8, 9.6,
19.2 & 38.4 kbaud
Drive •
Reversible motor control
of rudder.
Max continuous load 30
A, peak 50 A for 1s
or
•
On/off
solenoid control of rudder.
12/24 V DC,
common, load range 10
mA to 10 A, off current <1 mA
Engage Output for bypass/clutch. 12/24
V DC, min 10 mA, max 3 A
40
Technical specifications | NAC-2/NAC-3 Commissioning
Manual

## Page 82

Rudder Rudder angle, frequency input.
15 V, 1.4 to 5 kHz, resol. 20 Hz/°
Remote •
Input: External open/
close contact for remote
controller
•
Output: High/Low mode
indicator signal
Mode External open/close
or pulse contact for autopilot
disengage
Alarm External alarm output for
buzzer/relay. Max 100 mA,
voltage level as local supply
Physical
Weight 0.7 kg (1.6 lbs)
Compass Safe Distance 500 mm (20 inches)
Warranty
2 years
Technical specifications | NAC-2/NAC-3 Commissioning Manual
41

## Page 85

*988-11233-004*
