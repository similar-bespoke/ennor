import os
import re

# Define the repository directory (root of the repo)
repo_dir = "."
# Define file extensions to include
doc_extensions = (".pdf", ".txt", ".md")

# Base content as a template
base_content = """# Ennor Maintenance & Technical Documents Archive

#ennor

## 1. Engine Bay
    1.1 Yanmar 8LV370 - 
       1.1.1 Oil Filter Spec
       1.1.2 Fuel Filter Spec
    1.2 Calorifier - 
    1.3 Main Water Pump - 
    1.4 Webasto Heater - 

## 2. Energy Management
    2.1 Mastervolt MV 12/6000
    2.2 Generator - Fischer Panda 8000iPMS 6.4kW
    2.3 CZone
    2.4 Solar Panels - 2 x Solara S280M43 + 3 x Solara S705M43
    2.5 Shore Power system (breakers etc)

## 3. Thrusters
    3.1 Sleipnir SE100 - 

## 4. Helm
    4.1 Simrad NSS evo3S - 
    4.2 Simrad Autopilot - 
    4.3 Lenco Pro Trim Tabs - 
    4.4 Simrad VHF - 
    4.5 Sentinel Monitoring - 
    4.6 Lewmar Anchor chain counter
    4.7 SeaFire unit

## 5. Topside
    5.1 Simrad Radar - Halo20+ - 
    5.2 Marinco S/S 5” Spotlight - 
    5.3 Lumishore Floodlight - 
    5.4 Ominsense Ulysses MicroS+ thermal camera -
    5.5 Echomax AX Active Radar Reflector -
    5.6 Calypso Instruments ULP Wind Sensor - 
    5.7 Starlink Marine - 
    5.8 Iris 735 cameras
    5.9 IP Camera Encorder - Clinton Electronics E04HDA

## 6. Galley
    6.1 Oven
    6.2 Hob
    6.3 Fridge
    6.4 Fridge/Freezer

## 7. Cockpit
    7.1 Scanstrut Atmos Inflator
    7.2 Life raft
    7.3 Tender
    7.4 Torqueedo

## 8. Sundries
    8.1 Pre-delivery inspection checklist
"""

# Collect all files in the repo
file_map = {}
for root, _, files in os.walk(repo_dir):
    for file in files:
        if file.endswith(doc_extensions) and file != "resources.html":
            match = re.match(r"(\d+\.\d+)", file)
            if match:
                number = match.group(1)
                rel_path = os.path.relpath(os.path.join(root, file), repo_dir)
                file_map[number] = (file, rel_path)

# Start building the HTML with styling
html_lines = [
    "<!DOCTYPE html>",
    "<html lang='en'>",
    "<head>",
    "<meta charset='UTF-8'>",
    "<meta name='viewport' content='width=device-width, initial-scale=1.0'>",
    "<title>Ennor