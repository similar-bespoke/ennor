import os

# Define the repository directory (root of the repo)
repo_dir = "."
# Define file extensions to include
doc_extensions = (".md", ".pdf", ".txt")
# List to store file links
doc_links = []

# Walk through the repository
for root, _, files in os.walk(repo_dir):
    for file in files:
        if file.endswith(doc_extensions) and file != "README.md":  # Exclude README.md itself
            # Create relative path
            rel_path = os.path.relpath(os.path.join(root, file), repo_dir)
            # Create Markdown link
            link = f"- [{file}]({rel_path})"
            doc_links.append(link)

# Generate the content to append to README
content = "## Documents in Repository\n\n" + "\n".join(doc_links) + "\n"

# Read current README content
with open("README.md", "r") as f:
    readme_content = f.read()

# Append or update the document list section
marker = "## Documents in Repository"
if marker in readme_content:
    readme_content = readme_content.split(marker)[0] + content
else:
    readme_content += "\n" + content

# Write back to README
with open("README.md", "w") as f:
    f.write(readme_content)