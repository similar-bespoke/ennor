---
vessel: Ennor
title: "CZone Favourites Configuration Tool Instructions v1.1"
category: "Energy Management"
source_pdf: "library_czone/CZone Favourites Configuration Tool Instructions v1.1.pdf"
extraction_method: native
page_count: 15
converted: "2026-02-24"
---

# CZone Favourites Configuration Tool Instructions v1.1

**Vessel:** Ennor | **Category:** Energy Management
**Source PDF:** library_czone/CZone Favourites Configuration Tool Instructions v1.1.pdf | **Pages:** 15 | **Extraction:** native

---

## Page 1

CZone Favourites Tool
User Instructions

V1.1

## Page 2

2
EN / CZone® Favourites Tool Instructions



TABLE OF CONTENTS:

1
GENERAL INFORMATION .............................................................................................................................................. 3
1.1
Description ......................................................................................................................................................... 3
1.2
Use Of This Manual ............................................................................................................................................ 3
2
GETTING STARTED ........................................................................................................................................................ 4
2.1
What You Need .................................................................................................................................................. 4
2.2
Installing the CZone Favourites Tool .................................................................................................................. 4
3
CREATING A FAVOURITES PROJECT ......................................................................................................................... 6
3.1
Initial Setup ......................................................................................................................................................... 7
3.2
CZone favourites tool screen .............................................................................................................................. 8
3.3
Screen size/type and preview ............................................................................................................................. 9
3.4
Monitoring and Modes Configuration .................................................................................................................. 9
3.5
Boat Image Configuration ................................................................................................................................. 11
4
EXPORTING THE FAVOURITES PACKAGE ............................................................................................................... 13
5
EDITING CZONE CONFIGURATION ............................................................................................................................ 15

## Page 3

EN / CZone® Favourites Tool Instructions
3


1 GENERAL INFORMATION

1.1
DESCRIPTION

This manual will outline the necessary steps to create a favourites Project for a new or existing CZone system.  This project file
is necessary to build the favourites pages of the CZone 2.0  App with the required control, monitoring and modes items needed
for quick access.  Once the project file is completed it can be written to the CZone display and used to quickly access the
commonly used functions.

1.2
USE OF THIS MANUAL

Copyright © 2017 CZone. All rights reserved. Reproduction, transfer, distribution or storage of part or all the contents in this
document in any form without the prior written permission of CZone is prohibited.

## Page 4

4
EN / CZone® Favourites Tool Instructions


2 GETTING STARTED

2.1
WHAT YOU NEED

Before commencing a new Favourites project, ensure you have the following items:

•
A correctly-configured CZone network with a CZone Touch 5, 7 or 10 Display running CZone 2.0 (v6.12.4.0 or newer)
•
The CZone configuration file (.zcf) for that network, either saved to the computer you are working on or a removable
storage device (USB or SD card).
•
The CZone Favourites Tool software.
•
Optionally, suitable image file or files of the vessel or vehicle you wish to configure a graphical interface for.


2.2
INSTALLING THE CZONE FAVOURITES TOOL

Follow the below steps to install the CZone Favourites Tool.

1.
Double click on the ‘CZone Favourites Tool Installer’ file.

2.
Click Next.


3.
 Select a location for the program to be installed or click Next for the default location.

## Page 5

EN / CZone® Favourites Tool Instructions
5




4.
Select the Start Menu folder in which you would like to create shortcuts for the program or click Install for the default
location.


5.
When installation has completed click the Close button.  You can now launch the tool from the Start Menu.

## Page 6

6
EN / CZone® Favourites Tool Instructions



3 CREATING A FAVOURITES PROJECT

The purpose of the Favourites Project is to build custom favourites pages to be loaded onto a CZone Touch Display or Wireless
Interface (for iPad control).  The favourites pages are where the user has quick access to Modes, Monitoring and Control
circuits, including one or more vessel images for feedback of systems on and alarms. The favourites pages follow a grid format,
where items are placed on a fixed layout based on the display size.  This format allows flexibility on what type and where items
are placed for the best user experience.

See Figure 1 for an example of the Touch 5 Home Page, while Figure 2 shows an example of a similar page, with additional
options, on a Touch 10 display.





To build a Favourites Project a CZone Configuration File (.zcf) from the vessel is needed.  This is used to reference the existing
circuit and monitoring ID’s to ensure the system functions seamlessly from multiple displays.  You will also optionally need a
high-quality image (or images) in .PNG or .JPG format of the vessel if you want to implement a Boat View.


Modes Favourites
Monitoring and
Controls
Boat View
Figure 1: Touch 5 Example Home Page
Modes Favourites
Monitoring and
Controls
Boat View
Figure 2: Touch 10 Example Home Page

## Page 7

EN / CZone® Favourites Tool Instructions
7


3.1
INITIAL SETUP

Before you can start using the CZone Favourites Tool you need to create or open a Project that contains the configuration
information for the installation (vessel or vehicle) that this project relates to. You will see that the initial screen is largely blank,
with most options greyed out. The three active options are to start a New Project, Open a Project, or Import an existing .cfp
Favourites Package (from a previously-configured Touch 5 or Touch 10 display).

From the CZone Favourites Tool screen click on the New Project button.




1.
Enter a name for the project.

2.
Press Browse and select a directory to save the project, or type in the path to the required directory. Note the directory
will default to the same name you have entered for the project, within the CZone folder.

3.
Press Browse and select the CZone Configuration File (.zcf) that will be used to create the project. This file should
have been created previously using the CZone Config Tool.

4.
Select OK.



1
2
3

## Page 8

8
EN / CZone® Favourites Tool Instructions


3.2
CZONE FAVOURITES TOOL SCREEN

Once we have an active project, several more elements appear on the screen.

1.
Select the tab for the target display (Touch 10/Tablet, Touch 5 or Touch 7).  The layouts are independent, so you can
create two completely different favourites pages for each size.

2.
Use these buttons to add, edit or remove an image of your boat (See section 3.4 Boat Image Configuration) if you
want to create a visual display.

3.
Various display resolutions are available, to preview what the Favourites page will look like on different devices. Use
the drop-down options here to choose the target devices, such as an iPad. Note changing the display does not change
the layout of your Favourites page, merely provides a preview of how it will appear on that device.

4.
These tabs are where you select items from your configuration to add to the favourites page. The exact content of
these are imported from the configuration – only Circuits, Monitoring, Modes and Alarms that have previously been
created will appear here. You cannot create additional items in the CZone Favourites tool – those must be created
using the CZone Config Tool.

1
2
4
3
5

## Page 9

EN / CZone® Favourites Tool Instructions
9


5.
Multiple favourites pages can be created. This tab is used to select the page to work on, and add or remove additional
pages. On the device, favourites pages are accessed by swiping left or right between pages.

3.3
MONITORING AND MODES CONFIGURATION

Modes of Operation are most commonly added along the top of a Favourites Page. Below that you can add controls for
individual Circuits, as well as any items you would like to monitor (battery voltages, tanks levels etc.). These can be placed in
any order you prefer, and some controls have multiple display options.

Follow the steps below to add any favourite Modes of operation, Circuits and/or Monitoring items that the user would like
displayed on the Favourites page.



1.
Select the screen layout you wish to create a Favourite for (Touch 5 or Touch 10).

2.
Select the Modes tab from the top right.

3.
Drag and drop the required Modes from the imported CZone Configuration into the Modes bar (See item 4) along the
top of the screen layout.

4.
Although a maximum of four Modes can displayed simultaneously on the Touch 5 screen (Six Modes on the Touch
10), further modes can continue to be added. If there are more items than will fit on the screen then the modes bar
becomes scrollable, indicated by blue arrows on either end.

5.
Select either the Circuits or Monitoring tab from the top right.

6.
Drag and drop the required Circuits or Monitoring items from the imported CZone Configuration into the Monitoring
box in the centre of the screen layout.


2
3
4
6
5
1
9

## Page 10

10
EN / CZone® Favourites Tool Instructions



7.
When a circuit is dropped onto the screen layout, a dialog box appears that allows several options. Buttons can be
shown as a single on/off button (the default option), or as a double-throw button with separate on and off buttons. The
double throw can also be arranged horizontally or vertically, with the two buttons either side by side or one above the
other.







8.
Additionally, the icon on the button can be changed to something more representative of the
circuit being controlled. Hence a fan icon can be used for a blower, and snowflake for the air
conditioning, and so on. To change the icon, click inside the icon shown on the button, and a
list of alternatives appears. Click on the preferred option and it will be used. Click OK when
finished.


9.
Optionally, once you have dropped all the required circuits onto the screen layout, select
different displays and check how the page will render at other resolutions.


Repeat Step 1 for configuring further screen layouts.


7
8

## Page 11

EN / CZone® Favourites Tool Instructions
11


3.4
 BOAT IMAGE CONFIGURATION

In addition to the buttons and gauges, Circuits and Alarms can also be displayed visually over an image of the vessel or
vehicle. This is achieved by first importing a suitable image, and then dropping icons onto the image to show where they are
located. If one of the alarms should sound, a visual indicator will not only show what the alarm is but also where it is located.

Both .png and .jpg file format are supported. The best results are achieved with a .png file with a transparent background as
this format lets the image float over the display background colour. However, static images, such as a photograph of the boat,
are also supported. For best results the image should be approximately 4:3 ratio of width to height, although the image can be
resized and cropped to fill the space.  Note: maximum file size limits for any image is 5MB


1.
Select the Favourites page you wish to add the image to.

2.
Then select Add Image. Browse to find the image you wish to use, then select Open.

3.
Click the appropriate buttons to reposition the image on the page.

4.
You can also change the image width and height to fit the space.
1
2
3
4
5
6

## Page 12

12
EN / CZone® Favourites Tool Instructions


5.
You can Resize Without Cropping, which then pads of the image with blank space, or Resize With Cropping, which
then cuts some part of the image off depending on how it is resized.

6.
If the image has a transparent background (.png file) you can select what colour to use for the background. If your
image has a solid background then this option sets the colour of the padded areas that have been added to make the
image fit.

7.
And lastly, select OK to save the image.
Now the image has been placed, you can add circuits and alarms to that image. Note that Monitoring items cannot be added to
the boat image.

1.
Select the circuits tab from the top right.

2.
Drag and drop the required circuits from the imported CZone Configuration.

3.
Place these on the boat image where feedback from the system is required. This also
populates the dynamic control menu you will see on the device for that particular boat view.

4.
When you drop the icon, a dialog box appears allowing an appropriate icon to be selected, and
enables the option to hide the circuit when it is turned off. This simplifies the display.

Select the alarms tab and repeat if any alarms are required on the boat image.  There is no limit to alarms allowed.
Alarms cannot have their icon changed.

5.
Press the Save Project button to save the project.

Repeat the process if any other boat views or devices are required.



1
2
5
3
4

## Page 13

EN / CZone® Favourites Tool Instructions
13


4 EXPORTING THE FAVOURITES PACKAGE

Now that the Favourites Project is complete it needs to be packaged into a new format and sent to the device.  This file is a
CZone Favourites Package (.cfp) file. This file can either be saved to an SD card or USB memory stick and physically loaded
into the Touch  display, or sent over WiFi (Touch 5, 7 and Wireless Interface)

1.
In the CZone Favourites select Create .cfp Favourites Package.

2.
You will be prompted to Save the Project. Select OK.

3.
Now browse to the location where you wish to save the favourites package (such as an external memory card)


4.
If you wish to change the name of the file, edit the default filename created and press Save.

If you wish to send the file wirelessly to the Touch 5, 7 or Wireless Interface, you must be connected to it over Wi-Fi.  Refer to
the device’s user manual for details on this process.

Assuming you have followed those steps, you can send the favourites package to the device:

1.
In the CZone Favourites Tool, select Send .cfp Package to Device.

## Page 14

14
EN / CZone® Favourites Tool Instructions


2.
Select the Server corresponding to your CZone network. Enter username as “user” and password as “password”
(unless the default username and passwords have been changed on the device) and select Connect.

3.
The Favourites package should start sending to the device.


4.
The above window will show the progress of the upload.  Once the progress reaches 100%, click the OK button.  The
Touch 5 now has a copy of the Favourites Project that has been created. This will now be loaded on the display and
you will see the favourites pages as configured.


If the CZone Configuration is changed at any point (for example if a circuit has been added to the system) then go to Project >
Reload CZone Configuration and browse to the new config and select OK.  The Alarms/Circuits/Modes and Monitoring tabs will
be updated with any new changes. Make any changes to the favourites page and then follow these steps again to create the
new Favourites Package.

## Page 15

EN / CZone® Favourites Tool Instructions
15


5 EDITING CZONE CONFIGURATION

Any changes required to the CZone Configuration File are made with the CZone Config tool. This is a separate piece of
software which must be installed on your computer. It is best to edit the CZone Configuration File from within the CZone
Favourites Tool, as shown here, since the updates are then automatically pulled through to the Favourites file.

1.
In the Favourites Tool go to Project > Edit CZone Configuration

2.
The CZone Configuration Tool will open and load the .zcf file imported in the project.

3.
Make necessary changes to the .zcf file and then press ‘Save Config to File’.  An example would be adding a new
circuit.

4.
A window will open in the ‘Save CZone Config Here’ folder created during the Wireless Project setup. Save the new
.zcf file in this location and close the configuration tool. A prompt will then appear to say that changes have been
detected to the configuration.


5.
Select OK to confirm Configuration Changes and the CZone Favourites Tool will import the new file

6.
The new changes will now take effect.  In this example if we added a new circuit, that circuit will show in the Circuits
window and cab be dragged onto the boat view.



7.
Repeat this process for any further CZone Configuration changes.


6
