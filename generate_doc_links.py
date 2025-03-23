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
    "    font-size: 1rem;",          # Increased from 0.875rem (14px) to 1rem (16px)
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
    "    font-size: 1.375rem;",      # Increased from 1.25rem (20px) to 1.375rem (22px)
    "    margin-bottom: 1.25rem;",
    "    color: #333;",
    "}",
    "h2 {",
    "    font-family: 'Montserrat', sans-serif;",
    "    font-weight: 700;",
    "    font-size: 1rem;",          # Increased from 0.875rem (14px) to 1rem (16px)
    "    text-transform: uppercase;",
    "    margin-top: 2.5rem;",
    "    margin-bottom: 0.3125rem;",
    "    color: #333;",
    "}",
    "h3 {",
    "    font-family: 'Open Sans', sans-serif;",
    "    font-weight: 400;",
    "    font-size: 1rem;",          # Increased from 0.875rem (14px) to 1rem (16px)
    "    margin: 0.625rem 0 0.5rem 1.25rem;",
    "    color: #333;",
    "}",
    "h4 {",
    "    font-family: 'Open Sans', sans-serif;",
    "    font-weight: 400;",
    "    font-size: 1rem;",          # Increased from 0.875rem (14px) to 1rem (16px)
    "    margin: 0.5rem 0 0.5rem 1.875rem;",
    "    color: #333;",
    "}",
    "p {",
    "    margin: 0.625rem 0;",
    "}",
    "ul {",
    "    list-style-type: disc;",
    "    margin: 0;",
    "    padding-left: 2.5rem;",
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
    "        font-size: 1.25rem;",   # Increased from 1.1rem (17.6px) to 1.25rem (20px)
    "    }",
    "    h2 {",
    "        font-size: 0.875rem;",  # Increased from 0.75rem (12px) to 0.875rem (14px)
    "    }",
    "    h3, h4 {",
    "        font-size: 0.875rem;",  # Increased from 0.75rem (12px) to 0.875rem (14px)
    "    }",
    "}",
    "</style>",
    "</head>",
    "<body>",
]

# Process the base content and convert to HTML
lines = base_content.splitlines()
current_section = None
for line in lines:
    line = line.rstrip()
    if line.startswith("# "):
        html_lines.append(f"<h1>{line[2:]}</h1>")
    elif line.startswith("## "):
        if current_section:  # Close previous section's ul if it exists
            html_lines.append("</ul>")
        current_section = line[3:]
        html_lines.append(f"<h2>{current_section}</h2>")
        html_lines.append("<ul>")
    elif line.strip().startswith("#ennor"):
        html_lines.append(f"<p>{line.strip()}</p>")
    elif line.strip():
        match = re.match(r"^\s*(\d+\.\d+(?:\.\d+)?)\s+(.+)$", line.strip())
        if match:
            number, description = match.groups()
            indent_level = len(line) - len(line.lstrip())
            tag = "h3" if indent_level == 4 else "h4" if indent_level == 7 else "p"
            if number in file_map:
                file_name, rel_path = file_map[number]
                # Shortened link format: [number]_doc_link
                link_text = f"{number}_doc_link"
                html_lines.append(f"<li><{tag}>{number} {description} <a href='{rel_path}'>{link_text}</a></{tag}></li>")
            else:
                html_lines.append(f"<li><{tag}>{number} {description} <em>no file</em></{tag}></li>")
        else:
            html_lines.append(f"<p>{line}</p>")

# Close the last section's ul
if current_section:
    html_lines.append("</ul>")

html_lines.extend(["</body>", "</html>"])

# Write to resources.html
with open("resources.html", "w", encoding="utf-8") as f:
    f.write("\n".join(html_lines) + "\n")