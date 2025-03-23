import markdown
import os
import re

# Define the repository directory (root of the repo)
repo_dir = "."

# Define file extensions to include
doc_extensions = (".pdf", ".txt", ".md")

# Read base content from external file
with open("base_content.md", "r", encoding="utf-8") as f:
    base_content = f.read()

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

# Initialize Markdown converter for inline text
md = markdown.Markdown(extensions=['extra'])

# Start building the HTML with styling
html_lines = [
    "<!DOCTYPE html>",
    "<html lang='en'>",
    "<head>",
    "<meta charset='UTF-8'>",
    "<meta name='viewport' content='width=device-width, initial-scale=1.0'>",
    "<title>Ennor Maintenance & Technical Documents Archive</title>",
    "<link href='https://fonts.googleapis.com/css2?family=Montserrat:wght@700&family=Open+Sans:wght@400&display=swap' rel='stylesheet'>",
    "<style>",
    "body {",
    "    font-family: 'Open Sans', sans-serif;",
    "    font-size: 1rem;",
    "    line-height: 1.5;",
    "    margin: 0 auto;",
    "    padding: 20px;",
    "    max-width: 800px;",
    "    background-color: #F5F5EF;",
    "    color: #333;",
    "}",
    "h1 {",
    "    font-family: 'Montserrat', sans-serif;",
    "    font-weight: 700;",
    "    font-size: 1.375rem;",
    "    margin-bottom: 1.25rem;",
    "    color: #333;",
    "}",
    "h2 {",
    "    font-family: 'Montserrat', sans-serif;",
    "    font-weight: 700;",
    "    font-size: 1rem;",
    "    text-transform: uppercase;",
    "    margin-top: 2.5rem;",
    "    margin-bottom: 0.3125rem;",
    "    color: #333;",
    "}",
    "ul {",
    "    list-style-type: disc;",
    "    margin: 0;",
    "    padding-left: 2rem;",
    "}",
    "ul ul {",
    "    list-style-type: circle;",
    "    padding-left: 2rem;",
    "}",
    "li {",
    "    margin-bottom: 0.5rem;",
    "}",
    "a {",
    "    color: #0066cc;",
    "    text-decoration: underline;",
    "}",
    "a:hover {",
    "    color: #003366;",
    "}",
    "em {",
    "    color: #e74c3c;",
    "    font-style: italic;",
    "}",
    "@media (max-width: 600px) {",
    "    body {",
    "        padding: 15px;",
    "    }",
    "    h1 {",
    "        font-size: 1.25rem;",
    "    }",
    "    h2 {",
    "        font-size: 0.875rem;",
    "    }",
    "}",
    "</style>",
    "</head>",
    "<body>",
]

# Process the base content
lines = base_content.splitlines()
current_indent = 0
list_stack = []  # Track open <ul> tags

for line in lines:
    line = line.rstrip()
    if not line:
        continue

    # Calculate indentation level (2 spaces = 1 level)
    indent = len(line) - len(line.lstrip())
    indent_level = indent // 2

    # Close any excess list levels
    while len(list_stack) > indent_level:
        html_lines.append("</ul>")
        list_stack.pop()

    # Open new list levels if needed
    while len(list_stack) < indent_level:
        html_lines.append("<ul>")
        list_stack.append(True)

    # Process the line content
    if line.startswith("# "):
        if list_stack:  # Close any open lists before h1
            html_lines.extend(["</ul>"] * len(list_stack))
            list_stack.clear()
        html_lines.append(f"<h1>{md.convert(line[2:])}</h1>")
    elif line.startswith("## "):
        if list_stack:  # Close any open lists before h2
            html_lines.extend(["</ul>"] * len(list_stack))
            list_stack.clear()
        html_lines.append(f"<h2>{md.convert(line[3:])}</h2>")
    elif line.strip().startswith("- "):
        content = line.strip()[2:]  # Remove "- "
        # Extract number (e.g., "1.1", "1.1.1") if present
        number_match = re.match(r"(\d+(?:\.\d+)*)\s+(.+)", content)
        if number_match:
            number, description = number_match.groups()
            content_html = md.convert(description).replace('<p>', '').replace('</p>', '')
            # Check if this is a second-to-top level (e.g., "1.1", not "1" or "1.1.1")
            if number.count('.') == 1 and number in file_map:
                file_name, rel_path = file_map[number]
                link_text = f"{number}_doc_link"
                html_lines.append(f"<li>{number} {content_html} <a href='{rel_path}'>{link_text}</a></li>")
            else:
                html_lines.append(f"<li>{number} {content_html}</li>")
        else:
            content_html = md.convert(content).replace('<p>', '').replace('</p>', '')
            html_lines.append(f"<li>{content_html}</li>")
    else:
        if list_stack:  # Close lists if transitioning to paragraph
            html_lines.extend(["</ul>"] * len(list_stack))
            list_stack.clear()
        html_lines.append(f"<p>{md.convert(line.strip())}</p>")

    md.reset()

# Close any remaining lists
if list_stack:
    html_lines.extend(["</ul>"] * len(list_stack))

html_lines.extend(["</body>", "</html>"])

# Write to resources.html
with open("resources.html", "w", encoding="utf-8") as f:
    f.write("\n".join(html_lines) + "\n")