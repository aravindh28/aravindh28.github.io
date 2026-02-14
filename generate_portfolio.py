import json
from datetime import datetime, timezone
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader

# Initialize markdown processor with extensions
md_processor = markdown.Markdown(
    extensions=[
        'extra',        # Tables, fenced code blocks, etc.
        'nl2br',        # Convert newlines to <br>
        'sane_lists',   # Better list handling
        'codehilite',   # Code syntax highlighting
        'toc'           # Table of contents generation
    ],
    output_format='html5'
)

def markdown_filter(text):
    """Convert markdown text to HTML"""
    if not text:
        return ""
    # Reset processor state for multiple calls
    md_processor.reset()
    return md_processor.convert(text)

# Load JSON data
with Path("portfolio.json").open(encoding="utf-8") as f:
    data = json.load(f)

# Add any extra context if needed
data["current_year"] = datetime.now(tz=timezone.utc).year

# Inline SVG data for social links
if "social_links" in data:
    for link in data["social_links"]:
        if link.get("svg_path"):
            with Path(link["svg_path"]).open(encoding="utf-8") as svg_file:
                link["svg_data"] = svg_file.read()

# Filter featured projects for main portfolio
data["featured_projects"] = [p for p in data.get("projects", []) if p.get("featured", False)]

# Set up Jinja environment with custom filter
env = Environment(loader=FileSystemLoader("."), autoescape=True)
env.filters['markdown'] = markdown_filter

# Load templates
index_template = env.get_template("index_template.html")
resume_template = env.get_template("resume_template.html")
projects_template = env.get_template("projects_template.html")

# Render templates
html_output = index_template.render(**data)
resume_output = resume_template.render(**data)
projects_output = projects_template.render(**data)

# Write output files
with Path("index.html").open("w", encoding="utf-8") as f:
    f.write(html_output)

with Path("resume.html").open("w", encoding="utf-8") as f:
    f.write(resume_output)

with Path("projects.html").open("w", encoding="utf-8") as f:
    f.write(projects_output)

print("HTML files generated successfully!")
print("  - index.html (main portfolio)")
print("  - resume.html (print-friendly resume)")
print("  - projects.html (detailed projects page)")
