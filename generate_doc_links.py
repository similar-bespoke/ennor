import os
import re

# Define the repository directory (root of the repo)
repo_dir = "."
# Define file extensions to include
doc_extensions = (".pdf", ".txt", ".md")

# Base content as a template (in Markdown-like structure, but we'll convert to HTML)
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
        if file.endswith(doc_extensions) and file != "resources.html":  # Exclude resources.html itself
            match = re.match(r"(\d+\.\d+)", file)
            if match:
                number = match.group(1)
                rel_path = os.path.relpath(os.path.join(root, file), repo_dir)
                file_map[number] = (file, rel_path)

# Process the base content and convert to HTML
html_lines = [
    "<!DOCTYPE html>",
    "<html lang='en'>",
    "<head>",
    "<meta charset='UTF-8'>",
    "<title>Ennor Maintenance & Technical Documents Archive</title>",
    "</head>",
    "<body>",
]

lines = base_content.splitlines()
for line in lines:
    line = line.rstrip()  # Remove trailing whitespace
    if line.startswith("# "):
        html_lines.append(f"<h1>{line[2:]}</h1>")
    elif line.startswith("## "):
        html_lines.append(f"<h2>{line[3:]}</h2>")
    elif line.strip().startswith("#ennor"):
        html_lines.append(f"<p>{line.strip()}</p>")
    elif line.strip():
        match = re.match(r"^\s*(\d+\.\d+(?:\.\d+)?)\s+(.+)$", line.strip())
        if match:
            number, description = match.groups()
            indent_level = len(line) - len(line.lstrip())  # Count leading spaces
            tag = "h3" if indent_level == 4 else "h4" if indent_level == 7 else "p"
            if number in file_map:
                file_name, rel_path = file_map[number]
                html_lines.append(f"{' ' * indent_level}<{tag}>{number} {description} <a href='{rel_path}'>Link to {file_name}</a></{tag}>")
            else:
                html_lines.append(f"{' ' * indent_level}<{tag}>{number} {description} <em>no file</em></{tag}>")
        else:
            html_lines.append(f"<p>{line}</p>")

html_lines.extend(["</body>", "</html>"])

# Write to resources.html
with open("resources.html", "w", encoding="utf-8") as f:
    f.write("\n".join(html_lines) + "\n")