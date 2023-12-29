import os
import re

def extract_title_and_update_header(file_path):
    # Read the content of the Markdown file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Extract the title from the existing header
    title_match = re.search(r'#\s+(.*)\n', content)
    if title_match:
        old_title = title_match.group(1)
    else:
        old_title = "Untitled"

    # Remove the old-style header
    content = re.sub(r'^#\s+(.*)\n', '', content)

    # Create the new header
    new_header = f"---\ntitle: {old_title}\nlang-ref: {old_title}\n---\n\n"

    # Add the new header to the content
    new_content = new_header + content

    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def process_markdown_files(directory, ext = '.md'):
    # Loop through all files in the specified directory
    from pathlib import Path 
    directory = Path(directory)
    filenames = directory.glob('*.md')
    filenames = directory.glob('*/*.md')
    for filename in filenames:
        file_path = os.path.join(directory, filename)
        extract_title_and_update_header(file_path)
        print(f"Processed: {file_path}")

# Specify the directory containing your Markdown files
markdown_directory = './'

# Process Markdown files in the specified directory
process_markdown_files(markdown_directory)